from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

config = {
    # Create an app over here https://discordapp.com/developers/applications/me
    # and fill these fields out
    'client-id': os.getenv("DISCORD_APP_ID"),
    'client-secret': os.getenv("DISCORD_APP_TOKEN"),
    'bot-token': os.getenv("DISCORD_BOT_TOKEN"),
    
    # Rest API in https://developer.paypal.com/developer/applications
    'paypal-client-id': "Paypal client id",
    'paypal-client-secret': "Paypal client secret",
    
    # V2 reCAPTCHA from https://www.google.com/recaptcha/admin
    'recaptcha-site-key': os.getenv("RECAPTCHA_SITE_KEY"),
    'recaptcha-secret-key': os.getenv("RECAPTCHA_SECRET_KEY"),
    
    # Patreon
    'patreon-client-id': "Patreon client id",
    'patreon-client-secret': "Patreon client secret",

    'app-location': "./",
    'app-secret': "Type something random here, go wild. lolz",

    'database-uri': os.getenv("DATABASE_URL"),
    'redis-uri': os.getenv("REDIS_URL"),
    'websockets-mode': "eventlet",
    'engineio-logging': False,
    
    # https://titanembeds.com/api/webhook/discordbotsorg/vote
    'discordbotsorg-webhook-secret': "Secret code used in the authorization header for DBL webhook",
    
    # Sentry.io is used to track and upload errors
    "sentry-dsn": os.getenv("SENTRY_DSN"),
    "sentry-js-dsn": os.getenv("SENTRY_DSN"),
}
