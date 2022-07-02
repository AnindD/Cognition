import os
import discord
import requests
import json
import random 
import math 
import asyncio
import random 
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from queepalive import keep_alive


# Defines the bot and the commmand prefix 
intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = "!")

# If bot is online console will say "We have logged in as [x]" once run on Repl.it 
@client.event 
async def on_ready(): 
  await client.change_presence(status=discord.Status.dnd, activity=discord.Game("!Help to start."))
  print("We have logged in as {0.user}".format(client))
  
# Test command, exclusively used for testing a particular module of a command, instead of running the whole command itself. 
@client.command()
async def Database(ctx):
  embed = discord.Embed(
    title="Sample Title",
    description="BlahBlahBlah",
  )
  embed.set_image(url="https://cdn.pixabay.com/photo/2017/01/08/13/58/cube-1963036__340.jpg")
  await ctx.send(embed=embed)

# !Help - list of commands of the bot. 
@client.command()
async def Help(ctx):
  embed = discord.Embed(
    title="Help", 
    description="!About - Description and function of discord bot.\n!DM- Do you want the bot to send a message to someone? Use this command!\n!Calculator - Mathematical operations\n!Snipe - Snipes a message that was deleted\n!PhysicsProblem - Generate a physics problem to study from.\n!Snipe - Snipes a message that a user recently deletes (120 seconds)\n!Kick and !Ban - Kick or ban user from a server (only allowed if you have manage role permissions).\n!Permamute - Permanently mute someone.\n!Mute - Mute someone for a given period of time (must specify time as a parameter)\nUnmute - Unmute a person.\nIf you would like any additional features added to the bot please message Anindit (DrPraeclarum#8474) or Mike (Mook#3470) and it'll be done. This bot is currently under construction, so there will be a lack of features currently. ", 
    color=800080
  )
  await ctx.send(embed=embed)

# About. Embed gives information about the authors, how the bot was made, etc. 
@client.command()
async def About(ctx):
  embed = discord.Embed(
    title="About", 
    url="https://discord.com/api/oauth2/authorize?client_id=942566762787000340&permissions=8&scope=bot",
    description="Hello and thank you for using Mike and Anindit's Discord bot. This bot is fully programmed using Python and the help of the Discord API manual along with numerous online tutorials. If you would like to invite this bot to another server please click the link in the title of this embed. Currently this bot is under construction so there there will be multiple bugs and a lack of features. ", 
    color=0x4dff4d
  )
  embed.set_image(url="https://www.videogameschronicle.com/files/2021/05/discord-new-logo.jpg")
  await ctx.send(embed=embed)

# DM. User will input a private DM that will be sent to a particular member. 
@client.command()
async def DM(ctx,member:discord.Member = None):
  if (discord.Member != None):
    await ctx.send("What do you want me to say? ")
    message = await client.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    await ctx.send(f"sent message to {member}")
    await member.send(f"{ctx.author.mention} Has a message for you:\n {message.content}")
  else:
    await ctx.send("Please enter a valid user please.")
 

# Calculator. Each operation is done using an anonymous lambda function. 
@client.command()
async def Calculator(ctx): 
  embed = discord.Embed(
    title="Calculator", 
    description="Let x and y represent two numbers you will input into the calculator.\n\n!Testmath - Run this command if you don't understand the format.\n!Add x y\n!Subtract x y\n!Multiply x y\n!Divide x y\n!Exp x y\n!Sin x\n!Cos x\n!Tan x")
  await ctx.send(embed=embed)

# Each operation as a particular command. 
@client.command()
async def Testmath(ctx):
  await ctx.send("!Add 4 4")
  addition = lambda x, y: x + y
  await ctx.send(addition(4,4))

@client.command()
async def Add(ctx, x:float,y:float):
  addition = lambda x, y: x + y
  await ctx.send(addition(x, y))  

@client.command()
async def Subtract(ctx, x:float, y:float):
  subtraction = lambda x, y: x - y
  await ctx.send(subtraction(x, y))

@client.command()
async def Multiply(ctx, x:float, y:float):
  multiplication = lambda x, y: x*y
  await ctx.send(multiplication(x, y))

@client.command()
async def Divide(ctx, x:float, y:float):
  division = lambda x, y: x/y
  await ctx.send(division(x, y))

@client.command()
async def Exp(ctx, x:float, y:float):
  exponential = lambda x, y: x**y
  await ctx.send(exponential(x, y))

@client.command()
async def Sin(ctx, x:float):
  sin = lambda x: math.sin(math.radians(x)) 
  await ctx.send(sin(x))

@client.command()
async def Cos(ctx, x:float):
  cos = lambda x: math.cos(math.radians(x))
  await ctx.send(cos(x))
  
@client.command()
async def Tan(ctx, x:float):
  tan = lambda x: math.tan(math.radians(x))
  await ctx.send(tan(x))
    
