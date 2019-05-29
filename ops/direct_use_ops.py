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
from atomic_data_manager.ui.utils import ui_layouts, bl_stats
from atomic_data_manager.ops.utils import nuke, clean


# <editor-fold desc="Nuke Direct-Use Operators">
class ATOMIC_OT_nuke_collections(bpy.types.Operator):
    """Removes all collections"""
    bl_idname = "atomic.nuke_collections"
    bl_label = "Nuke Collections"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        collections = bpy.data.collections.keys()
        ui_layouts.box_list(
            layout=layout,
            items=collections,
            icon="OUTLINER_OB_GROUP_INSTANCE"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.collections()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_images(bpy.types.Operator):
    """Removes all images"""
    bl_idname = "atomic.nuke_images"
    bl_label = "Nuke Images"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        images = bpy.data.images.keys()
        ui_layouts.box_list(
            layout=layout,
            items=images,
            icon="IMAGE_DATA"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.images()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_lights(bpy.types.Operator):
    """Removes all lights"""
    bl_idname = "atomic.nuke_lights"
    bl_label = "Nuke Lights"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        lights = bpy.data.lights.keys()
        ui_layouts.box_list(
            layout=layout,
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.lights()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_materials(bpy.types.Operator):
    """Removes all materials"""
    bl_idname = "atomic.nuke_materials"
    bl_label = "Nuke Materials"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        materials = bpy.data.materials.keys()
        ui_layouts.box_list(
            layout=layout,
            items=materials,
            icon="MATERIAL"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.materials()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_node_groups(bpy.types.Operator):
    """Removes all node groups"""
    bl_idname = "atomic.nuke_node_groups"
    bl_label = "Nuke Node Groups"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        node_groups = bpy.data.node_groups.keys()
        ui_layouts.box_list(
            layout=layout,
            items=node_groups,
            icon="NODETREE"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.node_groups()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_particles(bpy.types.Operator):
    """Removes all particle systems"""
    bl_idname = "atomic.nuke_particles"
    bl_label = "Nuke Particles"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        particles = bpy.data.particles.keys()
        ui_layouts.box_list(
            layout=layout,
            items=particles,
            icon="PARTICLES"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.particles()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_textures(bpy.types.Operator):
    """Removes all textures"""
    bl_idname = "atomic.nuke_textures"
    bl_label = "Nuke Textures"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        textures = bpy.data.textures.keys()
        ui_layouts.box_list(
            layout=layout,
            items=textures,
            icon="TEXTURE"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.textures()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_nuke_worlds(bpy.types.Operator):
    """Removes all worlds"""
    bl_idname = "atomic.nuke_worlds"
    bl_label = "Nuke Worlds"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        worlds = bpy.data.worlds.keys()
        ui_layouts.box_list(
            layout=layout,
            items=worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        nuke.worlds()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
# </editor-fold>


# <editor-fold desc="Clean Direct-Use Operators">
class ATOMIC_OT_clean_collections(bpy.types.Operator):
    """Removes all unused collections"""
    bl_idname = "atomic.clean_collections"
    bl_label = "Clean Collections"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        collections = bl_stats.get_unused_collections()
        ui_layouts.box_list(
            layout=layout,
            items=collections,
            icon="OUTLINER_OB_GROUP_INSTANCE"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.collections()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_images(bpy.types.Operator):
    """Removes all unused images"""
    bl_idname = "atomic.clean_images"
    bl_label = "Clean Images"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        images = bl_stats.get_unused_images()
        ui_layouts.box_list(
            layout=layout,
            items=images,
            icon="IMAGE_DATA"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.images()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_lights(bpy.types.Operator):
    """Removes all unused lights"""
    bl_idname = "atomic.clean_lights"
    bl_label = "Clean Lights"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        lights = bl_stats.get_unused_lights()
        ui_layouts.box_list(
            layout=layout,
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.lights()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_materials(bpy.types.Operator):
    """Removes all unused materials"""
    bl_idname = "atomic.clean_materials"
    bl_label = "Clean Materials"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        materials = bl_stats.get_unused_materials()
        ui_layouts.box_list(
            layout=layout,
            items=materials,
            icon="MATERIAL"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.materials()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_node_groups(bpy.types.Operator):
    """Removes all unused node groups"""
    bl_idname = "atomic.clean_node_groups"
    bl_label = "Clean Node Groups"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        node_groups = bl_stats.get_unused_node_groups()
        ui_layouts.box_list(
            layout=layout,
            items=node_groups,
            icon="NODETREE"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.node_groups()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_particles(bpy.types.Operator):
    """Removes all unused particle systems"""
    bl_idname = "atomic.clean_particles"
    bl_label = "Clean Particles"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        particles = bl_stats.get_unused_particles()
        ui_layouts.box_list(
            layout=layout,
            items=particles,
            icon="PARTICLES"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.particles()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_textures(bpy.types.Operator):
    """Removes all unused textures"""
    bl_idname = "atomic.clean_textures"
    bl_label = "Clean Textures"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        textures = bl_stats.get_unused_textures()
        ui_layouts.box_list(
            layout=layout,
            items=textures,
            icon="TEXTURE"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.textures()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class ATOMIC_OT_clean_worlds(bpy.types.Operator):
    """Removes all unused worlds"""
    bl_idname = "atomic.clean_worlds"
    bl_label = "Clean Worlds"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        worlds = bl_stats.get_unused_worlds()
        ui_layouts.box_list(
            layout=layout,
            items=worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra space

    def execute(self, context):
        clean.worlds()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
# </editor-fold>


reg_list = [ATOMIC_OT_nuke_collections,
            ATOMIC_OT_nuke_images,
            ATOMIC_OT_nuke_lights,
            ATOMIC_OT_nuke_materials,
            ATOMIC_OT_nuke_node_groups,
            ATOMIC_OT_nuke_particles,
            ATOMIC_OT_nuke_textures,
            ATOMIC_OT_nuke_worlds,

            ATOMIC_OT_clean_collections,
            ATOMIC_OT_clean_images,
            ATOMIC_OT_clean_lights,
            ATOMIC_OT_clean_materials,
            ATOMIC_OT_clean_node_groups,
            ATOMIC_OT_clean_particles,
            ATOMIC_OT_clean_textures,
            ATOMIC_OT_clean_worlds]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)