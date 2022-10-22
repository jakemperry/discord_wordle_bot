def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'stats':
        return "I know words, but I'm still working on numbers."

    if p_message == '!help':
        return "`This is a help message that will be modified to be helpful later.`"

    