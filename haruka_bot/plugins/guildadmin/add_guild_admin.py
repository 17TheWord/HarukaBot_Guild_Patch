from nonebot import on_command
from nonebot_plugin_guild_patch import GuildMessageEvent
from nonebot.adapters.onebot.v11 import Bot
from ...database import DB as db
from ...utils import to_me, get_guild_member_info, get_haruka_guild_super_user_list

add_guild_admin_sub = on_command("添加管理", aliases={"添加"}, rule=to_me(), priority=5)
add_guild_admin_sub.__doc__ = """添加管理 ID"""


@add_guild_admin_sub.handle()
async def _(bot: Bot, event: GuildMessageEvent):
    get_msg = str(event.raw_message)
    if str(event.user_id) in await get_haruka_guild_super_user_list(bot):
        if "[CQ:at,qq=" in get_msg:
            guild_user_id = get_msg[
                            get_msg.index(']') - 18: get_msg.index(']')]

            await add_guild_admin_uid(guild_admin_uid=guild_user_id,
                                      guild_admin_info=await get_guild_member_info(bot=bot, guild_id=event.guild_id,
                                                                                   user_id=guild_user_id))
        else:
            await add_guild_admin_sub.finish("请正确使用命令： 添加 @xxx")
    else:
        await add_guild_admin_sub.finish("您无权限进行此操作")


async def add_guild_admin_uid(guild_admin_uid: str, guild_admin_info):
    """根据 ID添加管理员"""
    guild_admin_list = await db.get_guild_admin_sub_list()

    # 初始化数据库中管理员ID列表
    guild_admin_uid_list = []

    # 数据库中的用户列表
    for guild_admin in guild_admin_list:
        guild_admin_uid_list.append(guild_admin.guild_admin_uid)

    if guild_admin_uid in guild_admin_uid_list:
        return await add_guild_admin_sub.finish(f"@{guild_admin_info['nickname']} 已经是管理了")

    result = await db.add_guild_admin_sub(guild_admin_uid=guild_admin_uid)
    if result:
        return await add_guild_admin_sub.finish(f"已添加管理 @{guild_admin_info['nickname']}")
    else:
        return await add_guild_admin_sub.finish("添加失败")
