import json 
import _utils

def chatbot_server_setter(server_type):

    
    if server_type == "discord":
        discord_token = _utils.CONFIG.BOT_DISCORD_TOKEN
        import discord
        from chatbot.discord_server import MyDiscordServer
        server = MyDiscordServer()
        server.run(discord_token)

    elif server_type == "admin_page":
        http_server_port = _utils.CONFIG.BOT_HTTP_CLIENT_PORT
        http_server_uri = _utils.CONFIG.BOT_HTTP_CLIENT_URI    
        from chatbot.http_server import run_http_server
        run_http_server(http_server_uri, http_server_port)
