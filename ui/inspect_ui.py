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

This file contains the inspection user interface.

"""

import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class
from atomic_data_manager.stats import users
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Inspect Collections UI Operator
class ATOMIC_OT_inspect_collections(bpy.types.Operator):
    """Inspect Collections"""
    bl_idname = "atomic.inspect_collections"
    bl_label = "Inspect Collections"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        collections = bpy.data.collections
        collections_field = atom.collections_field \
            if atom.collections_field in collections.keys() else ""

        # inspect collections box list
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="collections_field",
            data="collections"
        )

        # mesh box list
        meshes = sorted(
            users.collection_meshes(collections_field)) \
            if collections_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Meshes",
            items=meshes,
            icon="OUTLINER_OB_MESH"
        )

        # light box list
        lights = sorted(
            users.collection_lights(collections_field)) \
            if collections_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Lights",
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        # camera box list
        cameras = sorted(
            users.collection_cameras(collections_field)) \
            if collections_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Cameras",
            items=cameras,
            icon="OUTLINER_OB_CAMERA"
        )

        # other objects box list
        others = sorted(
            users.collection_others(collections_field)) \
            if collections_field != "" else []

        ui_layouts.box_list_diverse(
            layout=layout,
            title="Other",
            items=others
        )

        # child collections box list
        children = sorted(
            users.collection_children(collections_field)) \
            if collections_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Child Collections",
            items=children,
            icon="OUTLINER_OB_GROUP_INSTANCE"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "COLLECTIONS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Images UI Operator
class ATOMIC_OT_inspect_images(bpy.types.Operator):
    """Inspect Images"""
    bl_idname = "atomic.inspect_images"
    bl_label = "Inspect Images"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        images = bpy.data.images
        images_field = atom.images_field \
            if atom.images_field in images.keys() else ""

        # inspect images header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="images_field",
            data="images"
        )

        # materials box list
        materials = sorted(
            users.image_materials(images_field)) \
            if images_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=materials,
            icon="MATERIAL"
        )

        # node groups box list
        materials = sorted(
            users.image_node_groups(images_field)) \
            if images_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=materials,
            icon="NODETREE"
        )

        # textures box list
        textures = sorted(
            users.image_textures(images_field)) \
            if images_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Textures",
            items=textures,
            icon="TEXTURE"
        )

        # worlds box list
        worlds = sorted(
            users.image_worlds(images_field)) \
            if images_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Worlds",
            items=worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "IMAGES"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Lights UI Operator
class ATOMIC_OT_inspect_lights(bpy.types.Operator):
    """Inspect Lights"""
    bl_idname = "atomic.inspect_lights"
    bl_label = "Inspect Lights"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        lights = bpy.data.lights
        lights_field = atom.lights_field \
            if atom.lights_field in lights.keys() else ""

        # inspect lights header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="lights_field",
            data="lights"
        )

        # light objects box list
        lights = sorted(
            users.light_objects(lights_field)) \
            if lights_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Light Objects",
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "LIGHTS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Materials UI Operator
class ATOMIC_OT_inspect_materials(bpy.types.Operator):
    """Inspect Materials"""
    bl_idname = "atomic.inspect_materials"
    bl_label = "Inspect Materials"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        materials = bpy.data.materials
        materials_field = atom.materials_field \
            if atom.materials_field in materials.keys() else ""

        # inspect materials header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="materials_field",
            data="materials"
        )

        # objects box list
        objects = sorted(
            users.material_objects(materials_field)) \
            if materials_field != "" else []

        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=objects
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "MATERIALS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Node Groups UI Operator
class ATOMIC_OT_inspect_node_groups(bpy.types.Operator):
    """Inspect Node Groups"""
    bl_idname = "atomic.inspect_node_groups"
    bl_label = "Inspect Node Groups"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        node_groups = bpy.data.node_groups
        node_groups_field = atom.node_groups_field \
            if atom.node_groups_field in node_groups.keys() else ""

        # inspect node groups header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="node_groups_field",
            data="node_groups"
        )

        # materials box list
        materials = sorted(
            users.node_group_materials(node_groups_field)) \
            if node_groups_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=materials,
            icon="MATERIAL"
        )

        # node groups box list
        node_groups = sorted(
            users.node_group_node_groups(node_groups_field)) \
            if node_groups_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=node_groups,
            icon="NODETREE"
        )

        # world box list
        worlds = sorted(
            users.node_group_worlds(node_groups_field)) \
            if node_groups_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Worlds",
            items=worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "NODE_GROUPS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Particles UI Operator
class ATOMIC_OT_inspect_particles(bpy.types.Operator):
    """Inspect Particle Systems"""
    bl_idname = "atomic.inspect_particles"
    bl_label = "Inspect Particles"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        particles = bpy.data.particles
        particles_field = atom.particles_field \
            if atom.particles_field in particles.keys() else ""

        # inspect particles header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="particles_field",
            data="particles"
        )

        # objects box list
        objects = sorted(
            users.particle_objects(particles_field)) \
            if particles_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Objects",
            items=objects,
            icon="OUTLINER_OB_MESH"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "PARTICLES"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Textures UI Operator
class ATOMIC_OT_inspect_textures(bpy.types.Operator):
    """Inspect Textures"""
    bl_idname = "atomic.inspect_textures"
    bl_label = "Inspect Textures"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic
        textures = bpy.data.textures
        textures_field = atom.textures_field \
            if atom.textures_field in textures.keys() else ""

        # inspect textures header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="textures_field",
            data="textures"
        )

        # brushes box list
        brushes = sorted(
            users.texture_brushes(textures_field)) \
            if textures_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Brushes",
            items=brushes,
            icon="BRUSH_DATA"
        )

        # particles box list
        particles = sorted(
            users.texture_particles(textures_field)) \
            if textures_field != "" else []

        ui_layouts.box_list(
            layout=layout,
            title="Particles",
            items=particles,
            icon="PARTICLES"
        )

        # objects box list
        objects = sorted(
            users.texture_objects(textures_field)) \
            if textures_field != "" else []

        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=objects,
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "TEXTURES"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Worlds UI Operator
class ATOMIC_OT_inspect_worlds(bpy.types.Operator):
    """Inspect Worlds"""
    bl_idname = "atomic.inspect_worlds"
    bl_label = "Inspect Worlds"

    def draw(self, context):
        layout = self.layout

        # inspect worlds header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="worlds_field",
            data="worlds"
        )

        # worlds box list
        ui_layouts.box_list(
            layout=layout,
            title="Worlds in Scene",
            items=bpy.data.worlds.keys(),
            icon="WORLD"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        atom = bpy.context.scene.atomic
        atom.active_inspection = "WORLDS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


reg_list = [
    ATOMIC_OT_inspect_collections,
    ATOMIC_OT_inspect_images,
    ATOMIC_OT_inspect_lights,
    ATOMIC_OT_inspect_materials,
    ATOMIC_OT_inspect_node_groups,
    ATOMIC_OT_inspect_particles,
    ATOMIC_OT_inspect_textures,
    ATOMIC_OT_inspect_worlds
]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
