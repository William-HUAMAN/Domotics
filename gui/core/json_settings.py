# ///////////////////////////////////////////////////////////////
#
# BY:WILLIAM HUAMÁN HUAMÁN
# PROJECT: E-THAN
# V: 1.0.0
#
# The present work is a simplified version of a Domotics Project,
# making use of a virtual assistant oriented to the management of
# some tasks that can be presented inside the house.
#
# ///////////////////////////////////////////////////////////////


# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////
    json_file = "settings.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Settings, self).__init__()

        # DICTIONARY WITH SETTINGS
        # Just to have objects references
        self.items = {}

        # DESERIALIZE
        self.deserialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # READ JSON FILE
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings
