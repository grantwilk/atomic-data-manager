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
from atomic_data_manager.ops.utils import clean, nuke, bl_stats
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Nuke Operator
class ATOMIC_OT_nuke(bpy.types.Operator):
    """Remove all data-blocks from the selected categories"""
    bl_idname = "atomic.nuke"
    bl_label = "CAUTION!"

    def draw(self, context):
        atom = bpy.context.scene.atomic
        layout = self.layout

        col = layout.column()
        col.label(text="Remove the following data-blocks?")

        # No Data Section
        if not (atom.collections or atom.images or atom.lights or atom.materials
                or atom.node_groups or atom.particles or atom.textures or atom.worlds):

            ui_layouts.box_list(
                layout=layout,
            )

        # Collections Section
        if atom.collections:
            collections = sorted(bpy.data.collections.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Collections",
                items=collections,
                icon="OUTLINER_OB_GROUP_INSTANCE"
            )

        # Images Section
        if atom.images:
            images = sorted(bpy.data.images.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Images",
                items=images,
                icon="IMAGE_DATA"
            )

        # Lights Section
        if atom.lights:
            lights = sorted(bpy.data.lights.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Lights",
                items=lights,
                icon="OUTLINER_OB_LIGHT"
            )

        # Materials Section
        if atom.materials:
            materials = sorted(bpy.data.materials.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Materials",
                items=materials,
                icon="MATERIAL"
            )

        # Node Group Section
        if atom.node_groups:
            node_groups = sorted(bpy.data.node_groups.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Node Groups",
                items=node_groups,
                icon="NODETREE"
            )

        # Particles Section
        if atom.particles:
            particles = sorted(bpy.data.particles.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Particle Systems",
                items=particles,
                icon="PARTICLES"
            )

        # Textures Section
        if atom.textures:
            textures = sorted(bpy.data.textures.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Textures",
                items=textures,
                icon="TEXTURE"
            )

        # Worlds Section
        if atom.worlds:
            worlds = sorted(bpy.data.worlds.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Worlds",
                items=worlds,
                icon="WORLD"
            )

        row = layout.row()  # extra spacing

    def execute(self, context):
        atom = bpy.context.scene.atomic

        if atom.collections:
            nuke.collections()
        if atom.images:
            nuke.images()
        if atom.lights:
            nuke.lights()
        if atom.materials:
            nuke.materials()
        if atom.node_groups:
            nuke.node_groups()
        if atom.particles:
            nuke.particles()
        if atom.textures:
            nuke.textures()
        if atom.worlds:
            nuke.worlds()

        bpy.ops.atomic.deselect_all()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Clean Operator
class ATOMIC_OT_clean(bpy.types.Operator):
    """Remove all unused data-blocks from the selected categories"""
    bl_idname = "atomic.clean"
    bl_label = "Clean"

    def draw(self, context):
        atom = bpy.context.scene.atomic
        layout = self.layout

        col = layout.column()
        col.label(text="Remove the following data-blocks?")

        # No Data Section
        if not (atom.collections or atom.images or atom.lights or atom.materials
                or atom.node_groups or atom.particles or atom.textures or atom.worlds):

            ui_layouts.box_list(
                layout=layout,
            )

        # Collections Section
        if atom.collections:
            collections = sorted(bl_stats.get_unused_collections())
            ui_layouts.box_list(
                layout=layout,
                title="Collections",
                items=collections,
                icon="OUTLINER_OB_GROUP_INSTANCE"
            )

        # Images Section
        if atom.images:
            images = sorted(bl_stats.get_unused_images())
            ui_layouts.box_list(
                layout=layout,
                title="Images",
                items=images,
                icon="IMAGE_DATA"
            )

        # Lights Section
        if atom.lights:
            lights = sorted(bl_stats.get_unused_lights())
            ui_layouts.box_list(
                layout=layout,
                title="Lights",
                items=lights,
                icon="OUTLINER_OB_LIGHT"
            )

        # Materials Section
        if atom.materials:
            materials = sorted(bl_stats.get_unused_materials())
            ui_layouts.box_list(
                layout=layout,
                title="Materials",
                items=materials,
                icon="MATERIAL"
            )

        # Node Group Section
        if atom.node_groups:
            node_groups = sorted(bl_stats.get_unused_node_groups())
            ui_layouts.box_list(
                layout=layout,
                title="Node Groups",
                items=node_groups,
                icon="NODETREE"
            )

        # Particles Section
        if atom.particles:
            particles = sorted(bl_stats.get_unused_particles())
            ui_layouts.box_list(
                layout=layout,
                title="Particle Systems",
                items=particles,
                icon="PARTICLES"
            )

        # Textures Section
        if atom.textures:
            textures = sorted(bl_stats.get_unused_textures())
            ui_layouts.box_list(
                layout=layout,
                title="Textures",
                items=textures,
                icon="TEXTURE"
            )

        # Worlds Section
        if atom.worlds:
            worlds = sorted(bl_stats.get_unused_worlds())
            ui_layouts.box_list(
                layout=layout,
                title="Worlds",
                items=worlds,
                icon="WORLD"
            )

        row = layout.row()  # extra spacing

    def execute(self, context):
        atom = bpy.context.scene.atomic

        if atom.collections:
            clean.collections()
        if atom.images:
            clean.images()
        if atom.lights:
            clean.lights()
        if atom.materials:
            clean.materials()
        if atom.node_groups:
            clean.node_groups()
        if atom.particles:
            clean.particles()
        if atom.textures:
            clean.textures()
        if atom.worlds:
            clean.worlds()

        bpy.ops.atomic.deselect_all()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Undo Operator
