import os
from time import sleep

setup = True
running = True

for root, dirs, files in os.walk("config_check"):
    for filename in files:
        if filename == "true.txt":
            print("Everything should be running smoothly....\n\n")
            setup = False

if setup:
    try:
        file1 = open("config_check/true.txt", "w")
        file1.write("The installation of Fupi-Vods should be working.")
        file1.close()
        os.system("python setup.py install")
    except Exception as e:
        print("Error: I couldn't install the setup.py\n Exact error message: {}".format(e))

print("If you want to quit just type \"quit\"\n\n")

while running:
    question = input("\nDownload or Videos?:\n")

    if question.lower() == "quit":
        running = False

    if question.lower() == "download":
        id = input("Give me the id of the vod:\n")
        try:
            os.system("twitch-dl download {}".format(id))
        except:
            print("It seems like you gave me a wrong ID\n")
            sleep(1)

        

    if question.lower() == "videos":
        creator = input("Give me a twitch username to search vods from:\n")
        try:
            os.system("twitch-dl videos {}".format(creator))
        except:
            print("No vods were found from that user :(")
            sleep(1)



