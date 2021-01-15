import requests
import json
import hashlib
from pathlib import Path

# Writing this for fun and to just write more python. I know libs exist

"""
Takes a file, submits it's sha1sum to VT
If the file is known, returns known
Alternatively, if that doesn't come back as detecting, it submits the script file to VT and returns if it's detected.

VT API endpoints used:
    File: https://www.virustotal.com/api/v3/files
        https://developers.virustotal.com/v3.0/reference#file
        Limit, 32MB. Why do you have a script larger than 32mb? Doing something phishy?
   
        The result returned by this endpoint is the object descriptor for the new analysis. 
        The ID contained in the descriptor can be used with the GET /analysis/{id} endpoint to get information about the analysis.

    Do this first: Check analysis: https://www.virustotal.com/api/v3/files/{id}
        {id} == sha256, sha1 or md5 of file

    Return info about the file we just uploaded: 
        https://developers.virustotal.com/v3.0/reference#analysis
        curl --request GET \
             --url https://www.virustotal.com/api/v3/analyses/{id} \
             --header 'x-apikey: <your API key>'

"""


# Make this a check eventually
#print("If you don't have your own API key, head here to grab one: https://developers.virustotal.com/v3.0/reference#getting-started this is registered to your own account, and won't affect mine")

API_BASE_URL = 'https://www.virustotal.com/api/v3/'

def fileTooLarge(file_path):
    # See if the file is larger than 32MB, as that's the VirusTotal API limit (there's another endpoint for that)
    file = Path(file_path)
    size = file.stat().st_size
    return size > 32000000 # TODO low priority: figure out VT specifics and get a precise number?

def get_digest(file_path):
# Copied from StackOverflow. Almost 32mb takes .25 seconds, we don't need to worry about perf here.
    h = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()

def checkHash(afile):
    # Upload the hash of the file to the VT files APIv3 endpoint
    # files/{id} = id == hash

    print("stub hash the file and check VT")

def uploadToVT(afile):
    # Upload the file to VT
    print("stub upload to VT")

def checkFile(vtid):
    # We uploaded the file, now use the returned id to get the processed results
    print("stub checkFile")

if __name__ == '__main__':
    size = fileTooLarge('xbb')
    print(size)
    #print(get_digest('xbb'))

