# Class-Notes
Notes for Stat679

9/18/2018
# git-notes-MB
-git push, git pull, git clone, git fetch, git status, git add <filename>, git commit -m "COMMIT_MESSAGE REQUIRED". How do
these different commands interact with the remote host (github), and communicate changes between it and your locally saved repository (on your machine?)
-what is a git merge conflict? How do conflicts get resolved? (also differences between fetch and pull)

# key takeaways
-git repos exist on the cloud (GitHub, origin). "git clone <url>" writes a local copy to the PC accessing it. "git fetch" creates a temporary file that is a snapshot of all current commits to the
origin, giving the contributor a chance to review the pending changes. "git merge" makes these commits reconcile with the version existing locally on that machine. "git pull" skips the review step and
copies/merges the changes immediately.
-merge conflicts occur when multiple commits are made to the same source, and the changes are very close to each other. Git does not know how to reconcile these changes; the master will pull these and
all possible changes will be included in the document simultaneously (marked as >>>>>> and <<<<<<; identical, or unchanged portions are marked with ======). Then merges are reconciled manually, and the
master must push the reconciled file back to the remote host (origin)
-"git add <filename>" moves the named file to the staging area. "git commit -m <"blahblahblah">" commits all staged files for pushing; a commit message detailing the modifications to the file, or what
the file is, is required (with some terms prohibited so that language is not ambiguous to other collaborators).
-"git status" shows what has been committed, alerts to any conflicts, shows what files have been changed or added in the local repo but remain to be committed to the remote repo.







