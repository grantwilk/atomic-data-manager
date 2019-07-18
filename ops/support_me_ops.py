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
import webbrowser
from bpy.utils import register_class, unregister_class


class ATOMIC_OT_support_me_web(bpy.types.Operator):
    """Opens the Remington Creative \"Support Me\" webpage"""
    bl_idname = "atomic.support_me_web"
    bl_label = "Support Me"

    def execute(self, context):
        webbrowser.open("https://remingtoncreative.com/support/")
        return {'FINISHED'}


reg_list = [ATOMIC_OT_support_me_web]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
