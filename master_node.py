#import web #similar to flask. use any of the two
from flask import Flask
from flask_restful import Resource, Api, request


app = Flask(__name__)
api = Api(app)

'''
'''
class master_node(Resource):
	def get(self):
		return 'Hello!!'

	def put(self):
		pass
		


def get_commits():
	# get the commit files from the github
	print ("Getting commits from Github")


api.add_resource(master_node, '/')

if __name__ == '__main__':
	# Get the commit files from the git
	get_commits()

	# get the total number of commits

	# Start the time

	# Start assigning tasks to the workers
	app.run(host='0.0.0.0', port=5000, debug=False)

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
