#!/usr/bin/env python

import base64

o = 'this_is_a_strong_key';

e = base64.b64encode(o)

print e

