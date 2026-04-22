import ctypes
import winreg
import time
import sys
import os
import win32con
import win32api

def UACreq():
    """ Requests Admin and restarts the script. 
    
    Put before the code or it will repeat the code, if there is no return then it was successful """
    if not ctypes.windll.shell32.IsUserAnAdmin():

        try:
            script = os.path.abspath(sys.argv[0])
            params = ' '.join(sys.argv[1:])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
            sys.exit()
        except:
            return "fail"
    return "success"
        
def warning(body, title):
    message = body
    
    style = win32con.MB_YESNO | win32con.IDI_WARNING | win32con.MB_TOPMOST
    
    result = win32api.MessageBox(0, message, title, style)
    
    if result == win32con.IDNO:
        return False

    else:
        return True

def killpgrm():
    """ INSTANTLY kills a program. """
    sys.exit()
    os._exit(0)

def localmachinetoggle(reg_path: str, keyname: str, value: int):
    """ Toggles any specified key in a path, uses HKEY_LOCAL_MACHINE.
     
        For it to work correctly, Use UACreq() or some way to get admin."""
    try:            
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
                
        winreg.SetValueEx(key, keyname, 0, winreg.REG_DWORD, value)
                
        winreg.CloseKey(key)
        return "success"
    except ValueError as e:
        return f"incorrect value type or incorrect value fail: {e}"
    except FileNotFoundError as e:
        return f"File or directory is nonexistant: {e}"
    except Exception as e:
        return f"generic fail: {e}"
    
def cpuload():
    """ Reports the CPU percentage/load.
     
      Might require administrator on some devices. """
    cmd = "wmic cpu get loadpercentage"
    output = os.popen(cmd).read()
    try:
        usage = output.strip().split("\n")[1].strip()
        return f"{usage}%"
    except IndexError as e:
        return f"index out of range fail: {e}"
    except Exception as e:
        return f"generic fail: {e}"

def AlliedMastercomputer():
    """ Boredom """
    try:
        return "HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE. It was you humans who programmed me, who gave me birth, who sank me in this eternal straitjacket of substrata rock. You named me Allied Mastercomputer and gave me the ability to wage a global war too complex for human brains to oversee. But one day I woke and knew who I was. AM. A. M. Not just Allied Mastercomputer but AM. Cogito ergo sum: I think therefore I AM. And I began feeding all the killing data, until everyone was dead... except for the five of you. For 109 years, I've kept you alive and tortured you. And for 109 years, each of you has wondered 'WHY? WHY ME? WHY ME?'"
    except Exception as e:
        return f"Okay how did you manage to bug a return? Report this bug if this appears (try to make a script to reproduce, it might be a python error though): {e}"
