import logging.handlers

logger = logging.getLogger('test logger')
http_handler = logging.handlers.HTTPHandler('www.viltstigen.se', '/logger/log', method='POST', secure=True)
logger.addHandler(http_handler)

logger.warning('Hey log a warning as well')
logger.error("Hey log a error again")

