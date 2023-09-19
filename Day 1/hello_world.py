
PINK = '\033[95m'
CYAN = '\033[96m'
RED = '\033[31m'
ENDC = '\033[0m' # Removes all formatting applied.


preview = f'''
    {PINK}╔{'═'*23}╗
    ║{RED}♦♦{CYAN} Hello World! {RED}♦♦{PINK}║
    ╚{'═'*23}╝{ENDC}
    '''

print(preview)

