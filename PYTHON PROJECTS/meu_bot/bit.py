import discord
from discord.ext import commands
import random as r
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("oi" * count_heh)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(r.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

from bot_logic import g_senha

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('oi'):
        await message.channel.send("Olá!")
    elif message.content.startswith('tchau'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('senha'):
        await message.channel.send("sua senha é " + g_senha(8))
    elif message.content.startswith('moeda'):
        lado = r.randint(1, 2)
        if lado == 1:
            await message.channel.send(f'Caiu coroa!')
        if lado == 2:
            await message.channel.send(f'Caiu cara!')

@bot.command()
async def meme(ctx):
    imagens = os.listdir('images')
    imagem = r.choice(imagens)
    with open(f'images/{imagem}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

bot.run("MTU1NDU0NTg5NzE4NDk2MDUzNA.GFkF4A.W98R41czZg7hnfhkHNRPKE_phyvMQ7sOoaWaCM")
