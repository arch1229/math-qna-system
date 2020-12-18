import sys 
import re 
import json
import logging

def is_hangul(text):
    #Check the Python Version
    py_ver3 =  sys.version_info >= (3, 0)

    if py_ver3 : # for Ver 3 or later
        enc_text = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            enc_text = text.decode('utf-8')
        else:
            enc_text = text

    han_count = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', enc_text))
    return han_count > 0


def get_config(file_path):
    logger = logging.getLogger("get_config")

    global CONFIG
    try : 
        logger.info("getting config...")
        with open(file_path, 'r') as f:
            CONFIG = Config(json.load(f))
    except Exception as e:
        logger.error(e)        

class Dict2Obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [Dict2Obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, Dict2Obj(b) if isinstance(b, dict) else b)

class Config():
    def __init__(self, c):
        self.BOT_DISCORD_TOKEN = c["BOT"]["DISCORD"]["TOKEN"]
        self.BOT_HTTP_CLIENT_URI = c["BOT"]["HTTP_CLIENT"]["URI"]
        self.BOT_HTTP_CLIENT_PORT = c["BOT"]["HTTP_CLIENT"]["PORT"]
        self.CAS_URI = c["CAS"]["URI"]
        self.DB_URI = c["KDB"]["URI"]

if __name__ == '__main__':
    get_config("config.json")
    print(CONFIG.BOT_DISCORD_TOKEN)