from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_cors import CORS, cross_origin
import logging
import _utils
from chatbot._bot import bot_answer
app = Flask (__name__)
CORS(app)
api = Api(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

def run_http_server(url, port):
    # init http app 
    # 이렇게 한게 굉장히 마음에 안듬 
    app.run(debug=True, host="0.0.0.0", port=port)

# TODO: 클래스를 함수 안에 넣어보기? 지금 구조가 마음에 안듬 근데 flask를 잘 몰라서 못건드는중.
class MyHttpServer(Resource):
    def __init__(self):
        self.logger = logging.getLogger("http_server")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sender', type=str)
        parser.add_argument('message', type=str)
        args = parser.parse_args()
        # print(request)
        sender = args['sender']
        message = args['message']
        # print(type(message))

        answer = bot_answer(sender, message, self.logger)
        data = {"recipient_id" : sender, "text": answer}
        response = Flask.Response(data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

# rest_url 설정하기 지금 adminpage에 setting된 정보는 "/webhooks/rest/webhook"
# init post func
api.add_resource(MyHttpServer, _utils.CONFIG.BOT_HTTP_CLIENT_URI)

