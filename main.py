#!/usr/bin/env python
'''
wordpress-cl.py
Main script for the wordpress-cl program

Using python_wordpress_xmlrpc library:
https://github.com/maxcutler/python-wordpress-xmlrpc
'''
# TODO
#

from wordpress_xmlrpc import Client
from config import Config
from posts import Post, ManagePost
import sys
import functions

def main():
	if sys.argv[1:] == []: exit()
	else: execute()

def execute():
	# TODO update this
	config     = Config()
	try:
		title      = sys.argv[1]
		file_name  = sys.argv[2]
	except IndexError:
		functions.exit()
		return
	wp         = Client(config.data[config.url], config.data[config.user], config.data[config.pwd])
	# Create a Post
	post       = Post(wp, title, file_name)
	manager    = ManagePost(post)
	manager.sendPost()

if __name__ == '__main__':
	main()
