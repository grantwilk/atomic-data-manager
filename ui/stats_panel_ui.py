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
from atomic_data_manager.ui.utils import blendstats
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Statistics SubPanel
class DATAMGR_PT_stats_panel(bpy.types.Panel):
    """
    The statistics panel is nested in the main Atomic Data Manager panel.
    This panel contains statistics about the file and each data set in the Blender file.
    """
    bl_label = "Stats for Nerds"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_parent_id = "DATAMGR_PT_main_panel"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr

        row = layout.row()
        row.label(text="Data Sets:")
        row.prop(dmgr, "stats_mode", expand=True, icon_only=True)

        box = layout.box()

        # UI Implementation
        # OVERVIEW
        if dmgr.stats_mode == 'OVERVIEW':
            row = box.row()
            row.label(text="Overview", icon='FILE')

            # BLEND FILE SIZE STATISTIC
            row = box.row()
            row.label(text="Blend File Size:     " + blendstats.blend_size())

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
                text=ui_layouts.number_suffix(str(blendstats.count_collections()), blendstats.count_unused_collections()))
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_lights()), blendstats.count_unused_lights()))
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_node_groups()), blendstats.count_unused_node_groups()))
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_textures()), blendstats.count_unused_textures()))

            # RIGHT COLUMN
            col = split.column()
            col.label(text="Images")
            col.label(text="Materials")
            col.label(text="Particles")
            col.label(text="Worlds")

            col = split.column()
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_images()), blendstats.count_unused_images()))
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_materials()), blendstats.count_unused_materials()))
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_particles()), blendstats.count_unused_particles()))
            col.label(
                text=ui_layouts.number_suffix(str(blendstats.count_worlds()), blendstats.count_unused_worlds()))

        # COLLECTIONS
        elif dmgr.stats_mode == 'COLLECTIONS':
            row = box.row()
            row.label(text="Collections", icon='GROUP')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_collections()))
            col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_collections()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_collections()))

        # IMAGES
        elif dmgr.stats_mode == 'IMAGES':
            row = box.row()
            row.label(text="Images", icon='IMAGE_DATA')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_images()))
            col.label(text="Placeholder")  # todo
            col.separator()
            col.label(text="Total Size: {0}".format(blendstats.images_size()))

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_images()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_images()))
            col.separator()
            col.label(text="Unused Size: {0}".format(blendstats.images_unused_size()))

        # LIGHTS
        elif dmgr.stats_mode == 'LIGHTS':
            row = box.row()
            row.label(text="Lights", icon='LIGHT')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_lights()))
            col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_lights()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_lights()))

        # MATERIALS
        elif dmgr.stats_mode == 'MATERIALS':
            row = box.row()
            row.label(text="Materials", icon='MATERIAL')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_materials()))
            col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_materials()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_materials()))

        # OBJECTS
        elif dmgr.stats_mode == 'OBJECTS':
            row = box.row()
            row.label(text="Objects", icon='OBJECT_DATA')

            split = box.split()
            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_objects()))

            col = split.column()
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_objects()))

        # NODE GROUPS
        elif dmgr.stats_mode == 'NODE_GROUPS':
            row = box.row()
            row.label(text="Node Groups", icon='NODETREE')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_node_groups()))
            col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_node_groups()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_node_groups()))

        # PARTICLES
        elif dmgr.stats_mode == 'PARTICLES':
            row = box.row()
            row.label(text="Particle Systems", icon='PARTICLES')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_particles()))
            col.label(text="Placeholder")  # todo
            col.separator()
            col.label(text="Particles: {0}".format(blendstats.count_emitted_particles()))

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_particles()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_particles()))
            col.separator()
            col.label(text="Visible: {0}".format(blendstats.count_emitted_particles_visible()))

        # TEXTURES
        elif dmgr.stats_mode == 'TEXTURES':
            row = box.row()
            row.label(text="Textures", icon='TEXTURE')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_textures()))
            col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_textures()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_textures()))

        # WORLDS
        elif dmgr.stats_mode == 'WORLDS':
            row = box.row()
            row.label(text="Worlds", icon='WORLD')

            split = box.split()

            col = split.column()
            col.label(text="Total: {0}".format(blendstats.count_worlds()))
            col.label(text="Placeholder")  # todo

            col = split.column()
            col.label(text="Unused: {0}".format(blendstats.count_unused_worlds()))
            col.label(text="Unnamed: {0}".format(blendstats.count_unnamed_worlds()))


reg_list = [DATAMGR_PT_stats_panel]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)