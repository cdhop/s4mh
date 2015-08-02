import sys
import os
import time
import hashlib
import json

def get_filepaths(directory):
	file_paths = []
	
	for root, directories, files in os.walk(directory):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)
	return file_paths

try:
	mypath = sys.argv[1]
	malware_list_file = 'malware_list.json' if len(sys.argv) < 3 else sys.argv[2]
	malware_json = json.load(open(malware_list_file))
	
	files = get_filepaths(mypath)
	
	for file in files:
		hash_value = hashlib.sha256(open(file,'rb').read()).hexdigest()
		mod_date = time.ctime(os.path.getmtime(file))
		
		for malware in malware_json:
			if malware["sha256"] == hash_value:
				print file + ": " + malware["name"] + ": " + mod_date

except IOError as e:
	print str(e.args)
	print "Error: " + e.strerror

except ValueError as e:
	print "Error: " + str(e)
