import discord
import logging
from inference import inference
from util.teacher_say import *
from util.nl2query import query_generator


LOGGING_LEVEL = logging.INFO
logger = logging.getLogger("inference_engine.discord_client")

class MyDiscordClient(discord.Client):
    async def on_ready(self):
        logger.info("Logged on as" + str(self.user))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if  TEACHER_INIT in message.content:
            query_data = query_generator(message.content)
            if len(query_data["element"]) == 0:
                await message.channel.send(QUESTION_NOT_DEFINE)   
            else :
                logger.debug(TEACHER_RECONIZE)
                # await message.channel.send(query_data)
                answer = inference(query_data)
                await message.channel.send(answer)
        else :
            logger.debug(str(message.author) + ": " + str(message.content))
            await message.channel.send(TEACHER_NEED_INIT)        


if __name__=='__main__':

	LOGGING_LEVEL = logging.DEBUG

	logger = logging.getLogger('discord_client')
	logger.setLevel(LOGGING_LEVEL)
	stream_hander = logging.StreamHandler()
	logger.addHandler(stream_hander)
    
    import json
    with open('config.json', 'r') as f:
        config = json.load(f)

    DISCORD_TOKEN = config['DISCORD_TOKEN']['TOKEN']

	client = MyClient()
	client.run(DISCORD_TOKEN)