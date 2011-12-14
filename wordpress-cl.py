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
import sys

ERROR_MSG_BAD_USE = "That's not the way you should use this program"
_FILE = "config.wp"

# Oh boy...
_url      = ""
_username = ""
_pwd      = ""

# 
def main():
    if sys.argv[1:] == []:
        exit()
    else:
        execute()

def execute():
    config     = readConfig()
    # TODO try except this ??
    _url       = config["url"]
    _username  = config["username"]
    _pwd       = config["password"]
    config     = {}
    title      = sys.argv[1]
    wp         = Client(_url, _username, _pwd)
    # Call new post
    post       = preparePost(title)
    wp.call(NewPost(post, True))

def preparePost(title):
    post = WordPressPost()
    post.title = title
    try:
        file_name = sys.argv[2]
    except Exception:
        exit()
    post.description = readPost(file_name)
    return post

def readPost(file_name):
    try:
        fopen = open(file_name, 'r')
	return fopen.read().replace("\n","")
    except Exception:
        exit()

def readConfig():
    fopen = open(_FILE, 'r')
    fopen.seek(0)
    line = fopen.readline()
    hashmap = {}
    while line != '':
        if line[0] == "#" or line[0] == "\n":
            # Comments = #
            line = fopen.readline()
            continue
        listaLine = line.split()
        # Remove the '='
        listaLine.pop(1)
        hashmap[listaLine[0]] = listaLine[1]
        line = fopen.readline()
    return hashmap

def exit():
    print ERROR_MSG_BAD_USE

if __name__ == '__main__':
    main()
