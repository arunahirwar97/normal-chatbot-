pip install chatterbot
pip install chatterbot_corpus

from chatterbot import ChatBot

# ##ChatterBot comes with built in adapter classes that allow it to connect to different types of databases.
# we will be using the SQLStorageAdapter which allows the chat bot to connect to SQL databases. By default, this
# adapter will create a SQLite database.
# 
# ##You can choose to use as many logic adapters as you would like. In this exa,ple we will use onelogic adapter .
# The MathematicalEvaluation adapter  solves math problems that use basic operations.
# This is basic mathamatics operation perform
bot = ChatBot(
'AAP',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
         'chatterbot.logic.MathematicalEvaluation',
         ],
database_uri='sqlite:///aapd1.sqlite3'
    
)

# Getting Responce 
#Ask any mathamatics basic operation perform example "What is 4441 multiply 258 ?"
aap = bot.get_responce(input())
print(aap)


# THis is return current time
bot1 = ChatBot(
'AAP',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
         'chatterbot.logic.TimeLogicAdapter',
         ],
database_uri='sqlite:///aapd2.sqlite3'
    
)


#Getting Responce
## Aks for question example "What is current time ?"
aap = bot1.get_responce(input())
print(aap)

