import datetime
from random import choice, choices
from interactions import Extension, listen, slash_command, SlashContext, OptionType, slash_option, SlashCommandChoice


class Availability (Extension):
    confirmations = {}  # Store user confirmations here
    users = []  # Array to store user information
    guilds = []  # Array to store guild information


    # Availability Command
    #===================================================================================
    '''
    availability command
    lists the next 7 days including today(day 0) and the next 6 days
    with the current time and date
    
    /availability [session time]
    '''
    @slash_command(name="availability", description="list the next 7 days including today(day 0) and the next 6 days with the current time and date", scopes=[1004738478149468191])
    @slash_option(
        name="session_time",
        description="what time is the session",
        required=True,
        opt_type=OptionType.STRING
    )
    async def availability_command(self, ctx: SlashContext, session_time: str):
        message = await ctx.send (f"```{list_week_string_maker(session_time)}```")
        last_avail_message = message.id

        # send reactions based off number of days
        emojies = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣","5️⃣", "6️⃣", "7️⃣", "❌"]

        for i in range(0, 9):
            await message.add_reaction(emojies[i])
    # ===================================================================================


    # Simple Availability Command
    # ===================================================================================
    @slash_command(name="av", description="list the next 7 days including today(day 0) and the next 6 days with the current time and date", scopes=[1004738478149468191])
    @slash_option(
        name="session_time",
        description="what time is the session",
        required=True,
        opt_type=OptionType.STRING
    )
    async def av_command(self, ctx: SlashContext, session_time: str):
        await self.availability_command(ctx, session_time)
    # ===================================================================================


# LIST WEEK STRING MAKER
# ===================================================================================
def list_week_string_maker(session_time): 
    '''
    list_week_string_maker
    takes in a session time and returns a string of the next 7 days
    including today(day 0) and the next 6 days
    with the corresponding date
    
    ex: 
    Session Time: 7:00 PM

    [0] Monday 1/4/2024 (Today)
    [1] Tuesday 1/5/2024
    [2] Wednesday 1/6/2024
    [3] Thursday 1/7/2024
    [4] Friday 1/8/2024
    [5] Saturday 1/9/2024
    [6] Sunday 1/10/2024
    [7] Monday 1/11/2024
    '''

    today = datetime.datetime.today()
    days = [today + datetime.timedelta(days=i) for i in range(8)]

    display_str = f"Session Time: {session_time}\n\n"
    display_str += f"[0] {days[0].strftime('%A %m/%d/%Y')} (Today)\n"

    for i in range(1, len(days)):
        display_str += f"[{i}] {days[i].strftime('%A %m/%d/%Y')}\n"
    return display_str
# ===================================================================================