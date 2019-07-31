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

This file contains the user interface for Atomic's statistics subpanel.

The statistics panel is nested in the main Atomic Data Manager panel. This
panel contains statistics about the Blender file and each data category in
it.

"""

import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class
from atomic_data_manager.stats import count
from atomic_data_manager.stats import misc
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Statistics SubPanel
class ATOMIC_PT_stats_panel(bpy.types.Panel):
    """The Atomic Data Manager \"Stats for Nerds\" panel"""
    bl_idname = "ATOMIC_PT_stats_panel"
    bl_label = "Stats for Nerds"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_parent_id = "ATOMIC_PT_main_panel"

    def draw(self, context):
        layout = self.layout
        atom = bpy.context.scene.atomic

        # categories selector / header
        row = layout.row()
        row.label(text="Categories:")
        row.prop(atom, "stats_mode", expand=True, icon_only=True)

        # statistics box
        box = layout.box()

        # overview statistics
        if atom.stats_mode == 'OVERVIEW':

            # category header label
            row = box.row()
            row.label(text="Overview", icon='FILE')

            # blender project file size statistic
            row = box.row()
            row.label(text="Blend File Size:     " + misc.blend_size())

            # cateogry statistics
            split = box.split()

            # left column
            col = split.column()

            # left column category labels
            col.label(text="Collections")
            col.label(text="Lights")
            col.label(text="Node Groups")
            col.label(text="Textures")

            col = split.column()

            # collection count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.collections()),
                    count.collections_unused()
                )
            )

            # light count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.lights()),
                    count.lights_unused()
                )
            )

            # node group count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.node_groups()),
                    count.node_groups_unused()
                )
            )

            # texture count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.textures()),
                    count.textures_unused()
                )
            )

            # right column
            col = split.column()

            # right column category labels
            col.label(text="Images")
            col.label(text="Materials")
            col.label(text="Particles")
            col.label(text="Worlds")

            col = split.column()

            # image count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.images()),
                    count.images_unused()
                )
            )

            # material count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.materials()),
                    count.materials_unused()
                )
            )

            # particle system count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.particles()),
                    count.particles_unused()
                )
            )

            # world count
            col.label(
                text=ui_layouts.number_suffix(
                    str(count.worlds()),
                    count.worlds_unused()
                )
            )

        # collection statistics
        elif atom.stats_mode == 'COLLECTIONS':

            # category header label
            row = box.row()
            row.label(text="Collections", icon='GROUP')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.collections())
            )

            # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.collections_unused())
            )

            col.label(
                text="Unnamed: {0}".format(count.collections_unnamed())
            )

        # image statistics
        elif atom.stats_mode == 'IMAGES':

            # category header label
            row = box.row()
            row.label(text="Images", icon='IMAGE_DATA')

            split = box.split()

            # total and missing count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.images())
            )

            col.label(
                text="Missing: {0}".format(count.images_missing())
            )

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.images_unused())
            )
            col.label(
                text="Unnamed: {0}".format(count.images_unnamed())
            )

        # light statistics
        elif atom.stats_mode == 'LIGHTS':
            row = box.row()
            row.label(text="Lights", icon='LIGHT')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.lights())
            )

            # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.lights_unused())
            )

            col.label(
                text="Unnamed: {0}".format(count.lights_unnamed())
            )

        # material statistics
        elif atom.stats_mode == 'MATERIALS':

            # category header label
            row = box.row()
            row.label(text="Materials", icon='MATERIAL')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.materials())
            )

            # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.materials_unused())
            )

            col.label(
                text="Unnamed: {0}".format(count.materials_unnamed())
            )

        # object statistics
        elif atom.stats_mode == 'OBJECTS':

            # category header label
            row = box.row()
            row.label(text="Objects", icon='OBJECT_DATA')

            # total count
            split = box.split()
            col = split.column()

            col.label(
                text="Total: {0}".format(count.objects())
            )

            # unnamed count
            col = split.column()

            col.label(
                text="Unnamed: {0}".format(count.objects_unnamed())
            )

        # node group statistics
        elif atom.stats_mode == 'NODE_GROUPS':

            # category header label
            row = box.row()
            row.label(text="Node Groups", icon='NODETREE')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.node_groups())
            )

            # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()
            col.label(
                text="Unused: {0}".format(count.node_groups_unused())
            )
            col.label(
                text="Unnamed: {0}".format(count.node_groups_unnamed())
            )

        # particle statistics
        elif atom.stats_mode == 'PARTICLES':

            # category header label
            row = box.row()
            row.label(text="Particle Systems", icon='PARTICLES')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.particles())
            )

            # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.particles_unused())
            )

            col.label(
                text="Unnamed: {0}".format(count.particles_unnamed())
            )

        # texture statistics
        elif atom.stats_mode == 'TEXTURES':
            row = box.row()
            row.label(text="Textures", icon='TEXTURE')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.textures())
            )

            # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.textures_unused())
            )

            col.label(
                text="Unnamed: {0}".format(count.textures_unnamed())
            )

        # world statistics
        elif atom.stats_mode == 'WORLDS':
            row = box.row()
            row.label(text="Worlds", icon='WORLD')

            split = box.split()

            # total and placeholder count
            col = split.column()

            col.label(
                text="Total: {0}".format(count.worlds())
            )

            # # col.label(text="Placeholder")  # TODO: remove placeholder

            # unused and unnamed count
            col = split.column()

            col.label(
                text="Unused: {0}".format(count.worlds_unused())
            )

            col.label(
                text="Unnamed: {0}".format(count.worlds_unnamed())
            )


reg_list = [ATOMIC_PT_stats_panel]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
