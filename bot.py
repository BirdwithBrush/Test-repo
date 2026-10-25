import discord
import random
from bot_logic import gen_pass

token = ""
# intents variable stores the permissions of the bot
intents = discord.Intents.default()
# Enable the permission to read message content
intents.message_content = True
# Create a bot and pass the intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message.author.id)
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$gen_pass'):
        parts = message.content.split()
        if len(parts) == 2 and parts[1].isdigit():
            length = int(parts[1])
            if length > 0:
                response = gen_pass(length)
                await message.channel.send(response)
            else:
                await message.channel.send("Enter a number greater than 0.")
        else:
            await message.channel.send("Usage: $gen_pass <length>")
    elif message.content.startswith('$flip_coin'):
        result = random.choice(["Heads", "Tails"])
        await message.channel.send(result)
    elif message.content == '$shutdown':
        if message.author.id == 1217937508286070846:
            await message.channel.send("Shutting down...")
            await client.close()
        else:
            await message.channel.send("Please enter a valid number! Example: $gen_pass 12")
    else:
        await message.channel.send(message.content)

client.run(token)
