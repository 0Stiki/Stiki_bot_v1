from configs import CONFIGS


class Reply:
    # BOT RESPONSES that could be reused... or I just wanted them here for easy Find-in....
    INIT_TEXT = f'-- Initilizing A Stiki-Bot --' \
                f'\nMode: {CONFIGS.ENVIRON}' \
                f'\nMain Input/Output Channel ID: {CONFIGS.CHANNELS_["main"]} ' \
                f'\nMain Dev Channel ID: {CONFIGS.CHANNELS_["dev_1"]}'\
                f'\nBACKUP DEV Channel ID: {CONFIGS.CHANNELS_["dev_2"]}'\
                f'\nWELCOME CHANNEL ID: {CONFIGS.CHANNELS_["welcome"]}'\
                f'\nSystem Events Channel ID: {CONFIGS.CHANNELS_["sys"]}  ' \
                f'\nHave A Stiki Kinda Day!' \
                f'\n-- Init Complete! --'

    INIT_TXT_006 = 'Bot: {0}, Initialized And Listening For: {1}'

    WELCOME_TEXT = 'Hey, {0.mention}, You sure are in a Stiki Place Now.' \
                   '\nHave Fun, Hang Around A While, and Enjoy Life!'

    INVALID_COMMAND = 'Hey, {0.mention}, {1} Is An Invalid Command \nTry /s help If You Are Stuck.'

    LIST_O_JOKES = ["No Chump, You be funny, I'm A Bot Not A Comedian...",
                    "My wife told me to stop impersonating a flamingo. I had to put my foot down.",
                    "I went to buy some camo pants but couldn’t find any.",
                    "I failed math so many times at school, I can’t even count then all.",
                    "I was wondering why the frisbee kept getting bigger and bigger,"
                    " but then it hit me."
                    ]


REPLY = Reply()
