from interactions import Extension, slash_command, SlashContext


class Help(Extension):
    # Help Command
    # ===================================================================================
    @slash_command(name="help", description="Show available commands and their descriptions")
    async def help_command(self, ctx: SlashContext):
        await ctx.send(help_message)
# ===================================================================================

help_message = """
**Available Commands:**

- `/roll`: Roll any dice expression
Usage: `/roll <expression>`
Example: `/roll 2d6+3`

- `/percentile`: Rolls a 2 percentile die
Usage: `/percentile [mod]`
Example: `/percentile 5`

- `/dice-engine`: Use the d20-dice engine, using standard syntax
Usage: `/dice-engine <expression>`
Example: `/dice-engine 2d20kh1 + 4d8`

- `/tools`: Links to 5e tools for rules and books
Usage: `/tools`
Example: `/tools`

- `/guess-number`: The Scum AI will read your mind
Usage: `/guess-number <number>`
Example: `/guess-number 42`

- `/join`: Auto rolls and joins the initiative order
Usage: `/join [mod]`
Example: `/join 5`

- `/display`: Display the current initiative order
Usage: `/display`
Example: `/display`
"""