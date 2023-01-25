import hashlib

from pathlib import Path

ARQUIVO_SENHAS = Path('../base_c_hash.csv')

def load_fields() -> list:
    with open(ARQUIVO_SENHAS, 'r') as fp:
        lines = fp.readlines()[1:]
    
    lines = list(map(lambda x: x.strip(), lines))

    return list(map(lambda x: x.split(';'), lines))

def user_exist(username: str) -> bool:
    usernames = list(map(lambda x: x[0], load_fields()))

    return username in usernames
        
def create_user(username: str, passwd: str) -> None:
    if not user_exist(username):

        # Implemente sua solução a partir daqui

        with open(ARQUIVO_SENHAS, 'a') as fp:
            fp.write(f'{username};{passwd}\n')
        
        print(f'User \'{username}\' created')
    else:
        print('Username already exists')

def get_user_index(username: str) -> int:
    if not user_exist(username):
        return -1

    for i, line in enumerate(load_fields()):
        if line[0] == username:
            return i
    
def login(username: str, passwd: str) -> bool:
    user_index = get_user_index(username)
    if user_index == -1:
        print('Incorrect username or password')
    elif user_index >= 0: 
        fields = load_fields()[user_index]

        # Implemente sua solução a partir daqui

def get_opt() -> int:
    try:
        return int(input('>>> '))
    except ValueError:
        print('Option does not exist')
        return -1

def motd() -> None:
    print('Welcome! Please, select an option:')
    print('\t1. Login')
    print('\t2. Create account')
    print('\t3. Exit')

def action_create_user() -> None:
    print('Please, provide your')
    uname = input('Username: ')
    passwd = input('Password: ')

    create_user(uname, passwd)

def action_login() -> None:
    print('Please, provide your')
    uname = input('Username: ')
    passwd = input('Password: ')

    login(uname, passwd)

commands = {
    1: action_login,
    2: action_create_user,
}

if __name__ == '__main__':
    while True:
        motd()
        opt = get_opt()

        if opt == 3:
            break

        commands[opt]()
        print()
        print('-='*30)
        print()