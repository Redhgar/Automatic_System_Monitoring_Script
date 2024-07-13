import psutil
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.test import MIMEText
#logging base settings

logging.basicConfig(filename='system_monitoring.log', 
			level=logging.INFO, 
			format='%(asctime)s - %(levelname)s - %(message)s')

def log_system_usage():
	while True:
		# cpu usage
		cpu_percent = psutil.cpu_percent(interval=1)
		
		# memory usage
		memory = psutil.virtual_memory()

		# disk usage
		disk = psutil.disk_usage('/')

		# network traffic
		net = psutil.net_io_counters()


		#logging
		logging.info(f'CPU usage: {cpu_percent}%')
		logging.info(f'Memory usage: {memory.percent}%')
		logging.info(f'Disk usage: {disk.percent}%')
		logging.info(f'Network incoming traffic: {net.bytes_recv}')

		# logtime
		time.sleep(60)

if __name__== '__main__':
	log_system_usage()
