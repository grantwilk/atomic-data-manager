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

This file contains Atomic's pie menu UI and its pie menu keymap
registration.

"""

import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class


# Atomic Data Manager Main Pie Menu
class ATOMIC_MT_main_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_main_pie"
    bl_label = "Atomic Data Manager"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # nuke all operator
        pie.operator(
            "atomic.nuke_all",
            text="Nuke All",
            icon="GHOST_ENABLED"
        )

        # clean all operator
        pie.operator(
            "atomic.clean_all",
            text="Clean All",
            icon="PARTICLEMODE"
        )

        # undo operator
        pie.operator(
            "atomic.undo",
            text="Undo",
            icon="LOOP_BACK"
        )

        # inspect category operator
        pie.operator(
            "wm.call_menu_pie",
            text="Inspect",
            icon="VIEWZOOM"
        ).name = "ATOMIC_MT_inspect_pie"

        # nuke category operator
        pie.operator(
            "wm.call_menu_pie",
            text="Nuke",
            icon="GHOST_ENABLED"
        ).name = "ATOMIC_MT_nuke_pie"

        # clean category operator
        pie.operator(
            "wm.call_menu_pie",
            text="Clean",
            icon="PARTICLEMODE"
        ).name = "ATOMIC_MT_clean_pie"


# Atomic Data Manager Nuke Pie Menu
class ATOMIC_MT_nuke_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_nuke_pie"
    bl_label = "Atomic Nuke"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # nuke node groups operator
        pie.operator("atomic.nuke_node_groups", icon="NODETREE")

        # nuke materials operator
        pie.operator("atomic.nuke_materials", icon="MATERIAL")

        # nuke worlds operator
        pie.operator("atomic.nuke_worlds", icon="WORLD")

        # nuke collections operator
        pie.operator("atomic.nuke_collections", icon="GROUP")

        # nuke lights operator
        pie.operator("atomic.nuke_lights", icon="LIGHT")

        # nuke images operator
        pie.operator("atomic.nuke_images", icon="IMAGE_DATA")

        # nuke textures operator
        pie.operator("atomic.nuke_textures", icon="TEXTURE")

        # nuke particles operator
        pie.operator("atomic.nuke_particles", icon="PARTICLES")


# Atomic Data Manager Clean Pie Menu
class ATOMIC_MT_clean_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_clean_pie"
    bl_label = "Atomic Clean"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # clean node groups operator
        pie.operator("atomic.clean_node_groups", icon="NODETREE")

        # clean materials operator
        pie.operator("atomic.clean_materials", icon="MATERIAL")

        # clean worlds operator
        pie.operator("atomic.clean_worlds", icon="WORLD")

        # clean collections operator
        pie.operator("atomic.clean_collections", icon="GROUP")

        # clean lights operator
        pie.operator("atomic.clean_lights", icon="LIGHT")

        # clean images operator
        pie.operator("atomic.clean_images", icon="IMAGE_DATA")

        # clean textures operator
        pie.operator("atomic.clean_textures", icon="TEXTURE")

        # clean materials operator
        pie.operator("atomic.clean_particles", icon="PARTICLES")


# Atomic Data Manager Inspect Pie Menu
class ATOMIC_MT_inspect_pie(bpy.types.Menu):
    bl_idname = "ATOMIC_MT_inspect_pie"
    bl_label = "Atomic Inspect"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # inspect node groups operator
        pie.operator("atomic.inspect_node_groups", icon="NODETREE")

        # inspect materials operator
        pie.operator("atomic.inspect_materials", icon="MATERIAL")

        # inspect worlds operator
        pie.operator("atomic.inspect_worlds", icon="WORLD")

        # inspect groups operator
        pie.operator("atomic.inspect_collections", icon="GROUP")

        # inspect lights operator
        pie.operator("atomic.inspect_lights", icon="LIGHT")

        # inspect images operator
        pie.operator("atomic.inspect_images", icon="IMAGE_DATA")

        # inspect textures operator
        pie.operator("atomic.inspect_textures", icon="TEXTURE")

        # inspect particles operator
        pie.operator("atomic.inspect_particles", icon="PARTICLES")


reg_list = [
    ATOMIC_MT_main_pie,
    ATOMIC_MT_nuke_pie,
    ATOMIC_MT_clean_pie,
    ATOMIC_MT_inspect_pie
]


keymaps = []


def register():
    for cls in reg_list:
        register_class(cls)

    # add keymap entry
    keyconfigs = bpy.context.window_manager.keyconfigs.addon

    keymap = keyconfigs.keymaps.new(
        name="Window",
        space_type='EMPTY',
        region_type='WINDOW'
    )

    keymap_items_menu = keymap.keymap_items.new(
        "wm.call_menu_pie",
        "D",
        "PRESS"
    )

    keymap_items_menu.properties.name = ATOMIC_MT_main_pie.bl_idname
    keymaps.append((keymap, keymap_items_menu))


def unregister():
    for cls in reg_list:
        unregister_class(cls)

    # remove keymap entry
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)

    keymaps.clear()
