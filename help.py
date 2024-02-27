from interactions import Extension, slash_command, SlashContext
from interactions.ext.paginators import Paginator
import interactions

class Help(Extension):
    # Help Command
    # ===================================================================================
    @slash_command(name="help", description="Show available commands and their descriptions")
    async def help_command(self, ctx: SlashContext):
        embeds = [
        interactions.Embed("__About__", about),
        interactions.Embed("__Roll Command:__", roll),
        interactions.Embed("__Percentile Dice Command:__", percent),
        interactions.Embed("__Join Initiative Command:__", join),
        interactions.Embed("__NPC Join Initiative Command:__", npc_join),
        interactions.Embed("__Custom Value Join Initiative Command:__", custom_join),
        interactions.Embed("__Display Initiative Command:__", display),
        interactions.Embed("__Clear Chat Command:__", clear),
        #interactions.Embed("__Rulebook Check Command:__", rules),
        interactions.Embed("__5e Tools Command:__", tools),
    ]
        paginator = Paginator.create_from_embeds(self.bot, *embeds)
        await paginator.send(ctx)
# ===================================================================================

roll = """

The `roll` command allows you to roll any dice expression. You can input a roll expression, such as `4d6+2`, and the bot will roll the dice and provide the result.

### Accepted Syntax
To use the `roll` command, use the following syntax:

/roll [expression]
/roll [expression, expression]

- `expression`: The roll expression you want to evaluate. It can contain various dice rolls and modifiers.

**Note: ** expressions are written in standard dice notation supporting advanced features like exploding dice, keeping higher or lower values, and nested expressions

### Examples
/roll [1d20]
- rolls a d20

/roll [1d20 + 2]
- rolls a d20 adds 2

/roll [2d6 - 2]
- rolls a d20 subtracts 2

/roll [2d20kh1]
- rolls 2d20 and returns the higher dice

/roll [2d6+3, 3d8, 1d20-2]
- rolls all 3 dice expressions separably from each other 

### Usage
You can use this command to simulate dice rolls for various tabletop role-playing games and other scenarios where random numbers are needed.

### Result Format
The command will provide the result in the following format:

:game_die: = [result]
[expression] = [roll_result]

- `[result]`: The final result of the dice roll.
- `[expression]`: The roll expression you provided.
- `[roll_result]`: The individual rolls and modifiers applied to calculate the result.

### Example Result
:game_die: = 15
2d6+3 = 4+6+3+2 = 15

This indicates a roll of 15 for the expression `2d6+3`.

**Note:** If you provide an invalid roll expression, the bot will respond with an error message.

**Example Error Response:**

invalid input: "Invalid expression"
"""

percent = """

The `percentile` command allows you to roll a 2 percentile die. This command simulates rolling two 10-sided dice (2d10) and adding an optional modifier to the result.

### Accepted Syntax
To use the `percentile` command, use the following syntax

/percentile [modifier]

- `[modifier]` (Optional): You can provide an optional modifier that will be added to the roll result. If not provided, the default modifier is `0`.

**Note:** the modifier also allows for the adding of additional rolls to the modifier

### Example
/percentile [10]
-rolls 2 percentile die with a modifier of +10.

/percentile [1d4+2]
-rolls 2 percentile die with a modifier of +1d4 and +2

### Usage
You can use this command to generate random percentage values for various purposes. The result will be within the valid percentage range of 0% to 100%.

### Result Format
The command will provide the result in the following format:

:game_die: = [result]%
2d10([tens_roll], [ones_roll]) + [modifier]

- `[result]`: The final percentage result.
- `[tens_roll]` and `[ones_roll]`: The individual rolls of the 2d10.
- `[modifier]`: The modifier added to the roll.

### Example Result
:game_die: = 75%
2d10(40, 5) + 30

This indicates a roll of 75% (40 + 5 + 30).

**Note:** If you provide an invalid modifier, the bot will handle it gracefully and provide the result accordingly.
"""

join = """

The `/join` command allows a user to automatically roll for initiative and join the initiative order. Users can optionally provide an initiative modifier.

### Accepted Syntax
/join [modifier]

- `[modifier]` (Optional): Initiative modifier, for example, '1' or '1d4 + 1'.

### Example

/join [2]

This command will roll for initiative and add the user to the initiative order with a modifier of +2.
"""

npc_join = """

The `/npc-join` command adds a non-player character (NPC) to the initiative order. You can specify the NPC's name and an optional initiative modifier.

### Accepted Syntax
/npc-join name [modifier]

- `name`: The name of the NPC.
- `[modifier]` (Optional): Initiative modifier, for example, '1' or '1d4 + 1'.

### Example
/npc-join [Goblin] [1]

This command will add an NPC named "Goblin" to the initiative order with an initiative modifier of +1.
"""

custom_join = """

The `/custom-join` command allows users to join the initiative with a custom initiative score and modifier.

### Accepted Syntax
/custom-join roll [modifier]

- `roll`: The initiative score from the straight roll.
- `[modifier]` (Optional): Initiative modifier.

**Note:** the modifier like other commands can also be a dice roll as well

### Example
/custom-join [15] [3]

This command will add the user to the initiative order with an initiative score of 15 and a modifier of +3.
"""
display = """

The `/display` command is used to display and interact with the current initiative order during tabletop role-playing games. It provides a visual representation of the initiative order and offers buttons for cycling through participants and clearing the initiative order.

### Accepted Syntax

/display

This command is used without any additional arguments.

### Functionality
When you use the `/display` command, it will display the current initiative order along with two buttons: "NEXT" and "CLEAR."

### NEXT Button
The "NEXT" button, when clicked, allows you to cycle through the initiative order to determine the next participant's turn.

**Functionality:**
- If there are participants remaining in the initiative order, clicking "NEXT" will display the next participant's name and indicate who is currently on deck.
- If there are no more participants in the initiative order, it will indicate that the initiative order is empty.

### CLEAR Button
The "CLEAR" button, when clicked, clears the entire initiative order, removing all participants from the list.

**Functionality**
- Clicking the "CLEAR" button will remove all participants from the initiative order, effectively resetting it.
"""

clear = """
### **WARNING!**
**THIS COMMAND WILL DELETE THE LAST 50 MESSAGES IN CHAT, BE SURE YOU WANT TO USE IT**

The `/clear` command is used to remove the last 50 messages from the current channel. This command can be helpful to clean up a channel by deleting messages that are no longer needed.

### Accepted Syntax
/clear

This command is used without any additional arguments.

### Functionality
When you use the `/clear` command, it will automatically delete the last 50 messages
"""

tools = """

The `/tools` command provides a convenient link to the 5eTools website, which is a valuable resource for accessing rules and books related to Dungeons & Dragons 5th edition (D&D 5e).

### Accepted Syntax
/tools

This command is used without any additional arguments.

### Functionality
The `/tools` command is a quick way to access the 5eTools website, where you can find a comprehensive collection of D&D 5e rules, information, and reference materials.

**Note:** The 5eTools website is a valuable online resource for D&D players and Dungeon Masters
"""

about = """
The **Scum Mage** emerges from the depths, summoned to be your mystical guide in the realm of Discord. This arcane bot is here to assist with all things Dungeons & Dragons, offering commands like /roll for dice rolling, /join for managing initiative, and /rulebook for answering your D&D questions. It even provides a direct link to the 5eTools website via /tools and helps you clean up the chat with /clear. Created by the enigmatic @scumble, Scum Mage is your trusty companion for D&D adventures in Discord.

*Version 1.00*
"""