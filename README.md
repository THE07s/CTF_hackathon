# Bandito
Just like Bandit... but tiny, and portable.

## Introduction
A lightweight containerised clone of OverTheWire's https://overthewire.org/wargames/bandit/ Bandit wargame. This project was borne as a part of project PWN (Portable Wargame NUC) to be able to deploy and play Wargames, CTFs, and Vulnerable VMs without internet access.

## Methodology
I believe that I can create a reproducible environment to practice Linux skills by utilising Docker, Ansible, Bash, and Python scripting.
Recreating each level of Bandit as I play through them will be similar to creating a writeup but incorporating the system administration and DevOps skills as I use them to help reinforce the learning.

Docker will be used to deploy a fresh instance of Alpine Linux and use Ansible Playbooks to build the Bandito environment level by level. Scripting languages such as Bash and Python will be utilised for automating Operating system-level tasks such as creating files/folders, randomising strings, creating users setting permissions etc.

Undertaking a project to create a Dockerized wargame like Bandit involves various skills across multiple domains:

**System Administration and Docker Skills**
Docker Proficiency: Learning how to create, build, and manage Docker containers, understanding Dockerfile, building container images, networking, and container orchestration.

**Linux System Administration:** Configuring SSH, managing users, understanding system files (e.g., sshd_config), working with permissions and configurations.

**Cybersecurity and Wargaming**
Security Fundamentals: Understanding security protocols, configuring SSH securely, managing user access, and considering the principles of least privilege.
Wargaming Concepts: Designing challenges, levels, or puzzles to improve user understanding of security concepts, including basic Unix commands, privilege escalation, cryptography, etc.

**Scripting and Automation**
Scripting Languages: Utilizing scripting languages like Bash, Python, or other languages to automate user creation, level setup, or challenges.
Automation Techniques: Using scripts or tools to automate repetitive tasks and configurations.

**Software Development Principles**
Version Control: Utilizing Git for version control, branching, committing, and pushing changes.
Continuous Integration: Implementing CI/CD pipelines for the project to automate building and testing.

**Problem-Solving and Troubleshooting**
Problem Identification: Analyzing errors, logs, and debugging to identify issues within the container or the SSH setup.
Critical Thinking: Developing challenges that require creative problem-solving and thinking outside the box.

## Requirements
- Docker - https://www.docker.com/

## Deployment
- TODO

## Acknowledgements
- OverTheWire https://overthewire.org/ - For creating the original Bandit.
- Alpine Linux https://www.alpinelinux.org/ - Creating a lightweight Linux distribution
- Deselikem https://dev.to/github/publishing-a-docker-image-to-githubs-container-repository-4n50 - 
