#!/usr/bin/env python3

import sys
import py2srbcyr as psc

cir = psc.SerbCyr()
data = sys.stdin.read()
print(cir.text_to_latin(data))
