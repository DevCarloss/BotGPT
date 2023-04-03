import discord
from discord.ext import commands
import os
import openai
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv('.env'))

# OPENAI Credentials
openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# Bot GPT 2.0 OPENAI
intents = discord.Intents.all()
client = commands.Bot(command_prefix='/',intents=intents)

# First Command
# Image Generation

# Learn how to generate or manipulate images with our DALL·E models
# Introduction

# The Images API provides three methods for interacting with images:
# Creating images from scratch based on a text prompt
# Creating edits of an existing image based on a new text prompt
# Creating variations of an existing image
# This guide covers the basics of using these three API endpoints with useful code samples. To see them in action, check out our DALL·E preview app.

@client.command()
async def ia_getimage(ctx,*,arg1):
    try:
        response = openai.Image.create(
            prompt = str(arg1),
            n = 1,
            size = "1024x1024"
        )
        imageUrl = response['data'][0]['url']
        embed = discord.Embed(
            title = "**ChatGPT Image Generator**",
            description = "Prompt: " + str(arg1),
            color = discord.Color.from_rgb(40,256,163)
        )
        embed.set_image(url=imageUrl)
        embed.set_footer(text="OPENAI" + '\n' + 'Discord Bot Developer: @DevCarloss')
        await ctx.send(embed=embed)

    except:
        embed = discord.Embed(
            title = "**Error Generating Response Try Again**",
            color = discord.Color.from_rgb(255,255,255)
        )
        embed.set_footer(text="OPENAI" + '\n' + 'Discord Bot Developer: @DevCarloss')
        await ctx.send(embed=embed)

# Second Command
# Chat Completions

# Using the OpenAI Chat API, you can build your own applications with gpt-3.5-turbo and gpt-4 to do things like:
# Draft an email or other piece of writing
# Write Python code
# Answer questions about a set of documents
# Create conversational agents
# Give your software a natural language interface
# Tutor in a range of subjects
# Translate languages
# Simulate characters for video games and much more
# This guide explains how to make an API call for chat-based language models and shares tips for getting good results. You can also experiment with the new chat format in the OpenAI Playground.

#Introduction
#Chat models take a series of messages as input, and return a model-generated message as output.
#Although the chat format is designed to make multi-turn conversations easy, it’s just as useful for single-turn tasks without any conversations (such as those previously served by instruction following models like text-davinci-003).

@client.command()
async def ia_chatcompletion(ctx,*,arg1):
    try:
        response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=[
              {"role": "user", "content": str(arg1)},
           ]
        )
        completion_result = response['choices'][0]['message']['content']
        embed = discord.Embed(
            title = "**ChatGPT Chat Completions**",
            description = '\n' + str(completion_result),
            color = discord.Color.from_rgb(197,240,55)
        )
        embed.set_footer(text="OPENAI" + '\n' + 'Discord Bot Developer: @DevCarloss')
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title = "**Error Generating Response Try Again**",
            color = discord.Color.from_rgb(255,255,255)
        )
        embed.set_footer(text="OPENAI" + '\n' + 'Discord Bot Developer: @DevCarloss')
        await ctx.send(embed=embed)

# Three Command
# Text Completions

# Learn how to generate or manipulate text
# Introduction
# The completion endpoint can be used for a wide variety of tasks. It provides a simple yet powerful interface for any of our templates. You enter some text as a prompt and the template will generate a text completion that tries to match whatever context or pattern you have provided. For example, if you give the API the prompt, "As Descartes said, I think therefore", it will return the conclusion "I am" with high probability.
# The best way to start exploring findings is through our Playground. It's simply a text box where you can send a prompt to generate a completion. To try it out for yourself, open this example in the Playground:
# Write a slogan for an ice cream shop.
# After submitting, you will see something like this:
# Write a slogan for an ice cream shop. We serve smiles with every spoonful!
# The actual conclusion you see may differ because the API is not deterministic by default. This means that you might get a slightly different conclusion every time you call it, even if your prompt remains the same. Setting the temperature to 0 will make the outputs more deterministic, but a small amount of variability may remain.
# This simple text entry interface means you can "program" the model by providing instructions or just a few examples of what you would like it to do. Your success often depends on the complexity of the task and the quality of your prompt. A good rule of thumb is to think about how you would write a word problem for a high school student to solve. A well-written prompt provides enough information so the model knows what you want and how it should respond.
# This guide covers general prompt design best practices and examples. To learn more about working with code using our Codex templates, visit our code guide.

@client.command()
async def ia_textcompletion(ctx,*,arg1):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=str(arg1),
            temperature=0.7,
            max_tokens=2048,
            n=1,
            stop=None
        )
        completion_result = response['choices'][0]['text']
        embed = discord.Embed(
            title = "**ChatGPT Text Completions**",
            description = '\n' + str(completion_result),
            color = discord.Color.from_rgb(160,160,160)
        )
        embed.set_footer(text="OPENAI" + '\n' + 'Discord Bot Developer: @DevCarloss')
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title = "**Error Generating Response Try Again**",
            color = discord.Color.from_rgb(255,255,255)
        )
        embed.set_footer(text="OPENAI" + '\n' + 'Discord Bot Developer: @DevCarloss')
        await ctx.send(embed=embed)
if __name__ == '__main__':
     client.run(os.getenv("BOTTOKEN"))