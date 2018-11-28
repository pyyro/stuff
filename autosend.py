#bot for spamming  twitch chat
import re
import time
import socket

HOST = "irc.twitch.tv"
PORT = 6667
CHAN = input("Insert channel name: ")
CHAN = "#" + CHAN
NICK = input("Your twitch name (all lowercase): ")
PASS = input("Copy paste what you get here www.twitchapps.com/tmi/: ")

sendmessage = input("What to send? ")
delay = int(input("And every how many seconds? "))

s = socket.socket()
s.connect((HOST, PORT))

s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        time.sleep(delay)
        s.send("PRIVMSG {} :{}\r\n".format(CHAN, sendmessage).encode("utf-8"))
