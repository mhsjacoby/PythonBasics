# Git Notes
Author: Maggie Jacoby<br>
Date: January 2021



### Creating a new repo
- `$ git init` the directory
- `$ git add .` all files
- commit
- create new repo in github 
- `$ git remote add origin <github location>`
- `$ git push -u origin master`

ref: https://kbroman.org/github_tutorial/pages/init.html

### Remove and stop tracking files in a repo (eg, .DS_Store)  
- Create a .gitignore file and add all files to untrack
- push changes
- `$ git rm -r --cached .`
- add and commit

ref:  
http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/  
https://www.pluralsight.com/guides/how-to-use-gitignore-file )

### Files to add to .gitignore
```
*/.DS_Store
*/.ipynb_checkpoints
*/__pycache__
.DS_Store
.ipynb_checkpoints
__pycache__
.gitignore
.gitattributes
```

### Add to .gitattributes
```
*.ipynb linguist-language=Python
```

***
## Branching

### Make and switch to new branch

`$ git checkout -b check_pi`
ref: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

### Merging

After updating branch `Maggie-Edits`:
```
    $ git checkout master
    $ git merge Maggie-Edits
```
If you start a merge and then want to cancel it: `$ git merge --abort`

ref: https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/ch07.html


### check git log:
`$ git log --oneline`

To reset to previous commit: `$ git reset <commit hash>` 

To view commit merges open file in text editor

### Delete branch
(locally)
`$ git branch --delete <branch> `
ref: https://gist.github.com/cmatskas/454e3369e6963a1c8c89