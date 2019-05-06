import logging
logging.basicConfig(filename='app.log', format='%(asctime)s-%(name)s - %(levelname)s - %(message)s',level=logging.INFO)
# logging.disable(logging.INFO)
a = 5
b = 2

try:
    logging.info(a)
    c = a / b
    logging.info(c)
except Exception as e:
    logging.exception("Exception occurred", exc_info=True)