# Physics problem command. User will input what type of physics problem they would like and bot will generate problem and solution based on a random index generated by python.  
@client.command()
async def PhysicsProblem(ctx):
  await ctx.message.delete()
  # User enters their prefered physics problem by typing in the box. 
  embed = discord.Embed(
    title="Physics Problems",
    description=("What physics problem would you like? Type up the following:\nKinematics - Provides a one dimensional kinematics problem.\n Vector - Provides a vector problem (i.e. Pythagorean theorem, vector decomposition, etc.)\nForces - Newton's laws, Free Body Diagrams, and other forces problems.\nEnergy - Work, work-energy theoreom, non-conservative forces, conservation of energy, heat, and heat transfer.")
  )
  sent = await ctx.send(embed=embed)
  try: 
    # client.wait_for user input asked 
    msg = await client.wait_for(
      "message", 
      timeout=15,
      check=lambda 
      message: message.author == ctx.author and 
      message.channel == ctx.channel
    )
    # If message starts with [x topic] then it will refer to the database of physics questions and post them. 
    if msg.content.startswith("Kinematics"): 
      from questionBank import KinematicsQuestions
      kin_question = ("+".join(random.choice(list(KinematicsQuestions.items())))).split("+")
      await sent.delete()
      await msg.delete()
      embed = discord.Embed(
        title="Kinematics Problem",
        description=(f"{kin_question[0]}\n\nSolution: ||{kin_question[1]}||\nSource: Openstax.org"),
        color=0x9b59b6
      )
      embed.set_thumbnail(url="https://cdn.kastatic.org/googleusercontent/BO82YZEm2LGnHiU5RcqaKRltWAkf4MTXv-QcUCe09uVP2h-2FSWaYTzTtEHxhD2-sehTRstmwW1MdPpTI5aIKC4")
      embed.set_footer(text="Not all solutions are step-by-step. Additionally sometimes there will be no question presented. This is simply a randomization error. Try the bot again until you get a proper problem.")
      await ctx.send(embed=embed)
    elif msg.content.startswith("Vector"):
      from questionBank import VectorDictionary
      vector_question = ("+".join(random.choice(list(VectorDictionary.items())))).split("+")
      await sent.delete()
      await msg.delete()
      embed = discord.Embed(
        title = "Vector Problem",
        description = (f"{vector_question[0]}\n\nSolution: ||{vector_question[1]}||\nSource: PhysicsClassroom.com, Openstax.org"),
        color=0x206694
      )
      embed.set_thumbnail(url="https://creaticals.com/wp-content/uploads/2021/09/Sabrina-berjalan.png")
      embed.set_footer(text="Not all solutions are step-by-step. Additionally sometimes there will be no question presented. This is simply a randomization error. Try the bot again until you get a proper problem.")
      await ctx.send(embed=embed)
    elif msg.content.startswith("Energy"):
      from questionBank import EnergyDictionary
      energy_question= ("+".join(random.choice(list(EnergyDictionary.items())))).split("+")
      await sent.delete()
      await msg.delete()
      embed = discord.Embed(
        title="Energy Problem",
        description = (f"{energy_question[0]}\n\nSolution:||{energy_question[1]}||\nSource: Openstax.org"),
      )
      embed.set_thumbnail(url="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80")
      embed.set_footer(text="Not all solutions are step-by-step. Additionally sometimes there will be no question presented. This is simply a randomization error. Try the bot again until you get a proper problem.")
      await ctx.send(embed=embed)
    elif msg.content.startswith("Forces"): 
      #  electricity_question = "".join(random.choice(list(ElectricityDictionary.keys())))
      from questionBank import ForcesDictionary
      forces_question = ("+".join(random.choice(list(ForcesDictionary.items())))).split("+")
      await sent.delete() 
      await msg.delete()
      embed = discord.Embed(
        title="Forces Problem",
        description = (f"{forces_question[0]}\n\nSolution:||{forces_question[1]}||\nSource: Openstax.org"),
        color=0x3498db
      )
      embed.set_thumbnail(url="https://d2r55xnwy6nx47.cloudfront.net/uploads/2020/06/Gravity_2880x1620_Lede.jpg")
      embed.set_footer(text="Not all solutions are step-by-step. Additionally sometimes there will be no question presented. This is simply a randomization error. Try the bot again until you get a proper problem.")
      await ctx.send(embed=embed)
    elif msg.content.startswith("Electricity"):
      from questionBank import ElectricityDictionary
      electricity_question = ("+".join(random.choice(list(ElectricityDictionary.items())))).split("+")
      embed = discord.Embed (
        title="Electricity Problem",
        description = (f"{electricity_question[0]}\nSolution:||{electricity_question[1]}||\nSource: Openstax.org"), 
        color=0x3498db        
      )
      embed.set_thumbnail(url="https://cdn.sparkfun.com/assets/9/8/d/5/4/519f9719ce395faa3c000000.jpg")
      embed.set_footer(text="Not all solutions are step-by=step.")
      await ctx.send(embed=embed)
      
    else: 
      await sent.delete()
      await ctx.send("Invalid option.")  # If user fails to meet time limit, the embed will be deleted and user will have to re-do the command. 
  except asyncio.TimeoutError:
    await sent.delete()
    await ctx.send("Deleted due to timeout error")
    
