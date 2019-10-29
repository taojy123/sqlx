
import os
import sys
import traceback

import sqlx


try:
	sqlx.auto('.')
except:
	traceback.print_exc()
	input('See https://github.com/taojy123/sqlx/blob/master/README.md for help')


