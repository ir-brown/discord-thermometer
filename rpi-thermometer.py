import discord
import thermometer
import asyncio
import bot_utils

low_temp	= 63.0
high_temp	= 90.0

client = discord.Client()
bot_token, weeby_id, channel_id = bot_utils.init()
alert = False

#Adjust this function to save recordings and report out on discord log
async def monitor_temp():
	await client.wait_until_ready()
	global alert
	while not client.is_closed:
		temp = thermometer.read_temp()
		if (low_temp >= temp or temp >= high_temp) and not alert:
			alert = True
		await asyncio.sleep(600)

# Alerts weeby if temperature is above/below threshold and continuing to climb/fall
# Alarm is cancelled when temperature falls between thresholds again
async def alarm():
	await client.wait_until_ready()
	global alert
	prev_temp = 0
	channel = discord.Object(id=channel_id)
	while alert and not client.is_closed:
		temp = thermometer.read_temp()
		if temp >= high_temp and temp > prev_temp:
			prev_temp = temp
			await client.send_message(channel, bot_utils.open_message(weeby_id, temp))
		if temp <= low_temp and temp < prev_temp:
			prev_temp = temp
			await client.send_message(channel, bot_utils.close_message(weeby_id, temp))
		if temp < high_temp and temp > low_temp:
			await client.send_message(channel, bot_utils.normal_temp())
			alert = False
		if alert:
			await asyncio.sleep(900)

@client.event
async def on_ready():
	print("Logged in as {}".format(client.user))
	print('------------------')
	client.loop.create_task(monitor_temp())
	client.loop.create_task(alarm())

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!hi'):
		await client.send_message(message.channel, 'Hello!')

	if message.content.startswith('!temp'):
		temp = thermometer.read_temp()
		await client.send_message(message.channel, 'Temperature - {}°F'.format(temp))

	if message.content.startswith('!alert'):
		global alert
		await client.send_message(message.channel, '{}'.format(alert))

	## Test commands ##

	# if message.content.startswith('!testcold'):
	# 	c,f = thermometer.read_temp()
	# 	await client.send_message(message.channel, bot_utils.generate_close_message(f))

	# if message.content.startswith('!testhot'):
	# 	c,f = thermometer.read_temp()
	# 	await client.send_message(message.channel, bot_utils.generate_open_message(f))

client.run(bot_token)
