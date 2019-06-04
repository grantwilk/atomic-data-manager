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
from atomic_data_manager.ops.utils import duplicate, delete


# Atomic Data Manager Inspection Rename Operator
class ATOMIC_OT_inspection_rename(bpy.types.Operator):
    """Rename this data-block"""
    bl_idname = "atomic.rename"
    bl_label = "Rename Data-Block To"

    def draw(self, context):
        atom = bpy.context.scene.atomic

        layout = self.layout
        row = layout.row()
        row.prop(atom, "rename_field", text="", icon="GREASEPENCIL")

    def execute(self, context):
        atom = bpy.context.scene.atomic
        inspection = atom.active_inspection

        name = atom.rename_field

        if inspection == 'COLLECTIONS':
            bpy.data.collections[atom.collections_field].name = name
            atom.collections_field = name

        if inspection == 'IMAGES':
            bpy.data.images[atom.images_field].name = name
            atom.images_field = name

        if inspection == 'LIGHTS':
            bpy.data.lights[atom.lights_field].name = name
            atom.lights_field = name

        if inspection == 'MATERIALS':
            bpy.data.materials[atom.materials_field].name = name
            atom.materials_field = name

        if inspection == 'NODE_GROUPS':
            bpy.data.node_groups[atom.node_groups_field].name = name
            atom.node_groups_field = name

        if inspection == 'PARTICLES':
            bpy.data.particles[atom.particles_field].name = name
            atom.particles_field = name

        if inspection == 'TEXTURES':
            bpy.data.textures[atom.textures_field].name = name
            atom.textures_field = name

        if inspection == 'WORLDS':
            bpy.data.worlds[atom.worlds_field].name = name
            atom.worlds_field = name

        atom.rename_field = ""
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=200)


class ATOMIC_OT_inspection_replace(bpy.types.Operator):
    """Replace all instances of this data-block with another data-block"""
    bl_idname = "atomic.replace"
    bl_label = "Replace Data-Block With"

    def draw(self, context):
        atom = bpy.context.scene.atomic
        inspection = atom.active_inspection

        layout = self.layout
        row = layout.row()

        if inspection == 'IMAGES':
            row.prop_search(atom, "replace_field", bpy.data, "images", text="")
        if inspection == 'LIGHTS':
            row.prop_search(atom, "replace_field", bpy.data, "lights", text="")
        if inspection == 'MATERIALS':
            row.prop_search(atom, "replace_field", bpy.data, "materials", text="")
        if inspection == 'NODE_GROUPS':
            row.prop_search(atom, "replace_field", bpy.data, "node_groups", text="")
        if inspection == 'PARTICLES':
            row.prop_search(atom, "replace_field", bpy.data, "particles", text="")
        if inspection == 'TEXTURES':
            row.prop_search(atom, "replace_field", bpy.data, "textures", text="")
        if inspection == 'WORLDS':
            row.prop_search(atom, "replace_field", bpy.data, "worlds", text="")

    def execute(self, context):
        atom = bpy.context.scene.atomic
        inspection = atom.active_inspection

        if inspection == 'IMAGES' and atom.replace_field in bpy.data.images.keys():
            bpy.data.images[atom.images_field].user_remap(bpy.data.images[atom.replace_field])
            atom.images_field = atom.replace_field

        if inspection == 'LIGHTS' and atom.replace_field in bpy.data.lights.keys():
            bpy.data.lights[atom.lights_field].user_remap(bpy.data.lights[atom.replace_field])
            atom.lights_field = atom.replace_field

        if inspection == 'MATERIALS' and atom.replace_field in bpy.data.materials.keys():
            bpy.data.materials[atom.materials_field].user_remap(bpy.data.materials[atom.replace_field])
            atom.materials_field = atom.replace_field

        if inspection == 'NODE_GROUPS' and atom.replace_field in bpy.data.node_groups.keys():
            bpy.data.node_groups[atom.node_groups_field].user_remap(bpy.data.node_groups[atom.replace_field])
            atom.node_groups_field = atom.replace_field

        if inspection == 'PARTICLES' and atom.replace_field in bpy.data.particles.keys():
            bpy.data.particles[atom.particles_field].user_remap(bpy.data.particles[atom.replace_field])
            atom.particles_field = atom.replace_field

        if inspection == 'TEXTURES' and atom.replace_field in bpy.data.textures.keys():
            bpy.data.textures[atom.textures_field].user_remap(bpy.data.textures[atom.replace_field])
            atom.textures_field = atom.replace_field

        if inspection == 'WORLDS' and atom.replace_field in bpy.data.worlds.keys():
            bpy.data.worlds[atom.worlds_field].user_remap(bpy.data.worlds[atom.replace_field])
            atom.worlds_field = atom.replace_field

        atom.replace_field = ""
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=200)


