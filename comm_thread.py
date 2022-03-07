class MathServerCommunicationThread(Thread):
	def __init__(self, conn, addr):
		Thread.__init__(self)
		self.conn = conn
		self.addr = addr

	def run(self):
		print("{} connected with back port {}".format(self.addr[0], self.addr[1]))
		self.conn.sendall("Simple Math Server developed by LAHTP \n\nGive any math expressions, and I will answer you :) \n\n$ ".encode())

		## APPLICATION LAYER 7
		p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
		output = ProcessOutputThread(p, self.conn)
		output.start()
