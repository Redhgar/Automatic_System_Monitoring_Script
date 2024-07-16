import psutil
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#logging base settings
logging.basicConfig(filename='system_monitoring.log',  #name of the logging file
			level=logging.INFO,		#level of logging 
			format='%(asctime)s - %(levelname)s - %(message)s') #logging format

#email settings
def send_email(subject, body):
	from_email =
	to_email =
	password = 

	#E-mail creation
	msg = MIMEMultipart()
	msg['From'] = from_email
	msg['To'] = to_email
	msg['Subject'] = subject

	msg.attach(MIMEText(body, 'plain'))

	#SMTP server settings and email sending
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(from_email, password)
	server.sendmail(from_email, to_email, msg.as_string())
	server.quit()

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

		

		#logging message
		log_message = (
			f'CPU usage: {cpu_percent}%'
			f'Memory usage: {memory.percent}%'
			f'Disk usage: {disk.percent}%'
			f'Network incoming traffic: {net.bytes_recv}'
		)
		#logging
		logging.info(log_message)

		#Sending email every 10th time (10 minutes)
		if int(time.time()) % 60 < 60:
			send_email('System data logs', log_message)

		time.sleep(60)
		

if __name__== '__main__':
	log_system_usage()
