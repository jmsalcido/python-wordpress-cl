from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import functions

class Post:
	'''Post class for the wordpress-cl program'''
	def readPost(self, file_name):
		try:
			fopen = open(file_name, 'r')
			txt = fopen.read()
			return txt
		except IOError:
			return ""

	def sendPost(self):
		return self.wp_client.call(NewPost(self.post, True))
		

	def preparePost(self):
		post = WordPressPost()
		post.title = self.title
		post.description = self.readPost(self.file_name)
		return post

	def __init__(self, wp_client, title = "", file_name = ""):
		self.title = title
		self.file_name = file_name
		self.wp_client = wp_client
		self.post = self.preparePost()