class ATOMIC_OT_undo(bpy.types.Operator):
    """Undo the previous action"""
    bl_idname = "atomic.undo"
    bl_label = "Undo"

    def execute(self, context):
        bpy.ops.ed.undo()
        return {'FINISHED'}


# Atomic Data Manager Smart Select Operator
class ATOMIC_OT_smart_select(bpy.types.Operator):
    """Auto-select categories with unused data"""
    bl_idname = "atomic.smart_select"
    bl_label = "Smart Select"

    def execute(self, context):
        data = bpy.data

        bpy.context.scene.atomic.collections = any(len(collection.all_objects.values()) == 0 for collection in data.collections)
        bpy.context.scene.atomic.images = any(image.users == 0 for image in data.images)
        bpy.context.scene.atomic.lights = any(lights.users == 0 for lights in data.lights)
        bpy.context.scene.atomic.materials = any(material.users == 0 for material in data.materials)
        bpy.context.scene.atomic.node_groups = any(node_group.users == 0 for node_group in data.node_groups)
        bpy.context.scene.atomic.particles = any(particle.users == 0 for particle in data.particles)
        bpy.context.scene.atomic.textures = any(texture.users == 0 for texture in data.textures)
        bpy.context.scene.atomic.worlds = any(world.users == 0 for world in data.worlds)

        return {'FINISHED'}


# Atomic Data Manager Select All Operator
class ATOMIC_OT_select_all(bpy.types.Operator):
    """Select all categories"""
    bl_idname = "atomic.select_all"
    bl_label = "Select All"

    def execute(self, context):
        bpy.context.scene.atomic.collections = True
        bpy.context.scene.atomic.images = True
        bpy.context.scene.atomic.lights = True
        bpy.context.scene.atomic.materials = True
        bpy.context.scene.atomic.node_groups = True
        bpy.context.scene.atomic.particles = True
        bpy.context.scene.atomic.textures = True
        bpy.context.scene.atomic.worlds = True
        return {'FINISHED'}


# Atomic Data Manager Deselect All Operator
class ATOMIC_OT_deselect_all(bpy.types.Operator):
    """Deselect all categories"""
    bl_idname = "atomic.deselect_all"
    bl_label = "Deselect All"

    def execute(self, context):
        bpy.context.scene.atomic.collections = False
        bpy.context.scene.atomic.images = False
        bpy.context.scene.atomic.lights = False
        bpy.context.scene.atomic.materials = False
        bpy.context.scene.atomic.node_groups = False
        bpy.context.scene.atomic.particles = False
        bpy.context.scene.atomic.textures = False
        bpy.context.scene.atomic.worlds = False

        return {'FINISHED'}


reg_list = [ATOMIC_OT_nuke,
            ATOMIC_OT_clean,
            ATOMIC_OT_undo,
            ATOMIC_OT_smart_select,
            ATOMIC_OT_select_all,
            ATOMIC_OT_deselect_all]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)
