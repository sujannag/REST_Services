#import web #similar to flask. use any of the two
from flask import Flask


app = Flask(__name__)

def get_commits():
	# get the commit files from the github
	print ("Getting commits from Github")

if __name__ == '__main__':
	# Get the commit files from the git
	get_commits()

	# get the total number of commits

	# Start the time

	# Start assigning tasks to the workers

	# end the time

	# Calculate the time

	# Plot the graphs



'''
urls = (
'/', 'index'
)

class index:
	def GET(self):
		return "Hello, world!!"


if __name__ == "__main__":
		app = web.application(urls, globals())
		app.run()
'''
