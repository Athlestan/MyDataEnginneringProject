# MyDataEnginneringProject
Learning big data tools

### git cheatsheet https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet

## Setting up a project: 
0. Set up Git on local machine https://help.github.com/en/github/getting-started-with-github/set-up-git#setting-up-git 
1. Create a repo https://help.github.com/en/github/getting-started-with-github/create-a-repo
2. Clone repo onto a local machine https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
  a. open Git Bash
  b. go to a directiry where you want to colne repo
  c. use git clone <https>
3. Commit first change https://help.github.com/en/github/getting-started-with-github/create-a-repo#commit-your-first-change
4. Download and merge changes from remote repository to a local one:
  a. Open Git Bash 
  b. go to repository 
  c. use git pull comand
  
## Setting up an environment
0. Use this tutorial http://davidiscoding.com/tutorial-configuring-the-clouderas-quickstart-vm

## Setting up virtual machine 
TODO: use static ip adress
1. In network setting change connection to (bridged)
2. type ifconfig and use first ip("inet") address
3. Connect using winscp and mobaxterm over ssh (port 22)

## Additional configuration
1. Installing pip for python3 https://pip.pypa.io/en/stable/installing/
    - download file get-pip.py
    - root -> python3 get-pip.py
2. Install kafka-python module
    - python3 -m pip install kafka-python
3. Change kafka setting in cloudera manager:
    - offsets.topic.replication.factor from 3 to 1
    - all of 3 "logging trashold" change to WARN so console output is clean

## Testing kafka
1. Create script test.py
2. Execute script: python3 test.py
3. In the same tame listhen for messages: kafka-console-consumer --bootstrap-server <>:9092 --topic test --group test_group
4. See group details: kafka-consumer-groups --bootstrap-server 192.168.0.73:9092  --describe --group test_group
