from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# TODO
# Test.

class ManagePost:
	'''Class to manage: read, send and prepare posts'''
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
		return self.post.wp_client.call(NewPost(self.post, True))

	def preparePost(self, post):
		'''Prepare the post'''
		newPost = WordPressPost()
		newPost.title = post.title
		newPost.description = self.readPost(post.file_name)
		return newPost

	def __init__(self, post):
		'''Init method'''
		self.post = self.preparePost(post)

class Post:
	'''Post class for the wordpress-cl program'''
	def __init__(self, wp_client, title = "", file_name = ""):
		'''Init method'''
		self.title = title
		self.file_name = file_name
		self.wp_client = wp_client
