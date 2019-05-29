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


class ATOMIC_MT_main_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_main_pie"
    bl_label = "Atomic Data Manager"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("atomic.undo", text="Undo", icon="LOOP_BACK")
        pie.operator("wm.call_menu_pie", text="Inspect", icon="VIEWZOOM").name = "ATOMIC_MT_inspect_pie"
        pie.operator("wm.call_menu_pie", text="Clean", icon="PARTICLEMODE").name = "ATOMIC_MT_clean_pie"
        pie.operator("wm.call_menu_pie", text="Nuke", icon="GHOST_ENABLED").name = "ATOMIC_MT_nuke_pie"


class ATOMIC_MT_nuke_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_nuke_pie"
    bl_label = "Atomic Nuke"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("atomic.nuke_node_groups", icon="NODETREE")
        pie.operator("atomic.nuke_materials", icon="MATERIAL")
        pie.operator("atomic.nuke_worlds", icon="WORLD")
        pie.operator("atomic.nuke_collections", icon="GROUP")
        pie.operator("atomic.nuke_lights", icon="LIGHT")
        pie.operator("atomic.nuke_images", icon="IMAGE_DATA")
        pie.operator("atomic.nuke_textures", icon="TEXTURE")
        pie.operator("atomic.nuke_particles", icon="PARTICLES")


class ATOMIC_MT_clean_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_clean_pie"
    bl_label = "Atomic Clean"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("atomic.clean_node_groups", icon="NODETREE")
        pie.operator("atomic.clean_materials", icon="MATERIAL")
        pie.operator("atomic.clean_worlds", icon="WORLD")
        pie.operator("atomic.clean_collections", icon="GROUP")
        pie.operator("atomic.clean_lights", icon="LIGHT")
        pie.operator("atomic.clean_images", icon="IMAGE_DATA")
        pie.operator("atomic.clean_textures", icon="TEXTURE")
        pie.operator("atomic.clean_particles", icon="PARTICLES")


class ATOMIC_MT_inspect_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_inspect_pie"
    bl_label = "Atomic Inspect"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("atomic.inspect_node_groups", icon="NODETREE")
        pie.operator("atomic.inspect_materials", icon="MATERIAL")
        pie.operator("atomic.inspect_worlds", icon="WORLD")
        pie.operator("atomic.inspect_collections", icon="GROUP")
        pie.operator("atomic.inspect_lights", icon="LIGHT")
        pie.operator("atomic.inspect_images", icon="IMAGE_DATA")
        pie.operator("atomic.inspect_textures", icon="TEXTURE")
        pie.operator("atomic.inspect_particles", icon="PARTICLES")


reg_list = [ATOMIC_MT_main_pie, ATOMIC_MT_nuke_pie, ATOMIC_MT_clean_pie, ATOMIC_MT_inspect_pie]
keymaps = []


def register():
    for cls in reg_list:
        register_class(cls)

    # add keymap entry
    kc = bpy.context.window_manager.keyconfigs.addon
    # km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    km = kc.keymaps.new(name="Window", space_type='EMPTY', region_type='WINDOW')

    kmi_menu = km.keymap_items.new("wm.call_menu_pie", "D", "PRESS")
    kmi_menu.properties.name = ATOMIC_MT_main_pie.bl_idname
    keymaps.append((km, kmi_menu))


def unregister():
    for cls in reg_list:
        unregister_class(cls)

    # remove keymap entry
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)

    keymaps.clear()
