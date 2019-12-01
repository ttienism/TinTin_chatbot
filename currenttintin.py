#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


#define the bot
bot = ChatBot(
    'TinTin',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.90,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)


#teaching the bot
trainer = ListTrainer(bot)
for knowledge in os.listdir('data'):
	BotMemory = open('data/'+knowledge, 'r')
	BotAnswer = BotMemory.readlines()
	trainer.train(BotAnswer)

while True:
     
    #Input from user
    message=input("You:")
    #if message is not "bye"
    if message.strip()!="bye":
        reply=bot.get_response(message)
        print("TinTin:",reply)
    #if message is "bye"
    if message.strip()=="bye":
        print("TinTin: bye")
        break
