# Bandit Level 1 → Level 2

## Level Goal
The password for the next level is stored in a file called - located in the home directory

Commands you may need to solve this level
`ls` , `cd` , `cat` , `file` , `du` , `find`

Helpful Reading Material
- Google Search for “dashed filename”
- Advanced Bash-scripting Guide - Chapter 3 - Special Characters

---
## Writeup
Upon successful login, we find we are in our home directory we can see this with the present working directory command `pwd`

[INSERT PWD output]

Listing the contents of our home directory we can see that we have a file called readme.

[INSERT LS OUTPUT]

We can output the contents of this file with the `cat` command. The trick to this level is that if you use a - character at the start of a file name, the cat program thinks that we are going to supply an option to the cat program. We can ensure that cat knows it is a file name by specifying this directory `cat ./-`

[INSERT CAT OUTPUT]

'''bash
pwd
ls -la
cat ./-
'''

bandit2:rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

---
# How to Replicate Level 1 → Level 2

