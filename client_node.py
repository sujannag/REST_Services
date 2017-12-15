#client_node.py

import requests
import os
import lizard
from re import match
from radon.complexity import SCORE
from radon.cli.harvest import CCHarvester
from radon.cli import Config
from shutil import rmtree
import base64

MASTER_URL = 'http://0.0.0.0:5000/'
NODE_SETUP_URL = 'http://0.0.0.0:5000/init'

user = "c3VqYW41NjE0QGdtYWlsLmNvbQ=="
passwd = "bmFncy50ZXN0MQ=="

class client_node:

	global MASTER_URL
	global NODE_SETUP_URL
	
	cc_path = ['./tmp']
	cc_config = Config(
		exclude='',
		ignore='venv',
		order=SCORE,
		no_assert=True,
		show_closures=False,
		min='A',
		max='F',
	)
	

	def __init__(self):
		self.finished = False;
		#self.files_list_url = requests.get(NODE_SETUP_URL).json()['url']
		self.files_list_url = requests.get(NODE_SETUP_URL, auth=(base64.b64decode(user), base64.b64decode(passwd))).json()['url']
		print(self.files_list_url)

	def compute_cc(self):

		while not self.finished:
			self.sha = self.get_job()
			if self.sha is None:
				print ("Empty Sha")
				continue

			file_tree = self.get_file_tree(self.sha)
			#print (file_tree)
		
			self.get_files(file_tree)
			avg_cc = self.get_average_cc()
			print (avg_cc)
		

	def get_job(self):
		'''
		Get jobs from the master node
		'''
		
		resp = requests.get(MASTER_URL)
		print (resp.status_code)
		
		if(resp.status_code == 200):
			return resp.json()['sha']
		self.finished = True


	def do_job(self):
		'''
		Calculate the cyclomatic complexity
		'''
		pass

	def get_file_tree(self, sha):
		#print type(self.files_list_url)
			
		resp = requests.get(self.files_list_url.format(sha), auth=(base64.b64decode(user), base64.b64decode(passwd)))
		if resp.status_code == 301:
			redirect_url = resp.headers['location'].split('?')[0]
			#resp = requests.get(redirect_url)
			resp = requests.get(redirect_url, auth=(base64.b64decode(user), base64.b64decode(passwd)))
		return resp.json()['tree']
		

	def get_files(self, file_tree):
	
		blob_urls = []
		count = 0
		
		if(True != os.path.isdir('tmp')):
			print("Creating Temp Directory")
			os.makedirs('tmp')
		else:
			print("Temp Directory already present!!")
		
		for item in file_tree:
			if item['type'] == 'blob' and self.is_py_file(item['path']):
			#if item['type'] == 'blob':
				blob_urls.append(item['url'])


		headers = {'Accept': 'application/vnd.github.v3.raw'}
		for index, url in enumerate(blob_urls):
			#print (index, url)
			resp = requests.get(url, headers=headers, auth=(base64.b64decode(user), base64.b64decode(passwd)))
			with open('./tmp/{}.py'.format(index), 'w') as tmp_file:
				count = count + 1
				tmp_file.write(resp.text)

		print ("Count", count)
		
	def get_average_cc(self):
		'''
		i = lizard.analyze_file('./tmp/0.py')
		print("CC",i.average_cyclomatic_complexity)
		'''
<<<<<<< HEAD
		'''
		# Using Lizard
=======
		# Using Lizard
		'''
>>>>>>> 237ae98760e222491f246d74d26f3fd1b24051c6
		print("Start Lizard testing")
		i = lizard.analyze_file("./tmp/0.py")
		print (i.__dict__)
		print i.function_list[0].__dict__
		
		print("End Lizard testing")
		'''
<<<<<<< HEAD

=======
>>>>>>> 237ae98760e222491f246d74d26f3fd1b24051c6
		results = CCHarvester(self.cc_path, self.cc_config)._to_dicts()
		if results == {}:
			rmtree('tmp')
			return 0

		total_cc = 0
		for filename in results.values():
			file_cc = 0
			for block in filename:
				try:
					file_cc += block['complexity']
				except TypeError:
					print("CC failed, file in script format with no classes/functions")

			total_cc += file_cc
		
		rmtree('tmp')
		print ("total cc", total_cc)
		print ("length of the results", len(results))
		return total_cc / len(results)

	def is_py_file(self, filename):
		return True if match('.*\.py', filename) is not None else False


if __name__ == '__main__':
	client = client_node()
	
<<<<<<< HEAD
	# Get the jobs from the master node
=======
	# Get the jobs from the master
>>>>>>> 237ae98760e222491f246d74d26f3fd1b24051c6
	client.compute_cc()


