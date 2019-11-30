#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os

#define the bot
bot = ChatBot(
    'TinTin', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {	
            'import_path': 'chatterbot.logic.BestMatch',
			'default_response': "Can you repeat in a different way?",
            'maximum_similarity_threshold': 0.1
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
			#'import_path': 'chatterbot.logic.logic_adapter'
        }
		])

#teaching the bot
trainer = ListTrainer(bot)
for knowledge in os.listdir('data'):
	BotMemory = open('data/'+knowledge, 'r')
	BotAnswer = BotMemory.readlines()
	trainer.train(BotAnswer)

#implement flask
app = Flask(__name__)
#apply socket.io
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/shutdown', methods=['GET'])
def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
		func()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bot.get_response(userText))
	if (userText.strip()=="bye"):
    		shutdown_server()
	
# while True:
# 	if __name__ == "__main__":
# 		socketio.run(app)
# 		break
		
