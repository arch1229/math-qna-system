import discord
from chatbot.discord_client import MyDiscordClient
from chatbot.http_client import http_client
import json 

def chatbot_client_setter(client_type, config):

    DISCORD_TOKEN = config['DISCORD_TOKEN']['TOKEN']
    HTTP_CLIENT_PORT = config['HTTP_CLIENT']["PORT"]
    HTTP_CLIENT_URL = config['HTTP_CLIENT']["URL"]    
    
	if client_type == "discord":
	    client = MyDiscordClient()
	    client.run(DISCORD_TOKEN)

	elif client_type == "admin_page":
		http_client()
