from pystyle import *
import os
from colorama import *
import time
import asyncio
import json
import websockets
from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import random

os.system('clear' if os.name == 'posix' else 'cls')

intro = """
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██╗   ██╗ ██████╗ ██╗ ██████╗███████╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██║   ██║██╔═══██╗██║██╔════╝██╔════╝
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║   ██║██║   ██║██║██║     █████╗         by ayhu
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝         
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝
                                                                                             
                                    > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.red_to_yellow, Colorate.Vertical, interval=0.035, enter=True)

print(f"""{Fore.LIGHTBLUE_EX}
      

██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██╗   ██╗ ██████╗ ██╗ ██████╗███████╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██║   ██║██╔═══██╗██║██╔════╝██╔════╝
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║   ██║██║   ██║██║██║     █████╗         by ayhu
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝         
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝
                                                                                             
           

""")

time.sleep(1)

Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)

Write.Print("\n> 1 - join voice ", Colors.red_to_yellow)

Write.Print("\n> 2 - voice spam ", Colors.red_to_yellow)

Write.Print("\n> 3 - exit ", Colors.red_to_yellow)



askim = int(input("\nchoice: "))


if askim == 1:
    print("Don't forget to put your tokens in Tokens.txt")

    with open("tokens.txt", "r") as token_file:
        tokens = token_file.readlines()
        server_id = input("Server ID: ")
        channel_id = input("Channel ID: ")

    async def connect(token):
        async with websockets.connect('wss://gateway.discord.gg/?v=9&encoding=json') as websocket:
            hello = await websocket.recv()
            hello_json = json.loads(hello)
            heartbeat_interval = hello_json['d']['heartbeat_interval']
            await websocket.send(json.dumps({"op": 2,"d": {"token": token.strip(),"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            await websocket.send(json.dumps({"op": 4,"d": {"guild_id": server_id,"channel_id": channel_id,"self_mute": False,"self_deaf": False}}))
            while True:
                await asyncio.sleep(heartbeat_interval/1000)
                try:
                    await websocket.send(json.dumps({"op": 1,"d": None}))
                except Exception:
                    break

    async def main():
        tasks = []
        for token in tokens:
            task = asyncio.create_task(connect(token))
            tasks.append(task)
        await asyncio.gather(*tasks)

    asyncio.run(main())

elif askim == 2:
    print("Don't forget to put your tokens in Tokens.txt")

    tokenlist = open("tokens.txt", 'r').read().splitlines()
    server = int(input("Server ID: "))
    channel = int(input("Channel ID: "))
    deaf = input("Deafen: (y/n) ")
    if deaf == "y":
        deaf = True
    if deaf == "n":
        deaf = False
    mute = input("Mute: (y/n) ")
    if mute == "y":
        mute = True
    if mute == "n":
        mute = False
    stream = input("Stream: (y/n) ")
    if stream == "y":
        stream = True
    if stream == "n":
        stream = False
    video = input("Video: (y/n) ")
    if video == "y":
        video = True
    if video == "n":
        video = False

    executor = ThreadPoolExecutor(max_workers=int(1000))

    def run(token):
        ws = WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
        hello = loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
        ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
        ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
        
        
        stay_duration = 1
        wait_duration = 1
        
        while True:
            sleep(stay_duration)
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": None,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))  # çık
            sleep(wait_duration)
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))  # gir

    os.system(f"title Total Tokens: {len(tokenlist)}")
    i = 0
    for token in tokenlist:
        executor.submit(run, token)
        i += 1
        print("[+] Joined voice channel")
        
        sleep(random.uniform(0.1, 0.1))

elif askim == 3:
    print("Exiting the program...")
else:
    print("You have entered invalid. Please try again.")
