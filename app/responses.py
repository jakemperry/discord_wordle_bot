def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'stats':
        return "I know words, but I'm still working on numbers."

    if p_message == '!help':
        return "`This is a help message that will be modified to be helpful later.`"
    if p_message == "todays answer" or "today's answer":
        return "Today's word has five letters, one of which is probably a vowel."
    