import discord
from discord.ext import commands, tasks
from itertools import cycle
import os



intents = discord.Intents.all()
intents.message_content = True
my_secret = os.environ['TOKEN']
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='.',intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return




@client.event
@commands.has_permissions(administrator=True)
async def on_reaction_add(reaction, user):
  if (reaction.emoji == '✉️'):
    txt=reaction.message.content
    msg1 = await reaction.message.channel.send("Please enter channel id")
    def check(m):
      return m.author == user and m.channel == reaction.message.channel
    message = await client.wait_for("message", check=check)
    sti = int(message.content)
    channel = client.get_channel(sti)
    await channel.send(txt)
    await reaction.message.delete()
    await message.delete()
    await msg1.delete()

  if (reaction.emoji == '📧'):
    txt=reaction.message.content
    msg1 = await reaction.message.channel.send("Please enter channel id")
    def check(m):
      return m.author == user and m.channel == reaction.message.channel
    message = await client.wait_for("message", check=check)
    sti = int(message.content)
    channel = client.get_channel(sti)
    Moji = await channel.send(txt)
    
    await reaction.message.delete()
    await message.delete()
    await msg1.delete()
    

    lop = 0
    while lop<1:
      msg2 = await reaction.message.channel.send("Please give emoji names")
      def check(m):
        return m.author == user and m.channel == reaction.message.channel
      message = await client.wait_for("message", check=check)
      myReaction = message.content
      if myReaction == "stop":
        await msg2.delete()
        await message.delete()
        break
      else: 
        await Moji.add_reaction(myReaction)
        await msg2.delete()
        await message.delete()
        
        
  if (reaction.emoji == '📨'):
    txt=reaction.message.content
    msg1 = await reaction.message.channel.send("Please enter message id")
    def check(m):
      return m.author == user and m.channel == reaction.message.channel
    message = await client.wait_for("message", check=check)
    sti = (message.content)
    message = await reaction.message.channel.fetch_message(sti)
    await message.edit(content=txt)


  
  if (reaction.emoji == '🎀'):
    txt=reaction.message.content
    msg1 = await reaction.message.channel.send("Please enter message id")
    def check(m):
      return m.author == user and m.channel == reaction.message.channel
    message = await client.wait_for("message", check=check)
    sti = (message.content)
    messageReact = await reaction.message.channel.fetch_message(sti)

    lop = 0
    while lop<1:
      msg2 = await reaction.message.channel.send("Please give emoji names")
      def check(m):
        return m.author == user and m.channel == reaction.message.channel
      message = await client.wait_for("message", check=check)
      myReaction = message.content
      if myReaction == "stop":
        await msg2.delete()
        await message.delete()
        break
      else: 
        await messageReact.add_reaction(myReaction)
        await msg2.delete()
        await message.delete()



  

status = cycle(['PokemonGO','UUM'])

@bot.event
async def on_ready():
  change_status.start()
  print("Your bot is ready")

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

client.run(my_secret)

