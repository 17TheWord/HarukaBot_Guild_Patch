from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.typing import T_State

from nonebot_plugin_guild_patch import GuildMessageEvent
from ...database import DB as db
from ...utils import get_type_id, permission_check, to_me, handle_uid, if_guild_admin

delete_sub = on_command("取关", aliases={"删除主播"}, rule=to_me(), priority=5)
delete_sub.__doc__ = """取关 UID"""

delete_sub.handle()(permission_check)

delete_sub.handle()(handle_uid)


@delete_sub.got("uid", prompt="请输入要取关的UID")
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if isinstance(event, GuildMessageEvent):
        if await if_guild_admin(bot, event):
            await del_uid(event=event, state=state)
        else:
            await delete_sub.finish("您无权限进行此操作")
    else:
        await del_uid(event=event, state=state)


async def del_uid(event, state):
    """根据 UID 删除 UP 主订阅"""
    uid = str(state["uid"])
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
