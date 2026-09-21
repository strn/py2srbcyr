#!/usr/bin/env python3

import sys
import py2srbcyr as psc

data = sys.stdin.read()
print(psc.text_to_cyrillic(data), end="")
