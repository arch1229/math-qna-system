import discord
import logging
from chatbot._bot import bot_answer


class MyDiscordServer(discord.Client):

    async def on_ready(self):
        self.logger = logging.getLogger("discord_server.on_ready")
        self.logger.info("Logged on as" + str(self.user))

    async def on_message(self, message):
        # don't respond to ourselves
        self.logger = logging.getLogger("discord_server.on_message")
        if message.author == self.user:
            return

        answer = bot_answer(message.author, message.content, self.logger)
        await message.channel.send(answer)        

# Test code
if __name__=='__main__':
 
    logger = logging.getLogger("inference_engine.discord_server")
    logger = logging.getLogger('discord_server')
    logger.setLevel(LOGGING_LEVEL)
    stream_hander = logging.StreamHandler()
    logger.addHandler(stream_hander)
    
    import json
    with open('../config.json', 'r') as f:
        config = json.load(f)

    DISCORD_TOKEN = config['DISCORD']['TOKEN']

    server = MyDiscordServer()
    server.run(DISCORD_TOKEN)