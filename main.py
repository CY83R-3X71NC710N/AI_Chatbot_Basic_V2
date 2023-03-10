from functions import *
import time

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

if identity == 'Mark':
    print('Welcome, Mark. Happy to have you at home.')
    time.sleep(3)
elif identity == 'Jane':
    print('Mark is out right now, but you are welcome to the house.')
    time.sleep(3)
else:
    print('Your access is denied here.')
    time.sleep(3)
    exit()

    
# rules for responding to different identities
# write your code here

# custom data
house = [
    "Who is owner of this house?",
    "Mark Nicholas is the owner of this house.",
    "Where was I born?",
    "Bro, I ain't even know some dude in a basement decided to program me.",
    "What is my favorite book?",
    "That is easy. Your favourite book is deus ex machina.",
    "What is my favorite movie?",
    "You have watched a documentary named documentary more times than I can count. (Lie because I cool robot and you are human with error I can count 100% everything you have done)",
    "What is my favorite sport?",
    "You have always loved esports.",
]
custom_train(home_bot, house)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
# write your code here

# start chatbot
start_chatbot(home_bot)
