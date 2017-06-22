#! usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from github import Github
from time import sleep
from subprocess import call

user_name = 'ring00'
password = '1478963zhangwei'
repo_name = 'git-pull-test'

g = Github(user_name, password)

repo = g.get_user(user_name).get_repo(repo_name)
print(repo.url)

latest_commit = repo.get_commits()[0]

while True:
	sleep(10)
	commit = repo.get_commits()[0]
	print(commit)
	if commit != latest_commit:
		latest_commit = commit
		call("run.sh", shell=True)
