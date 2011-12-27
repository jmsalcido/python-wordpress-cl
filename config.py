'''
config.py
Config script for the wordpress-cl program
'''

import sys
import functions

# ConfigObj to create default config.wp
_CONFIGOBJ_ERROR = "You can't create the default config.wp install ConfigObj: easy_install ConfigObj"
try:
	from configobj import ConfigObj
except ImportError:
	print _CONFIGOBJ_ERROR

# Messages
_FILE_EXISTING_MSG = "There is a configuration file existing, remove it first if you want to create a new config.wp file or change the name of the file in the source code."

# Name of the file
_FILE = "config.wp"

# TODO
# 

class Config:
	'''Config class'''
	url  = "url"
	user = "username"
	pwd  = "password"
		
	def readConfig(self):
		'''Read the configuration file on: _FILE var'''
		fopen = open(_FILE, 'r')
		fopen.seek(0)
		line = fopen.readline()
		hashmap = {}
		while line != '':
			if line[0] == "#" or line[0] == "\n":
				line = fopen.readline()
				continue
			lista = line.split()
			lista.pop(1)
			hashmap[lista[0]] = lista[1]
			line = fopen.readline()
		return hashmap

	def __init__(self):
		self.data = self.readConfig()

def create():
	'''Creates a new configuration file on _FILE var, needs ConfigObj from configobj module'''
	config = ConfigObj()
	config.filename = _FILE
	try:
		config["url"]      = "http://blog.url/xmlrpc.php"
		config["username"] = "user"
		config["password"] = "pwd"
		config.write()
	except ImportError:
		print _CONFIGOBJ_ERROR

if __name__ == "__main__":
	try:
		fopen = open(_FILE, 'r')
		print _FILE_EXISTING_MSG
	except IOError:
		create()
