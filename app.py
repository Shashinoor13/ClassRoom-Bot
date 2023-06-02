import os
import discord
from discord.ext import commands

# from dotenv import load_dotenv
# import random

# load_dotenv()
# DISCORD_TOEKN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)


import json

file = open("routine.json")
Routine = json.load(file)


def format_response(day):
    response = (
        "**"
        + day
        + "**\n"
        + "9:00 : "
        + Routine[day]["09:00"]
        + "\n10:00 : "
        + Routine[day]["10:00"]
        + "\n11:00 : "
        + Routine[day]["11:00"]
        + "\n12:00 : "
        + Routine[day]["12:00"]
        + "\n13:00 : "
        + Routine[day]["13:00"]
        + "\n14:00 : "
        + Routine[day]["14:00"]
        + "\n15:00 : "
        + Routine[day]["15:00"]
    )
    return response


@bot.event
async def on_ready():
    print(f"{bot.user} succesfully logged in!")


@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user:
        return

    if message.content == "hello":
        await message.channel.send(f"Hi {message.author}")
    if message.content == "bye":
        await message.channel.send(f"Bye {message.author}")

    if message.content.lower() == "routine-sun":
        response = format_response("Sunday")
        await message.channel.send(response)
    if message.content.lower() == "routine-mon":
        response = format_response("Monday")
        await message.channel.send(response)
    if message.content.lower() == "routine-tue":
        response = format_response("Tuesday")
        await message.channel.send(response)
    if message.content.lower() == "routine-wed":
        response = format_response("Wednesday")
        await message.channel.send(response)
    if message.content.lower() == "routine-thu":
        response = format_response("Thursday")
        await message.channel.send(response)
    if message.content.lower() == "routine-fri":
        response = format_response("Friday")
        await message.channel.send(response)
    if message.content.lower() == "routine-sat":
        response = "**Kina chaiyo Sanibar Pani Class?**"
        await message.channel.send(response)
    if message.content.lower() == "routine-help":
        response = (
            "**Commands**\n"
            + "routine-sun\n"
            + "routine-mon\n"
            + "routine-tue\n"
            + "routine-wed\n"
            + "routine-thu\n"
            + "routine-fri\n"
            + "routine-sat\n"
        )
        await message.channel.send(response)
    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
