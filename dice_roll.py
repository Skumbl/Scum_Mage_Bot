from interactions import Extension, slash_command, SlashContext, OptionType, slash_option
import random
import re
import d20
from d20.stringifiers import SimpleStringifier, Dice, Die

class Dice_Roll(Extension):


    # Roll Command
    # ===================================================================================
    @slash_command(name="roll", description="Roll any dice expression")
    @slash_option(
        name="expression",
        description="input a roll expression, ex: 4d6+2",
        required=True,
        opt_type=OptionType.STRING
    )
    async def roll_command(self, ctx: SlashContext, expression: str):
        expression.replace(" ", "")
        expressions = expression.split(", ")
        for express in expressions:
            try:
                roll_result_str = reformat_dice_roll(express)
                await ctx.send(":game_die:" + f" = {roll_result_str}")
            except Exception as e:
                await ctx.send(f"invalid input: \"{e}\"\n*mods crush his skull in* 💀")
    # ===================================================================================


    # Roll Simplified Command
    # ===================================================================================
    @slash_command(name="r", description="Roll any dice expression")
    @slash_option(
        name="expression",
        description="input a roll expression, ex: 4d6+2",
        required=True,
        opt_type=OptionType.STRING
    )
    async def r_command(self, ctx: SlashContext, expression: str):
        await self.roll_command(ctx, expression)
    # ===================================================================================


# ROLL FORMATTER
# ===================================================================================
class CustomStringifier(d20.SimpleStringifier):
    def _stringify(self, node):
        if not node.kept:
            return f"~~{node.number}~~"
        return super()._stringify(node)
    
    def _str_expression(self, node):
        return f"**{int(node.total)}**\n{self._stringify(node.roll)}"

def reformat_dice_roll(input_roll):
    return str(d20.roll(input_roll, stringifier=CustomStringifier()))
# ===================================================================================
