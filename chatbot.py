#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('TinTin')

#teaching the bot
trainer = ListTrainer(bot)
for knowledge in os.listdir('data'):
	BotMemory = open('data/'+knowledge, 'r').readlines()
	trainer.train(BotMemory)

#TinTin's speaking
while True:
        # Input from user
    message=input("You:")
        #if message is not "bye"
    if message.strip()!="bye":
        reply=bot.get_response(message)
        print("TinTin:",reply)
        # if message is "bye"
    if message.strip()=="bye":
        print("TinTin: bye")
        break

