# Bandit Level 0
## Level Goal
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

## Commands you may need to solve this level
`ssh`

## Helpful Reading Material
- [Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)

---
# Walkthrough
Using the SSH information, log into the bandit server using the credentials provided.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

On successful login, go to [level 1](level0-1.md) challenge to attempt to advance to the next level.

---
# How to replicate Level 0
- Create a bandito0 user
- enable SSH on the player SSH port (2222)
- give bandit0 a home directory


In the `/etc/bandit_pass` directory, only the owner has read permissions for the password file. Each bandit password text file is owned by that user, meaning you can only read the password for the currently logged-on user.

<img width="650" alt="image" src="https://github.com/rmcmillan34/bandito/assets/16860457/49da99d7-5690-46eb-944c-22020375dbbc">


