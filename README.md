# HarukaBot_Guild_Patch
可以让 **HarukaBot** 适用于 **频道** 的方法。

> 提示： 本补丁没有经过充分测试, 不建议在生产环境使用, 如果发现任何问题请自行解决  
> 或  
> 提交[Issues](https://github.com/17TheWord/HarukaBot_Guild_Patch/issues/new) ，因个人能力有限不保证解决issue


## [HarukaBot](https://haruka-bot.sk415.icu)——优雅的 B 站推送 QQ 机器人

## 食用方法
### 前置需求：  
  - [nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)：频道适配补丁
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
- 中的 `plugins.nonebot_plugin_guild_patch` 部分  
- 替换为自己的频道适配补丁的位置  
- 在NoneBot中，`bot.py` 所在的目录为 `根目录`  
- 可根据此 `根目录` 更改相对位置
---
### 环境设置（我猜的，所以我设置了）：  
  - 频道和群的 `@方式` 可能不相同，所以建议 `关闭`  
  - 在你的环境配置文件中设置 （如：`.env.dev` 中）  
  - 新建一行，写入：`Haruka_TO_ME=False`
---
### 安装：
- 将文件替换即可  
- 假设 `haruka_bot` 目录为 `根目录`


- 替换 `database` 目录下的 `models.py`  
- 替换 `utils` 目录下的 `__init__.py`
---
### 已知问题：
- 建议关闭@机器人命令，因为不清楚频道与群的@方式是否相同 `Haruka_TO_ME=False`
- ~~建议~~ **强烈建议**推送频道设为只读：
  - 由于频道用户ID不同于QQ号，所以猜测超级用户不会生效
  - 经测试，频道内不存在权限系统，任何人都可以使用命令，在使用时请慎重检查频道人员成分
> 再次提示: 本补丁没有经过充分测试, 不建议在生产环境使用, 如果发现任何问题请自行解决  
> 或  
> 提交[Issues](https://github.com/17TheWord/HarukaBot_Guild_Patch/issues/new) ，因个人能力有限不保证解决issue
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

## 问题记录：
### 2022/5/26
- 因为不清楚频道与群的@方式是否相同，建议关闭@机器人命令 `Haruka_TO_ME=False`
- 因数据库中数据类型改动，需要删除数据库重新订阅！！！！！！
- 建议推送频道设为只读，频道内权限与群内权限不一定相同（应该是不同的，在频道内输入开启权限并没有什么反应）
