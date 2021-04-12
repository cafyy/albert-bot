import sys

from albert_bot.albert_bot import MyClient

if __name__ == "__main__":
    client = MyClient()
    client.run('discord token')
