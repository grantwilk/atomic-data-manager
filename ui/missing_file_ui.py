"""
Copyright (C) 2019 Remington Creative

This file is part of Atomic Data Manager.

Atomic Data Manager is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Atomic Data Manager is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with Atomic Data Manager.  If not, see <https://www.gnu.org/licenses/>.
"""

import bpy
from bpy.app.handlers import persistent
from bpy.utils import register_class, unregister_class
from atomic_data_manager import config
from atomic_data_manager.stats import missing
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Detect Missing Files Popup
class ATOMIC_OT_detect_missing(bpy.types.Operator):
    """Detect missing files in this project"""
    bl_idname = "atomic.detect_missing"
    bl_label = "Missing File Detection"

    recovery_option: bpy.props.EnumProperty(
        items=[
            ('IGNORE', 'Ignore Missing Files', 'Ignore the missing files and leave them offline'),
            ('RELOAD', 'Reload Missing Files', 'Reload the missing files from their existing filepaths'),
            ('REMOVE', 'Remove Missing Files', 'Remove the missing files from the project'),
            ('SEARCH', 'Search for Missing Files (coming soon)', 'Search for the missing files in a directory'),
            ('REPLACE', 'Specify Replacement Files (coming soon)', 'Replace missing files with new files'),
            ],
        default='IGNORE'
    )

    def draw(self, context):
        layout = self.layout
        missing_images = missing.images()
        missing_libraries = missing.libraries()

        if missing_images or missing_libraries:
            row = layout.row()
            row.label(text="Atomic has detected one or more missing files in your project!")

            if missing_images:
                ui_layouts.box_list(
                    layout=layout,
                    title="Images",
                    items=missing_images,
                    icon="IMAGE_DATA",
                    columns=3
                )

            if missing_libraries:
                ui_layouts.box_list(
                    layout=layout,
                    title="Libraries",
                    items=missing_libraries,
                    icon="LIBRARY_DATA_DIRECT",
                    columns=3
                )

            row = layout.separator()  # extra space

            row = layout.row()
            row.label(text="What would you like to do?")

            row = layout.row()
            row.prop(self, 'recovery_option', text="")

        else:
            row = layout.row()
            row.label(text="No missing files were found!")

            ui_layouts.box_list(
                layout=layout
            )

        row = layout.separator()  # extra space

    def execute(self, context):
        if self.recovery_option == 'RELOAD':
            bpy.ops.atomic.reload_missing('INVOKE_DEFAULT')
        elif self.recovery_option == 'SEARCH':
            bpy.ops.atomic.search_missing('INVOKE_DEFAULT')
        elif self.recovery_option == 'REPLACE':
            bpy.ops.atomic.replace_missing('INVOKE_DEFAULT')
        elif self.recovery_option == 'REMOVE':
            bpy.ops.atomic.remove_missing('INVOKE_DEFAULT')

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=500)


@persistent
def autodetect_missing_files(dummy=None):
    if config.enable_missing_file_warning and (missing.images() or missing.libraries()):
        bpy.ops.atomic.detect_missing('INVOKE_DEFAULT')


reg_list = [ATOMIC_OT_detect_missing]


def register():
    for item in reg_list:
        register_class(item)

    bpy.app.handlers.load_post.append(autodetect_missing_files)


def unregister():
    for item in reg_list:
        unregister_class(item)

    bpy.app.handlers.load_post.remove(autodetect_missing_files)
