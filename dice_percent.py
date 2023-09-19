from interactions import Extension, slash_command, SlashContext, OptionType, slash_option
import random
import re
import d20

class Dice_Percent(Extension):
    # Percentile Command
    # ===================================================================================
    @slash_command(name="percentile", description="Rolls a 2 percentile die")
    @slash_option(
        name="mod",
        description="optional modifier",
        required=False,
        opt_type=OptionType.STRING
    )
    async def percentile_command(self, ctx: SlashContext, mod:  str='0'):
        calculated_mod = d20.roll(str(mod)).total
        roll_result_str = percentile_dice(calculated_mod)
        await ctx.send(roll_result_str)
    # ===================================================================================

# Percentile Dice Helper Function
# ===================================================================================
def percentile_dice(modifier):
    # Roll two 10-sided dice (2d10)
    tens_roll = random.randint(0, 9) * 10
    ones_roll = random.randint(0, 9)

    # Calculate the total result with the modifier
    result = tens_roll + ones_roll + modifier

    # Ensure the result is within the valid percentage range (0-100)
    result = max(0, min(result, 100))

    # Convert the result and rolls to a string and return it
    result_str = f":game_die: = **{result}**%\n2d10({tens_roll}, {ones_roll}) + {modifier}"
    return result_str
# ===================================================================================