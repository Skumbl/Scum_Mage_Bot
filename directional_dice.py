import d20
import random
from interactions import Extension, slash_command, SlashContext, OptionType, slash_option

class Directional (Extension):


    # Directional Command
    # ===================================================================================
    @slash_command(name="directional", description="Roll a directional dice")
    async def directional_command(self, ctx: SlashContext):
        result = roll_directional_die(directional_faces)
        arrow = interpret_directional_result(result, arrow_symbols)
        await ctx.send(f"Directional 🎲 = {arrow} ({result})")
    # ===================================================================================
        
    # Directional Simplified Command
    # ===================================================================================
    @slash_command(name="dir", description="Roll a directional dice")
    async def dir_command(self, ctx: SlashContext):
        await self.directional_command(ctx)
    # ===================================================================================
        

# DIRECTIONAL DICE ROLL
# ===================================================================================
def roll_directional_die(faces):
    """Roll a directional die with the specified faces."""
    return random.choice(faces)
# ===================================================================================


# INTERPRET DIRECTIONAL RESULT
# ===================================================================================
def interpret_directional_result(result, arrow_symbols):
    """Interpret the result of a directional die roll and return the corresponding arrow symbol."""
    return arrow_symbols.get(result, "Unknown Direction")

# Define the directional faces and corresponding arrow symbols
directional_faces = ["North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest"]
arrow_symbols = {
    "North": "↑",
    "Northeast": "↗",
    "East": "→",
    "Southeast": "↘",
    "South": "↓",
    "Southwest": "↙",
    "West": "←",
    "Northwest": "↖"
}
# ===================================================================================