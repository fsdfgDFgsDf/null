import os, sys, requests
from pathlib import Path

APP_ROOT = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_ROOT))

# Now import normally
from ex.logger import log

asciiart = Path(f'{os.getcwd()}/src/content/ascii.art').read_text(encoding='utf-8')

def gettoken():
    print('TOKEN >> ', end='')
    token = input()
    log('LOG', '1', 'Grabbed token.')

    return token

def verifytoken(token):
    token = token
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
        "Authorization": token
    }

    response = requests.get(url, headers=headers)
    log('LOG', '1', 'Verifying token against Discord API.')

    if response.status_code == 200:
        valid = 'VALID'
        log('LOG', '1', 'Token is valid, returning to menu')
        return valid, token[:-65] + '(' + '*' * 10 + ')'
    else:
        valid = 'INVALID'
        log('ERR', '3', 'Token is invalid, returning to menu')
        return valid, None

print(asciiart)
log('LOG', '1', 'Starting menu.')

token = gettoken()
print(asciiart)
valid, masked = verifytoken(token)

print(f'                              TOKEN >> {masked}\n                                    STATUS >> {valid}\n')
log('LOG', '1', 'Printed results, sucsessful run.')