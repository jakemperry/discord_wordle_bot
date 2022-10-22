from wordle_stats import pull_stats

def handle_response(message, author) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'stats':
        last_week_stats, lw_wins, lw_win_pct, lw_plays, lw_play_avg, last_month_stats, lm_wins, lm_win_pct, lm_plays, lm_play_avg = pull_stats(author)

        return f"{author}, in the last week you've won {lw_wins} games ({lw_win_pct}%).  You made {lw_plays} word guesses, averaging about {lw_play_avg} guesses per game. \n\nIn the last month, you've won {lm_wins} games ({lm_win_pct}%).  You made {lm_plays} word guesses, averaging about {lm_play_avg} guesses per game."
    
    if p_message == 'stats details':
        last_week_stats, lw_wins, lw_win_pct, lw_plays, lw_play_avg, last_month_stats, lm_wins, lm_win_pct, lm_plays, lm_play_avg = pull_stats(author)
        return f"{author}, here's a detailed view of your wordle games over the last month. \n\n{last_month_stats}"

    if p_message == 'ranking':
        return "Stop comparing yourself to others (at least until you have enough data)"

    if p_message == '!help':
        return f"Hey {author}, you can try the following commands to get information:\n\n`stats`: returns a summary of your weekly and monthly stats\n\n`stats details`: see a big ol' list of all your game data for the last month\n\n`ranking`: see how you compare against others playing in this wordle channel\n\n\nAny time you post a Wordle game (copy/paste whatever NYT gives you), I'll track your score.  You'll know I've saved your game info when I react with an emoji that matches however many plays you had in the game ('4' for 4 guesses, 'X' for not being able to guess the word in 6 tries)."
    
    if p_message == "todays answer":
        return "Today's word has five letters, one of which is probably a vowel."
    