import importlib.util
import os
import sys
from os.path import isfile, join
from pathlib import Path

import flet as ft





class Mod:
    def __init__(self, module_name, file_path, __index = 0):
        self.module_name = module_name,
        self.file_path = file_path,
        self.index = __index,


class ModuleHandler():
    def __init__(self, __mod_list = []):
        test_mod = Mod('.AppBar', 'appbar')
        __mod_list = [test_mod]
        for mod in __mod_list:
            module_name = mod.module_name
            file_path =mod.file_path
            self.import_modules(module_name, file_path)
            # self.selected_control_group = self.control_groups[0]

    def import_modules(self, module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        print(f"{module_name!r} has been imported")
        
ModuleHandler()