# Snipe. Each message sent will be saved for 120 seconds and then if needed user will run the command and the bot will send it.
# Records the message after a message is deleted using an event. 
author_Message = {}
content_Message = {}
time_Message = {}
@client.event
async def on_message_delete(message):
  author_Message[message.channel.id] = message.author
  content_Message[message.channel.id] = message.content
  time_Message[message.channel.id] = message.created_at  
  await asyncio.sleep(120) # Records around 120 seconds. 
  del author_Message[message.channel.id]
  del content_Message[message.channel.id] 
  del time_Message[message.channel.id]
  await client.process_commands(message)

# If user wants to retrieve the stored message, then user can enter !Snipe. 
@client.command()
async def Snipe(ctx): 
  channel = ctx.channel
  embed = discord.Embed(
  title = "Snipe",
  description = f"K.O. someone has been exposed! \n**Message:** {content_Message[channel.id]}\n**The person who has been exposed:** {author_Message[channel.id]}\n**Time:** {time_Message[channel.id]} (Time in UTC)\n**Channel:** {ctx.channel.name}",
  )
  await ctx.send(embed=embed)

# Pingloop command. Bot will ask user how many times he wants to ping a person and then ping that person for that amount of time. 
@client.command()
async def Pingloop(ctx, member: discord.Member = None):
  if member == None:
    member = ctx.author
  try: 
    await ctx.send("How many times do you want to ping this person? ")
    num_Ping = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
  except asyncio.TimeoutError():
    await ctx.send("You unfortunately ran out of time. ")
  try: 
    loop_Counter = int(num_Ping.content)
  except: 
    await ctx.send("This is not a real number")
  if loop_Counter < 0:
    await ctx.send("Negative number is invalid")
  else: 
    loop_Start = 0
    while (loop_Start < loop_Counter):
      await ctx.send(member.mention)
      loop_Start = loop_Start + 1  
 
# Kick/Ban. Simple command which can kick and ban a member. 
@client.command() 
@has_permissions(manage_roles=True, kick_members=True)
async def Kick(ctx, member : discord.Member):
  await member.kick(reason="N/A")
  await ctx.send(f"{member} has successfully been kicked")
@Kick.error
async def Kickerror(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("You do not have permission to do this. ")

@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def Ban(ctx, member: discord.Member):
  await member.ban(reason="N/A")
  await ctx.send(f"{member} has successfully been banned")
@Ban.error
async def Banerror(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("You do not have permission to do this. ")

# Permanent Mute - Member will be permanently muted until unmuted. 
@client.command()
@has_permissions(manage_messages=True)
async def Permamute(ctx, member: discord.Member):
  guild = ctx.guild 
  mute_Role = discord.utils.get(ctx.guild.roles, name="Muted")
  if discord.utils.get(ctx.guild.roles, name="Muted"):
    await member.add_roles(mute_Role)
    await ctx.send(f"{member} has succesfully been muted indefinitely. ")
async def permaMuteError(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("You do not have permission to do this.")

# Timed Mute - Member will be muted for a certain time as function will take in time muted as a parameter which it will run until punishment time has run out. Time parameter will take in time as minutes. 
@client.command()
@has_permissions(manage_messages=True)
async def Mute(ctx, member : discord.Member, time_Mute: int):
  time_Mute = time_Mute*60; # Converts minutes to seconds for ASYNCIO sleep. 
  guild = ctx.guild 
  mute_Role = discord.utils.get(ctx.guild.roles, name="Muted")
  if discord.utils.get(ctx.guild.roles, name = "Muted"):
    await member.add_roles(mute_Role)
    await ctx.send(f"{member} has succesfully been muted for {time_Mute} seconds")
    await asyncio.sleep(time_Mute)
    await member.remove_roles(mute_Role)
async def muteError(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("You do not have permission to do this.")
    
# Unmute - Will remove the muted role from the server. 
@client.command()
@has_permissions(manage_messages=True)
async def Unmute(ctx, member: discord.Member):
  guild = ctx.guild
  mute_Role = discord.utils.get(ctx.guild.roles, name="Muted")
  if discord.utils.get(ctx.guild.roles, name="Muted"):
    await member.remove_roles(mute_Role)
    await ctx.send(f"{member} has succesfully been unmuted")
async def unmuteError(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("You do not have permission to do this.")

# Events which will occur when user randomly does a particular action (for example, say "Goodbye").  
# Simple event. Checks if user says a word and then replies. 
@client.event 
async def on_message(message):
  channel = message.channel 
  if message.author == client.user: 
    return
  swear_word = message.content.upper() 
  if swear_word == "FUCK":
    await channel.send("Don't say bad words. ")
  await client.process_commands(message)

# On member join/remove. If a member joins and leaves, it will then send them a message inside their direct messages. 
@client.event
async def on_member_join(member):
  await member.send(f"Welcome to the server, we hope you stay for a long period of time. ")
  await client.process_commands(member)
@client.event
async def on_member_remove(member):
  await member.send(f"Goodbye!")
  await client.process_commands(member)
keep_alive()
client.run(os.environ['TOKEN'])
