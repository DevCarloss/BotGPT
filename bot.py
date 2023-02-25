import discord
import json
from discord.ext import commands
from discord import app_commands
import dotenv
import os
import requests
dotenv.load_dotenv(dotenv.find_dotenv("env"))

# Bot GPT Discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/',intents=intents)

@bot.command()

async def completion(ctx,*,arg1):
    url = "https://api.openai.com/v1/completions"
    headers = {
     "Content-Type": "application/json",
     "Authorization": "Bearer " + os.getenv("APITOKEN"),
     "Accept": "application/json"
    }
    data = json.dumps({
     "model": "text-davinci-003",
     "prompt": str(arg1),
     "temperature": 0.5, 
     "max_tokens": 2048
    })

    req_API = requests.post(url,headers=headers,data=data).json()

    try:
        for texto in req_API['choices']:
            embed = discord.Embed(
                title = "**"+ "BotGPT" + "**",
                description =   "\n" + "\n" + texto['text'],
                color = discord.Color.from_rgb(183,207,117)
            )
            embed.set_footer(text="OpenAI")
            await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title = "**" + "Bot GPT" + "**",
            description= "\n" + "\n" + "Desculpe! Houve um erro a o tentar processar a resposta",
            color = discord.Color.from_rgb(183,207,117)
        )
        embed.set_footer(text="OpenAI")
        await  ctx.send(embed=embed)

@bot.command()

async def helper(ctx):
    titulo = 'BotGPT'
    descricao = 'É um bot desenvolvido na linguagem python' + '\n' + 'que ultiliza a API da OpenAI para obter as resposta dos comandos' + '\n' + '\n'  + 'Comandos' + '\n' + '\n' +  '**' + '``/completion``' + '**' + '\n' +  'Para Gerar e Editar Textos'
    embed = discord.Embed(
        title = "**" +  titulo + '**',
        description = descricao,
        color = discord.Color.from_rgb(255,255,255)
    )
    embed.set_footer(text="OpenAI")
    await ctx.send(embed=embed)

    
bot.run(os.getenv("BOTTOKEN"))