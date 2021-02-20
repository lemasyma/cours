---
title:          "DEVI: Presentation"
date:           2021-02-18 14:00
categories:     [Image S8, DEVI]
tags:           [Image, DEVI, S8]
description: Presentation
---
Lien de la [note Hackmd](https://hackmd.io/@lemasymasa/SkrIFCi-d)

Joseph Chazalon, Clement Demoulins
February 2021
EPITA Research & Development Laboratory (LRDE)

# About this course
This is a course about *containers* using **Docker**
- What it is
- How to use it for simple, then less simple cases
- Practice

# Tools an grading
Graded content for *each sessions* using *Moodle*
- For sessions 1 and 2: 10 min quiz on Moodle at the end of each session

# Software stack illustrated
A real case of 2 incompatible software stacks we had to handle
![](https://i.imgur.com/qdNKnkp.png)

## Many solutions
- Use libs with forward/backwared compatibility
- FIx bad dependency declarations in packages
- Use lnagugae compatibility layer
- Rebuild stuff manually
- Install various versions of libs at different places

## Dependency hell
When you have to rebuild manually, step by step, all your software stack checking each dependency

## What are you paid for ?
Waht you really want is simply to separate:
- your development & product software stack
- your os & userland software stack

*And what about deployement ?*

## Deployement challenge
![](https://i.imgur.com/xxvZddk.png)

## Solutions
- Containers
    - Beaucoup plus leger
    - Demarrage presque immediat
- Virtual Machines
    - Emuler le systeme d'exploitation
    - Devoir reserver RAM, CPU, etc.
    - On peut avoir plusieurs VMs sur une meme machine

Containers and virtual machines
- are 2 good solutions to software stack isolation
- have similar resource isolation and allocation benefits(CPU, mem, net & disk IO)
- but function differently because
    - containers virtualize the OS (the kernel)
    - instead of hardware
- so containers are
    - lighter and faster than VMs (min storage)
    - more portable
    - less secure

# Docker
## Promises
1. lightweight
2. easy deployement

## Benefits for dev
Build once... run anywhere
- portable runtime env
- no worries about missing dependencies
- run each app in its own isolated container
- Automate testing, integration, packaging

## Befenits for admin
Configure once... run anything
- Make the entire lifecycle more efficient, consistent and repeatable
- Increase the quality of code

## Docker adoption
<div class="alert alert-info" role="alert" markdown="1">
Docker was launched **in 2013 (8 years ago)** and became a massive trend.
</div>
- Github project search "docker" $\rightarrow$ $\gt$ 45 000 projects

## Reasons for NOT using (Docker) containers (currently)
- Archive your program (because it is not made for that)
- Your program uses OSX primitives
- ~~Your program runs on Windows only~~
- You need to deploy many containers on clusters

## Demo1: VSCode Remote Container
![](https://i.imgur.com/IUDCpqd.png)

## Implementation of Docker Containers
Under the hood, Docker is built on the following components:
- The Go programming language
- The following features of the Linux kernel
    - Namespaces
    - groups
    - capabilities

### Namespaces
According to *man namespaces*:
> A namespace wraps a global system resource in an abstraction that **makes it appear to the processes within the namespace** that hey have their own isolated instance of the global resource.  Changes to the global resource are visible to other processes that are members of the namespace, but  are invisible to other processes.  One use of namespaces is to implement containers.


### Cgroups
According to *man cgroups*
> Control  groups, usually referred to as cgroups, are a Linux kernel feature which allow processes to be organized into hierarchical groups whose usage of various types of resources can then be limited and monitored.  The kernel's cgroup interface is provided through a  pseudo-filesystem  called cgroupfs.   Grouping is implemented in the core cgroup kernel code, while resource tracking and limits are implemented in a set of per-resource-type subsystems (memory, CPU, and so on).


### Capabilites
According to **man capabilities**:
> Traditional UNIX implementations distinguish two categories of processes: privileged processes (whose effective user ID is 0, referred to as superuser or root), and unprivileged processes (whose effective UID is nonzero).  Privileged processes bypass  all  kernel permission checks, while unprivileged processes are subject to full permission checking based on the process's credentials (usu ally: effective UID, effective GID, and supplementary group list). Starting with kernel 2.2, Linux divides the privileges traditionally associated with superuser into distinct units, known as capabilities, which can be independently enabled and disabled.  Capabilities are a per-thread attribute.

## Open Container Initiative runtime (container) specifications
Container configuration, lifecycle, and how to rpx them using JSON files.
- creating
    - the container is being created
- created
    - the runtime has finished the create operation, and the container process has neither exited nor executed the user-specified program
- running
    - the container process has executed the user-specified program but has not exited
- stopped

## Open Container Initiative image specifications
An image stores the files for the root FS of a *container*, ie the files or containerized program will see

Problem(s)
- Many containers share the same basis (Ubuntum Alpine, Debian, etc.)
- because we do not want to rebuild a complete software stajc by hand down to the kernel

Solution:
- Split images into meaningful **layers** *Ubuntu base, Python dependencies, App...*
- **Share common layers** between containers in read-only
- Add a **thin writable layer** on top of this stack of layers
- View this stack as a **single, consistent and writable filesystem**

### Image Layers
Efficiency implemented using *Copy-on-Write (COW)*
![](https://i.imgur.com/M6H0few.png)

## Open Container Initiative distribution specifications
API protocol to facilitate distribution of images:
- What is a repository
- How to list, pull, push images
- HTTP API

## Images and containers
When using Dokcer, you think about *images* and *containers*
![](https://i.imgur.com/LhPOzCy.png)

## Good to remember
* A (Docker) *container* is just:
    * a root filesystem with some bind mounts containing all the software stack down to the kernel
    * a control policy enforced by the kernel with some isolation mechanisms: PID, network, etc.
    * some environment variables, kernel configuration and automatically generated file: for hostname, DNS resolution, etc.
    * *an abstract view of a group of processes not even a single kernel object*

# Using Docker
## Regular workflow
1. Obtain an image
``` bash
docker image pull USER/IMAGENAME:TAG
docker image import ARCHIVE
docker image build ...
```
2. Create a container for image
``` bash
docker container create --name CONTAINER_NAME IMAGE
```
3. Start the container
``` bash
docker container start CONTAINER_NAME
```
4. (opt.) execute more programs within the container
``` bash
docker container exec CONTAINER_NAME
```
5. Attach your console to the container
``` bash
docker container
```
6. manage/monitor the container

# Container storage explained
## Storage overview
![](https://i.imgur.com/fcCOfax.png)

## Where is Docker data stored ?
Under `var/lib/docker`

## Base image content
![](https://i.imgur.com/hjtKZTn.png)

## Bind mounts
![](https://i.imgur.com/zI8A1WU.png)

## Volumes
What
- Shareable space management by Docker
- Can bes used to share data between container
- Create using docker `volume create VOLNAME` or `--volume` or `--mount type=volume` on start/run
- **Survive container removal**: must be removed manually

Where
- Stored under `/var/lib/docker/volumes/+` name or unique id

## Reusing volumes for another container
It is possible to mount volumes from another container.
This can be convenient in several cases:
- get a shell in a super minimal container
- migrate a database
- upgrade a container

## Fragile isolation with host
- Relies on kernel security
- You can share a lot of things with host
- Many public images run services as *root*