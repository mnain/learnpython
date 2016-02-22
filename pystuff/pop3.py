#!/usr/bin/python
 
import poplib
 
accounts = [
	 {'server' : 'mail.nain.cc',
	  'user' : 'madan@nain.cc',
	  'pass' : 'Kri28shn!0'
	 },
	 {'server' : 'mail.mnain.org',
	  'user' : 'madan@mnain.org',
	  'pass' : 'Kri28shn!0'
	 }
	 ]
 
#print str(accounts)
for ac in accounts:
	print 'Handle %s' % ac['server']
	pop = poplib.POP3(ac['server'])
	pop.user(ac['user'])
	pop.pass_(ac['pass'])
	(count, sz) = pop.stat()
	for i in range(1,count+1):
		pop.dele(i)
		print "%s: Delete %d" % (ac['server'],i)
	pop.quit()
