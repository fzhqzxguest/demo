				版本管理工具介绍—Git篇
一.安装完成后，还需要最后一步设置，在命令行输入：
 git config --global user.name 用户名
 git config --global user.email 邮箱t@gmail.com

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
 git remote add origin https://github.com/fzhqzxguest/learngit  //https

 git remote add origin git@github.com:michaelliao/learngit.git    //ssh

 git push -u origin master

接下来，可用第三、第四步骤来上传，修改和删除文件等操作。


从现在起，只要本地作了提交，就可以通过命令：
 git push origin master