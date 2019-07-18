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

from atomic_data_manager.ops import main_ops, inspect_ops, direct_use_ops, missing_file_ops, support_me_ops


def register():
    main_ops.register()
    inspect_ops.register()
    direct_use_ops.register()
    missing_file_ops.register()
    support_me_ops.register()


def unregister():
    main_ops.unregister()
    inspect_ops.unregister()
    direct_use_ops.unregister()
    missing_file_ops.unregister()
    support_me_ops.unregister()