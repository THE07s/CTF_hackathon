# Bandito
Just like Bandit... but tiny, and portable.

## Introduction
A lightweight containerised clone of OverTheWire's https://overthewire.org/wargames/bandit/ Bandit wargame. This project was borne as a part of project PWN (Portable Wargame NUC) to be able to deploy and play Wargames, CTFs, and Vulnerable VM's without internet access.

## Methodology
My theory is that by utilising Docker, Ansible, Bash, and Python scripting, I can create a reproducible environment to practice Linux skills.
Recreating each level as I play through them will be similar to creating a writeup.

Docker will be used to deploy a fresh instance of Alpine Linux, and use Ansible Playbook's to build the Bandito environment level by level. Scripting languages such as Bash and Python will be utilised for Operating System level tasks such as creating folders, random strings, creating users setting permissions etc.

## Requirements
- Docker - https://www.docker.com/

## Deployment
- TODO

## Acknowledgements
- OverTheWire https://overthewire.org/ - For creating the original Bandit.
- Alpine Linux https://www.alpinelinux.org/ - Creating a lightweight Linux distribution
