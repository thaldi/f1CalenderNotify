import socket
import win32.lib.win32serviceutil as win32serviceutil
import win32.servicemanager as servicemanager
import win32.win32event as win32event
import win32.win32service as win32service


class SMWinServiceBase(win32serviceutil.ServiceFramework):

    _svc_name_ = "SampleleService"
    _svc_display_name_ = "Sample Service"
    _svc_description_ = "Service Sample Description"

    @classmethod
    def parse_command_line(cls):

        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):

        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):

        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):

        self.start()
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )
        self.main()

    def start(self):

        pass

    def stop(self):

        pass

    def main(self):

        pass


if __name__ == "__main__":
    SMWinServiceBase.parse_command_line()
