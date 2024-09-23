from time import time
from struct import pack
from struct import unpack

def unpack_string(data):
	result = ''
	for i in data:
		if i == 0: break
		result += chr(i)

	return result

class ServerEntry:
	challenge = 0
	challenge2 = 0
	gamedir = ''
	protocol = 0

	def setInfoString(self, data):
		self.challenge2 = unpack('<I', data[:4])[0]
		self.protocol = unpack('<H', data[4:6])[0]
		self.gamedir = unpack_string(data[6:])

		self.die = time() + 600

		self.check = (self.challenge == self.challenge2) and (self.protocol >= 25)
		return self.check

	def __init__(self, addr, challenge):
		# Address
		self.addr = addr
		# Shortcuts for generating query
		self.queryAddr = b''
		for i in reversed(addr[0].split('.')):
			self.queryAddr += pack('B', int(i))
		self.queryAddr += pack('H', int(addr[1]))

		# Random number that server must return
		self.challenge = challenge
		self.sentChallengeAt = time()

		# This server is not checked
		# So it will not get into queries
		self.check = False

		# Remove server after this time.
		# This maybe not instant
		self.die = self.sentChallengeAt + 600
