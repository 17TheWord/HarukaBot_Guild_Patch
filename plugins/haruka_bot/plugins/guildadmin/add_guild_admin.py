from nonebot import on_command
from plugins.nonebot_plugin_guild_patch import GuildMessageEvent

from ...GuildSuperUsers import GuildSuperUserList
from ...database import DB as db
from ...utils import to_me

add_guild_admin_sub = on_command("添加管理", aliases={"添加"}, rule=to_me(), priority=5)
add_guild_admin_sub.__doc__ = """添加管理 ID"""


@add_guild_admin_sub.handle()
async def _(event: GuildMessageEvent):
    if str(event.user_id) in list(GuildSuperUserList):
        if "at" in str(event.raw_message):
            guild_user_id = str(event.raw_message)[str(event.raw_message).index(']') - 18: str(event.raw_message).index(']')]
            await add_guild_admin_uid(guild_admin_uid=guild_user_id)
        else:
            await add_guild_admin_sub.finish("请正确使用命令： 添加 @xxx")

    else:
        await add_guild_admin_sub.finish("您无权限进行此操作")


async def add_guild_admin_uid(guild_admin_uid):
    """根据 ID添加管理员"""
    guild_admin_list = await db.get_guild_admin_sub_list()

    if guild_admin_uid in guild_admin_list:
        return add_guild_admin_sub.finish(f"（{guild_admin_uid}）已经是管理了")

    result = await db.add_guild_admin_sub(guild_admin_uid=guild_admin_uid)
    if result:
        return await add_guild_admin_sub.finish(f"已添加管理（{guild_admin_uid}）")
    else:
        return await add_guild_admin_sub.finish("添加失败")
