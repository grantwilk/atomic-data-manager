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
from bpy.utils import register_class, unregister_class


class ATOMIC_PT_preferences_panel(bpy.types.AddonPreferences):
    bl_idname = "atomic_data_manager"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic

        split = layout.split()

        col = split.column()
        col.label(text="UI Preferences:")
        col.prop(atom, "enable_missing_file_warning", text="Show Missing File Warning")
        col.prop(atom, "enable_stats_for_nerds", text="Show Stats for Nerds Panel")

        col = split.column()
        col.label(text="Other Preferences:")
        col.prop(atom, "ignore_fake_users", text="Ignore Fake Users")


reg_list = [ATOMIC_PT_preferences_panel]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
