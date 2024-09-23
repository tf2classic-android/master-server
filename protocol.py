class MasterProtocol:
	# Client To Master
	clientQuery = b'1'

	# Server To Master
	challengeRequest = b'w' # xFF
	addServer = b'y'
	removeServer = b'z'

	# Master To Client
	queryPacketHeader = b'\xff\xff\xff\xffJ'

	# Master To Server
	challengePacketHeader = b'\xff\xff\xff\xffx'
