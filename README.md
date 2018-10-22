# Class-Notes
Notes for Stat679

9/26/2018
# git-notes-MB
* git push, git pull, git clone, git fetch, git status, git add <filename>, git commit -m "COMMIT_MESSAGE REQUIRED". How do
these different commands interact with the remote host (github), and communicate changes between it and your locally saved repository (on your machine?)
* what is a git merge conflict? How do conflicts get resolved? (also differences between fetch and pull)

# key takeaways
* git repos exist on the cloud (GitHub, origin). "git clone <url>" writes a local copy to the PC accessing it. "git fetch" creates a temporary file that is a snapshot of all current commits to the
origin, giving the contributor a chance to review the pending changes. "git merge" makes these commits reconcile with the version existing locally on that machine. "git pull" skips the review step and
copies/merges the changes immediately.
* merge conflicts occur when multiple commits are made to the same source, and the changes are very close to each other. Git does not know how to reconcile these changes; the master will pull these and
all possible changes will be included in the document simultaneously (marked as >>>>>> and <<<<<<; identical, or unchanged portions are marked with ======). Then merges are reconciled manually, and the
master must push the reconciled file back to the remote host (origin)
* "git add <filename>" moves the named file to the staging area. "git commit -m <"blahblahblah">" commits all staged files for pushing; a commit message detailing the modifications to the file, or what
the file is, is required (with some terms prohibited so that language is not ambiguous to other collaborators).
* "git status" shows what has been committed, alerts to any conflicts, shows what files have been changed or added in the local repo but remain to be committed to the remote repo.
* and don't forget, "git push" is the last thing you need to do to send this to remote!!


sed s/pattern/replacement/ filename > newfile # do NOT redirect to input file because you are using the stream from the current file and you don't want to edit that stream at the same time
sed ("stream editor")


10/08/2018
git log --graph 
#traces all recent additions made to the file (copy pastes the SHA from just before the divergence)

git log --all
#shows all previous versions
git checkout master 
#is used to hop branches while in 'detached head mode' 
#going back in time with git: always use `--` to specify the file state you want to go back to. THIS IS WHY IT'S IMPORTANT TO TAG EVERY VERSION OF YOUR PROJECT, IT'S LIKE A BACKUP FROM THAT POINT IN 
#TIME


#bare repository: a repository that only has the .git folder (no other files). This is used by git to back-calculate between the current (up to date) version on master and the version you are requesting 
#to view, then pulls those files into this .git folder for you to see

#Branches and Master: Branches are used by git to easily switch between versions. A branch is a living version that is a copy of the current master, and it can be evolved separately from master. 
#Committing to Master advances Master ahead of the other branches so pay attention to which branch you're on while preparing to commit

#git checkout master changes all the files to match what was on the master.

* branches are only pointers, do not hold information; the commits hold information
