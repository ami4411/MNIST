import logging
import logging.config 
import yaml
import sys

class Logger:

	def __init__(self, run_mode):
		self.run_mode = run_mode

	def log(self):
		with open('logger/config.yaml', 'r') as f:

		    log_cfg = yaml.safe_load(f.read())

		logging.config.dictConfig(log_cfg)
		logger = logging.getLogger(self.run_mode)
		logger.setLevel(logging.INFO)

		return logger
