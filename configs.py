from discord import Intents


class Configs:
    ENVIRON = 'DEV'  # or 'PRO'
    TOKEN = '*****************************'
    # commands 0 and 1, when joined = COMMAND_PREFIX > 2 chars to proceed every command
    COMMAND_0 = '/'
    COMMAND_1 = 's'
    # Comma Seperated List Of Owners
    BOT_OWNERS = [978406101756301342, 986858192778698773]
    # USERS With Custom Commands
    CUSTOM_USER_JEZZ = 245737063469547530
    # Dict Of Channels By ID... Only Add integers..
    CHANNELS_ = {'dev_1': 987076201728327740,
                 'dev_2': 987076268115755059,
                 'welcome': 987073676287549534,
                 'main': 987074653879152720,
                 'join_log': 987076414480191508,
                 'leave_log': 987115716123705424,
                 'bot_log': 987106227903414293,
                 'sys': 987076454573563934
                 }
    # List of all commands the bot will accept... use to verify input from user is usable
    ACTUAL_COMMAND_LIST = ['joke', 'info', 'help', 'money', 'jezz', 'skrew-styx', 'tf-is-stikibot', 'commands']

    @property
    def INTENTS(self):
        intent = Intents.default()
        intent.members = True
        return intent

    @property
    def COMMAND_PREFIX(self):
        return f'{self.COMMAND_0}{self.COMMAND_1}'


CONFIGS = Configs()
