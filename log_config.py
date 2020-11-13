import logging

LOG_FILENAME = "messages.log"
# Logging toolbox 🔊
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("webhook")
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
fileHandler = logging.FileHandler(LOG_FILENAME, encoding='UTF-8')
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

# logging.getLogger('walker').propagate = False