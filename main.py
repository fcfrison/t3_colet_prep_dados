import sys
from extract import extract
from transform import transform
if sys.argv[1]=='extract':
    extract()
if sys.argv[1]=='transform':
    transform()