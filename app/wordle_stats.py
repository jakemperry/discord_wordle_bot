# import pandas as pd

def mine_scores(message):
    print(message)
    message_chunks = message.replace("\n"," ").split(" ")
    game_score = message_chunks[2].split("/")[0]
    if game_score == "X":
        game_score = "0"
    game_score = int(game_score)
    if game_score > 0:
        win = True
    else: win = False

    return message_chunks, game_score, win