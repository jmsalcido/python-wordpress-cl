from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# TODO
# Class ManagePost
#   Params: Post
#   Methods: sendPost, readPost and preparePost

class Post:
	'''Post class for the wordpress-cl program'''
	def readPost(self, file_name):
		'''Read the post and return the parsed text'''
		# TODO LOTS OF THINGS, must parse correctly the text and all, but its 4 o clock in the morning... c'mon.
		try:
			fopen = open(file_name, 'r')
			txt = fopen.read()
			return txt
		except IOError:
			return ""

	def sendPost(self):
		'''Send post to the blog and return the post id'''
		return self.wp_client.call(NewPost(self.post, True))
		

	def preparePost(self):
		'''Prepare the post'''
		post = WordPressPost()
		post.title = self.title
		post.description = self.readPost(self.file_name)
		return post

	def __init__(self, wp_client, title = "", file_name = ""):
		'''Init class'''
		self.title = title
		self.file_name = file_name
		self.wp_client = wp_client
		self.post = self.preparePost()
