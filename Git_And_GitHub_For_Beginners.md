## Terms

- directory -> folder
- terminal or command line -> interface for text commands
- CLI -> Command Line Interface
- repository -> project, or the folder/place where your project is kept
- Git -> tool that tracks the changes in your code over time
- GiHUb -> a website where you host all of your Git repositories online

## Git Commands

- clone -> bring a repository that is hosted somewhere like GitHub into a folder on your local machine
- add -> track your files and changes (updated, created of deleted files) in Git
- commit -> save your file in Git
- push -> upload Git commits to a remote repo, like GitHub
- pull -> download changes from remote repo to your local machine (the opposite of push)

## Git Workflow

Let's suppose you've made some changes to a file on your local machine and you want to save those changes and push them to your remote repository on GitHub.

- git checkout <Development_Branch> -> moves you to your development branch
- git status -> show all the files that were updated, created of deleted but haven't been saved in a commit yet
- git add . -> add all the files listed in the previous command
- git add <File_Name> -> same as above but track only the specific file
- git commit -m "Some Description" -> save all your files in Git, but still locally
- git push -> upload Git commits to your remote repo on GitHub
- git push origin <Development_Branch> -> "origin" stands for the location of your Git repo and <Development_Branch> is the branch you want to push to (note: since I typed the command "git checkout -b <Development_Branch> upstream/<Surname_Name>" to create my development branch this is the only way to upload Git commits on my remote repo. The command "git push" will result in an error message and will be rejected)



