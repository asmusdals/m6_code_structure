import sys
from loguru import logger

logger.remove()  # Remove the default logger
logger.add(sys.stdout, level="WARNING")  # Only WARNING and above


logger.debug("used for debug")
logger.info("used for info messages about code")
logger.warning("alt virker men der er fejl i noget")
logger.error("der er fejl i process")
logger.critical("noget er dybt godnat og terminerer processs")

logger.add("logs/my_log.log",level="DEBUG",rotation="100 MB")
