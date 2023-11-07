# Level 0-1

## Level Goal
The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

## Commands you may need to solve this level
`ls`,`cd`,`cat`,`file`,`du`,`find`

---
# Writeup
We will first ensure we are in our home directory with the `cd` commaand, we will then list all files including hidden files using `ls -la` and finally we will output the contents of readme by running `cat readme`

```bash
cd
ls -la
cat /home/bandit0/readme`
```
bandit1:NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

<img width="650" alt="image" src="https://github.com/rmcmillan34/bandito/assets/16860457/f70e47a9-02f7-45a7-a2c1-26e631e14cc9">

---
# How to replicate Level 1
- Create a bandito1 player and password
- Give bandito1 player access to the SSH game port (2222)
- Create a readme file with bandito1 password as the contents
- Configure the home directory as follows:
  
<img width="650" alt="image" src="https://github.com/rmcmillan34/bandito/assets/16860457/601c90b1-2fda-4f29-a2c0-ab83bd52934d">

Bandit1 has read-write permission as the owner of the readme file, bandit0 group has read-only permissions for the readme text file. `chmod 640 readme`

