import os
import random

import discord
from discord.ext import commands


RECOMMENDATIONS = {
    "energia": [
        "Apague as luzes ao sair de um cômodo e aproveite a luz natural durante o dia.",
        "Desligue da tomada carregadores e aparelhos que não estiver usando.",
        "Prefira lâmpadas LED, que consomem menos energia e duram mais.",
        "Use a máquina de lavar com carga completa para evitar ciclos desnecessários.",
    ],
    "agua": [
        "Feche a torneira enquanto escova os dentes ou ensaboa a louça.",
        "Tome banhos mais curtos para economizar água e energia.",
        "Conserte torneiras com vazamento assim que puder.",
        "Reaproveite água da chuva ou da lavagem de frutas para regar plantas.",
    ],
    "residuos": [
        "Separe recicláveis limpos e secos dos resíduos orgânicos.",
        "Use uma composteira para transformar restos de alimentos em adubo.",
        "Prefira garrafas, canecas e sacolas reutilizáveis aos descartáveis.",
        "Antes de jogar algo fora, veja se pode consertar, doar ou reutilizar.",
    ],
    "ar": [
        "Evite queimar lixo ou folhas; a fumaça prejudica a qualidade do ar.",
        "Mantenha os ambientes ventilados e limpe o pó com um pano úmido.",
        "Se possível, prefira produtos sem fragrâncias fortes e com menos compostos voláteis.",
        "Não fume dentro de casa: a fumaça também polui o ar interno.",
    ],
    "limpeza": [
        "Use apenas a quantidade necessária de produtos de limpeza.",
        "Escolha produtos biodegradáveis e com menos embalagem quando possível.",
        "Nunca misture produtos de limpeza, especialmente água sanitária com outros produtos.",
        "Evite aerossóis quando houver uma alternativa sem spray.",
    ],
    "compras": [
        "Planeje as refeições e as compras para evitar desperdício de alimentos.",
        "Prefira produtos duráveis, reparáveis e com pouca embalagem.",
        "Compre alimentos da estação e de produtores locais quando possível.",
        "Reutilize potes e embalagens antes de comprar novos recipientes.",
    ],
}

CATEGORY_ALIASES = {
    "água": "agua",
    "águas": "agua",
    "lixo": "residuos",
    "reciclagem": "residuos",
    "resíduos": "residuos",
    "qualidade do ar": "ar",
    "limpeza": "limpeza",
    "compras": "compras",
    "energia": "energia",
}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command(name="dica")
async def dica(ctx, *, categoria: str = ""):
    """Envia uma recomendação geral ou de uma categoria específica."""
    categoria = categoria.strip().casefold()
    categoria = CATEGORY_ALIASES.get(categoria, categoria)

    if not categoria:
        categoria = random.choice(list(RECOMMENDATIONS))
    elif categoria not in RECOMMENDATIONS:
        categorias = ", ".join(RECOMMENDATIONS)
        await ctx.send(
            f"Não conheço essa categoria. Escolha entre: {categorias}."
        )
        return

    recomendacao = random.choice(RECOMMENDATIONS[categoria])
    await ctx.send(f"**Dica de {categoria}:** {recomendacao}")


@bot.command(name="categorias")
async def categorias(ctx):
    """Lista os temas disponíveis para as recomendações."""
    await ctx.send(
        "Temas disponíveis: " + ", ".join(RECOMMENDATIONS) + ". "
        "Exemplo: `!dica agua`."
    )


@bot.command(name="ajuda")
async def ajuda(ctx):
    """Mostra como usar o bot."""
    await ctx.send(
        "**Bot de dicas para reduzir a poluição em casa**\n"
        "`!dica` — recebe uma dica aleatória.\n"
        "`!dica energia` — recebe uma dica sobre um tema específico.\n"
        "`!categorias` — lista os temas disponíveis.\n"
        "Temas: energia, agua, residuos, ar, limpeza e compras."
    )


token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    raise RuntimeError(
        "Defina a variável de ambiente DISCORD_BOT_TOKEN com o token do bot."
    )

bot.run(token)