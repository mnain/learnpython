#!/usr/bin/env python

HOSTNAME            = 0
LEVEL               = HOSTNAME+1
AUTH_PROTOCOL       = LEVEL+1
PRIVACY_PROTOCOL    = AUTH_PROTOCOL+1
PRIVACY_PASSPHRASE  = PRIVACY_PROTOCOL+1
USERNAME            = PRIVACY_PASSPHRASE+1
AUTH_PASSPHRASE     = USERNAME+1
TYPE                = AUTH_PASSPHRASE+1

columns = [ 'hostname',                 # 0
            'level',                    # 1
            'auth_protocol',            # 2
            'privacy_protocol',         # 3 
            'privacy_passphrase',       # 4
            'username',                 # 5
            'auth_passphrase',          # 6
            'type'                      # 7
            ]

if __name__ == "__main__":
	print ",".join(columns)
