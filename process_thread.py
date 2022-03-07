class ProcessOutputThread(Thread): #OOPS
	def __init__(self, proc, conn):
		Thread.__init__(self)
		self.proc = proc
		self.conn = conn
