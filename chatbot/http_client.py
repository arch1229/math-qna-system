from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

from inference import inference
from util.teacher_say import *
from util.nl2query import query_generator
import logging

logger = logging.getLogger("inference_engine.http_client")

app = Flask (__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def http_client():
    app.run(debug=True, host="0.0.0.0", port=5005)

class GetQuestion(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sender', type=str)
        parser.add_argument('message', type=str)
        args = parser.parse_args()
        # print(request)
        sender = args['sender']
        message = args['message']
        print(type(message))

        answer = ""
        
        if  TEACHER_INIT in message:
            query_data = query_generator(message)
            if len(query_data["element"]) == 0:
                answer = QUESTION_NOT_DEFINE   
            else :
                logger.debug(TEACHER_RECONIZE)
                # await message.channel.send(query_data)
                answer = inference(query_data)
        else :
            logger.debug(sender + ": " + str(message))
            answer = TEACHER_NEED_INIT       


        return [{"recipient_id" : sender, "text": answer}]


api.add_resource(GetQuestion, "/webhooks/rest/webhook")

