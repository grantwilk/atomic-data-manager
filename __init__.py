"""
Copyright (C) 2019 Grant Wilk

This file is part of Data MGR.

Data MGR is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Data MGR is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with Data MGR.  If not, see <https://www.gnu.org/licenses/>.
"""


import bpy
from bpy.utils import register_class, unregister_class
from atomic_data_manager import ui, ops

bl_info = {
    "name": "Data Manager",
    "author": "Grant Wilk",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "location": "Properties > Scene",
    "category": "Data",
    "description": "An advanced set of data management tools for Blender.",
    "wiki_url": "https://github.com/grantwilk/Data-Manager-Beta",  # TODO
    "tracker_url": "https://github.com/grantwilk/Data-Manager-Beta"  # TODO
}


# Data MGR Properties
class DATAMGR_PG_main(bpy.types.PropertyGroup):
    # Main Panel Toggle Buttons
    collections: bpy.props.BoolProperty(default=False)
    images: bpy.props.BoolProperty(default=False)
    lights: bpy.props.BoolProperty(default=False)
    materials: bpy.props.BoolProperty(default=False)
    node_groups: bpy.props.BoolProperty(default=False)
    particles: bpy.props.BoolProperty(default=False)
    textures: bpy.props.BoolProperty(default=False)
    worlds: bpy.props.BoolProperty(default=False)

    # Inspect Datablock Search Fields
    collections_field: bpy.props.StringProperty()
    images_field: bpy.props.StringProperty()
    lights_field: bpy.props.StringProperty()
    materials_field: bpy.props.StringProperty()
    node_groups_field: bpy.props.StringProperty()
    particles_field: bpy.props.StringProperty()
    textures_field: bpy.props.StringProperty()
    worlds_field: bpy.props.StringProperty()

    # Other Properties
    active_inspection: bpy.props.EnumProperty(
        items=[('COLLECTIONS', 'Collections', 'Collections'),
               ('IMAGES', 'Images', 'Images'),
               ('LIGHTS', 'Lights', 'Lights'),
               ('MATERIALS', 'Materials', 'Materials'),
               ('NODE_GROUPS', 'Node Groups', 'Node Groups'),
               ('PARTICLES', 'Particles', 'Particles'),
               ('TEXTURES', 'Textures', 'Textures'),
               ('WORLDS', 'Worlds', 'Worlds')],
        default='COLLECTIONS'
    )

    stats_mode: bpy.props.EnumProperty(
        items=[('OVERVIEW', 'Overview', 'Overview', 'FILE', 0),
               ('COLLECTIONS', 'Collections', 'Collections', 'GROUP', 1),
               ('IMAGES', 'Images', 'Images', 'IMAGE_DATA', 2),
               ('LIGHTS', 'Lights', 'Lights', 'LIGHT', 3),
               ('MATERIALS', 'Materials', 'Materials', 'MATERIAL', 4),
               ('OBJECTS', 'Objects', 'Objects', 'OBJECT_DATA', 5),
               ('NODE_GROUPS', 'Node Groups', 'Node Groups', 'NODETREE', 6),
               ('PARTICLES', 'Particle Systems', 'Particle Systems', 'PARTICLES', 7),
               ('TEXTURES', 'Textures', 'Textures', 'TEXTURE', 8),
               ('WORLDS', 'Worlds', 'Worlds', 'WORLD', 9)],
        default='OVERVIEW'
    )

    rename_field: bpy.props.StringProperty()
    replace_field: bpy.props.StringProperty()


def register():
    register_class(DATAMGR_PG_main)
    bpy.types.Scene.datamgr = bpy.props.PointerProperty(type=DATAMGR_PG_main)

    ui.register()
    ops.register()


def unregister():
    unregister_class(DATAMGR_PG_main)
    del bpy.types.Scene.datamgr

    ui.unregister()
    ops.unregister()

