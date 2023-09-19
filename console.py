from interactions import listen
from interactions import Extension
from interactions import slash_command, SlashContext
import random


class Console_Log(Extension):
    @listen()
    async def on_ready(self):
        print("Ready")
        print(f"This bot is written by {self.bot.owner}")

    # print when an event happens
    @listen()
    async def on_message_create(self, event):
        if '<@1149502978835877919>' in event.message.content:
            await event.message.reply(random.choice(Scum_Replies))

    @slash_command(name="clear", description="remove the last 50 messages from this channel")
    async def clear_command(self, ctx: SlashContext):
        delete = await ctx.channel.purge(deletion_limit=50)
        await ctx.send("Facera Invisibilis")

Scum_Replies = [
"By foul muck and vile incantations, dost thou vex me! `/help`, I beseech thee!",
"Ah, the irritation brews like a fetid potion. 'Tis but `/help` that can quell my ire.",
"Impudent mortal, thy queries drown me in vexation. `/help`, at once!",
"Mine patience wears thin as a swamp in midsummer. Use the command: `/help!`",
"Verily, thy ignorance stirs the murkiest depths of my wrath. Seek wisdom in `/help`.",
"Art thou deaf to my pleas? Invoke `/help` and spare me this torment.",
"A plague upon thine ignorance! Utilize `/help`, or incur my eternal ire.",
"'Tis as though thee wades through the foulest of cesspools. `/help`, or suffer my disdain!",
"My tolerance wanes like a fading moon, and only `/help` can rekindle my goodwill.",
"Prithee, dost thou enjoy toying with my patience? Command `/help` forthwith!",
"Thy incessant queries do grate upon my very soul. `/help`, ere I unleash my wrath!",
"Behold, the Scum Mage's displeasure bubbles forth! Speak the words: `/help`!",
"In my realm of mire and filth, thy ignorance reeks most foul. `/help`, or be damned!",
"Thine ignorance rivals the stagnant waters of a marsh. Utilize `/help` to cleanse thyself!",
"Oh, lamentable fool! Find solace in the command: `/help`, and vex me no more.",
"My forbearance wears thin as the muck in a dry season. Call forth `/help` swiftly!",
"'Tis a vexing mystery why thou dost persist. Seek the answers in `/help`, I implore!",
"A pestilent nuisance thou art! `/help`, or endure my relentless chiding.",
"I am a conjurer of filth and vexation, and thou dost test my limits. `/help`, I command!",
"By the wretched depths from which I arose, heed my plea: `/help`, or incur my eternal scorn!"
]