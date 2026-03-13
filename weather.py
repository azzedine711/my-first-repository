from random import choice

print("ROCK PAPER SCISSOR !")
the_user = str(input(("choose: ")))
the_bot = choice (["rock","paper","scissor"])
print("the bot choose: " + the_bot)

if the_user == the_bot:
    print("its a tie")
elif the_user == "paper" and the_bot == "rock":
    print("you won")
elif the_user == "paper" and the_bot == "scissor":
    print("the bot won")
elif the_user == "rock" and the_bot == "scissor":
    print("you won")
elif the_user == "rock" and the_bot == "paper":
    print("the bot won")
elif the_user == "scissor" and the_bot == "paper":
    print("you won")
elif the_user == "scissor" and the_bot == "rock":
    print("the bot won")