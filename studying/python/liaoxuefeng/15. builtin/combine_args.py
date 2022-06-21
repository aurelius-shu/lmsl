from argparse import Namespace
from collections import ChainMap
import os, argparse

defauts = {'user': 'guest', 'color': 'red'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# 查找时，现在 command_line_args 中查找，如果没有，再在 os.environ 查找，最后时 defaults
combined_args = ChainMap(command_line_args, os.environ, defauts)

print('color=%s' % combined_args['color'])
print('user=%s' % combined_args['user'])
