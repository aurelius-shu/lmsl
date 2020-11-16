import pdb
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)

logging.info('xxx')