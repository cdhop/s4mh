# s4mh
Scan for malware by hash

This python script will scan a specified path for malware. It does this by hashing all the files found, and then comparing the hashes against entries found in a malware list file.

The malware list file is a collection of JSON objects.  Each JSON object has a SHA256 hash value, and the name of the Malware (if known).

It is possible to create your own malware list file (or add entries to the one provided) to scan more/different malware.
