## Terms

- directory -> folder
- terminal or command line -> interface for text commands
- CLI -> Command Line Interface
- repository -> project, or the folder/place where your project is kept
- Git -> tool that tracks the changes in your code over time
- GiHub -> a website where you host all of your Git repositories online

## Git Commands

- clone -> bring a repository that is hosted somewhere like GitHub into a folder on your local machine
- add -> track your files and changes (updated, created of deleted files) in Git
- commit -> save your file in Git
- push -> upload Git commits to a remote repo, like GitHub
- pull -> download changes from remote repo to your local machine (the opposite of push)
- checkout -> switch between branches
- branch -> list all branches and indicate the current one
- diff -> compare two versions of the code and show all the lines that have been changed
- status -> display the state of the working directory and the staging area
- log -> show a log of all the commits

## Lab Class Git Workflow

Let's suppose you've made some changes to a file on your local machine (let's say on your "development branch", because you want to develop your code in a different branch than the main) and you want to save those changes and push them to your remote repository on GitHub:

- git checkout <Development_Branch>-> switch to your development branch
- git status -> show all the files that were updated, created or deleted but haven't been saved in a commit yet
- git add . -> add all the files listed in the previous command
- git add <File_Name> -> same as above but track only the specific file
- git commit -m "Some Description" -> save all your files in Git, but still locally
- git push origin <Development_Branch> -> upload Git commits to your remote repository on GitHub; "origin" stands for the location of your Git repository and <Development_Branch> is the branch you want to push to (note: since I typed the command "git checkout -b <Development_Branch> upstream/<Surname_Name>" to create my development branch this is the only way to upload Git commits on your remote repository. The command "git push" will result in an error message and will be rejected)

If you want to delete a file:

- git rm <File_Name>
- git add .
- git commit -m "Some Description"
- git push origin <Development_Branch>

If you want to unstage a file (you added it but didn't want to):

- git reset <File_Name>

If you want to undo the last commit:

- git reset HEAD~1 -> HEAD is a pointer to the last commit, while ~1 means that HEAD will point back one commit further

If you want to go back to a specific commit:

- git log -> show a log of all the commits so you can copy the hash of the specific commit you want to go back to
- git reset hash -> unstage all the changes until the specific commit
- git reset --hard hash -> as above but in this case you actually delete all the changes

## Lab Class Routine

Let's suppose that the upstream repository (i.e. the "professor's repository on GitHub") has been updated with respect to your forked version. If it had, then in order to merge the changes into your main branch on your local machine:

- git checkout main
- git fetch upstream
- git merge upstream/main

Then, if you want to upload the changes to your remote repository on GitHub (origin/main):

- git checkout main
- git add .
- git commit -m "Some Description"
- git push origin main

Let's suppose you also want to get the updates from the main to your <Development_Branch> (because you want to work on the new exercises uploaded by the professor):

- git checkout <Development_Branch>
- git merge main

Moreover, in the case your pull request has been recently approved, make sure to synch your development branch:

- git checkout <Development_Branch>
- git fetch upstream <Surname_Name>
- git merge upstream/<Surname_Name>

Then, if you want to upload the changes to your remote repo on GitHub (origin/<Development_Branch>):

- git checkout <Development_Branch>
- git add .
- git commit -m "Some Description"
- git push origin <Development_Branch>