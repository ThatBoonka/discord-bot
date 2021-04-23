import discord
import random

SERVER_NAME = "Bot Playground"
client = discord.Client()
 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.guilds}')
    guild = discord.utils.find(lambda g: g.name == SERVER_NAME, client.guilds)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.isnumeric():
        number = int(message.content)
        await message.channel.send(number+1)

    if message.content[0] == "?":
        if 'coin' in message.content.lower():
            flip = random.randint(0, 1)
            if flip == 1:
                await message.channel.send('Heads')
            else:
                await message.channel.send('Tails')

        if 'image' in message.content.lower():
            rand_idx = random.randint(1,38)
            file_path = f'./img/{rand_idx}.jpg'
            await message.channel.send(file=discord.File(file_path))
        
        if 'video' in message.content.lower():
            rand_idx = random.randint(1,5)
            file_path = f'./vid/{rand_idx}.mp4'
            await message.channel.send(file=discord.File(file_path))

        if 'r' in message.content.lower():
            result = 0
            info = message.content[2:].lower().split ('d')
            for i in range(int(info [0])):
                result = random.randint(1,int(info[1]))
                await message.channel.send(str(result))                   
        
        # if 'self' in message.content.lower():
        #     file_path = './bot.py'
        #     await message.channel.send(file=discord.File(file_path))

    # if 'joe' in message.content.lower():
    #     await message.channel.send('mama')
    # if 'happy birthday' in message.content.lower():
    #     await message.channel.send('Happy Birthday! 🎈🎉')

@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel
    if channel is not None and channel.id == '822833330877759503':
       cloned_channel = await channel.clone(name='new_channel')
    print(channel)

client.run(TOKEN)