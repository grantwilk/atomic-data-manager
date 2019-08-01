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

This file contains the direct use operators, intended to be used with
Atomic's pie menu interface. However, they can be implemented anywhere
if they need to be.

These operators basically wrap the functions from ops.utils.nuke.py and
ops.utils.clean.py into operators so they can be easily called by other
intefaces in Blender.

"""

import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class
from atomic_data_manager.ui.utils import ui_layouts
from atomic_data_manager.ops.utils import nuke
from atomic_data_manager.ops.utils import clean
from atomic_data_manager.stats import unused


# Atomic Data Manager Nuke All Operator
class ATOMIC_OT_nuke_all(bpy.types.Operator):
    """Remove all data-blocks from the selected categories"""
    bl_idname = "atomic.nuke_all"
    bl_label = "CAUTION!"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.label(text="Remove the following data-blocks?")

        collections = sorted(bpy.data.collections.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Collections",
            items=collections,
            icon="OUTLINER_OB_GROUP_INSTANCE"
        )

        images = sorted(bpy.data.images.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Images",
            items=images,
            icon="IMAGE_DATA"
        )

        lights = sorted(bpy.data.lights.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Lights",
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        materials = sorted(bpy.data.materials.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=materials,
            icon="MATERIAL"
        )

        node_groups = sorted(bpy.data.node_groups.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=node_groups,
            icon="NODETREE"
        )

        particles = sorted(bpy.data.particles.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Particle Systems",
            items=particles,
            icon="PARTICLES"
        )

        textures = sorted(bpy.data.textures.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Textures",
            items=textures,
            icon="TEXTURE"
        )

        worlds = sorted(bpy.data.worlds.keys())
        ui_layouts.box_list(
            layout=layout,
            title="Worlds",
            items=worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra spacing

    def execute(self, context):

        nuke.collections()
        nuke.images()
        nuke.lights()
        nuke.materials()
        nuke.node_groups()
        nuke.particles()
        nuke.textures()
        nuke.worlds()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Clean All Operator
class ATOMIC_OT_clean_all(bpy.types.Operator):
    """Remove all unused.py data-blocks from the selected categories"""
    bl_idname = "atomic.clean_all"
    bl_label = "Clean All"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.label(text="Remove the following data-blocks?")

        collections = sorted(unused.collections_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Collections",
            items=collections,
            icon="OUTLINER_OB_GROUP_INSTANCE"
        )

        images = sorted(unused.images_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Images",
            items=images,
            icon="IMAGE_DATA"
        )

        lights = sorted(unused.lights_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Lights",
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        materials = sorted(unused.materials_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=materials,
            icon="MATERIAL"
        )

        node_groups = sorted(unused.node_groups_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=node_groups,
            icon="NODETREE"
        )

        particles = sorted(unused.particles_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Particle Systems",
            items=particles,
            icon="PARTICLES"
        )

        textures = sorted(unused.textures_deep())
        ui_layouts.box_list(
            layout=layout,
            title="Textures",
            items=textures,
            icon="TEXTURE"
        )

        worlds = sorted(unused.worlds())
        ui_layouts.box_list(
            layout=layout,
            title="Worlds",
            items=worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra spacing

    def execute(self, context):

        clean.collections()
        clean.images()
        clean.lights()
        clean.materials()
        clean.node_groups()
        clean.particles()
        clean.textures()
        clean.worlds()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Nuke Collections Operator
class ATOMIC_OT_nuke_collections(bpy.types.Operator):
    """Remove all collections from this project"""
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


# Atomic Data Manager Nuke Images Operator
class ATOMIC_OT_nuke_images(bpy.types.Operator):
    """Remove all images from this project"""
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


# Atomic Data Manager Nuke Lights Operator
class ATOMIC_OT_nuke_lights(bpy.types.Operator):
    """Remove all lights from this project"""
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


# Atomic Data Manager Nuke Materials Operator
class ATOMIC_OT_nuke_materials(bpy.types.Operator):
    """Remove all materials from this project"""
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


# Atomic Data Manager Nuke Node Groups Operator
class ATOMIC_OT_nuke_node_groups(bpy.types.Operator):
    """Remove all node groups from this project"""
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


# Atomic Data Manager Nuke Particles Operator
class ATOMIC_OT_nuke_particles(bpy.types.Operator):
    """Remove all particle systems from this project"""
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


# Atomic Data Manager Nuke Textures Operator
class ATOMIC_OT_nuke_textures(bpy.types.Operator):
    """Remove all textures from this project"""
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


# Atomic Data Manager Nuke Worlds Operator
class ATOMIC_OT_nuke_worlds(bpy.types.Operator):
    """Remove all worlds from this project"""
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


# Atomic Data Manager Clean Collections Operator
class ATOMIC_OT_clean_collections(bpy.types.Operator):
    """Remove all unused.py collections from this project"""
    bl_idname = "atomic.clean_collections"
    bl_label = "Clean Collections"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        collections = unused.collections_deep()
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


# Atomic Data Manager Clean Images Operator
class ATOMIC_OT_clean_images(bpy.types.Operator):
    """Remove all unused.py images from this project"""
    bl_idname = "atomic.clean_images"
    bl_label = "Clean Images"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        images = unused.images_deep()
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

# Atomic Data Manager Clean Lights Operator
class ATOMIC_OT_clean_lights(bpy.types.Operator):
    """Remove all unused.py lights from this project"""
    bl_idname = "atomic.clean_lights"
    bl_label = "Clean Lights"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        lights = unused.lights_deep()
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


# Atomic Data Manager Clean Materials Operator
class ATOMIC_OT_clean_materials(bpy.types.Operator):
    """Remove all unused.py materials from this project"""
    bl_idname = "atomic.clean_materials"
    bl_label = "Clean Materials"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        materials = unused.materials_deep()
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


# Atomic Data Manager Clean Node Groups Operator
class ATOMIC_OT_clean_node_groups(bpy.types.Operator):
    """Remove all unused.py node groups from this project"""
    bl_idname = "atomic.clean_node_groups"
    bl_label = "Clean Node Groups"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        node_groups = unused.node_groups_deep()
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


# Atomic Data Manager Clean Particles Operator
class ATOMIC_OT_clean_particles(bpy.types.Operator):
    """Remove all unused.py particle systems from this project"""
    bl_idname = "atomic.clean_particles"
    bl_label = "Clean Particles"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        particles = unused.particles_deep()
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


# Atomic Data Manager Clean Textures Operator
class ATOMIC_OT_clean_textures(bpy.types.Operator):
    """Remove all unused.py textures from this project"""
    bl_idname = "atomic.clean_textures"
    bl_label = "Clean Textures"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        textures = unused.textures_deep()
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


# Atomic Data Manager Clean Worlds Operator
class ATOMIC_OT_clean_worlds(bpy.types.Operator):
    """Remove all unused.py worlds from this project"""
    bl_idname = "atomic.clean_worlds"
    bl_label = "Clean Worlds"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Remove the following data-blocks?")

        worlds = unused.worlds()
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


reg_list = [
    ATOMIC_OT_nuke_all,
    ATOMIC_OT_clean_all,

    ATOMIC_OT_nuke_collections,
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
    ATOMIC_OT_clean_worlds
]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)
