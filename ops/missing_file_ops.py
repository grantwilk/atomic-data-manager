"""
Copyright (C) 2019 Grant Wilk

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
from atomic_data_manager.ops.utils import bl_stats
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Detect Missing Files Operator
class ATOMIC_OT_detect_missing(bpy.types.Operator):
    """Detects missing files in the project"""
    bl_idname = "atomic.detect_missing"
    bl_label = "Missing File Detection"

    recovery_option: bpy.props.EnumProperty(
        items=[
            ('IGNORE', 'Ignore Missing Files', 'Ignore the missing files and leave them offline'),
            ('RELOAD', 'Reload Missing Files', 'Reload the missing files from their existing filepaths'),
            ('SEARCH', 'Search for Missing Files (under development)', 'Search for the missing files in a directory'),
            ('REPLACE', 'Specify Replacement Files (under development)', 'Replace missing files with new files'),
            ('REMOVE', 'Remove Missing Files', 'Remove the missing files from the project'),
            ],
        default='IGNORE'
    )

    def draw(self, context):
        layout = self.layout
        missing_images = bl_stats.get_missing_images()

        if missing_images:
            row = layout.row()
            row.label(text="Atomic has detected one or more missing files in your project!")

            ui_layouts.box_list(
                layout=layout,
                items=missing_images,
                icon="IMAGE_DATA",
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
        elif self.recovery_option == 'REMOVE':
            bpy.ops.atomic.remove_missing('INVOKE_DEFAULT')
        elif self.recovery_option == 'SEARCH':
            bpy.ops.atomic.search_missing('INVOKE_DEFAULT')
        elif self.recovery_option == 'REPLACE':
            bpy.ops.atomic.replace_missing('INVOKE_DEFAULT')

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=500)


# Atomic Data Manager Reload Missing Files Operator
class ATOMIC_OT_reload_missing(bpy.types.Operator):
    """Reload missing files"""
    bl_idname = "atomic.reload_missing"
    bl_label = "Reload Missing Files"

    def execute(self, context):
        for image_key in bl_stats.get_missing_images():
            bpy.data.images[image_key].reload()
        bpy.ops.atomic.reload_report('INVOKE_DEFAULT')
        return {'FINISHED'}


# Atomic Data Manager Reload Missing Files Report Operator
class ATOMIC_OT_reload_report(bpy.types.Operator):
    """Reload report for missing files"""
    bl_idname = "atomic.reload_report"
    bl_label = "Missing File Reload Report"

    def draw(self, context):
        layout = self.layout
        missing_images = bl_stats.get_missing_images()

        if missing_images:
            row = layout.row()
            row.label(text="Atomic was unable to reload the following files:")

            ui_layouts.box_list(
                layout=self.layout,
                items=missing_images,
                icon='IMAGE_DATA',
                columns=3
            )

        else:
            row = layout.row()
            row.label(text="All files successfully reloaded!")

        row = layout.row()  # extra space

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Remove Missing Files Operator
class ATOMIC_OT_remove_missing(bpy.types.Operator):
    """Removes all missing files from the project"""
    bl_idname = "atomic.remove_missing"
    bl_label = "Remove Missing Files"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        ui_layouts.box_list(
            layout=layout,
            items=bl_stats.get_missing_images(),
            icon="IMAGE_DATA",
            columns=2
        )

        row = layout.row()  # extra space

    def execute(self, context):
        for image_key in bl_stats.get_missing_images():
            bpy.data.images.remove(bpy.data.images[image_key])
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Search for Missing Files Operator
class ATOMIC_OT_search_missing(bpy.types.Operator):
    """Searches for missing files"""
    bl_idname = "atomic.search_missing"
    bl_label = "Search for Missing Files"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Unsupported Operation!")

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Replace Missing Files Operator
class ATOMIC_OT_replace_missing(bpy.types.Operator):
    """Replace missing files"""
    bl_idname = "atomic.replace_missing"
    bl_label = "Replace Missing Files"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Unsupported Operation!")

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


@persistent
def call_detect_missing(dummy=None):
    if bl_stats.get_missing_images():
        bpy.ops.atomic.detect_missing('INVOKE_DEFAULT')


reg_list = [
    ATOMIC_OT_detect_missing,
    ATOMIC_OT_reload_missing,
    ATOMIC_OT_reload_report,
    ATOMIC_OT_remove_missing,
    ATOMIC_OT_search_missing,
    ATOMIC_OT_replace_missing,
    ]


def register():
    for item in reg_list:
        register_class(item)

    bpy.app.handlers.load_post.append(call_detect_missing)


def unregister():
    for item in reg_list:
        unregister_class(item)
