#client_node.py

import requests


class client_node:

	master_url = 'http://0.0.0.0:5000/'
	#node_setup_url = 
	
	def __init__(self):
		#self.value = requests.get(self.master_url).json()['url']
		self.value = requests.get(self.master_url).json()
		print self.value

if __name__ == '__main__':
	client = client_node()


