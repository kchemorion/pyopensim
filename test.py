#!/usr/bin/env python

import opensim as osim

def check_comak_availability():
    try:
        # Attempt to access a COMAK class, modify this line according to the actual class names used in your installation
        comak_class = osim.COMAKTool()
        print("COMAK is available in this installation of OpenSim.")
    except AttributeError:
        print("COMAK is not available in this installation of OpenSim.")
    except Exception as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    check_comak_availability()
