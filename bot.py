from os import environ

from twitchio.ext import commands


class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=environ["irc_token"],
            client_id=environ["client_id"],
            api_token=environ["api_token"],
            nick=environ["nick"],
            prefix="!",
            initial_channels=["kenan7"],
        )

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f"Ready | {self.nick}")

    async def event_message(self, message):
        print(f"Received command: {message.content}")
        await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name="test")
    async def my_command(self, ctx):
        message = f"Hello {ctx.author.name}!"
        print(f"Sent message: {message}")
        await ctx.send(message)

    # @commands.event
    # async def event_command_error(ctx, err):
    #     if type(err) != commands.errors.BadArgument:
    #         pass
    #     else:
    #         print("Command was given a bad argument, ignoring errors")
