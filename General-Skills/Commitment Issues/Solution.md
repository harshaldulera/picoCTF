Simply got the flag by restoring to a previous commit.

```
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git log                                              
commit e1237df82d2e69f62dd53279abc1c8aeb66f6d64 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:14 2024 +0000

    remove sensitive info

commit 3d5ec8a26ee7b092a1760fea18f384c35e435139
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:14 2024 +0000

    create flag
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git checkout 3d5ec8a26ee7b092a1760fea18f384c35e435139
message.txt: needs merge
error: you need to resolve your current index first
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git status                                           
On branch master
You are currently reverting commit 3d5ec8a.
  (fix conflicts and run "git revert --continue")
  (use "git revert --skip" to skip this patch)
  (use "git revert --abort" to cancel the revert operation)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add/rm <file>..." as appropriate to mark resolution)
        deleted by them: message.txt

no changes added to commit (use "git add" and/or "git commit -a")
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git reset                                          
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ git checkout 3d5ec8a26ee7b092a1760fea18f384c35e435139
Note: switching to '3d5ec8a26ee7b092a1760fea18f384c35e435139'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 3d5ec8a create flag
                                                                                                                                                                              
┌──(kali㉿kali)-[~/Desktop/pico/drop-in]
└─$ cat message.txt 
picoCTF{s@n1t1z3_30e86d36}
```

Flag:
```
picoCTF{s@n1t1z3_30e86d36}
```