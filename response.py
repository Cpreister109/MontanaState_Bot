from random import choice

def get_response(user_input):
    lowered = user_input.lower()

    if lowered == '':
        return '....nothing?'
    elif 'hi' in lowered:
        return 'Welcome to Montana State!'
    elif 'what server is this?' in lowered:
        return 'A test server of course!!'
    elif 'how are you?' in lowered:
        return 'Great! I hope you are doing well too!'
    else:
        return choice(['I dont understand...', 'Try again', 'Can you say that any differently?'])
