"""Functions related to the terminal output
interface of the pulse charging system"""

BLUE   = '\033[34m'
WHITE  = '\033[37m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
RED    = '\033[31m'

def stats(*args):
    print(f"{BLUE}{'  |  '.join([str(round(e,3)) if isinstance(e, float) else str(e) for e in args])}{WHITE}")

def begin(cycle_number):
    print(f"{GREEN}BEGIN CYCLE {cycle_number}{WHITE}")
    
def pulse():
    print(f"{GREEN}PULSE CHARGING...{WHITE}")

def taper():
    print(f"{GREEN}TAPER CHARGING...{WHITE}")

def stand(sec):
    print(f"{GREEN}STANDING FOR {sec} SEC...{WHITE}")

def discharge():
    print(f"{GREEN}DISCHARGING...{WHITE}")

def exit_ok():
    print(f"{GREEN}PROCESS COMPLETE, NOW EXITING{WHITE}")

def kb_interrupt():
    print(f"{YELLOW}CTRL+C PRESSED{WHITE}")
    
def exception(e):
    print(f"{RED}UNHANDLED EXCEPTION:\n{e}{WHITE}")