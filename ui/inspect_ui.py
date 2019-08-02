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


# bool that triggers an inspection update if it is True when the
# inspection's draw() method is called
inspection_update_trigger = False


def update_inspection(self, context):
    global inspection_update_trigger
    inspection_update_trigger = True


# Atomic Data Manager Inspect Collections UI Operator
class ATOMIC_OT_inspect_collections(bpy.types.Operator):
    """Inspect Collections"""
    bl_idname = "atomic.inspect_collections"
    bl_label = "Inspect Collections"

    # user lists
    users_meshes = []
    users_lights = []
    users_cameras = []
    users_others = []
    users_children = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect collections box list
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="collections_field",
            data="collections"
        )

        # inspection update code
        if inspection_update_trigger:

            # if key is valid, update the user lists
            if atom.collections_field in bpy.data.collections.keys():
                self.users_meshes = \
                    users.collection_meshes(atom.collections_field)
                self.users_lights = \
                    users.collection_lights(atom.collections_field)
                self.users_cameras = \
                    users.collection_cameras(atom.collections_field)
                self.users_others = \
                    users.collection_others(atom.collections_field)
                self.users_children = \
                    users.collection_children(atom.collections_field)

            # if key is invalid, empty the user lists
            else:
                self.users_meshes = []
                self.users_lights = []
                self.users_cameras = []
                self.users_others = []
                self.users_children = []

            inspection_update_trigger = False

        # mesh box list
        ui_layouts.box_list(
            layout=layout,
            title="Meshes",
            items=self.users_meshes,
            icon="OUTLINER_OB_MESH"
        )

        # light box list
        ui_layouts.box_list(
            layout=layout,
            title="Lights",
            items=self.users_lights,
            icon="OUTLINER_OB_LIGHT"
        )

        # camera box list
        ui_layouts.box_list(
            layout=layout,
            title="Cameras",
            items=self.users_cameras,
            icon="OUTLINER_OB_CAMERA"
        )

        # other objects box list
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Other",
            items=self.users_others
        )

        # child collections box list
        ui_layouts.box_list(
            layout=layout,
            title="Child Collections",
            items=self.users_children,
            icon="OUTLINER_OB_GROUP_INSTANCE"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "COLLECTIONS"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Images UI Operator
class ATOMIC_OT_inspect_images(bpy.types.Operator):
    """Inspect Images"""
    bl_idname = "atomic.inspect_images"
    bl_label = "Inspect Images"

    # user lists
    users_compositors = []
    users_materials = []
    users_node_groups = []
    users_textures = []
    users_worlds = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect images header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="images_field",
            data="images"
        )

        # inspection update code
        if inspection_update_trigger:

            # if key is valid, update the user lists
            if atom.images_field in bpy.data.images.keys():
                self.users_compositors = \
                    users.image_compositors(atom.images_field)
                self.users_materials = \
                    users.image_materials(atom.images_field)
                self.users_node_groups = \
                    users.image_node_groups(atom.images_field)
                self.users_textures = \
                    users.image_textures(atom.images_field)
                self.users_worlds = \
                    users.image_worlds(atom.images_field)

            # if key is invalid, empty the user lists
            else:
                self.users_compositors = []
                self.users_materials = []
                self.users_node_groups = []
                self.users_textures = []
                self.users_worlds = []

            inspection_update_trigger = False

        # compositors box list
        ui_layouts.box_list(
            layout=layout,
            title="Compositors",
            items=self.users_compositors,
            icon="NODE_COMPOSITING"
        )

        # materials box list
        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=self.users_materials,
            icon="MATERIAL"
        )

        # node groups box list
        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=self.users_node_groups,
            icon="NODETREE"
        )

        # textures box list
        ui_layouts.box_list(
            layout=layout,
            title="Textures",
            items=self.users_textures,
            icon="TEXTURE"
        )

        # worlds box list
        ui_layouts.box_list(
            layout=layout,
            title="Worlds",
            items=self.users_worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "IMAGES"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

# Atomic Data Manager Inspect Lights UI Operator
class ATOMIC_OT_inspect_lights(bpy.types.Operator):
    """Inspect Lights"""
    bl_idname = "atomic.inspect_lights"
    bl_label = "Inspect Lights"

    # user lists
    users_objects = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect lights header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="lights_field",
            data="lights"
        )

        # inspection update code
        if inspection_update_trigger:
            # if key is valid, update the user lists
            if atom.lights_field in bpy.data.lights.keys():
                self.users_objects = users.light_objects(atom.lights_field)

            # if key is invalid, empty the user lists
            else:
                self.users_objects = []

            inspection_update_trigger = False

        # light objects box list
        ui_layouts.box_list(
            layout=layout,
            title="Light Objects",
            items=self.users_objects,
            icon="OUTLINER_OB_LIGHT"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "LIGHTS"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Materials UI Operator
class ATOMIC_OT_inspect_materials(bpy.types.Operator):
    """Inspect Materials"""
    bl_idname = "atomic.inspect_materials"
    bl_label = "Inspect Materials"

    # user lists
    users_objects = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect materials header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="materials_field",
            data="materials"
        )

        # inspection update code
        if inspection_update_trigger:

            # if key is valid, update the user lists
            if atom.materials_field in bpy.data.materials.keys():
                self.users_objects = \
                    users.material_objects(atom.materials_field)

            # if key is invalid, empty the user lists
            else:
                self.users_objects = []

            inspection_update_trigger = False

        # objects box list
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=self.users_objects
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "MATERIALS"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Node Groups UI Operator
class ATOMIC_OT_inspect_node_groups(bpy.types.Operator):
    """Inspect Node Groups"""
    bl_idname = "atomic.inspect_node_groups"
    bl_label = "Inspect Node Groups"

    # user lists
    users_compositors = []
    users_materials = []
    users_node_groups = []
    users_textures = []
    users_worlds = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect node groups header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="node_groups_field",
            data="node_groups"
        )

        # inspection update code
        if inspection_update_trigger:

            # if key is valid, update the user lists
            if atom.node_groups_field in bpy.data.node_groups.keys():

                self.users_compositors = \
                    users.node_group_compositors(atom.node_groups_field)
                self.users_materials = \
                    users.node_group_materials(atom.node_groups_field)
                self.users_node_groups = \
                    users.node_group_node_groups(atom.node_groups_field)
                self.users_textures = \
                    users.node_group_textures(atom.node_groups_field)
                self.users_worlds = \
                    users.node_group_worlds(atom.node_groups_field)

            # if key is invalid, empty the user lists
            else:
                self.users_compositors = []
                self.users_materials = []
                self.users_node_groups = []
                self.users_textures = []
                self.users_worlds = []

            inspection_update_trigger = False

        # compositors box list
        ui_layouts.box_list(
            layout=layout,
            title="Compositors",
            items=self.users_compositors,
            icon="NODE_COMPOSITING"
        )

        # materials box list
        ui_layouts.box_list(
            layout=layout,
            title="Materials",
            items=self.users_materials,
            icon="MATERIAL"
        )

        # node groups box list
        ui_layouts.box_list(
            layout=layout,
            title="Node Groups",
            items=self.users_node_groups,
            icon="NODETREE"
        )

        # textures box list
        ui_layouts.box_list(
            layout=layout,
            title="Textures",
            items=self.users_textures,
            icon="TEXTURE"
        )

        # world box list
        ui_layouts.box_list(
            layout=layout,
            title="Worlds",
            items=self.users_worlds,
            icon="WORLD"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "NODE_GROUPS"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Particles UI Operator
class ATOMIC_OT_inspect_particles(bpy.types.Operator):
    """Inspect Particle Systems"""
    bl_idname = "atomic.inspect_particles"
    bl_label = "Inspect Particles"

    # user lists
    users_objects = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect particles header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="particles_field",
            data="particles"
        )

        # inspection update code
        if inspection_update_trigger:

            # if key is valid, update the user lists
            if atom.particles_field in bpy.data.particles.keys():

                self.users_objects = \
                    users.particle_objects(atom.particles_field)

            # if key is invalid, empty the user lists
            else:
                self.users_objects = []

            inspection_update_trigger = False

        # objects box list
        ui_layouts.box_list(
            layout=layout,
            title="Objects",
            items=self.users_objects,
            icon="OUTLINER_OB_MESH"
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "PARTICLES"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Inspect Textures UI Operator
class ATOMIC_OT_inspect_textures(bpy.types.Operator):
    """Inspect Textures"""
    bl_idname = "atomic.inspect_textures"
    bl_label = "Inspect Textures"

    # user lists
    users_compositors = []
    users_brushes = []
    users_particles = []
    users_objects = []

    def draw(self, context):
        global inspection_update_trigger
        atom = bpy.context.scene.atomic

        layout = self.layout

        # inspect textures header
        ui_layouts.inspect_header(
            layout=layout,
            atom_prop="textures_field",
            data="textures"
        )

        # inspection update code
        if inspection_update_trigger:

            # if the key is valid, update the user lists
            if atom.textures_field in bpy.data.textures.keys():

                self.users_compositors = \
                    users.texture_compositor(atom.textures_field)
                self.users_brushes = \
                    users.texture_brushes(atom.textures_field)
                self.users_objects = \
                    users.texture_objects(atom.textures_field)
                self.users_particles = \
                    users.texture_particles(atom.textures_field)

            # if the key is invalid, set empty the user lists
            else:
                self.users_compositors = []
                self.users_brushes = []
                self.users_particles = []
                self.users_objects = []

            inspection_update_trigger = False

        # brushes box list
        ui_layouts.box_list(
            layout=layout,
            title="Brushes",
            items=self.users_brushes,
            icon="BRUSH_DATA"
        )

        # compositors box list
        ui_layouts.box_list(
            layout=layout,
            title="Compositors",
            items=self.users_compositors,
            icon="NODE_COMPOSITING"
        )

        # particles box list
        ui_layouts.box_list(
            layout=layout,
            title="Particles",
            items=self.users_particles,
            icon="PARTICLES"
        )

        # objects box list
        ui_layouts.box_list_diverse(
            layout=layout,
            title="Objects",
            items=self.users_objects,
        )

        row = layout.row()  # extra row for spacing

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "TEXTURES"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
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
        # update inspection context
        atom = bpy.context.scene.atomic
        atom.active_inspection = "WORLDS"

        # trigger update on invoke
        global inspection_update_trigger
        inspection_update_trigger = True

        # invoke inspect dialog
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
