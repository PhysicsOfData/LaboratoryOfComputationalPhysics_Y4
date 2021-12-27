git checkout main
git fetch upstream
git merge upstream/main -m "Standard sync - main"

git checkout dev
git fetch upstream Jordan_Daniel-Harley
git merge upstream/Jordan_Daneil-Harley -m "Standard sync - dev"

git pull

git merge main

