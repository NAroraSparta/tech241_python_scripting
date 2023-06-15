Create GitHub Repos for all your folders and sync to them.
Make a new repo called "tech241_python_scripting"
make a README.md
Inside cover:

 ```python

What is scripting?

#  Piece of code which you can use to automate a repetitive task.
# Saves time and takes away human error.

 Scripting refers to the process of writing and executing scripts, which are sets of 
instructions or commands written in a programming or scripting language. Scripts are 
typically used to automate tasks, perform repetitive actions, and streamline processes.
In the context of DevOps, scripting plays a crucial role in enabling efficient and
consistent software development, deployment, and operations.

```python_scripting

# Scripting vs Programming
Script is only ever 1 file and very targeted, specific to the task, simple to read, limited scope, written in high-level language(can be read and understood by humans)

Programming is lots of codes, wide scope, flexible and complex to grasp and low-level language(can only be read and understood by machines)

Python is easy, libraries help a lot, Language interoperability, large community, open source(lots of free plugins)
```
```python
Why is scripting important for Devops engineers?
 1. Automation
2. Configuration management...-> IaC--> Config management and Orchestration
Here are just some examples of way we use scripts in DevOps:

1. Python script to query a database
2. Python script to execute a shell command or script
3. Query logs for alerts
4. Python script to take a backup
5. Python script for K8 containers
6. Python script to fetch I.P's of an autoscaling group
7. Lambda function to stop instances on a weekend
8. Python script for ETL jobs
9. Find the expiry date of an SSL certificate
10. Develop CLI applications using Python
11. Automating CRUD(create, read, update and delete)
12. Custom scripts for config management
```

```
Few reasons why scripting is important for DevOps engineers:

Automation: DevOps aims to automate various aspects of software development, deployment,
 and infrastructure management. Scripting allows DevOps engineers to automate routine 
 tasks, such as building and deploying applications, provisioning and configuring 
 infrastructure, monitoring system health, and more. Automation through scripting saves 
 time, reduces errors, and increases productivity.

Infrastructure as Code (IaC): In DevOps, infrastructure is often managed through code 
using IaC principles. Scripting allows engineers to define and configure infrastructure
components, such as servers, networks, and storage, using scripts. These scripts can be
 version controlled, easily replicated, and shared among team members. By scripting 
 infrastructure, DevOps engineers can ensure consistency, scalability, and 
 reproducibility across different environments.

Configuration Management: Scripting helps in managing and maintaining consistent configurations across various systems and environments. Tools like Puppet, Chef, Ansible, or PowerShell DSC (Desired State Configuration) use scripts to define and enforce system configurations. DevOps engineers can write scripts to install software packages, configure settings, and manage dependencies, ensuring that systems are correctly provisioned and configured.

Continuous Integration and Deployment (CI/CD): CI/CD is a critical practice in DevOps, enabling rapid and frequent software releases. Scripting allows DevOps engineers to define the steps involved in the CI/CD pipeline, including building, testing, and deploying applications. With scripts, engineers can automate the entire process, ensuring consistent and reliable deployments across different environments.

Troubleshooting and Debugging: When issues arise in the development or production environment, scripting can be invaluable for troubleshooting and debugging. By writing scripts, DevOps engineers can collect diagnostic information, analyze logs, perform tests, and investigate system behavior more efficiently. Scripts can automate repetitive troubleshooting steps, allowing engineers to quickly identify and resolve problems.

```


 
```python
Bonus: Example of a simple script

print("Hello World")
```

```python
For Scripting, use the following pointers:

Clear names
Arguments should be obvious
Remember to use return
Use comments
Type hints so that you know what it was meant for.
```
```python

Important Python Modules for DevOps
    
    
os (Interacting with the operating system)
platform (Access to underlying platform data)
subprocess (Subprocess management)
sys (System specific parameters and functions)
psutil (Process and system utilities)
re (Regular Expression Operations)
scapy (Packet manipulation)
Requests (HTTP library)
urllib3 (HTTP client)
logging (Error logging)
getpass (Portable password input)
boto3 (AWK Software development kit, SDK. Allows interaction with AWS from Python)
paramiko (SSH)
JSON (JSON encoder and decoder
PyYAML (YAML parser & emitter for Python)
pandas (Data science, but useful for automating CSV's)
smtplib (STMP)
```
```python


# Basics of Scripting in Python

# Libraries and Module
# Module is a collection of function
# Library is a collection of modules and much heftier version.
```
```python
# Seven "core" modules in Python (no need to install them are pre-built)
# sys ---> for system
#
# import sys
#
# # Get Python Version
# print(sys.version)
```
```

# import os       ### os for operating system and files n folders
#
# # Get current working directory
# print(os.getcwd())
# # os.chdir()
```
```
#
# import subprocess       # Lets this file work with other programs
#
# subprocess.run(["python", "hello_world.py"])
```
```
# import  math
#
# pi = math.pi
# pi_string = str(pi)
# print("The value of pi is" + pi_string)
```

```
# import random
# random = random.randrange(1, 15)
# print(random)
```
```
# import datetime
#
# whatisthedate = datetime.datetime.now()
# print(whatisthedate)
```
```
import json         # mainly used to translate data/ communicate between two systems

x = {
    "name": "neha",
    "age": 30,
    "city": "Amritsar"
}

y = json.dumps(x)

print(type(x))
print(type(y))
```
```
# Using os to do things

import  os
#
# os.system("echo 'Hello world!")

# Make and change directories

# Change a directory

directory = 'test_dir1'

parent_dir = "C:/Users/Venkat"

path = os.path.join(parent_dir, directory)
```
```
# Create Directory

# os.mkdir(path)

# Putting a new file in the new directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    tofile = "Contents of the file is written here"
    file1.write(tofile)

print("File " + filename + " created in " + directory + " folder")
```
```python
import os
import subprocess

# Stores the file path to the current file
script_dir = os.path.dirname(__file__)

# Stores the filepath to the script you want to run
script_absolute_path = os.path.join(script_dir + "/shell_script.sh")

# Calls the shell file and runs it
subprocess.call(['sh', script_absolute_path])
```













