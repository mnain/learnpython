import win32serviceutil
import win32service
import win32event
import servicemanager


class Service(win32serviceutil.ServiceFramework):
	_svc_name_ = 'DemoService'
	_svc_display_name_ = 'DemoService'
	_svc_description_ = 'DemoService description ...'

	
	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		self.isAlive = True


	def SvcStop(self):
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		self.isAlive = False

		
	def SvcDoRun(self):
		while self.isAlive:
			rc=win32event.WaitForSingleObject(self.hWaitStop, 1000)
			servicemanager.LogInfoMsg("looping")
		win32event.SetEvent(self.hWaitStop)