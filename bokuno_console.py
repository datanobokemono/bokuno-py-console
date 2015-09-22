""" Module for getting console arguments and many other useful features.
"""
import sys

# Get arguments from command line as python Dictionary
def get_args():
	commands = {}
	last_command = ""
	first = 1

	def is_command(arg):
		return len(arg) > 1 and arg[0] == '-'

	for arg in sys.argv:
		if is_command(last_command):
			commands[last_command] = 0 if is_command(arg) else arg
			last_command = arg if is_command(arg) else ""
		elif is_command(arg):
			last_command = arg

	# If last argument was also command
	if is_command(last_command):
		commands[last_command] = 0

	return commands

# Output str to console and keep the cursor at the same line
# Used for outputting progress data
def update_print(str):
	sys.stdout.flush()
	print(str, end='')