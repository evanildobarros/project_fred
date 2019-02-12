from django.test import TestCase

# Create your tests here.
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')


# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.portuguese")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.portuguese.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.portuguese.conversations")