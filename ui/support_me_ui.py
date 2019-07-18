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
import time
from bpy.app.handlers import persistent
from bpy.utils import register_class, unregister_class
from atomic_data_manager import config
from atomic_data_manager.ui import preferences_ui


# Copy the popup operator's value to its respective config variable, then have preferences_ui copy it to preferences
def update_preferences(self, context):
    config.enable_support_me_popup = not self.stop_showing_support_popup
    preferences_ui.copy_config_to_prefs()


# Show the support me popup if config's enable_support_me_popup is true
@persistent
def show_support_me_popup(dummy=None):
    support_me_interval = 60  # seconds
    next_show_time = config.last_support_me_popup + support_me_interval

    if config.enable_support_me_popup and time.time() > next_show_time:
        bpy.ops.atomic.show_support_me('INVOKE_DEFAULT')
        config.last_support_me_popup = time.time()
        preferences_ui.copy_config_to_prefs()


# Atomic Data Manager Support Me Popup
class ATOMIC_OT_support_me_popup(bpy.types.Operator):
    """Displays the Atomic \"Support Me\" popup"""
    bl_idname = "atomic.show_support_me"
    bl_label = "Like Atomic Data Manager?"
    bl_options = {'REGISTER', 'UNDO'}

    stop_showing_support_popup: bpy.props.BoolProperty(
        default=False,
        update=update_preferences
    )

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.label(text="Please consider supporting Remington Creative!")

        separator = layout.separator()

        row = layout.row()
        row.scale_y = 2
        row.operator("atomic.support_me_web", text="Support Me", icon="FUND")

        row = layout.row()
        row.prop(self, "stop_showing_support_popup", text="Don't Show Me This")

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


reg_list = [ATOMIC_OT_support_me_popup]


def register():
    for cls in reg_list:
        register_class(cls)

    bpy.app.handlers.load_post.append(show_support_me_popup)


def unregister():
    for cls in reg_list:
        unregister_class(cls)

    bpy.app.handlers.load_post.remove(show_support_me_popup)
