from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

config = {
    'bot-token': os.getenv("DISCORD_BOT_TOKEN"),
    
    'database-uri': os.getenv("DATABASE_URL"),
    
    'redis-uri': os.getenv("REDIS_URL"),
    
    'titan-web-url': os.getenv("TITAN_WEB_URL"),
    
    'titan-web-app-secret': "app secret from the webapp lolz",
    
    'discord-bots-org-token': "DiscordBots.org Post Stats Token",
    
    'bots-discord-pw-token': "bots.discord.pw Post Stats Token",
    
    'logging-location': "./titanbot.log",
    
    "sentry-dsn": os.getenv("SENTRY_DSN"),
}
