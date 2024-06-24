import json
import os

import aiohttp
import discord
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


async def send_rasa_message(message, user):
	headers = {
		'Content-Type': 'application/json',
	}

	data = json.dumps(
		{
			'sender': user,
			'text': message,
		}
	)

	async with aiohttp.ClientSession() as session:
		async with session.post(
				'http://localhost:5005/webhooks/discord/webhook',
				headers=headers,
				data=data
		) as response:
			return await response.json()


@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	response = await send_rasa_message(message.content, message.author.id)
	for res in response:
		content = res.get('text') or res.get('image')
		await message.channel.send(content)


bot.run(os.getenv("DISCORD_TOKEN"))
