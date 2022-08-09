from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.typing import T_State

from nonebot_plugin_guild_patch import GuildMessageEvent
from ...GuildSuperUsers import GuildSuperUserList
from ...database import DB as db
from ...utils import get_type_id, permission_check, to_me, handle_uid

delete_sub = on_command("取关", aliases={"删除主播"}, rule=to_me(), priority=5)
delete_sub.__doc__ = """取关 UID"""

delete_sub.handle()(permission_check)

delete_sub.handle()(handle_uid)


@delete_sub.got("uid", prompt="请输入要取关的UID")
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if isinstance(event, GuildMessageEvent):
        subs = await db.get_guild_admin_sub_list()

        # 初始化数据库中管理员ID列表
        guild_admin_uid_list = []

        # 数据库中的用户列表
        for guild_admin in subs:
            guild_admin_uid_list.append(guild_admin.guild_admin_uid)

        # 获取用户信息
        guild_user_info = await bot.call_api("get_guild_member_profile", guild_id=event.guild_id, user_id=event.user_id)

        # 判断是否为超管
        if str(event.user_id) in list(GuildSuperUserList):
            await del_uid(event=event, state=state)

        # 判断是否在数据库表中
        elif str(event.user_id) in guild_admin_uid_list:
            await del_uid(event=event, state=state)

        # 判断是否为管理员身份组
        elif await if_admin_group(bot, event):
            await del_uid(event=event, state=state)

        else:
            await delete_sub.finish("您无权限进行此操作")
    else:
        await del_uid(event=event, state=state)


async def if_admin_group(bot, event: GuildMessageEvent):
    guild_member_info = await bot.call_api("get_guild_member_profile", guild_id=event.guild_id, user_id=event.user_id)
    for per_role in guild_member_info['roles']:
        if per_role['role_name'] in bot.config.haruka_guild_admin_groups:
            return True
    return False


async def del_uid(event, state):
    """根据 UID 删除 UP 主订阅"""
    uid = state["uid"]
    name = getattr(await db.get_user(uid=uid), "name", None)
    if name:
        result = await db.delete_sub(
            uid=uid, type=event.message_type, type_id=get_type_id(event)
        )
    else:
        result = False

    if result:
        await delete_sub.finish(f"已取关 {name}（{uid}）")
    await delete_sub.finish(f"UID（{uid}）未关注")
