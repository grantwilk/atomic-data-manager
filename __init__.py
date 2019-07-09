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
from atomic_data_manager import ui, ops
from atomic_data_manager.updater import addon_updater_ops

bl_info = {
    "name": "Atomic Data Manager",
    "author": "Remington Creative",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "location": "Properties > Scene",
    "category": "Data",
    "description": "An advanced set of data management tools for Blender.",
    "wiki_url": "https://remingtoncreative.com/software/blender/atomic-data-manager",
    "tracker_url": "https://github.com/grantwilk/atomic-data-manager/issues"
}


# Atomic Data Manager Properties
class ATOMIC_PG_main(bpy.types.PropertyGroup):
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
        items=[
            ('COLLECTIONS', 'Collections', 'Collections'),
            ('IMAGES', 'Images', 'Images'),
            ('LIGHTS', 'Lights', 'Lights'),
            ('MATERIALS', 'Materials', 'Materials'),
            ('NODE_GROUPS', 'Node Groups', 'Node Groups'),
            ('PARTICLES', 'Particles', 'Particles'),
            ('TEXTURES', 'Textures', 'Textures'),
            ('WORLDS', 'Worlds', 'Worlds')
        ],
        default='COLLECTIONS'
    )

    stats_mode: bpy.props.EnumProperty(
        items=[
            ('OVERVIEW', 'Overview', 'Overview', 'FILE', 0),
            ('COLLECTIONS', 'Collections', 'Collections', 'GROUP', 1),
            ('IMAGES', 'Images', 'Images', 'IMAGE_DATA', 2),
            ('LIGHTS', 'Lights', 'Lights', 'LIGHT', 3),
            ('MATERIALS', 'Materials', 'Materials', 'MATERIAL', 4),
            ('OBJECTS', 'Objects', 'Objects', 'OBJECT_DATA', 5),
            ('NODE_GROUPS', 'Node Groups', 'Node Groups', 'NODETREE', 6),
            ('PARTICLES', 'Particle Systems', 'Particle Systems', 'PARTICLES', 7),
            ('TEXTURES', 'Textures', 'Textures', 'TEXTURE', 8),
            ('WORLDS', 'Worlds', 'Worlds', 'WORLD', 9)
        ],
        default='OVERVIEW'
    )

    rename_field: bpy.props.StringProperty()
    replace_field: bpy.props.StringProperty()


def register():
    # Add-on updater registration
    addon_updater_ops.register(bl_info)

    register_class(ATOMIC_PG_main)
    bpy.types.Scene.atomic = bpy.props.PointerProperty(type=ATOMIC_PG_main)

    # Atomic package registration
    ui.register()
    ops.register()


def unregister():
    # Atomic package unregistration
    ui.unregister()
    ops.unregister()

    unregister_class(ATOMIC_PG_main)
    del bpy.types.Scene.atomic
