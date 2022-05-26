# HarukaBot_Guild_Patch
可以让 **HarukaBot** 适用于 **频道** 的方法。

## HarukaBot——优雅的 B 站推送 QQ 机器人
- [文档](https://haruka-bot.sk415.icu)
- [Github](https://github.com/SK-415/HarukaBot)

## 食用方法
前置需求：  
  - [nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)：频道适配补丁
  - 目录结构参考：
```
📦 HarukaBot-master
├── 📂 plugins
│   ├── 📂 haruka_bot      # haruka_bot 插件！不是 HarukaBot本身 
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
若目录结构不同：
- 请在 `utils` 中的 `__init__.py` 中修改 第20行：  
- `from plugins.nonebot_plugin_guild_patch import GuildMessageEvent`  
- 中的 `plugins.nonebot_plugin_guild_patch` 部分  
- 替换为自己的频道适配补丁的位置  
- 在NoneBot中，`bot.py` 所在的目录为 `根目录`  
- 可根据此 `根目录` 更改相对路径
---
环境设置（我猜的，所以我设置了）：  
  - 频道和群的 `@方式` 可能不相同，所以建议 `关闭`  
  - 在你的环境配置文件中设置 （如：`.env.dev` 中）  
  - 新建一行，写入：`Haruka_TO_ME=False`
---
安装：
- 将文件替换即可  
- 假设 `haruka_bot` 目录为 `根目录`
- 
- 替换 `database` 目录下的 `models.py`  
- 替换 `utils` 目录下的 `__init__.py`

## 特别感谢

- [SK-415/HarukaBot](https://github.com/SK-415/HarukaBot)： 感谢SK佬做出如此优雅的机器人。
- [@mnixry](https://github.com/mnixry)： 感谢混淆佬为HarukaBot项目提供的**技♂术指导**。
- [@wosiwq](https://github.com/wosiwq)： 感谢 W 桑撰写的「小小白白话文」。
- [nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)： 感谢混淆佬提供的频道适配补丁。
- [NoneBot2](https://github.com/nonebot/nonebot2)： HarukaBot 使用的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)： 稳定完善的 CQHTTP 实现。
- [bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)： 非常详细的 B 站 API 文档。
- [bilibili_api](https://github.com/Passkou/bilibili_api)： Python 实现的 B 站 API 库。
