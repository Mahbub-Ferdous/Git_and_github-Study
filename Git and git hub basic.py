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
         		
         		
         		
         		
         		
    1. Configure git     ---- when you open your git then confirm that your git is configure, if you check youu configuration then command--
  
  							git config --global user.name
  							git config --global user.email or 
  							git config -l                      [its much easy to see all information]
  							
  	   if, the configuration is not yet properly then configure it first by command given below:
  	      
  	                        git config --global user.name "userName"
  	                        git config --global user.email"userEmail"
  	                        
  2. Git initialize   ------  if you want to initialize a folder then make a folder and then command git init then git always follow your
     creating directory : 
  
                            git init or
                            git init .         [if you need all folder initialize]
                            
  3. Git add for staging area : ----  if you want to add file in your local git repository then command git add then it go to then
     staging area .
  
                            git add .         [  . for all file in the current directory ]
                            git add -A           [ it also for all  add]
                            git add 'fileName which you want add'       [ individual] 
                            
                            
  4. Git commit : ----  if you want to commit some file in the local repository then command :
  
                            git commit -m "write your commit masssage"    [must write your commit massage for next correction and update] 
                            git log            [for see commit id ,details,author name etc]
                            git commit --amend -m "and your specific changing in your file massage write here"
                              
                              
  5. you must make ssh key on your git hub account by using git hub assistance,
  
  
  6. Git push : 
  
                           git remote add origin 'copy paste the remote repository address'
                           git push -u origin main 
                           git push -u origin master 
                           
                           
  7. Git log : if you see the details of git commit id number and then command :-
  
                           git log 
                           git log --oneline 
                           git log show 
                           git log checkout 
                           
                           
  8. Git pull or clone : if you want to clone someone github file then copy the repository ip and then command ::
  
                           git pull 'copy paste the others repository link'
                           git clone 'copy paste the others repository link'
                           
                           
  9. Git branch : if your 3 guys works in a projects and the projects in default master/main branch. and you wanrt to submit your codding
     in another branch cause the main file is master app file so if you push your codding on a branch then projects manager test then
     merge the main or master file its to easy to work remotely with few dev:
  
                           git branch                         [if you see how much branches have in the repository]
                           git branch 'branchName'            [if you want to create a new branch on be half of master repo]
                           git checkout 'branchName' [if you want to commit on you branch then go to the created branch with this command]
                           git checkout -            [if you want to go again your past branch]
                           git push -u origin 'branchName'  [if you want to push you file on your created branch]
                           git checkout -b 'branchName'      [if you want to create and switch a branch in one command]  
                           git branch -d 'branchName'       [if you delete any branch then use this command]
                           
                           
                           
 10. Pull request:  if you want to getting a pull request its most important thing in github for work together in one file 
     cause when you call a pull request then you send some description about your changes and you select you code viewer or manager 
     also you create some lebel like bug, question, if your pull request is valid and there have no conflicts or bugs then project
     manager or lead engineer merge the pull request and then he/she merge it 
     
     [basically merge is depends on pull request first of all you create a branch for didnt destroy your master file then your
     correction push to the branch and then create a pull request with reviewer and description and level, cause this is the pointer of
     a lead engineer to merge your pull request]
     
     [if your pull request and merge complete then command git log --oneline - then you cant see the new file cause you want to 
     pull the file again then command -- git pull and then again command -- git log --oneline and see the magic tan tana ]
     
     
 11. Git rebase : 
 
 
 

///git hub theke branch delete kora == git push origin -d branchName
         		
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




# here almost all the git command we use day to day life in our life 



                       
