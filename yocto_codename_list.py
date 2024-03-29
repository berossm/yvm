"""This module contains the yocto release codenames

This needs to be maintained as new releases are added to the schedule.
The current list is from https://wiki.yoctoproject.org/wiki/Releases
The name list 
"""
import os
import sys

LAST_MAJOR = 5

versions = {"inky": 0.3, "clyde": 0.4, "blinky": 0.5, "pinky": 0.6,
            "purple": 0.7, "green": 0.8, "laverne": 0.9,
            "bernard": 1.0, "edison": 1.1, "denzil": 1.2, "danny": 1.3,
            "dylan": 1.4, "dora": 1.5, "daisy": 1.6, "dizzy": 1.7, "fido": 1.8,
            "jethro": 2.0, "krogoth": 2.1, "morty": 2.2, "pyro": 2.3,
            "rocko": 2.4, "sumo": 2.5, "thud": 2.6, "warrior": 2.7,
            "zeus": 3.0, "dunfell": 3.1, "gatesgarth": 3.2, "hardknott": 3.3, "honister": 3.4,
            "kirkstone": 4.0, "langdale": 4.1, "mickledore": 4.2, "nanbield": 4.3,
            "scarthgap": 5.0}

if __name__ == '__main__':
    short_name = os.path.basename(__file__)
    print(f"This python file ({short_name}) is not intended to be executed directly.")
    sys.exit(1)
