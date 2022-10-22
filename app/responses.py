from wordle_stats import mine_scores

def handle_response(message) -> str:
    p_message = message.lower()

    # if p_message[0:6] =='wordle':
    #     print(p_message)
    #     # message_chunks, game_score, win = mine_scores(p_message)
    #     # print(f"win={win}")
    #     # if win == False:
    #     #     win_response= "Rough game, better luck next time"
    #     # else: win_response = f"Congrats, you won the game in {game_score} plays!"
    #     # return win_response
            
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'stats':
        return "I know words, but I'm still working on numbers."

    if p_message == '!help':
        return "`This is a help message that will be modified to be helpful later.`"
    
    if p_message == "todays answer":
        return "Today's word has five letters, one of which is probably a vowel."
    