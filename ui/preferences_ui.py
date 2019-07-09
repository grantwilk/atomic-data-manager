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
from atomic_data_manager import config


# Updates Atomic variables in config.py for global use
def update_preferences(self, context):
    config.enable_missing_file_warning = self.enable_missing_file_warning
    config.enable_stats_for_nerds = self.enable_stats_for_nerds
    config.ignore_fake_users = self.ignore_fake_users


class ATOMIC_PT_preferences_panel(bpy.types.AddonPreferences):
    bl_idname = "atomic_data_manager"

    enable_missing_file_warning: bpy.props.BoolProperty(
        description="Display a warning if Atomic detects one or more missing files in your project",
        update=update_preferences
    )

    enable_stats_for_nerds: bpy.props.BoolProperty(
        description="Display the \"Stats for Nerds\" panel in the main Atomic Data Manager panel",
        update=update_preferences
    )

    ignore_fake_users: bpy.props.BoolProperty(
        description="Let the clean tool remove unused data-blocks even if they have fake users",
        update=update_preferences
    )

    def draw(self, context):
        layout = self.layout

        split = layout.split()

        col = split.column()
        col.label(text="UI Preferences:")
        col.prop(self, "enable_missing_file_warning", text="Show Missing File Warning", )
        col.prop(self, "enable_stats_for_nerds", text="Show Stats for Nerds Panel")

        col = split.column()
        col.label(text="Other Preferences:")
        col.prop(self, "ignore_fake_users", text="Ignore Fake Users")


reg_list = [ATOMIC_PT_preferences_panel]


def register():
    for cls in reg_list:
        register_class(cls)

    # Make sure add-on preferences are updated on registration
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons["atomic_data_manager"].preferences
    config.enable_missing_file_warning = addon_prefs.enable_missing_file_warning
    config.enable_stats_for_nerds = addon_prefs.enable_stats_for_nerds
    config.ignore_fake_users = addon_prefs.ignore_fake_users


def unregister():
    for cls in reg_list:
        unregister_class(cls)
