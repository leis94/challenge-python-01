# Resolve the problem!!

PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
    'Ana',
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi'
    'Oscar',
]


def is_palindrome(palindrome):
    espacios = 0
    for x in palindrome:
        if ' ' in x: 
            espacios += 1 
    
    palindrome_alrevez = palindrome[::-1]
    igual, aux = 0, 0
    for ind in range(0, len(palindrome)):
        if palindrome[ind].isspace():
            continue
        
        elif palindrome_alrevez[aux].isspace():
            aux += 1
            palindrome[ind].lower() == palindrome_alrevez[aux].lower()
            igual += 1
            aux += 1            
            continue
        
        elif palindrome[ind].lower() == palindrome_alrevez[aux].lower():
            igual += 1
        aux += 1



    if (len(palindrome) - espacios) == igual:
        return True
        

def validate():
    for palindrome in PALINDROMES:
        if not is_palindrome(palindrome):
            return False

    for not_palindrome in NOT_PALINDROMES:
        if is_palindrome(not_palindrome):
            return False
    return True


def run():
    if validate():
        print('Completaste el test')
    else:
        print('No completaste el test')


if __name__ == '__main__':
    run()
