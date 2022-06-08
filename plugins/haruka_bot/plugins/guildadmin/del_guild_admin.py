from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.internal.matcher import Matcher
from nonebot.internal.params import ArgPlainText
from nonebot.params import CommandArg
from plugins.nonebot_plugin_guild_patch import GuildMessageEvent

from ...GuildSuperUsers import GuildSuperUserList
from ...database import DB as db
from ...utils import to_me

del_guild_admin_sub = on_command("删除管理", aliases={"删除"}, rule=to_me(), priority=5)
del_guild_admin_sub.__doc__ = """删除管理 ID"""


@del_guild_admin_sub.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("uid", args)


@del_guild_admin_sub.got("uid", prompt="你想删除哪位频道管理呢？")
async def _(event: GuildMessageEvent, _uid=ArgPlainText("uid")):
    if str(event.user_id) in list(GuildSuperUserList):
        await del_guild_admin_uid(guild_admin_uid=_uid)
    else:
        await del_guild_admin_sub.finish("您无权限进行此操作")


async def del_guild_admin_uid(guild_admin_uid):
    """根据 ID添加管理员"""
    guild_admin_list = await db.get_guild_admin_sub_list()

    if guild_admin_uid in guild_admin_list:
        return del_guild_admin_sub.finish(f"（{guild_admin_uid}）已经是管理了")

    result = await db.del_guild_admin_sub(guild_admin_uid=guild_admin_uid)
    if result:
        return await del_guild_admin_sub.finish(f"已删除管理（{guild_admin_uid}）")
    else:
        return await del_guild_admin_sub.finish("删除失败")
