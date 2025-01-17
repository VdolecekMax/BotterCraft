import requests
import os
import random
import time

os.system("cls")

def Integer(Question: str):
    while True:
        response = input(Question)

        try:
            response = int(response)
            return int(response)
            
        except ValueError:
            print("\033[A" + " " * (os.get_terminal_size().columns - 6) + "\033[A")

def String(Question: str):
    while True:
        response = input(Question)

        try:
            response = str(response)
            return str(response)
            
        except ValueError:
            print("\033[A" + " " * (os.get_terminal_size().columns - 6) + "\033[A")



score = Integer("Enter final score: ")
Time = Integer("Enter final time(ms): ")
name = String("Enter name of bots: ")
ammountOfBots = Integer("Enter ammount of bots: ")
activityId = Integer("Enter activityId: ")
templateId = Integer("Enter templateId: ")

print("----------------------------------------")
print("")

def PostToLeaderBoadr():

    Payload = {
        "score": score,
        "time": Time,
        "name": name + str(random.randint(1, 1000)),

        "mode": 1,
        "activityId": activityId,
        "templateId": templateId
    }

    response = requests.post("https://wordwall.net/leaderboardajax/addentry", data=Payload)
    print("\033[A" + " " * (os.get_terminal_size().columns - 6) + "\033[A")


    if response.status_code != 200:
        print("Somethng went wrong")
    else:
        print(f"Connecting bot {Payload["name"]}")

for i in range(ammountOfBots):
    PostToLeaderBoadr()

os.system("pause")