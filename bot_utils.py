# Bot token used to login
# Fist line of 'ids-txt'
def get_bot_token():
	f = open('ids.txt', 'r')
	lines = f.readlines()
	f.close()
	bot_token = lines[0].strip()
	return bot_token

# Weeby user ID in rpi-thermometer server
# Second line of 'ids-txt'
def get_weeby():
	f = open('ids.txt', 'r')
	lines = f.readlines()
	f.close()
	weeby = '<@{}>'.format(lines[1].strip())
	return weeby

# Rpi-thermometer channel ID
# Third line of 'ids.txt'
def get_channel_id():
	f = open('ids.txt', 'r')
	lines = f.readlines()
	f.close()
	channel = '{}'.format(lines[2].strip())
	return channel

def generate_close_message(temp_f):
	close_message = get_weeby() +'\n'
	close_message += ':snowflake::rotating_light: *CLOSE THE WINDOWS* :rotating_light::snowflake:\n'
	close_message += ':snowflake::rotating_light:    *Temperature: {:.1f} F*     :rotating_light::snowflake:'.format(temp_f)
	return close_message

def generate_open_message(temp_f):
	open_message = get_weeby() + '\n'
	open_message += ':fire: :rotating_light: *OPEN THE WINDOWS* :rotating_light: :fire:\n'
	open_message += ':fire: :rotating_light:   *Temperature: {:.1f} F*    :rotating_light: :fire:'.format(temp_f)
	return open_message