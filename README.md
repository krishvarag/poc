# poc
Proof Of Concept experiments

# Windows Setup
```
GIT_SSH=plink
create putty fro github.com ; user : git
git clone git@github.com:krishvarag/poc
git push origin HEAD:main

# Method 2 
Add to .gitconfig and store pwd in a file 
[user]
	email = krishvarag@gmail.com
	name = Suresh Krishnan Varaghur

[credential]
   helper = store --file ~/credentials

credentials:
https://krishvarag:TOKEN@github.com
```
