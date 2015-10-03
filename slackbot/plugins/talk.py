from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import random

responses_hello = [
  'sup',
  'yo.',
  'hay'
]

responses_69 = [
  'lol',
  'nice',
  'haha 69',
  'NICE ^^',
  ':wink:'
]

responses_420 = [
  'hehe',
  'blaze it!',
  ':pineapple::train:',
  'yo i\'m serious you wanna?',
  'NICE ^^'
]

@respond_to('$', re.IGNORECASE)
def hello_reply(message):
    message.reply( random.choice(responses_hello) )


@listen_to('69')
def hello_send(message):
    message.send( random.choice(responses_69) )


@listen_to('420')
def hello_send(message):
    message.send( random.choice(responses_420) )