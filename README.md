# REST_Services

It calculates the cyclomatic complexity of python files. A master-worker architecture is followed which is using a work_stealing model. The master stores the jobs in a queue, and using rest api, the client requests jobs from the master, until the master has no more job to give. Once the entire work is done, it calulates the total time required for completing the task. The Master also keeps a count of total client worker nodes which requests jobs from the master. 

The aim of this exercise is to present a corelation between the total number of workers available and the total time required to complete the job at hand.

# Setup:
The setup was hosted on the local machine, as well as on VM's in the open scss nebula infrastructure provided by TCD. Virtual Environment was used while developing the code base. 

Steps to host the master and clients on different open scss nebula machines are:
1. Login into the open scss nebula machines using ssh, in my case I had access to 4 machines.
2. Make sure the http proxy is set in all the machines.
3. Do a git clone on all the machines, "git clone https://github.com/sujannag/REST_Services.git"
4. Make sure to change the MASTER_URL and the NODE_SETUP_URL in the master_node.py with the ip address of the machine, where the code is intended to run.
5. Setup the virtual environment using the command "virtualenv REST_Services"
6. source REST_Services/bin/activate
7. Run the master_node.py on one machine, and multiplt client_node.py on other nebula machines.
8. We should be able to see log messages indicating that work being taken by the client nodes.
9. Kill the server using ctrl+c, once all the work is done.

A possible draw back of the system is 

This service can also be run on a local machine for evaluation.

# Test Results:
The setup was tested in two scenarios, first in a local machine, and secondly on the open scss nebula machines.