# Atomic Data Manager Inspection Toggle Fake User Operator
class ATOMIC_OT_inspection_toggle_fake_user(bpy.types.Operator):
    """Save this data-block even if it has no users"""
    bl_idname = "atomic.toggle_fake_user"
    bl_label = "Toggle Fake User"

    def execute(self, context):
        atom = bpy.context.scene.atomic
        inspection = atom.active_inspection

        if inspection == 'IMAGES':
            image = bpy.data.images[atom.images_field]
            bpy.data.images[atom.images_field].use_fake_user = not image.use_fake_user
        if inspection == 'LIGHTS':
            light = bpy.data.lights[atom.lights_field]
            bpy.data.lights[atom.lights_field].use_fake_user = not light.use_fake_user
        if inspection == 'MATERIALS':
            material = bpy.data.materials[atom.materials_field]
            bpy.data.materials[atom.materials_field].use_fake_user = not material.use_fake_user
        if inspection == 'NODE_GROUPS':
            node_group = bpy.data.node_groups[atom.node_groups_field]
            bpy.data.node_groups[atom.node_groups_field].use_fake_user = not node_group.use_fake_user
        if inspection == 'TEXTURES':
            texture = bpy.data.textures[atom.textures_field]
            bpy.data.textures[atom.textures_field].use_fake_user = not texture.use_fake_user
        if inspection == 'WORLDS':
            world = bpy.data.worlds[atom.worlds_field]
            bpy.data.worlds[atom.worlds_field].use_fake_user = not world.use_fake_user

        return {'FINISHED'}


# Atomic Data Manager Inspection Duplicate Operator
class ATOMIC_OT_inspection_duplicate(bpy.types.Operator):
    """Make a single-user copy of this data-block"""
    bl_idname = "atomic.inspection_duplicate"
    bl_label = "Inspection Duplicate"

    def execute(self, context):
        atom = bpy.context.scene.atomic
        inspection = atom.active_inspection

        if inspection == 'COLLECTIONS':
            key = atom.collections_field
            collections = bpy.data.collections

            if key in collections.keys():
                copy_key = duplicate.collection(key)
                atom.collections_field = copy_key

        elif inspection == 'IMAGES':
            key = atom.images_field
            images = bpy.data.images

            if key in images.keys():
                copy_key = duplicate.image(key)
                atom.images_field = copy_key

        elif inspection == 'LIGHTS':
            key = atom.lights_field
            lights = bpy.data.lights

            if key in lights.keys():
                copy_key = duplicate.light(key)
                atom.lights_field = copy_key

        elif inspection == 'MATERIALS':
            key = atom.materials_field
            materials = bpy.data.materials

            if key in materials.keys():
                copy_key = duplicate.material(key)
                atom.materials_field = copy_key

        elif inspection == 'NODE_GROUPS':
            key = atom.node_groups_field
            node_groups = bpy.data.node_groups

            if key in node_groups.keys():
                copy_key = duplicate.node_group(key)
                atom.node_groups_field = copy_key

        elif inspection == 'PARTICLES':
            key = atom.particles_field
            particles = bpy.data.particles

            if key in particles.keys():
                copy_key = duplicate.particle(key)
                atom.particles_field = copy_key

        elif inspection == 'TEXTURES':
            key = atom.textures_field
            textures = bpy.data.textures

            if key in textures.keys():
                copy_key = duplicate.texture(key)
                atom.textures_field = copy_key

        elif inspection == 'WORLDS':
            key = atom.worlds_field
            worlds = bpy.data.worlds

            if key in worlds.keys():
                copy_key = duplicate.world(key)
                atom.worlds_field = copy_key

        return {'FINISHED'}


# Atomic Data Manager Inspection Delete Operator
class ATOMIC_OT_inspection_delete(bpy.types.Operator):
    """Force delete this data-block"""
    bl_idname = "atomic.inspection_delete"
    bl_label = "Inspection Delete"

    def execute(self, context):
        atom = bpy.context.scene.atomic
        inspection = atom.active_inspection

        if inspection == 'COLLECTIONS':
            key = atom.collections_field
            collections = bpy.data.collections

            if key in collections.keys():
                delete.collection(key)
                atom.collections_field = ""

        elif inspection == 'IMAGES':
            key = atom.images_field
            images = bpy.data.images

            if key in images.keys():
                delete.image(key)
                atom.images_field = ""

        elif inspection == 'LIGHTS':
            key = atom.lights_field
            lights = bpy.data.lights

            if key in lights.keys():
                delete.light(key)
                atom.lights_field = ""

        elif inspection == 'MATERIALS':
            key = atom.materials_field
            materials = bpy.data.materials

            if key in materials.keys():
                delete.material(key)
                atom.materials_field = ""

        elif inspection == 'NODE_GROUPS':
            key = atom.node_groups_field
            node_groups = bpy.data.node_groups

            if key in node_groups.keys():
                delete.node_group(key)
                atom.node_groups_field = ""

        elif inspection == 'PARTICLES':
            key = atom.particles_field
            particles = bpy.data.particles
            if key in particles.keys():
                delete.particle(key)
                atom.particles_field = ""

        elif inspection == 'TEXTURES':
            key = atom.textures_field
            textures = bpy.data.textures

            if key in textures.keys():
                delete.texture(key)
                atom.textures_field = ""

        elif inspection == 'WORLDS':
            key = atom.worlds_field
            worlds = bpy.data.worlds

            if key in worlds.keys():
                delete.world(key)
                atom.worlds_field = ""

        return {'FINISHED'}


reg_list = [ATOMIC_OT_inspection_rename,
            ATOMIC_OT_inspection_replace,
            ATOMIC_OT_inspection_toggle_fake_user,
            ATOMIC_OT_inspection_duplicate,
            ATOMIC_OT_inspection_delete]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)
