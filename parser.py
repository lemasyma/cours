import os
import sys
import fileinput
import re

replacements = {':::info':'<div class="alert alert-info" role="alert" markdown="1">', ':::warning':'<div class="alert alert-warning" role="alert" markdown="1">', ':::danger':'<div class="alert alert-danger" role="alert" markdown="1">', ':::success':'<div class="alert alert-success" role="alert" markdown="1">', ':::':'</div>'}

is_details = False
lines = []

print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )

# Read in the file
with open(fileToSearch, 'r') as file :
  filedata = file.read()

# Replace the target string
for line in filedata.split('/n'):
    for src, target in replacements.items():
        line = line.replace(src, target)
    lines.append(line)

# Write the file out again
with open(fileToSearch, 'w') as file:
    for line in lines:
        file.write(line)