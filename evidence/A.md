# Evidence (Student A)

## E1
```
origin	https://github.com/kareemahmoud/lantern.git (fetch)
origin	https://github.com/kareemahmoud/lantern.git (push)
```

## E2
```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   notes.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.txt

--- git diff (not staged) ---
diff --git a/notes.txt b/notes.txt
index cb2ea67..ba46e93 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1,2 +1,3 @@
 placeholder
 first line
+second line
--- git diff --staged ---
diff --git a/notes.txt b/notes.txt
index 48cdce8..cb2ea67 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1 +1,2 @@
 placeholder
+first line
```

## E4
```
*   d3f7004 merge: combine done flag with strip fix
|\  
| * 6f4ed1b feat(tasks): add done flag to new tasks
* | d2e66af fix(tasks): strip whitespace from task title
|/  
* 13dbdbd docs(notes): add first project notes
* 557ea85 refactor(notes): rename draft.txt to notes.txt
* 8d6c6a1 chore(notes): add draft placeholder file
* 591cec0 feat(cli): add argparse add and list commands
* ce41d9d feat(tasks): add add_task and list_tasks
* 56c320e docs(readme: upadting readme content formating)
*   8946083 Merge branch 'main' of https://github.com/kareemahmoud/lantern
```

## E5
### Drill (a)
```
28fb6da HEAD@{0}: commit (amend): docs(notes): add second note line
81d2414 HEAD@{1}: commit: docs(notes): add secnd note line
b835a59 HEAD@{2}: pull --no-rebase origin main: Merge made by the 'ort' strategy.
1d34c9f HEAD@{3}: commit: chore(git): stop tracking .env and add gitignore
b6e7882 HEAD@{4}: commit: chore(config): add local environment settings
d3f7004 HEAD@{5}: commit (merge): merge: combine done flag with strip fix
```
### Drill (c)
```
429db1d HEAD@{0}: reset: moving to 429db1d
dc3aa6a HEAD@{1}: reset: moving to HEAD~1
429db1d HEAD@{2}: commit: docs(notes): add third note line
dc3aa6a HEAD@{3}: pull --no-rebase origin main: Merge made by the 'ort' strategy.
```

## E7
```
remote: error: GH006: Protected branch update failed for refs/heads/main.        
remote: 
remote: - Changes must be made through a pull request.        
To https://github.com/kareemahmoud/lantern.git
 ! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'https://github.com/kareemahmoud/lantern.git'
```
