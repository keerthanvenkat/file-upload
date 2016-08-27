from .base import *

try:
	from .dev import *
except:
	pass
# else:
# 	print DEBUG
# 	print MIDDLEWARE_CLASSES

try:
	from .prod import *
except:
	pass