import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def mine_scores(player, text):
    # print(text)
    # print(player)
    game_day = datetime.now().strftime("%Y-%m-%d")
    game_time = datetime.now().strftime("%H:%M:%S")
    print(game_time)
    message_chunks = text.replace("\n"," ").split(" ")
    game_num = int(message_chunks[1])
    game_score = message_chunks[2].split("/")[0]
    if game_score == "X":
        game_plays = message_chunks[4:10]
    else: game_plays = message_chunks[4:(4+int(game_score))]

    play_cnt = len(game_plays)
    play_nums = np.arange(1, play_cnt+1, 1, dtype=int)
    if game_score == "X":
        game_score = "0"
    game_score = int(game_score)
    if game_score > 0:
        win = True
    else: win = False

    record = pd.DataFrame(
        {
            "date": game_day,
            "time": game_time,
            "player": player,
            "game_num" : game_num,
            "play_cnt": play_cnt,
            "play_num" : play_nums,
            "game_plays": game_plays,
            "game_score": game_score,
            "win": win
        }
    )

    # record.to_csv(os.path.join("stats","test_stats.csv"), mode='a', header=False)
    record.to_csv(os.path.join("..","stats","main_stats.csv"), mode='a', header=False)

    return game_time, player, play_cnt, game_plays, game_score, win

def pull_stats(user):
    last_week = (datetime.today()-timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    last_month = (datetime.today()-timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
    # records = pd.read_csv(os.path.join("stats","test_stats.csv"), header=0)
    records = pd.read_csv(os.path.join("..","stats","main_stats.csv"), header=0)
    records.reset_index(inplace=True)
    records = records[["date","time", "player","game_num","play_cnt", "play_num","game_plays","game_score","win"]]

    player_df = records.loc[records["player"] == user]
    last_week_stats = player_df[["date","time",'game_num','play_cnt','win']].loc[player_df["date"] > last_week].groupby(["date","time",'game_num']).mean()

    lw_wins = last_week_stats['win'].values.sum()
    lw_win_pct = round((lw_wins/last_week_stats['win'].count())*100,1)
    lw_plays = last_week_stats['play_cnt'].sum()
    lw_play_avg = round(lw_plays/last_week_stats['play_cnt'].count(),2)

    last_month_stats = player_df[["date","time",'game_num','play_cnt','win']].loc[player_df["date"] > last_month].groupby(["date","time",'game_num']).mean()

    lm_wins = last_month_stats['win'].values.sum()
    lm_win_pct = round((lm_wins/last_month_stats['win'].count())*100,1)
    lm_plays = last_month_stats['play_cnt'].sum()
    lm_play_avg = round(lm_plays/last_month_stats['play_cnt'].count(),2)

    return last_week_stats, lw_wins, lw_win_pct, lw_plays, lw_play_avg, last_month_stats, lm_wins, lm_win_pct, lm_plays, lm_play_avg