# HarukaBot_Guild_Patch

可以让 **HarukaBot** 适用于 **频道** 的方法。

> 提示： 本补丁没有经过充分测试, 不建议在生产环境使用, 如果发现任何问题请自行解决，  
> 或  
> 提交[Issues](https://github.com/17TheWord/HarukaBot_Guild_Patch/issues/new) （因个人能力有限不保证百分百解决）。

## HarukaBot——优雅的 B 站推送 QQ 机器人

- [文档](https://haruka-bot.sk415.icu)
- [Github](https://github.com/SK-415/HarukaBot)

## 食用方法

### 前置需求：

- [nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)：频道适配补丁。
- 目录结构参考：

```
📦 HarukaBot-master
├── 📂 plugins
│   ├── 📂 haruka_bot      # haruka_bot 的插件！不是 HarukaBot本身 
│   └── 📂 nonebot_plugin_guild_patch        # 频道适配插件
├── 📂 src                 # 或是 HarukaBot-master
├── 📜 .env                # 可选的
├── 📜 .env.dev            # 可选的
├── 📜 .env.prod           # 可选的
├── 📜 .gitignore
├── 📜 bot.py
├── 📜 docker-compose.yml
├── 📜 Dockerfile
├── 📜 pyproject.toml
└── 📜 README.md
```

### 若目录结构不同：

- 请在 `utils` 中的 `__init__.py` 中修改 第20行：


- `from plugins.nonebot_plugin_guild_patch import GuildMessageEvent`


- 中的 `plugins.nonebot_plugin_guild_patch` 部分，


- 替换为自己的频道适配补丁的位置。


- 在NoneBot中，`bot.py` 所在的目录为 `根目录`


- 可根据此 `根目录` 更改相对位置

---

### 环境设置（我猜的，所以我设置了）：

- 频道和群的 `@方式` 可能不相同，所以建议 `关闭`。


- 在你的环境配置文件中设置 （如：`.env.dev` 中），


- 新建一行，写入：`Haruka_TO_ME=False`。

---

### 安装：

- 假设 `haruka_bot` 目录为 `根目录`：

    - 替换 `database` 目录下的 `models.py`
    - 替换 `database` 目录下的 `db.py`

    - 替换 `utils` 目录下的 `__init__.py`

    - 替换 `plugins` 目录下的 `__init__.py`
    - 替换 `plugins` --> `sub` 目录下的 `add_sub.py` 和 `delete_sub.py`
    - 复制 `plugins` 目录下的 `guildadmin` 到你的 `plugins` 目录


- 设置频道超级用户，以下步骤 **二选一** ！！！
    1. 将 `GuildSuperUsers.py` 放到 `根目录 haruka_bot` 中：
        - 修改 `GuildSuperUserList = ["xxxxxx","xxxxxx"]`
        - 将 `xxxxxx` 替换为你要设置的超级用户的 `频道用户ID`
    2. 在 `根目录haruka_bot` 目录新建 `GuildSuperUsers.py`
        - 输入 `GuildSuperUserList = ["xxxxxx","xxxxxx"]`：
        - 将 `xxxxxx` 替换为你要设置的超级用户的 `频道用户ID`


- 设置频道管理员：
  - 在频道中使用命令 `添加 / 删除 用户频道ID` 即可进行管理员的增减操作
  - 管理员可以使用 `关注 / 取关` 功能
  - 只有超级用户才可以使用该命令
  - ~~通过 @ 对管理员进行增减操作~~ （咕咕咕）

---

### 已知问题 & 更新 2022 / 6 / 8：

- 新添加：频道超级用户列表，在频道命令中添加判定用户频道ID是否在列表中，以暂时解决权限问题。


- 新添加：
    - 指令添加频道管理员功能：
        - 频道超级用户可在频道中使用 `添加 / 删除 用户频道ID` 来设置频道Bot管理员。
        - 管理员只能使用机器人的 `关注 / 取关` 功能，没有其他权限。


- **仍旧建议**关闭@机器人命令，因为不清楚频道与群的@方式是否相同 `Haruka_TO_ME=False`


- 建议推送频道设为只读：
    - 虽然暂时解决了权限问题，但频道主/频道管理员，你也不想让你的推送子频道充斥各种聊天信息吧。
    - ~~由于频道用户ID不同于QQ号，猜测超级用户不会生效~~ 已通过设置频道超级用户暂时解决。

> 再次提示: 本补丁没有经过充分测试, 不建议在生产环境使用, 如果发现任何问题请自行解决，  
> 或  
> 提交[Issues](https://github.com/17TheWord/HarukaBot_Guild_Patch/issues/new) （因个人能力有限不保百分百证解决）。
---

## 特别感谢

- [SK-415/HarukaBot](https://github.com/SK-415/HarukaBot)： 感谢SK佬做出如此优雅的机器人。
- [@mnixry](https://github.com/mnixry)： 感谢混淆佬为HarukaBot项目提供的**技♂术指导**。
- [@wosiwq](https://github.com/wosiwq)： 感谢 W 桑撰写的「小小白白话文」。
- [nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)： 感谢混淆佬提供的频道适配补丁。
- [NoneBot2](https://github.com/nonebot/nonebot2)： HarukaBot 使用的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)： 稳定完善的 CQHTTP 实现。
- [bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)： 非常详细的 B 站 API 文档。
- [bilibili_api](https://github.com/Passkou/bilibili_api)： Python 实现的 B 站 API 库。

## 更新 & 问题记录：

### 已知问题2022 / 5 / 28：

- 新添加频道超级用户列表，在频道命令中添加判定 `频道用户 ID` 是否在列表中，以暂时解决权限问题
- **仍旧建议**关闭 `@ 机器人` 命令，因为不清楚频道与群的 `@ 方式` 是否相同 `Haruka_TO_ME=False`
- 建议推送频道设为只读：
    - 虽然暂时解决了权限问题，但 `频道主 / 频道管理员`，你也不想让你的推送子频道充斥各种聊天信息吧。
    - 由于 `频道用户 ID` 不同于 `QQ 号`，猜测超级用户不会生效

### 2022 / 5 / 26-2

- 建议 **关闭** `@ 机器人` 命令，因为不清楚频道与群的 `@ 方式` 是否相同 `Haruka_TO_ME=False`
- ~~建议~~ **强烈建议**推送频道设为只读：
    - 由于 `频道用户 ID` 不同于 `QQ 号`，**猜测** 超级用户不会生效
    - 经测试，频道内不存在权限系统，任何人都可以使用命令，在使用时请慎重检查频道人员成分

### 2022 / 5 / 26-1

- 因为不清楚频道与群的 `@ 方式` 是否相同，建议 **关闭** `@ 机器人` 命令 `Haruka_TO_ME=False`
- 因数据库中数据类型改动，需要删除数据库重新订阅！！！！！！
- 建议推送频道设为只读，频道内权限与群内权限不一定相同（应该是不同的，在频道内输入开启权限并没有什么反应）
