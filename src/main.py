#-*- coding:utf-8 -*-
import argparse
import os 
import logging

from _utils import get_config
from _setter.chatbot_server_setter import chatbot_server_setter

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client_type", 
        type    = str,
        default = "discord", 
        help    = "Input client type what you want to start [ discord | admin_page ]") 
    # parser.add_argument("--log_level", 
    #     type    = int,
    #     default = "20", 
    #     help    = "[debug=10|info=20|warning=30|error=40|critical=50]") 
    return parser.parse_args()


if __name__=="__main__":
    # logger set
    # 로그레벨은 여기서 설정하도록 하기 
    logging.basicConfig(level=logging.INFO, \
        format='[%(asctime)s][%(levelname)s:%(name)s] %(message)s', \
        datefmt='%m/%d/%Y %I:%M:%S %p')

    main_logger = logging.getLogger("QA-SERVICE")
    main_logger.info("service start")

    args = parse_args()
    get_config('config.json')
    
    chatbot_server_setter(args.client_type)

    main_logger.info("service end")
