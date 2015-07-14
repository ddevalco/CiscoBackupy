# CiscoBackupy

This project is an easy-to-use script for export configuration in Cisco devics.

## Installation

Install the requiremnts.txt file using the follwong command - 
```bash
pip install -r requirements.txt
```

##configuration

Edit the configuraiton.py and provide the following informaiton - 
```python
ip_list = ['']                # Set the ip address of one or more cisco devices to backup.
cisco_username = 'cisco'      # Set the username of your cisco device/s.
cisco_password = ''           # Set the password for your cisco device/s.
```
## Usage 

Run the following command and replcae path-param with the backup path you want.
```bash
python CiscoBackupy.py --backup-path path-param
```

##Author
* Ran Franco - http://www.ranfranco.com
