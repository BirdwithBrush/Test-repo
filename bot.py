import discord
import random
from discord.ext import commands
from bot_logic import gen_pass as generate_password

token = ""

# Intents variable stores the permissions of the bot
intents = discord.Intents.default()

# Enable the permission to read message content
intents.message_content = True

# Create a bot with a command prefix
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# Hello command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


# Bye command
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")


# Password generator command
@bot.command()
async def gen_pass(ctx, length: int):
    if length > 0:
        response = generate_password(length)
        await ctx.send(response)
    else:
        await ctx.send("Enter a number greater than 0.")


# Flip a coin command
@bot.command()
async def flip_coin(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(result)


# Shutdown command
@bot.command()
async def shutdown(ctx):
    if ctx.author.id == 1217937508286070846:
        await ctx.send("Shutting down...")
        await bot.close()
    else:
        await ctx.send("You do not have permission to shut down this bot.")

bot.run(token)
