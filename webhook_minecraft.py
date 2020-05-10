# Import Library
import sys # system library for getting the command line argument
import requests
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed

# your webhook url here
webhook_url = "https://discordapp.com/api/webhooks/709005830174933022/z58I_2SEdMXsEsMGT80QolRTdE4wFM1sIUL6sXqPShepRjyig6AsAZekgqi1E3CWc91U"

port = str(25565) # your port forwarding
ip_public = requests.get('http://ip.42.pl/raw').text # get ip public
address = ip_public+":"+port

# send online status 
def server_run_status(webhook_url):
    webhook = DiscordWebhook(webhook_url)
    embed = DiscordEmbed(title='Server Status', description='Server is online!', color=242424)
    embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/894/PNG/512/Tick_Mark_Circle_icon-icons.com_69145.png')
    embed.set_timestamp()
    embed.add_embed_field(name='Address', value=address)
    webhook.add_embed(embed)
    response = webhook.execute()

# send offline status
def server_offline_status(webhook_url):
    webhook = DiscordWebhook(webhook_url)
    embed = DiscordEmbed(title='Server Status', description='Server is offline!', color=242424)
    embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/894/PNG/512/Close_Icon_Circle_icon-icons.com_69142.png')
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()

# run server.jar
proc = subprocess.Popen([r'start.bat'], creationflags=subprocess.CREATE_NEW_CONSOLE)

# if process is terminante then send online status to webhhook
if(proc.poll() == None):
    server_run_status(webhook_url)

# wait until server is offline then send offline status to webhook
proc.wait()
server_offline_status(webhook_url)