from interactions import Extension, slash_command, SlashContext

class Tools(Extension):


    # Link 5e tools
    # ===================================================================================
    @slash_command(name="tools", description="links 5e tools for rules and books")
    async def rules_command(self, ctx: SlashContext):
        await ctx.send("__5eTools:__ \nhttps://5e.tools/")
    # ===================================================================================
        
    # Tools Simplified Command
    # ===================================================================================
    @slash_command(name="t", description="links 5e tools for rules and books")
    async def t_command(self, ctx: SlashContext):
        await self.rules_command(ctx)
    # ===================================================================================