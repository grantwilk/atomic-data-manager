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

This file handles the registration of the atomic_data_manager.ui package

"""

from atomic_data_manager.ui import main_panel_ui
from atomic_data_manager.ui import stats_panel_ui
from atomic_data_manager.ui import inspect_ui
from atomic_data_manager.ui import missing_file_ui
from atomic_data_manager.ui import missing_file_ui
from atomic_data_manager.ui import pie_menu_ui
from atomic_data_manager.ui import preferences_ui
from atomic_data_manager.ui import support_me_ui


def register():
    # register preferences first so we can access variables in config.py
    preferences_ui.register()

    # register everything else
    main_panel_ui.register()
    stats_panel_ui.register()
    inspect_ui.register()
    missing_file_ui.register()
    pie_menu_ui.register()
    support_me_ui.register()


def unregister():
    main_panel_ui.unregister()
    stats_panel_ui.unregister()
    inspect_ui.unregister()
    missing_file_ui.unregister()
    pie_menu_ui.unregister()
    preferences_ui.unregister()
    support_me_ui.unregister()
