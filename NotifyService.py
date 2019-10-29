import time
from WinServiceBase import SMWinServiceBase
import f1Scheduler as f1


class F1Notify(SMWinServiceBase):
    _svc_name_ = "F1NotifyService"
    _svc_display_name_ = "F1 Notify Service"
    _svc_description_ = "Running every hour for check to race date. If there is a race notify with windows toast."

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:

            f1.Check()

            time.sleep(60 * 60)


if __name__ == "__main__":
    F1Notify.parse_command_line()
