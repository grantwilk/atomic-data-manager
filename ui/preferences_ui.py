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
from atomic_data_manager.updater import addon_updater_ops
from atomic_data_manager import config


# Returns the user preferences for Atomic
def get_atomic_preferences():
    preferences = bpy.context.preferences
    return preferences.addons.get("atomic_data_manager").preferences


# Copies the values of the variables in config.py to Atomic's preferences for long-term storage
def copy_config_to_prefs():
    atomic_preferences = get_atomic_preferences()
    atomic_preferences.enable_missing_file_warning = config.enable_missing_file_warning
    atomic_preferences.ignore_fake_users = config.ignore_fake_users


# Copies the values of Atomic's preferences to the variables in config.py for global use
def copy_prefs_to_config(self, context):
    atomic_preferences = get_atomic_preferences()
    config.enable_missing_file_warning = atomic_preferences.enable_missing_file_warning
    config.ignore_fake_users = atomic_preferences.ignore_fake_users


class ATOMIC_PT_preferences_panel(bpy.types.AddonPreferences):
    bl_idname = "atomic_data_manager"

    # Preference Properties
    enable_missing_file_warning: bpy.props.BoolProperty(
        description="Display a warning if Atomic detects missing files in your project",
        update=copy_prefs_to_config
    )

    enable_support_me_popup: bpy.props.BoolProperty(
        description="Occasionally display a popup asking if you would like to support Remington Creative",
        update=copy_prefs_to_config
    )

    ignore_fake_users: bpy.props.BoolProperty(
        description="Let the clean tool remove unused data-blocks even if they have fake users",
        update=copy_prefs_to_config
    )

    # CG Cookie Add-on Updater Properties
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
        col.prop(self, "enable_missing_file_warning", text="Show Missing File Warning", )
        col.prop(self, "enable_support_me_popup", text="Enable Support Me Popup")
        col.prop(self, "ignore_fake_users", text="Ignore Fake Users")

        row = layout.row()  # extra space

        addon_updater_ops.update_settings_ui(self, context)


reg_list = [ATOMIC_PT_preferences_panel]


def register():
    for cls in reg_list:
        register_class(cls)

    # Make sure global preferences are updated on registration
    copy_prefs_to_config(None, None)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
