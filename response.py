from random import choice

def get_response(user_input):
    lowered = user_input.lower()

    if lowered == '':
        return '....nothing?'
    elif 'hello' in lowered:
        return 'Welcome to Montana State!'
    else:
        return choice(['I dont understand...', 'Try again', 'Can you say that any differently?'])
