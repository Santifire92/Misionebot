import discord
import os
import random

bar_triggers = ['barras', 'beef', 'cabio']
laugh_triggers = ['jaj']
nicebot_triggers = ['nice']
bar_responses = ['Uoooo!', 'RUIDOOOOOO']
laugh_responses = ['Ooooo jojojo']

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for keyword in bar_triggers:
        if keyword in message.content.lower():
            response = random.choice(bar_responses)
            await message.channel.send(response)

    for keyword in laugh_triggers:
        if keyword in message.content.lower():
            response = random.choice(laugh_responses)
            await message.channel.send(response)

@bot.command(aliases=['paly', 'queue', 'que'])
async def play(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('barras.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


client.run("ODAzNDU5Njc4MDc0ODMwODU4.YA-GIg.yXyD-JW_owlaBCrc5A71enmoZlk")