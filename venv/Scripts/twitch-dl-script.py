#!C:\Users\johkm\PycharmProjects\Fupi-Vods\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'twitch-dl==0.1.0','console_scripts','twitch-dl'
__requires__ = 'twitch-dl==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('twitch-dl==0.1.0', 'console_scripts', 'twitch-dl')()
    )
