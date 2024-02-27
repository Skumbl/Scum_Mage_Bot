from interactions import Extension, slash_command, SlashContext, OptionType, slash_option, SlashCommandChoice
import random

class Fudge_Dice_Roll(Extension):


    # Fudge Command
    # ===================================================================================
    @slash_command(name="fudge", description="returns a fudged result")
    async def fudge_command(self, ctx: SlashContext):
        fudge_result = roll_fudge_die()
        d20_range = fudge_to_d20_range(fudge_result)
        return await ctx.send(f"🍫 🎲  = {d20_range}")


    # Fudge Simplified Command
    # ===================================================================================
    @slash_command(name="f", description="returns a fudged result", scopes=[1004738478149468191])
    async def f_command(self, ctx: SlashContext):
        await self.fudge_command(ctx)
    # ===================================================================================


# FUDGE DICE ROLL
# ===================================================================================
def roll_fudge_die():
    """Roll a single Fudge die and return the result (+, 0, -)."""
    fudge_die_faces = ["+", "0", "-"]
    return random.choice(fudge_die_faces)
# ===================================================================================


# FUDGE TO D20 RANGE
# ===================================================================================
def fudge_to_d20_range(fudge_result):
    """Map Fudge die results to d20-style ranges with a bell curve centered around the middle."""
    if fudge_result == "+":
        return random.randint(12, 18)  # Skewed towards the middle and good outcomes
    elif fudge_result == "0":
        return random.randint(11, 19)  # Skewed towards the middle and neutral outcomes
    elif fudge_result == "-":
        return random.randint(10, 16)  # Skewed towards the middle and bad outcomes
# ===================================================================================