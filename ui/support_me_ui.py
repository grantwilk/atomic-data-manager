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

---

This file contains the user interface and some helper functions for the
support Remington Creative popup.

"""

import bpy
import time
from bpy.utils import register_class
from bpy.utils import unregister_class
from bpy.app.handlers import persistent
from atomic_data_manager import config
from atomic_data_manager.ui import preferences_ui


def get_current_day():
    # returns the current day since the start of the computer clock
    seconds_per_day = 86400
    return int(time.time() / seconds_per_day)


def update_enable_show_support_me_popup(self, context):
    # copy the inverse of the stop show support popup property to Atomic's
    # enable support me popup preference
    preferences_ui.set_enable_support_me_popup(
        not self.stop_showing_support_popup)


@persistent
def show_support_me_popup(dummy=None):
    # shows the support me popup if the 5 day interval has expired and the
    # enable support me popup preference is enabled

    popup_interval = 5  # days

    current_day = get_current_day()
    next_day = config.last_popup_day + popup_interval

    if config.enable_support_me_popup and current_day >= next_day:
        preferences_ui.set_last_popup_day(current_day)
        bpy.ops.atomic.show_support_me('INVOKE_DEFAULT')


# Atomic Data Manager Support Me Popup Operator
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

        # call to action label
        col = layout.column(align=True)
        col.label(
            text="Consider supporting our free software development!"
        )

        separator = layout.separator()  # extra space

        # never show again toggle
        row = layout.row()
        row.prop(
            self, "stop_showing_support_popup", text="Never Show Again"
        )

        # support remington creative button
        row = layout.row()
        row.scale_y = 2
        row.operator(
            "atomic.open_support_me",
            text="Support Remington Creative",
            icon="FUND"
        )

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

    # reset day counter if it equals zero of if it is in the future
    if config.last_popup_day == 0 \
            or config.last_popup_day > get_current_day():
        preferences_ui.set_last_popup_day(get_current_day())


def unregister():
    for cls in reg_list:
        unregister_class(cls)

    bpy.app.handlers.load_post.remove(show_support_me_popup)
