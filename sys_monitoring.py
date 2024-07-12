import psutil
import time
import logging

#logging alap beállítások

logging.basicConfig(filename='system_monitoring.log', 
			level=logging.INFO, 
			format='%(asctime)s - %(levelname)s - %(message)s')

