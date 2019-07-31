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

This file contains the Atomic preferences UI, preferences properties, and
some functions for syncing the preference properties with external factors.

"""

import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class
from atomic_data_manager import config
from atomic_data_manager.updater import addon_updater_ops


def set_enable_support_me_popup(value):
    # sets the value of the enable_support_me_popup boolean property

    bpy.context.preferences.addons["atomic_data_manager"]\
        .preferences.enable_support_me_popup = value
    copy_prefs_to_config(None, None)
    bpy.ops.wm.save_userpref()


def set_last_popup_day(day):
    # sets the value of the last_popup_day float property

    bpy.context.preferences.addons["atomic_data_manager"]\
        .preferences.last_popup_day = day
    copy_prefs_to_config(None, None)
    bpy.ops.wm.save_userpref()


def copy_prefs_to_config(self, context):
    # copies the values of Atomic's preferences to the variables in
    # config.py for global use

    preferences = bpy.context.preferences

    atomic_preferences = preferences.addons['atomic_data_manager']\
        .preferences

    config.enable_missing_file_warning = \
        atomic_preferences.enable_missing_file_warning

    config.enable_pie_menu_ui = \
        atomic_preferences.enable_pie_menu_ui

    config.enable_support_me_popup = \
        atomic_preferences.enable_support_me_popup

    config.ignore_fake_users = \
        atomic_preferences.ignore_fake_users

    config.last_popup_day = \
        atomic_preferences.last_popup_day


# Atomic Data Manager Preference Panel UI
class ATOMIC_PT_preferences_panel(bpy.types.AddonPreferences):
    bl_idname = "atomic_data_manager"

    # atomic preferences
    enable_missing_file_warning: bpy.props.BoolProperty(
        description="Display a warning on startup if Atomic detects "
                    "missing files in your project",
        default=True,
        update=copy_prefs_to_config
    )

    enable_pie_menu_ui: bpy.props.BoolProperty(
        description="Enable the Atomic pie menu UI, so you can clean "
                    "your project from anywhere. Just press \"D\"!",
    )

    enable_support_me_popup: bpy.props.BoolProperty(
        description="Occasionally display a popup asking if you would "
                    "like to support Remington Creative",
        default=True,
        update=copy_prefs_to_config
    )

    ignore_fake_users: bpy.props.BoolProperty(
        description="Let the clean tool remove unused data-blocks "
                    "even if they have fake users",
        default=False,
        update=copy_prefs_to_config
    )

    last_popup_day: bpy.props.FloatProperty(
        default=0,
        update=copy_prefs_to_config
    )

    # add-on updater properties
    auto_check_update: bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=True,
    )

    updater_intrval_months: bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0,
        max=6
    )
    updater_intrval_days: bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
    )
    updater_intrval_hours: bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
    )
    updater_intrval_minutes: bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )

    def draw(self, context):
        layout = self.layout

        col = layout.column()

        # enable missing file warning toggle
        col.prop(
            self,
            "enable_missing_file_warning",
            text="Show Missing File Warning"
        )

        # enable pie menu ui toggle
        col.prop(
            self,
            "enable_pie_menu_ui",
            text="Enable Pie Menu UI"
        )

        # enable support me popup toggle
        col.prop(
            self,
            "enable_support_me_popup",
            text="Show \"Support Me\" Popup"
        )

        # ignore fake users toggle
        col.prop(
            self,
            "ignore_fake_users",
            text="Ignore Fake Users"
        )

        separator = layout.separator()  # extra space

        # add-on updater box
        addon_updater_ops.update_settings_ui(self, context)


reg_list = [ATOMIC_PT_preferences_panel]


def register():
    for cls in reg_list:
        register_class(cls)

    # make sure global preferences are updated on registration
    copy_prefs_to_config(None, None)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
