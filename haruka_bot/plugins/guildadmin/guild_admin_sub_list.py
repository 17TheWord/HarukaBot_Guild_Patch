from nonebot import on_command
from nonebot_plugin_guild_patch import GuildMessageEvent
from nonebot.adapters.onebot.v11 import Bot
from ...database import DB as db
from ...utils import permission_check, to_me, get_guild_member_info, get_haruka_guild_super_user_list

guild_admin_sub_list = on_command("频道管理列表", aliases={"管理列表"}, rule=to_me(), priority=5)
guild_admin_sub_list.__doc__ = """频道管理列表"""

guild_admin_sub_list.handle()(permission_check)


@guild_admin_sub_list.handle()
async def _(bot: Bot, event: GuildMessageEvent):
    """发送当前Bot的频道管理列表"""
    if str(event.user_id) in await get_haruka_guild_super_user_list(bot):
        message = "（所有频道共用管理列表）\n管理员：\n\n"
        subs = await db.get_guild_admin_sub_list()

        # 数据库内频道管理
        for guild_admin in subs:
            guild_admin_info = await get_guild_member_info(bot=bot, guild_id=event.guild_id,
                                                           user_id=guild_admin.guild_admin_uid)
            message += f"\t@{guild_admin_info['nickname']} \n"
        message += "\n身份组：\n\n"
        for guild_admin_group in list(bot.config.haruka_guild_admin_group_list):
            message += "\t" + guild_admin_group

        await guild_admin_sub_list.finish(message)
    else:
        await guild_admin_sub_list.finish("您无权限进行此操作")
