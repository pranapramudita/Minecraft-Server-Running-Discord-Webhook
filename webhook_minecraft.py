# Import Library
import sys # system library for getting the command line argument
import http.client # web library
import os
import requests
import subprocess
import atexit
import time

def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    # print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            # print ('%s in r[i]' %(name))
            return r[i]
    return []

def send_message(message):
    webhookurl = "https://discordapp.com/api/webhooks/703937050713522197/S_SICnyjQeZvvVl9YidyTRT-VF_CcmHGWY7jpDE6LMkncpzHKfWvvQDTwpfZt1alSNfe" # your webhook URL
 
    # compile the form data (BOUNDARY can be anything)
    formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
  
    # get the connection and make the request
    connection = http.client.HTTPSConnection("discordapp.com")
    connection.request("POST", webhookurl, formdata, {
        'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
        'cache-control': "no-cache",
        })

    # get the response
    response = connection.getresponse()
    result = response.read()

    # return back to the calling function with the result
    return result.decode("utf-8")
    
# get ip public with port
ip_public = requests.get('http://ip.42.pl/raw').text+":25565"

# send message
text = "**Minecraft Server sedang berjalan pada alamat berikut : `"+ip_public+"`**"

send_message(text)

# run server
proc = subprocess.Popen([r'start.bat'])

# run_condition = getTasks('java.exe') and getTasks('conhost.exe') and getTasks('cmd.exe')

# send_message("**Server Offline**")