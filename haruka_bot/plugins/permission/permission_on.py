from nonebot import on_command
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER

from ...database import DB as db, DBGuild as db_guild
from ...utils import group_only, to_me
from nonebot_plugin_guild_patch import GuildMessageEvent, GUILD_SUPERUSER

permission_on = on_command(
    "开启权限",
    rule=to_me(),
    permission=GROUP_OWNER | GROUP_ADMIN | SUPERUSER | GUILD_SUPERUSER,
    priority=5,
)
permission_on.__doc__ = """开启权限"""

permission_on.handle()(group_only)


@permission_on.handle()
async def _(event: GroupMessageEvent | GuildMessageEvent):
    """开启当前群权限"""
    if event.message_type == "guild":
        if await db_guild.set_guild_permission(event.guild_id, event.channel_id, True):
            await permission_on.finish("已开启权限，只有管理员和主人可以操作")
    else:
        if await db.set_permission(event.group_id, True):
            await permission_on.finish("已开启权限，只有管理员和主人可以操作")
    await permission_on.finish("权限已经开启了，只有管理员和主人可以操作")
