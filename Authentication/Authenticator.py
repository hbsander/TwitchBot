from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope

from Credentials import APP_ID, APP_SECRET, TARGET_CHANNEL

# Credentials
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
CHANNEL = TARGET_CHANNEL

async def authenticate():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    return twitch