# Bandit Level 0
## Level Goal
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

## Commands you may need to solve this level
`ssh`

## Helpful Reading Material
[Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
[How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)

---
# Walkthrough
Using the SSH information log into the bandit server using the credentials provided.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

On successful login, go to [level 1](level0-1.md) challenge to try advance to the next level.

---
# How to replicate Level 0
