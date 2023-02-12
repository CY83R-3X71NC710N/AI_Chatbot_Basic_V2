from functions import *

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
# write your code here

# custom data
house_owner = [
    "Who is owner of this house?",
    "Mark Nicholas is the owner of this house."
]
house_owner = [
    "Who is owner of this house?",
    "Mark Nicholas is the owner of this house."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
# write your code here

# start chatbot
start_chatbot(home_bot)
