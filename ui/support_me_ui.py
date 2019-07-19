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


# Returns the current day since the start of the computer clock
def get_current_day():
    seconds_per_day = 86400
    return int(time.time() / seconds_per_day)


# Copy the inverse of the local stop_showing_support_popup to Atomic's preferences for enable_support_me_popup
def update_enable_show_support_me_popup(self, context):
    preferences_ui.set_enable_support_me_popup(not self.stop_showing_support_popup)

# Show the support me popup if config's enable_support_me_popup is true
@persistent
def show_support_me_popup(dummy=None):
    popup_interval = 5  # days

    current_day = get_current_day()
    next_day = config.last_popup_day + popup_interval

    if config.enable_support_me_popup and current_day >= next_day:
        preferences_ui.set_last_popup_day(current_day)
        bpy.ops.atomic.show_support_me('INVOKE_DEFAULT')


# Atomic Data Manager Support Me Popup
class ATOMIC_OT_support_me_popup(bpy.types.Operator):
    """Displays the Atomic \"Support Me\" popup"""
    bl_idname = "atomic.show_support_me"
    bl_label = "Like Atomic Data Manager?"
    bl_options = {'REGISTER', 'UNDO'}

    stop_showing_support_popup: bpy.props.BoolProperty(
        default=False,
        update=update_enable_show_support_me_popup
    )

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.label(text="Consider supporting our free software development!")

        separator = layout.separator()

        row = layout.row()
        row.prop(self, "stop_showing_support_popup", text="Never Show Again")

        row = layout.row()
        row.scale_y = 2
        row.operator("atomic.support_me_web", text="Support Remington Creative", icon="FUND")

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

    # Reset day counter if it equals zero of if it is in the future
    if config.last_popup_day == 0 or config.last_popup_day > get_current_day():
        preferences_ui.set_last_popup_day(get_current_day())


def unregister():
    for cls in reg_list:
        unregister_class(cls)

    bpy.app.handlers.load_post.remove(show_support_me_popup)
