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
from bpy.utils import register_class, unregister_class
from atomic_data_manager.stats import missing
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Reload Missing Files Operator
class ATOMIC_OT_reload_missing(bpy.types.Operator):
    """Reload missing files"""
    bl_idname = "atomic.reload_missing"
    bl_label = "Reload Missing Files"

    def execute(self, context):
        # reload images
        for image_key in missing.images():
            bpy.data.images[image_key].reload()

        # reload libraries
        for lib_key in missing.libraries():
            bpy.data.libraries[lib_key].reload()

        # call reload report
        bpy.ops.atomic.reload_report('INVOKE_DEFAULT')
        return {'FINISHED'}


# Atomic Data Manager Reload Missing Files Report Operator
class ATOMIC_OT_reload_report(bpy.types.Operator):
    """Reload report for missing files"""
    bl_idname = "atomic.reload_report"
    bl_label = "Missing File Reload Report"

    def draw(self, context):
        layout = self.layout
        missing_images = missing.images()
        missing_libraries = missing.libraries()

        if missing_images or missing_libraries:
            row = layout.row()
            row.label(text="Atomic was unable to reload the following files:")

            if missing_images:
                ui_layouts.box_list(
                    layout=self.layout,
                    items=missing_images,
                    icon='IMAGE_DATA',
                    columns=2
                )

            if missing_libraries:
                ui_layouts.box_list(
                    layout=self.layout,
                    items=missing_images,
                    icon='LIBRARY_DATA_DIRECT',
                    columns=2
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
    """Remove all missing files from this project"""
    bl_idname = "atomic.remove_missing"
    bl_label = "Remove Missing Files"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        ui_layouts.box_list(
            layout=layout,
            items=missing.images(),
            icon="IMAGE_DATA",
            columns=2
        )

        row = layout.row()  # extra space

    def execute(self, context):
        for image_key in missing.images():
            bpy.data.images.remove(bpy.data.images[image_key])

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# TODO: Implement search for missing once file browser bugs are fixed
# Atomic Data Manager Search for Missing Files Operator
class ATOMIC_OT_search_missing(bpy.types.Operator):
    """Search a specified directory for the missing files"""
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


# TODO: Implement replace missing once file browser bugs are fixed
# Atomic Data Manager Replace Missing Files Operator
class ATOMIC_OT_replace_missing(bpy.types.Operator):
    """Replace each missing file with a new file"""
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





reg_list = [
    ATOMIC_OT_reload_missing,
    ATOMIC_OT_reload_report,
    ATOMIC_OT_search_missing,
    ATOMIC_OT_replace_missing,
    ATOMIC_OT_remove_missing
    ]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)
