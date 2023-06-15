# Basics of Scripting in Python

# Libraries and Module
# Module is a collection of function
# Library is a collection of modules and much heftier version.
#
# Seven "core" modules in Python (no need to install them are pre-built)
# sys ---> for system
#
# import sys
#
# # Get Python Version
# print(sys.version)
#
# import os       ### os for operating system and files n folders
#
# # Get current working directory
# print(os.getcwd())
# # os.chdir()
#
# import subprocess       # Lets this file work with other programs
#
# subprocess.run(["python", "hello_world.py"])

# import  math
#
# pi = math.pi
# pi_string = str(pi)
# print("The value of pi is" + pi_string)

# import random
# random = random.randrange(1, 15)
# print(random)
#
# import datetime
#
# whatisthedate = datetime.datetime.now()
# print(whatisthedate)

import json         # mainly used to translate data/ communicate between two systems

x = {
    "name": "neha",
    "age": 30,
    "city": "Amritsar"
}

y = json.dumps(x)

print(type(x))
print(type(y))











