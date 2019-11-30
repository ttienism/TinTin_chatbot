#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
import os

#define the bot
bot = ChatBot(
    'TinTin',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.90,
            'default_response': 'I am sorry I don\'t understand, but I\'m a work in progress.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

#teaching the bot
trainer = ListTrainer(bot)
for knowledge in os.listdir('data'):
	BotMemory = open('data/'+knowledge, 'r').readlines()
	trainer.train(BotMemory)

#implement flask
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	if (userText.strip()=="bye"):
		return 'botmsg'=="bye"
	else:
		return str(bot.get_response(userText))
	
while True:
	if __name__ == "__main__":
		app.run()
		#break
