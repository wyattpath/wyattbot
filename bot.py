import discord
from discord.ext import commands

TOKEN = 'NTAyNTkwNjE5MDEzNjExNTQw.DqqQHA.Hn7V8ef9xUcHlvInozZ1YwdMhV4'

client = commands.Bot(command_prefix  = 'wyatt ')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Test'))
    print('Bot is ready.')

#autorole
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Example Role')
    await client.add_roles(member, role)

#clear
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('{} messages deleted.'.format(amount))

#logs the users messages
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)

'''
#reposts message when message is deleted
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))
'''

#returns Pong
@client.command()
async def ping():
    await client.say('Pong!')

#returns the message
@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


client.run(TOKEN)
