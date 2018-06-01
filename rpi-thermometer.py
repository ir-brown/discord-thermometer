import discord
import thermometer
import asyncio
import bot_utils

client = discord.Client()
temp_threshold_low 	= 60.0
temp_threshold_high = 85.0
channel_id = bot_utils.get_channel_id()
bot_token = bot_utils.get_bot_token()

async def monitor_temp():
	await client.wait_until_ready()
	channel = discord.Object(id=channel_id)
	while not client.is_closed:
		c,f = thermometer.read_temp()
		if f <= temp_threshold_low:
			await client.send_message(channel, bot_utils.generate_close_message(f))
		if f >= temp_threshold_high:
			await client.send_message(channel, bot_utils.generate_open_message(f))
		await asyncio.sleep(600)

@client.event
async def on_ready():
	print("Logged in as {}".format(client.user))
	print('------------------')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		await client.send_message(message.channel, 'Hello!')

	if message.content.startswith('!temp'):
		c,f = thermometer.read_temp()
		await client.send_message(message.channel, 'Temperature - F: {:.1f}'.format(f))

	## Test commands ##

	# if message.content.startswith('!testcold'):
	# 	c,f = thermometer.read_temp()
	# 	await client.send_message(message.channel, bot_utils.generate_close_message(f))

	# if message.content.startswith('!testhot'):
	# 	c,f = thermometer.read_temp()
	# 	await client.send_message(message.channel, bot_utils.generate_open_message(f))


client.loop.create_task(monitor_temp())
client.run(bot_token)
