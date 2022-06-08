from nonebot import on_command

from ...database import DB as db
from ...utils import permission_check, to_me

guild_admin_sub_list = on_command("频道管理列表", aliases={"管理列表"}, rule=to_me(), priority=5)
guild_admin_sub_list.__doc__ = """频道管理列表"""

guild_admin_sub_list.handle()(permission_check)


@guild_admin_sub_list.handle()
async def _():
    """发送当前Bot的频道管理列表"""
    message = "频道管理列表（所有频道共用管理列表）\n\n"
    subs = await db.get_guild_admin_sub_list()
    for guild_admin in subs:
        message += guild_admin.guild_admin_uid + "\n"
    await guild_admin_sub_list.finish(message)
