# from lib2to3.pgen2 import token
import config
import discord
import responses
import emoji
from wordle_stats import mine_scores

async def send_message(message, user_message, author, is_private):
    try: 
        response = responses.handle_response(user_message, author)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = config.botToken
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Bot should only listen to/process messages from the wordle channel
        if message.channel.name != 'wordle':
            return
 
        # Get data about the user
        username = str(message.author)
        user_nick = str(message.author.nick)
        user_message = str(message.content)
        channel = str(message.channel)
        # message_id = message.id

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
        # print(message)

        if user_message[0:6] =='Wordle':
            game_time, player, play_cnt, game_plays, game_score, win = mine_scores(username, user_message)
            
            if game_score == 0:
                score_emoji = "❌"
            elif game_score == 1:
                score_emoji = "🐐"
            elif game_score == 2:
                score_emoji = "2️⃣"
            elif game_score == 3:
                score_emoji = "3️⃣"
            elif game_score == 4:
                score_emoji = "4️⃣"
            elif game_score == 5:
                score_emoji = "5️⃣"
            else: score_emoji = "6️⃣"
            await message.add_reaction(score_emoji)

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, username, is_private=True)
        else:
            await send_message(message, user_message, username, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)