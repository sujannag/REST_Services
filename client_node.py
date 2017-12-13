#client_node.py

import requests
import os
#import lizard


MASTER_URL = 'http://0.0.0.0:5000/'
NODE_SETUP_URL = 'http://0.0.0.0:5000/init'

class client_node:

	global MASTER_URL
	global NODE_SETUP_URL

	def __init__(self):
		self.files_list_url = requests.get(NODE_SETUP_URL).json()['url']
		print(self.files_list_url)

	def compute_cc(self):
		self.sha = self.get_job()
		if self.sha is None:
			print ("Empty Sha")
			#continue

		file_tree = self.get_file_tree(self.sha)
		#print (file_tree)
		
		self.get_files(file_tree)
		avg_cc = self.get_average_cc()
		

	def get_job(self):
		'''
		Get jobs from the master node
		'''
		
		resp = requests.get(MASTER_URL)
		print (resp.status_code)
		
		if(resp.status_code == 200):
			return resp.json()['sha']

	def do_job(self):
		'''
		Calculate the cyclomatic complexity
		'''
		pass

	def get_file_tree(self, sha):
		#print type(self.files_list_url)
			
		resp = requests.get(self.files_list_url.format(sha))
		if resp.status_code == 301:
			redirect_url = resp.headers['location'].split('?')[0]
			resp = requests.get(redirect_url)
		return resp.json()['tree']
		

	def get_files(self, file_tree):
	
		blob_urls = []
		
		if(True != os.path.isdir('tmp')):
			print("Creating Temp Directory")
			os.makedirs('tmp')
		else:
			print("Temp Directory already present!!")
		
		for item in file_tree:
			#if item['type'] == 'blob' and self.is_py_file(item['path']):
			if item['type'] == 'blob':
				blob_urls.append(item['url'])

	    #headers = {'Accept': 'application/vnd.github.v3.raw'}
		#TODO: Try to change this logic	
		for index, url in enumerate(blob_urls):
			#print (index, url)
			resp = requests.get(url)
			with open('./tmp/{}.py'.format(index), 'w') as tmp_file:
				tmp_file.write(resp.text)
		
	def get_average_cc(self):
		
		i = lizard.analyze_file('./tmp')
		print("CC",i.average_cyclomatic_complexity)

if __name__ == '__main__':
	client = client_node()
	
	# Get the jobs fr
	client.compute_cc()


