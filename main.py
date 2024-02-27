from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option
from interactions.api.events import MessageCreate
from d20 import roll
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if BOT_TOKEN is None:
    print("Error: BOT_TOKEN environment variable is not set.")
    exit(1)

# intents are what events we want to receive from discord, `DEFAULT` is usually fine
bot = Client(intents=Intents.DEFAULT)


# Load All Extension Functions into main
# ===================================================================================
bot.load_extension("console") # logs if a message is received (DOES NOT LOG DATA)
bot.load_extension("dice_roll") # the base dice roller in scum mage format
bot.load_extension("dice_percent") # percentile dice using scum mage format
bot.load_extension("directional_dice") # directional dice
bot.load_extension("help") # lists out all / commands and their syntax
bot.load_extension("tools")  # links 5eTools
bot.load_extension("initiative") # handles all init commands
bot.load_extension("fudge_dice") # fudge dice
bot.load_extension("availability") # checks player availability
#bot.load_extension("rulebook") NO LONGER BEING IMPLEMENTED
# ===================================================================================


# This is stupid, and I don't know why I did it, but I did, and it's here
# Guess the Number
# ===================================================================================
@slash_command(name="guess-number", description="The Scum AI will read your mind")
@slash_option(
    name="number",
    description="what number are you thinking of, and I'll guess",
    required=True,
    opt_type=OptionType.INTEGER
)
async def guess_command(ctx: SlashContext, number: int):
    await ctx.send(f"thinking ....\nis it .....\n{number}")
# ===================================================================================


bot.start(BOT_TOKEN)