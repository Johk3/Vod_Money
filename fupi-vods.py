import os
from time import sleep

setup = True
running = True
allfiles = os.listdir()

for root, dirs, files in os.walk("config_check"):
    for filename in files:
        if filename == "true.txt":
            print("Everything should be running smoothly....\n\n")
            setup = False

if setup:
    try:
        os.system("python setup.py install && cd youtube && python setup.py install")
        file1 = open("config_check/true.txt", "w")
        file1.write("The installation of Fupi-Vods should be working.")
        file1.close()
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
            newfiles = os.listdir()
            for file in newfiles:
                if file not in allfiles:
                    os.system("move \"{}\" output".format(file))
                    vod_path = os.path.dirname(os.path.abspath(__file__)) + "\\output\\{}".format(file)
                    title = input("Title of the video:\n")
                    description = input("Description of the video:\n")
                    tags = input("Tags for the video. Example: mutter, beethoven:\n")
                    os.system("cd youtube/bin && youtube-upload --title=\"{}\" --description=\"{}\" --tags=\"{}\" "
                              "--category=Gaming --default-language=\"en\" --client-secrets=client_id.json \"{}\"".format(title, description, tags, vod_path))
        except:
            print("It seems like you gave me a wrong ID\n")
            sleep(1)

        # newfiles = os.listdir()
        #
        # for file in newfiles:
        #     if file not in allfiles:
        #         print(file)


    if question.lower() == "videos":
        creator = input("Give me a twitch username to search vods from:\n")
        try:
            os.system("twitch-dl videos {}".format(creator))
        except:
            print("No vods were found from that user :(")
            sleep(1)



