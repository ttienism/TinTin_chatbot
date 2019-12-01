#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from flask import Flask, render_template, request


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
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

#TinTin's speaking
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
