#-*- coding:utf-8 -*-
import argparse
import json
import os 
import logging
from time import sleep


from util.setter.chatbot_client_setter import chatbot_client_setter

logger = logging.getLogger("inference_engine")
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client_type", 
        type    = str,
        default = "discord", 
        help    = "Input client type what you want to start [ discord, admin_page ]") 
    # parser.add_argument("--teacher_name", 
    #     type    = str,
    #     default = "아이린", 
    #     help    = "Input teacher name ") 
    return parser.parse_args()

def config_check():
    pass

def config_update():
    pass

def main():
    args = parse_args()
    LOGGING_LEVEL = logging.DEBUG
    logger.setLevel(LOGGING_LEVEL)
    with open('config.json', 'r') as f:
        config = json.load(f)


    chatbot_client_setter(args.client_type, config)

if __name__=="__main__":
    logger.info("---------------------------------------")
    logger.info("QuA inference engine start")
    logger.info('---------------------------------------\n')
    main()
    sleep(0.05)
    logger.info("\n---------------------------------------")
    logger.info("QuA inference engine end")
    logger.info("---------------------------------------")
