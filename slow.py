import os
import sys
import time
from time import sleep

def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(20. / 60)

slowprints("■■■■■■■■■■100%")


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2 / 100)

slowprint('''[ >>>>>>>>>>>>>>>>>>>>>>> ]100%''')

slowprint('''
╭━━━━━━━━━━━━━━━━━━━━╮
┃       ● ════       ┃
┃████████████████████┃
┃████████████████████┃
┃████████████████████┃
┃████████████████████┃
┃██+-+-+-+-+-+-+-+███┃
┃██|D|O|N|E|4|U|S|███┃
┃██+-+-+-+-+-+-+-+███┃
┃████████████████████┃
┃████████████████████┃
┃████████████████████┃
┃████████████████████┃
┃    =     ○     <   ┃
╰━━━━━━━━━━━━━━━━━━━━╯

''')

slowprint('''
                       // ¤ \\
                       \\ ¤ //
                        \\\//
                        (___)
                        (___)
                        (___)
             \_____/\__/     \__/ \_____/
              \ _ ​[  . *DONE4US* . ]​ _ /
                   \___𓬞*ROHIT*�___/
                     . \ __°__ /.
                       |\_°_/|
                        [|\_/|]
                        [|[¤]|]
                        [|;¤;|]
                        [;;¤;;]
                       ;;;;¤]|]\\
                      ;;;;;¤]|]-\\
                     ;;;;;[¤]|]--\\
                    ;;;;;|[¤]|]---\\
                   ;;;;;[|[¤]|]|---|
                  ;;;;;[|[¤]|]|---|
                  ;;;;[|[¤]|/---/
                  ;;;[|[¤]/---/
                  ;;[|[¤/---/
                    ;[|[/---/
                    [|/---/
                    /---/
                   /---/|]
                 /---/]|];
               /---/¤]|]
              |---|[¤]|];;;
              |---|[¤]|];;;;
               \--|[¤]|];;;;
                 \-|[¤]|];;;;
                   \|[¤]|];;;
                     \\¤//
                       \|/ ''')


slowprint('''
▂▃▅▇█▓▒░۩۞۩ *Done4us* ۩۞۩░▒▓█▇▅▃▂ ''')