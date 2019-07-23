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
from atomic_data_manager.stats import stats
from atomic_data_manager.stats import count
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Statistics SubPanel
class ATOMIC_PT_stats_panel(bpy.types.Panel):
    """
    The statistics panel is nested in the main Atomic Data Manager panel.
    This panel contains statistics about the file and each data set in the Blender file.
    """
    bl_idname = "ATOMIC_PT_stats_panel"
    bl_label = "Stats for Nerds"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_parent_id = "ATOMIC_PT_main_panel"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic

        row = layout.row()
        row.label(text="Categories:")
        row.prop(atom, "stats_mode", expand=True, icon_only=True)

        box = layout.box()

        # UI Implementation
        # OVERVIEW
        if atom.stats_mode == 'OVERVIEW':
            row = box.row()
            row.label(text="Overview", icon='FILE')

            # BLEND FILE SIZE STATISTIC
            row = box.row()
            row.label(text="Blend File Size:     " + stats.blend_size())

            # DATA SET STATISTICS
            split = box.split()

            # LEFT COLUMN
            col = split.column()
            col.label(text="Collections")
            col.label(text="Lights")
            col.label(text="Node Groups")
            col.label(text="Textures")

            col = split.column()
            col.label(
                text=ui_layouts.number_suffix(str(count.collections()), count.unused_collections()))
            col.label(
                text=ui_layouts.number_suffix(str(count.lights()), count.unused_lights()))
            col.label(
                text=ui_layouts.number_suffix(str(count.node_groups()), count.unused_node_groups()))
            col.label(
                text=ui_layouts.number_suffix(str(count.textures()), count.unused_textures()))

            # RIGHT COLUMN
            col = split.column()
            col.label(text="Images")
            col.label(text="Materials")
            col.label(text="Particles")
            col.label(text="Worlds")

            col = split.column()
            col.label(
                text=ui_layouts.number_suffix(str(count.images()), count.unused_images()))
            col.label(
                text=ui_layouts.number_suffix(str(count.materials()), count.unused_materials()))
            col.label(
                text=ui_layouts.number_suffix(str(count.particles()), count.unused_particles()))
            col.label(
                text=ui_layouts.number_suffix(str(count.worlds()), count.unused_worlds()))

        # COLLECTIONS
        elif atom.stats_mode == 'COLLECTIONS':
            row = box.row()
            row.label(text="Collections", icon='GROUP')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.collections()))
            # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_collections()))
            col.label(text="Unnamed: {0}".format(count.unnamed_collections()))

        # IMAGES
        elif atom.stats_mode == 'IMAGES':
            row = box.row()
            row.label(text="Images", icon='IMAGE_DATA')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.images()))
            col.label(text="Missing: {0}".format(count.missing_images()))

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_images()))
            col.label(text="Unnamed: {0}".format(count.unnamed_images()))

        # LIGHTS
        elif atom.stats_mode == 'LIGHTS':
            row = box.row()
            row.label(text="Lights", icon='LIGHT')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.lights()))
            # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_lights()))
            col.label(text="Unnamed: {0}".format(count.unnamed_lights()))

        # MATERIALS
        elif atom.stats_mode == 'MATERIALS':
            row = box.row()
            row.label(text="Materials", icon='MATERIAL')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.materials()))
            # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_materials()))
            col.label(text="Unnamed: {0}".format(count.unnamed_materials()))

        # OBJECTS
        elif atom.stats_mode == 'OBJECTS':
            row = box.row()
            row.label(text="Objects", icon='OBJECT_DATA')

            split = box.split()
            col = split.column()
            col.label(text="Total: {0}".format(count.objects()))

            col = split.column()
            col.label(text="Unnamed: {0}".format(count.unnamed_objects()))

        # NODE GROUPS
        elif atom.stats_mode == 'NODE_GROUPS':
            row = box.row()
            row.label(text="Node Groups", icon='NODETREE')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.node_groups()))
            # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_node_groups()))
            col.label(text="Unnamed: {0}".format(count.unnamed_node_groups()))

        # PARTICLES
        elif atom.stats_mode == 'PARTICLES':
            row = box.row()
            row.label(text="Particle Systems", icon='PARTICLES')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.particles()))
            # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_particles()))
            col.label(text="Unnamed: {0}".format(count.unnamed_particles()))

        # TEXTURES
        elif atom.stats_mode == 'TEXTURES':
            row = box.row()
            row.label(text="Textures", icon='TEXTURE')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.textures()))
            # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_textures()))
            col.label(text="Unnamed: {0}".format(count.unnamed_textures()))

        # WORLDS
        elif atom.stats_mode == 'WORLDS':
            row = box.row()
            row.label(text="Worlds", icon='WORLD')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(count.worlds()))
            # # col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(count.unused_worlds()))
            col.label(text="Unnamed: {0}".format(count.unnamed_worlds()))


reg_list = [ATOMIC_PT_stats_panel]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
