import socket
from subprocess import Popen, STDOUT, PIPE
from threading import Thread
from comm_thread import MathServerCommunicationThread
from process_thread import ProcessOutputThread
