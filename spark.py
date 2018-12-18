from flask import *
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket_io = SocketIO(app)


if __name__ == '__main__':
    socket_io.run(app, debug=True)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@socket_io.on("message")
def request(message):
    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = '유저가 입장하였습니다.'
        to_client['type']

    else:
        to_client['message'] = message
        to_client['type'] = 'normal'

    send(to_client, broadcast=True)
