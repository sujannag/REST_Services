#import web #similar to flask. use any of the two
from flask import Flask
from flask_restful import Resource, Api, request
from collections import deque
from time import time
#from git import Repo
import requests
from threading import Lock
import base64

#GIT_REPO_PATH = "git_repo/pacman"
GIT_REPO_PATH = 'https://api.github.com/repos/weixsong/pacman/commits'
GIT_REPO_FILES_PATH = 'https://api.github.com/repos/weixsong/pacman/git/trees/{}'
#GIT_REPO_PATH = 'https://api.github.com/repos/vilbeyli/Pacman/commits'
#GIT_REPO_FILES_PATH = 'https://api.github.com/repos/vilbeyli/Pacman/git/trees/{}'

user = "c3VqYW41NjE0QGdtYWlsLmNvbQ=="
passwd = "bmFncy50ZXN0MQ=="

g_total_no_of_commits = 0
g_clients_connected_count = 0

# define queue for storing the jobs that needs to be done by the clients
job_queue = deque()

# Lock for the job queue
job_queue_lock = Lock()
clients_connected_count_lock = Lock()
cc_lock = Lock()


app = Flask(__name__)
api = Api(app)


'''
'''
class master_node(Resource):
	
	def get(self):
		#return 'Hello!!'
		'''
		Give jobs to the client nodes till there are no more jobs to give
		There can be multiple client nodes asking for Jobs. Hence implement
		locks on the job_queue
		'''
		global job_queue
		global job_queue_lock
		
		print ("Sending jobs!!")
		with job_queue_lock:
			try:
				return{'sha': job_queue.popleft()}

			except IndexError:
				# TODO: Check out the error codes
				return '', 204

	def put(self):
		
		global g_end_time
		'''
		get the calculated Cyclomatic complexity from the client nodes 
		and store it in a list
		'''
		cc_value = float(requests.form['cc'])
		
		with cc_lock:
			cyclomatic_complexity += cc_value
			cc_count += 1

			'''
			Check if all the commits have been exhausted, if yes shutdown the master node.
			'''
			if(cc_count == g_total_no_of_commits):
				return '', 503
			return '', 204

class setup_node(Resource):
	
	def get(self):
		'''
		Maintain the count of clients connecting to the master node
		'''
		global GIT_REPO_FILES_PATH
		global g_clients_connected_count
		global clients_connected_count_lock
		
		with clients_connected_count_lock:
			g_clients_connected_count += 1
		
		print("New Client Connected!!", g_clients_connected_count)
		return {'url': GIT_REPO_FILES_PATH}
		
	def put(self):
		pass

def get_commits():
	# get the commit files from the github
	print ("Getting commits from Github")

	global GIT_REPO_PATH
	global job_queue
	
	#resp = requests.get(GIT_REPO_PATH)
	resp = requests.get(GIT_REPO_PATH, auth=(base64.b64decode(user), base64.b64decode(passwd)))
	print(resp)

	while 'next' in resp.links:
		for item in resp.json():
			job_queue.append(item['sha'])
		#resp = requests.get(resp.links['next']['url'])
		resp = requests.get(resp.links['next']['url'], auth=(base64.b64decode(user), base64.b64decode(passwd)))
		print resp
	print(resp.json())

	# store the commits in a queue
	for item in resp.json():
		job_queue.append(item['sha'])


	#repo = Repo(GIT_REPO_PATH)
	#print repo
	#sha = repo.head.reference.commit.hexsha
	
def plot_graph():
	print("Plot Graph")

def calculate_average_cc():
	print("Average CC")
	
	global g_clients_connected_count

def plot_graph():
	print("Plot Graph")

def shutdown_master():
	print "shutdown master"
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

api.add_resource(master_node, '/')
api.add_resource(setup_node, '/init')

if __name__ == '__main__':
	# Get the commit files from the git
	get_commits()

	# get the total number of commits
	g_total_no_of_commits = len(job_queue)
	print ('total_no_of_commits: ', g_total_no_of_commits)

	# Start the time
	start_time = time()

	# Start assigning tasks to the workers
	app.run(host='0.0.0.0', port=5000, debug=False)

	end_time = time()

	# Calculate the total time required
	delta_time = end_time - start_time
	print delta_time

	print("Clients:", g_clients_connected_count)
	print("Time Required:", delta_time)


	print("\nKill the Server\n")

	print("\nShutdown Server\n")


	# get the data onto a file to plot it out
	with open('time_required.txt', 'a') as time_required:
		time_required.write('Clients: {}\n Time: {}\n'.format(g_clients_connected_count, delta_time))
		


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
