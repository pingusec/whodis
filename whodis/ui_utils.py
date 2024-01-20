# +--------------------+
# | Const declarations |
# +--------------------+

LINE_UP = '\033[1A' # ANSI char to move to prev line
LINE_CLEAR = '\x1b[2K' # ANSI char to clear the line


# +------------+
# | UI Methods |
# +------------+

def clear(num_lines: int = 1):
    """Clears a user specified number of lines from stdout. Clears a default value of 1 line"""
    for x in range(num_lines):
        print(LINE_UP, end=LINE_CLEAR)


# +------------------------------------------------+
# | Methods to return commonly accessed UI content |
# +------------------------------------------------+

def getMainMenu():
    """Returns rich formatted main-menu content
    
    Returns:
    str:Multi-line string of main-menu options
    """

    title = r'''[cyan1]
          _               _ _     
__      _| |__   ___   __| (_)___ 
\ \ /\ / / '_ \ / _ \ / _` | / __|
 \ V  V /| | | | (_) | (_| | \__ \
  \_/\_/ |_| |_|\___/ \__,_|_|___/
-----------------------------------[cyan1]

[white]1) Fake login page[white]
'''
    return title


def getFakeLoginMenuOptions():
    """Returns rich formatted list of available fake login pages

    Returns:
    str:Multi-line string of avaiable login pages
    """

    fake_login_options = r'''[white]Available login pages:

1) Testing example[white]
'''
    return fake_login_options