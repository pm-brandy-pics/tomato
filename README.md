<h1>hello</h1>
i like tomatoes
<br>
i am cat
<br>
i like playing COD
<br>
using git is fun
<br>
vim is super fun



10. Pushing Updates
 Git push
Transfer the commits from your local repository to a remote server.
Push data to remote server:
$ git push origin master 
Force push data:
$ git push <remote><branch> -f 
Delete a remote branch by push command:
$ git push origin -delete edited
11. Pulling updates
 Git pull
Pull the data from the server:
$ git pull origin master
Pull a remote branch:
$ git pull <remote branch URL>
 Git fetch
Downloads branches and tags from one or more repositories.
Fetch the remote repository:
$ git fetch< repository Url>
Fetch a specific branch:
$ git fetch <branch URL><branch name>
Fetch all the branches simultaneously:
$ git fetch –all
Synchronize the local repository:
$ git fetch origin
12. Undo changes
 Git revert
Undo the changes
$ git revert
Revert a particular commit:
$ git revert <commit-ish>
 Git reset
Reset the changes:
$ git reset –hard
$ git reset –soft
$ git reset --mixed
13. Removing files
 Git rm
Remove the files from the working tree and from the index:
$ git rm <file Name>
Remove files from the Git But keep the files in your local repository:
$ git rm --cached
