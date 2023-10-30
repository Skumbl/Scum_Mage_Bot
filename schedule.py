import datetime
from interactions import Extension, slash_command, SlashContext, OptionType, slash_option

class Schedule (Extension):
    @slash_command(name="schedule", description="Schedule a time to play")
    @slash_option(
        name="weeks",
        description="How many weeks from now?",
        required=True,
        opt_type=OptionType.INTEGER
    )
    async def schedule_command(self, ctx: SlashContext, weeks: int):
        await ctx.send(f"Schedule 📅 \n {list_days(weeks)}")

def list_days(num_weeks):
    today = datetime.date.today()
    days = [today + datetime.timedelta(days=i) for i in range(num_weeks * 7)]

    for i, day in enumerate(days):
        day_str = day.strftime("%m/%d %A")
        if i == 0:
            day_str += " (Today)"
        print(f"[{i}] {day_str}")