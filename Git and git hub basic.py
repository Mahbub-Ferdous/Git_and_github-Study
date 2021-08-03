/// now we learn basic git operations and command :


         1. Creating Repositories:
         		
         		A. git init
         		
         2. Making Changes :
         
         		A. Status
         		B. Add
         		c. Command
         		
         3. Parallel Development:
         
         		A. Branch
         		B. Merge
         		C. Rebase
         		
         4. Syncing Repositories:
         
         		A. Origin 
         		B. Push 
         		C. Pull
         		
**** git init = command create a new repository ****
**** git clone = when you command clone then you clone a repository then basically you create a copy of the original repository in your machine ****
**** git fork = when you fork a repository then a copy will be available on your github accounts ****



**** your are using vim then make a file then write something and git status then command : 🤗️git add fileName🤗️ so now we add our recently created vim file now we going to commit this file command : 🤗️ git commit -m "your massage"🤗️[we pass a masaage], now the command we use, command === 🤗️git log🤗️ this comand gives us a commit number to ready for push then command : git show 'commit number' first 10 number, then we re write our vim file then we check the git status and we saw the changes and getiing git add .(. means all) command then again git commit -m "your massage" now the inportancy of git commit massage now again git log command then command give me two commit it one is past and another is re writing commit then again git show 'new commit number' first 10 number then machine gives the changes of 2 file :



flow chart given below: 


First step: Command line step by step--- <vim fileName>
                                               *
                                               *
                                               *
                                      <write in vim and save>
                                               *
                                               *
                                               *
                                         <git status>
                                               *
                                               *
                                               *
                                      <git add fileName>
                                               *
                                               *
                                               *
                                 <git commit -m "pass massage">
                                               *
                                               *
                                               *
                                           <git log>
                                               *
                                               *
                                               *
                          <git show 'at least 7 char on commit id'>
                                               *
                                               *
                                               *
                                        <vim fileName>
                                               *
                                               *
                                               *
                                        <edited on vim>
                                               *
                                               *
                                               *
                                          <git status>
                                               *
                                               *
                                               *
                                       <git add fileName>
                                               *
                                               *
                                               *
                             <git commit -m "pass the new massage">
                                               *
                                               *
                                               *
                                           <git log>
                                               *
                                               *
                                               *
                                    <git show 'new commit id'>
                                               *
                                               *
                                               *
                                       <see the changes>                  



***** check local repository file command == git ls-files *****



***** for deploy a local repository to remote repository:  

                          < git remote add origin 'copy and paste remote repository http link' >
                                                        *
                                                        *
                                                < git remote -v >      [for check success to connect local and remote repository]
                                                        *
                                                        *                                                
                                            < git push origin master           [for push the remote repository]
                                                        *
                                                        *
                                       < give your user name & password >
                                                        *
                                                        *                
                       < the work done and your commit already deploy your remote repository >
                       
                       
                       
/// git e ekta file amra over write korte parbo and setar jonno commit korar somoy ekta clue massage rehe dibo

/// git e amr user name thik ache kina check command == git config --global user.name

/// git log diye k ki change korlo and ami o konta kokhn change korlam seta r clue and date time id number show korar command == git log

/// kono file re write korar por abar jodi notun ta na hoye ager ta e thik hoy then ager file call korar command :

git log --oneline [you find 2 files id, head id is always correction commit ] then jetay jete chai tar command == git chechout "which file id numbercopy paste"

/// git gui open on ubuntu command line is : git gui

/// keu jodi amar file edit kore and seta amr lage then command == git pull origin master , then ja ja edit hoiche sob amr file e add hoye jabe

/// then abar git log dile k ki change korche setar details dekha jabe 

/// ekta pura file clone korar jonno http link copy kore ekta folder kore oi folder e giye command == git clone link

//// git push korar another command : git push -u origin master           jodi ami oi folder age pull kore thaki

/// branchin er first command == git branch

/// opening new branch then command === git branch 'branch name' then again git branch * new branch show korbe then jei branch e jete chai tar jonno command == git checkout 'destination branch name' now create a branch succesfully so we add a file in directory then push it on github branch then add kora and then commit kora then command == git push -u origin 'branch name'


/// ekhon file amra jodi master e jete chai tahole command == git checkout master then file show only master 

/// then amra jodi abar branch e jete chai simply command == git checkout branch name then branch er file show korbe 





Jodi keu amr file e kono contribute i mean edit kore then seta amr local repository update korar jonno simple termina e sei directory te giye simple command === git pull origin master

jodi amar sei change valo na lage i mean valid na hoy then again command == git log , eta diye k ki change korlo author and time date dekhe amra janbo k ki change korlo then amar ager file e rakhte chaile command === git checkout 'ager file er id number copy paste'
then local repository ager ta hoye jabe  








**** kono file branch theke master e merge korte chaile amake obossoi master brach e switch korte hobe , command = git checkout master 


then merge korte chaile simply command === git merge branch name 



**** branch delete korar command === git branch -d branchName 

///git hub theke branch delete kora == git push origin -d branchName
                       
                       
                       
