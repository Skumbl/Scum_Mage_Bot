from interactions import Extension, slash_command, SlashContext, OptionType, slash_option, SlashCommandChoice
import random
import re
import d20
from d20.stringifiers import SimpleStringifier, Dice, Die

class Fudge_Dice_Roll(Extension):
    @slash_command(name="fudge", description="returns a fudged result")
    @slash_option(
        name="expression", 
        description="The roll expression you want to evaluate. It can contain various dice rolls and modifiers.", 
        required=True, 
        type=OptionType.STRING
        )

    async def fudge_command(self, ctx: SlashContext):
        return await ctx.send(fudge_roll(expression, fudge))

def roll_fudge_dice():
    """Roll Fudge dice and return the result."""
    # Create a list representing the faces of a Fudge die
    fudge_die_faces = ["+", "+", "0", "0", "-", "-"]
    
    # Roll the Fudge die
    result = random.choice(fudge_die_faces)
    
    return result

def roll_fudge_dice_n_times(n):
    """Roll Fudge dice n times and return the results as a list."""
    results = [roll_fudge_dice() for _ in range(n)]
    return results

def calculate_fudge_score(results):
    """Calculate the Fudge score based on the results of rolling Fudge dice."""
    score = 0
    for result in results:
        if result == "+":
            score += 1
        elif result == "-":
            score -= 1
    return score