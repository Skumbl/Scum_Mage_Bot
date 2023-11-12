from interactions import Extension, slash_command, SlashContext, OptionType, slash_option
import os
from interactions.ext.paginators import Paginator
import interactions
import openai

AI_TOKEN = os.getenv("AI_TOKEN")
openai.api_key = AI_TOKEN

class Console_Log(Extension):
    @slash_command(name="rulebook", description="look up any D&D 5e rules")
    @slash_option(
        name="ask",
        description="D&D 5e rules question, must end in a question mark (?)",
        required=True,
        opt_type=OptionType.STRING
    )
    async def rule_command(self, ctx: SlashContext, ask: str):
        try:
            response = check_rules(ask)
        except:
            response = "the Dev ran out of money"

         # need to defer it, otherwise, it fails
        
        await ctx.defer()
        embeds = [
        interactions.Embed("Question:", ask),
        interactions.Embed("Answer:", response),
    ]
        #paginator = Paginator.create_from_string(self.bot, response, page_size=250)
        paginator = Paginator.create_from_embeds(self.bot, *embeds)
        await paginator.send(ctx)


def check_rules(question):
    # Define the prompt for your GPT-3 query
    prompt = f"In the context of Dungeons and Dragons's 5th edition: {question}"

    # Call the GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",  #"text-davinci-002" for more cost-effective options.
        prompt=prompt,
        max_tokens=400,  # Adjust the length as needed
        api_key=AI_TOKEN
    )

    # Extract and return the generated answer
    answer = response.choices[0].text.strip()
    return answer
