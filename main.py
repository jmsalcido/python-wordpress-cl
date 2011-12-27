#!/usr/bin/env python
'''
wordpress-cl.py
Main script for the wordpress-cl program

Using python_wordpress_xmlrpc library:
https://github.com/maxcutler/python-wordpress-xmlrpc
'''
#import wordpresslib
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
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

#def preparePost(title):
#	post = WordPressPost()
#	post.title = title
#	try:
#		file_name = sys.argv[2]
#	except IndexError:
#		exit()
#	post.description = readPost(file_name)
#	return post

#def readPost(file_name):
#	try:
#		fopen = open(file_name, 'r')
#		#return fopen.read().replace("\n","")
#		return fopen.read()
#	except IOError:
#		exit()

#def exit():
#	print ERROR_MSG_BAD_USE

if __name__ == '__main__':
	main()
