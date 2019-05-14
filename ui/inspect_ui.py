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
from atomic_data_manager.ops.utils import blendusers
from atomic_data_manager.ui.utils import ui_layouts


# COLLECTIONS
class DATAMGR_OT_inspect_collections(bpy.types.Operator):
    """Inspect Collections"""
    bl_idname = "datamgr.inspect_collections"
    bl_label = "Inspect Collections"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        collections = bpy.data.collections
        collections_field = dmgr.collections_field if dmgr.collections_field in collections.keys() else ""

        # Inspect Collections Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="collections_field",
            data="collections"
        )

        # Mesh Section
        meshes = sorted(blendusers.collection_mesh(collections_field)) if collections_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Meshes",
            items=meshes,
            icon="OUTLINER_OB_MESH"
        )

        # Light Section
        lights = sorted(blendusers.collection_light(collections_field)) if collections_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Lights",
            items=lights,
            icon="OUTLINER_OB_LIGHT"
        )

        # Camera Section
        cameras = sorted(blendusers.collection_camera(collections_field)) if collections_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Cameras",
            items=cameras,
            icon="OUTLINER_OB_CAMERA"
        )

        # Others Section
        others = sorted(blendusers.collection_others(collections_field)) if collections_field != "" else []
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Other",
            items=others
        )

        # Child Collections Section
        children = sorted(blendusers.collection_child(collections_field)) if collections_field != "" else []
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
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "COLLECTIONS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# IMAGES
class DATAMGR_OT_inspect_images(bpy.types.Operator):
    """Inspect Images"""
    bl_idname = "datamgr.inspect_images"
    bl_label = "Inspect Images"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        images = bpy.data.images
        images_field = dmgr.images_field if dmgr.images_field in images.keys() else ""

        # Inspect Images Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="images_field",
            data="images"
        )

        # Materials Box List
        materials = sorted(blendusers.image_materials(images_field)) if images_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=materials,
            icon="NODE_MATERIAL"
        )

        # Node Groups Box List
        materials = sorted(blendusers.image_node_groups(images_field)) if images_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=materials,
            icon="NODETREE"
        )

        # Objects Box List
        objects = sorted(blendusers.image_objects(images_field)) if images_field != "" else []
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=objects
        )

        # Worlds Box List
        worlds = sorted(blendusers.image_worlds(images_field)) if images_field != "" else []
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
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "IMAGES"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# LIGHTS
class DATAMGR_OT_inspect_lights(bpy.types.Operator):
    """Inspect Lights"""
    bl_idname = "datamgr.inspect_lights"
    bl_label = "Inspect Lights"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        lights = bpy.data.lights
        lights_field = dmgr.lights_field if dmgr.lights_field in lights.keys() else ""

        # Inspect Lights Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="lights_field",
            data="lights"
        )

        # Light Objects Box List
        lights = sorted(blendusers.lights_lights(lights_field)) if lights_field != "" else []
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
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "LIGHTS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# MATERIALS
class DATAMGR_OT_inspect_materials(bpy.types.Operator):
    """Inspect Materials"""
    bl_idname = "datamgr.inspect_materials"
    bl_label = "Inspect Materials"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        materials = bpy.data.materials
        materials_field = dmgr.materials_field if dmgr.materials_field in materials.keys() else ""

        # Inspect Materials Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="materials_field",
            data="materials"
        )

        # Objects Box List
        objects = sorted(blendusers.material_objects(materials_field)) if materials_field != "" else []
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=objects
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "MATERIALS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# NODE GROUPS
class DATAMGR_OT_inspect_node_groups(bpy.types.Operator):
    """Inspect Node Groups"""
    bl_idname = "datamgr.inspect_node_groups"
    bl_label = "Inspect Node Groups"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        node_groups = bpy.data.node_groups
        node_groups_field = dmgr.node_groups_field if dmgr.node_groups_field in node_groups.keys() else ""

        # Inspect Node Groups Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="node_groups_field",
            data="node_groups"
        )

        # Materials Box List
        materials = sorted(blendusers.node_groups_materials(node_groups_field)) \
            if node_groups_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=materials,
            icon="NODE_MATERIAL"
        )

        # Node Groups Box List
        node_groups = sorted(blendusers.node_groups_node_groups(node_groups_field)) \
            if node_groups_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=node_groups,
            icon="NODETREE"
        )

        # World Box List
        worlds = sorted(blendusers.node_groups_world(node_groups_field)) \
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
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "NODE_GROUPS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# PARTICLES
class DATAMGR_OT_inspect_particles(bpy.types.Operator):
    """Inspect Particle Systems"""
    bl_idname = "datamgr.inspect_particles"
    bl_label = "Inspect Particles"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        particles = bpy.data.particles
        particles_field = dmgr.particles_field if dmgr.particles_field in particles.keys() else ""

        # Inspect Particles Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="particles_field",
            data="particles"
        )

        # Objects Box List
        objects = sorted(blendusers.particles_objects(particles_field)) if particles_field != "" else []
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
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "PARTICLES"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# TEXTURES
class DATAMGR_OT_inspect_textures(bpy.types.Operator):
    """Inspect Textures"""
    bl_idname = "datamgr.inspect_textures"
    bl_label = "Inspect Textures"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        textures = bpy.data.textures
        textures_field = dmgr.textures_field if dmgr.textures_field in textures.keys() else ""

        # Inspect Textures Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="textures_field",
            data="textures"
        )

        # Brushes Box List
        brushes = sorted(blendusers.textures_brushes(textures_field)) if textures_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Brushes",
            items=brushes,
            icon="BRUSH_DATA"
        )

        # Particles Box List
        particles = sorted(blendusers.textures_particles(textures_field)) if textures_field != "" else []
        ui_layouts.box_list(
            layout=layout,
            title="Particles",
            items=particles,
            icon="PARTICLES"
        )

        # Objects Box List
        objects = sorted(blendusers.textures_objects(textures_field)) if textures_field != "" else []
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=objects,
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "TEXTURES"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# WORLDS
class DATAMGR_OT_inspect_worlds(bpy.types.Operator):
    """Inspect Worlds"""
    bl_idname = "datamgr.inspect_worlds"
    bl_label = "Inspect Worlds"

    def draw(self, context):
        layout = self.layout

        # Inspect Worlds Header
        ui_layouts.inspect_header(
            layout=layout,
            dmgr_prop="worlds_field",
            data="worlds"
        )

        # Worlds Box List
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
        dmgr = bpy.context.scene.datamgr
        dmgr.active_inspection = "WORLDS"
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


reg_list = [DATAMGR_OT_inspect_collections,
            DATAMGR_OT_inspect_images,
            DATAMGR_OT_inspect_lights,
            DATAMGR_OT_inspect_materials,
            DATAMGR_OT_inspect_node_groups,
            DATAMGR_OT_inspect_particles,
            DATAMGR_OT_inspect_textures,
            DATAMGR_OT_inspect_worlds,]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
