				版本管理工具介绍—Git篇
一.安装完成后，还需要最后一步设置，在命令行输入：
 git config --global user.name fzhqzxguest
 git config --global user.email fzhqzxguest@gmail.com
二.创建版本库
1.第一步，选择一个合适的地方，创建一个空目录(D:/learngit)：
cd D:
mkdir learngit
cd learngit
2.第二步，通过git init命令把这个目录变成Git可以管理的仓库：
git init
三.把文件添加到版本库
1.言归正传，现在我们在D:/learngit目录下，编写一个readme.txt文件，内容如下：
Git is a version control system.
Git is free software.
2.用命令git add告诉Git，把文件添加到仓库(此步可撤消)：
git add readme.txt
git status

此步可撤消，撤消命令如下：
法一：Git会告诉你，git checkout -- file可以丢弃工作区的修改：
git checkout -- readme.txt
法二.用命令git reset HEAD file可以把暂存区的修改撤销掉（unstage），重新放回工作区：
git reset HEAD readme.txt
3.用命令git commit告诉Git，把文件提交到仓库：
git commit -m "readme.txt"
git status
提交后，用git diff HEAD -- readme.txt命令可以查看工作区和版本库里面最新版本的区别：
git diff HEAD -- readme.txt 
四.删除本地文件和版本库文件（配合git status使用。）
1.删除本地文件
 rm test.txt
2.从版本库中删除该文件
git rm test.txt
如果删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本：
git checkout -- test.txt
3.如果没有删错，就用以下命令提交，完全删除
git commit -m "test.txt"
五.添加远程库
在GitHub创建一个Git仓库,Create a new repo.
 git remote add origin https://github.com/fzhqzxguest/learngit.git //https
 git remote add origin git@github.com:michaelliao/learngit.git    //ssh
 git remote add origin https://github.com/fzhqzxguest/learngit.git
 
 从现在起，只要本地作了提交，就可以通过命令：
 git push origin master 

 或者用
git push https://github.com/fzhqzxguest/demo.git master 

六、一些问题解决（换github网址时，换问题3解决）
参照 http://www.jianshu.com/p/01975e421ddb

问题1：
$git remote add origin https://github.com/Yapril/April-Taurus.git
fatal:remote origin already exists.
解决：
先输入$ git remote rm origin
再输入$ git remote add origin https://github.com/Yapril/April-Taurus.git

问题2：
解决：
一般push前要先pull以下
键入$git pull origin master
再键入 git push https://github.com/fzhqzxguest/demo.git master 

问题3：
解决：
用户名和密码对应的是github上的

问题4：

解决：
git 在pull或者合并分支的时候有时会遇到这个界面。可以不管(直接下面3,4步)，如果要输入解释的话就需要:
1.按键盘字母 i 进入insert模式
2.修改最上面那行黄色合并信息,可以不修改
3.按键盘左上角"Esc"
4.输入":wq",注意是冒号+wq,按回车键即可

七、注意点
考虑到版本还会更新，而master是主分支，可以在其下新建一个develop分支，最后开发完毕后合并到master中(还不是很懂下次碰到问题在解决)



