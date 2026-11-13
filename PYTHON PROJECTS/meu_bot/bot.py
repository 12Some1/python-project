import discord
from m1l3.bot_logic import g_senha
import random as r

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


client.run("MTU1NDU0NTg5NzE4NDk2MDUzNA.GFkF4A.W98R41czZg7hnfhkHNRPKE_phyvMQ7sOoaWaCM")

