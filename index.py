import random
import discord
import time
from datetime import datetime
from configs import CONFIGS as SETTINGS
from replys import REPLY as REPLIES
# Commands are entered as COMMAND_PREFIX 'space' ACTUAL_COMMAND
# EXAMPLE cmd = /s joke


class StikiBotV2(discord.Client):
    DEV_CH_1, DEV_CH_2, PRO_CH, WEL_CH, SYS_CH = None, None, None, None, None
    JOIN_LOG, LEAVE_LOG, BOT_LOG, BOT_USER = None, None, None, None
    CH_LIST, INIT_TIME = list(), None

    @property
    def CHANNELS(self):
        return SETTINGS.CHANNELS_

    # Bot Is Initialized And Awaiting Commands
    async def on_ready(self):
        # Set init Time
        self.INIT_TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Get Channels By ID's > Stored In Configs - Save them as class Vars To Use Elsewhere
        self.DEV_CH_1 = self.get_channel(self.CHANNELS['dev_1'])
        self.DEV_CH_2 = self.get_channel(self.CHANNELS['dev_2'])
        self.PRO_CH = self.get_channel(self.CHANNELS['main'])
        self.WEL_CH = self.get_channel(self.CHANNELS['welcome'])
        self.SYS_CH = self.get_channel(self.CHANNELS['sys'])
        self.JOIN_LOG = self.get_channel(self.CHANNELS['join_log'])
        self.LEAVE_LOG = self.get_channel(self.CHANNELS['leave_log'])
        self.BOT_LOG = self.get_channel(self.CHANNELS['bot_log'])
        # Misc Typing And Debug prints
        # print(f' TYPE: {type(self.DEV_CH_1)}')
        # Build A List OF The Actual Channels For To Loop Through
        self.CH_LIST = [self.DEV_CH_1, self.DEV_CH_2, self.PRO_CH, self.WEL_CH, self.SYS_CH,
                        self.LEAVE_LOG, self.BOT_LOG]
        # Drop The Short msg in all channels that can receive commands EXCEPT BOT LOG
        short_init_msg = REPLIES.INIT_TXT_006.format(self.user, SETTINGS.COMMAND_PREFIX)
        for i in self.CH_LIST:
            if i != self.BOT_LOG:
                await i.send(short_init_msg)
        # Send Long Init To Bot Log
        await self.BOT_LOG.send(REPLIES.INIT_TEXT)
        # Log it Serverside
        print(REPLIES.INIT_TEXT)

    # New Members - Say Hi, Assign Role, Steal Info.. Etc >  Outbound messages to # System
    async def on_member_join(self, member):
        # Sleep for 3 sec to give them time to get in the server good
        time.sleep(3)
        # set Time Stamp
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Get Welcome Message(.format(member))
        welcome_msg = REPLIES.WELCOME_TEXT.format(member)
        # First Log it to Join Log Channel
        await self.JOIN_LOG.send(f'NewUser -- {member} Signup @{now}')
        # Then Say Hi in the WELCOME channel!!
        await self.WEL_CH.send(welcome_msg)
        # Log It Serverside Also
        print(welcome_msg)

    async def on_member_remove(self, member):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        await self.LEAVE_LOG.send(f'{member} > has left: {now}')

    # Command Logic - :) Can be Re-factored more - #FknStiki
    async def on_message(self, message):
        print(f'Got MSG:{message.content}')  # For Debugging
        user_cmd = message.content.lower()  # command coming fom the user == Str
        # This is where the user input is checked for the prefix > 1st 2 characters = /s
        user_cmd_prefix = f'{user_cmd[0]}{user_cmd[1]}'

        if (len(f'{message.content}') <= 2) or (user_cmd_prefix != SETTINGS.COMMAND_PREFIX):
            return

        # this represents first set of characters after /s and then a SPACE
        if not len(user_cmd) >= 3:
            await self.BOT_LOG.send(f'ERR IN CMD FLOW > CMD: {user_cmd}')
        user_actual_command = user_cmd.split(' ')[1]

        # --- HANDLE COMMON NON-COMMAND RELATED MESSAGES --- #

        # See if the message is from the bot, the wrong channel, or not a command > True = skip processing
        if message.author == self.user:
            # Message by bot - Do Not Process - Print is for Debugging and can be commented out
            print('Skipping MSG: The Bot Sent This MSG.')
            return

        if message.channel.id not in self.CHANNELS.values():
            # Message not from correct dev/prod channel -  Same As Above - Comment out Print if not debugging
            print(f'Skipping Command: {user_cmd} > Did Not Originate From A Command Channel.')
            return

        if user_cmd_prefix != SETTINGS.COMMAND_PREFIX:
            # Message Not A Command -  Same Again -  Comment Out Print
            print('Message Not A Command')
            return

        if user_actual_command not in SETTINGS.ACTUAL_COMMAND_LIST:
            # Invalid Command After /s - Send Help
            print('Message Is An Invalid Command')
            await message.channel.send(REPLIES.INVALID_COMMAND.format(message.author, user_actual_command))

        # Run through a List o jokes and say one....Maybe
        outbound_msg = REPLIES.LIST_O_JOKES[random.randint(0, len(REPLIES.LIST_O_JOKES) - 1)] \
            if user_actual_command == 'joke' else REPLIES.INVALID_COMMAND.format(message.author, user_actual_command)

        # Owner Only Commands
        if message.author.id in SETTINGS.BOT_OWNERS:
            if user_actual_command == "tf-is-stikibot":
                outbound_msg = 'You Are The Real Stiki, Tf you asking me for?'
            if user_actual_command == 'skrew-styx':
                outbound_msg = 'Yea, That Guy Pisses Me Off Too... '

        if message.author.id == SETTINGS.CUSTOM_USER_JEZZ:
            if user_actual_command == 'jezz':
                outbound_msg = 'You Are The Real Jezz, So Sayith The Stiki?'
            if user_actual_command == 'money':
                outbound_msg = 'Chuhhh Chingggg... AmiRite?'

        # ---Etc commands --- #
        if user_actual_command == 'help':
            outbound_msg = f'Hi, {self.user}, Here To Save The Day.' \
                  f'\nFor A list Of Commands Type: /s commands' \
                  f'\nTo Learn more about Stiki Bots Type: /s info' \
                  f'\nMore To Come!!'

        if user_actual_command == 'commands':
            outbound_msg = f'Ok, {self.user}, ' \
                           f'\nThe Commands(For Now) are /s followed by a space and then' \
                           f' followed by one of the following keywords.'
            for c in SETTINGS.ACTUAL_COMMAND_LIST:
                outbound_msg = f'{outbound_msg} \n{c}, '

        if user_actual_command == 'info':
            outbound_msg = f'Ok... {str(message.author).split("#")[0]}, ' \
                           f' wants to know more about Stiki Bots!' \
                           f'\nTo Learn more about Stiki Bots You should ask Stiki..' \
                           f'\nMe Just Dum Bot.... Member?'

        print(outbound_msg)
        await message.channel.send(outbound_msg)


Stiki = StikiBotV2(intents=SETTINGS.INTENTS)
Stiki.run(SETTINGS.TOKEN)
