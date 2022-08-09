# HarukaBot_Guild_Patch

可以让 **HarukaBot** 适用于 **频道** 的方法。

> 提示： 本补丁没有经过充分测试, 不建议在生产环境使用, 如果发现任何问题请自行解决，  
> 或  
> 提交[Issues](https://github.com/17TheWord/HarukaBot_Guild_Patch/issues/new) （因个人能力有限不保证百分百解决）。

## HarukaBot——优雅的 B 站推送 QQ 机器人

- [文档](https://haruka-bot.sk415.icu)


- [Github](https://github.com/SK-415/HarukaBot)

## 使用方法

### 前置需求

- [Haruka_Bot](https://github.com/SK-415/HarukaBot)  版本：1.4.0

- [nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)：频道适配补丁。

- Python 3.10.5 （本人环境）

---

### 安装

- 脚手架安装
  - `pip install haruka_bot`
  - `pip install nonebot-plugin-guild-patch`
- NoneBot2 插件商店安装
  - `pip install nb-cli`
  - `nb plugin install haruka_bot`
  - `nb plugin install nonebot-plugin-guild-patch`

```
#目录结构参考：

📦 HarukaBot                             # Bot项目
├── 📂 haruka                            # Bot
└── 📂 venv                              # 虚拟环境
    └── 📂 Lib
        └── 📂 site-packages
            └── 📂 haruka_bot            # 通过脚手架或nb商店下载的haruka_bot
                ├── 📂 database          # 替换
                │   ├── 📜 db.py
                │   └── 📜 models.py
                ├── 📂 plugins
                │   ├── 📂 guildadmin    # 增加
                │   │   ├── 📜 __init__.py
                │   │   ├── 📜 add_guild_admin.py
                │   │   ├── 📜 del_guild_admin.py
                │   │   └── 📜 guild_admin_sub.py
                │   ├── 📂 pusher        # 替换
                │   │   ├── 📜 dynamic_pusher.py
                │   │   └── 📜 live_pusher.py
                │   ├── 📂 sub           # 替换
                │   │   ├── 📜 add_sub.py
                │   │   └── 📜 delete_sub.py
                │   └── 📜 __init__.py   # 替换
                └── 📂 utils             # 替换
                    └── 📜 __init__.py
```

- 在虚拟环境 `venv` 目录找到 `haruka_bot`，并设此为此时的根目录
  - **修改数据库存储方式**
  - 替换 `database` 目录的 `models.py`
  - 替换 `database` 目录的 `db.py`


  - **修改工具包**
  - 替换 `utils` 目录的 `__init__.py`
  - 在 `utils` --> `__init__.py` 文件中如下修改
    - 脚手架安装
      - `from nonebot.adapters.onebot.v11.exception import ActionFailed, NetworkError`
      - 因两者 `nonebot2` 版本问题，续修改为
      - `from nonebot.adapters.onebot.v11 import ActionFailed, NetworkError`
    - NoneBot2 插件商店安装
      - 无需修改
  
  - **启用频道适配补丁**
    - 脚手架安装
      - `haruka_bot` --> `__main__.py`
      - 在 `if __name__ == "__main__":` 之前
      - 填写 `nonebot.load_plugin("nonebot_plugin_guild_patch")`
    - NoneBot2 插件商店安装
      - 无需修改

  - **修改关注与推送的方法**
  - 替换 `plugins` 目录的 `__init__.py`
  - 替换 `plugins` --> `sub` 目录的 `add_sub.py` 和 `delete_sub.py`
  - 替换 `plugins` --> `pusher` 目录的 `dynamic_pusher.py` 和 `live_pusher.py`

  - **增加频道管理员操作命令**
  - 复制 `plugins` 目录下的 `guildadmin` 到 `plugins`

---

### 使用

- **其他命令与 `Haruka` 无异**


- **设置频道管理员：**
    - 在频道中使用命令 `添加 / 取消 @xxx` 即可进行管理员的增减操作
    - 管理员可以使用 `关注 / 取关` 功能
    - 只有 **超级用户** 才可以增减管理员
    - 通过 `@` 对管理员进行增减操作


- **设置频道管理员身份组：**
    - 新建一行，写入 `Haruka_GUILD_ADMIN_NAME = ["xxx", "xxxx"]`，
    - 将 `xxx` 替换为你的频道管理员的身份组的名称，
    - 支持多个身份组（其实是目前没有一键挪人的功能，干脆直接多个组解决）。


- 设置频道超级用户
    - 新建一行
    - `Haruka_Guild_Super_User_List = ["xxxxxxxxxx"]`
    - 将 `xxxxxxxxxx` 替换为超级用户的ID

---

### 配置文件参考
```
HOST=127.0.0.1

PORT=8080

LOG_LEVEL=DEBUG

# Windows 用户请将此项设置为false
FASTAPI_RELOAD=false    
      
# 超级用户（频道不可用）
SUPERUSERS=["xxxxxx"]  
       
# Bot 昵称
NICKNAME=[]        
           
# 命令头
COMMAND_START=[""]  
          
# 关闭 @ 前置
Haruka_TO_ME=False       
     
# 频道管理员身份组
Haruka_Guild_Admin_Group_List=["Haruka"]

# 频道超级用户（仅Haruka）
Haruka_Guild_Super_User_List=["144115218675408360"]

```

---

### *最新问题 & 更新 2022 / 8 / 9：*

- **新增：**
  - 将 `频道ID + 子频道ID` 字段分割成两个字段
  - 配置文件设置 `超级用户ID` 与 `管理员身份组`
    
- **改动：**
  - 安装方法改动
    - 原版 `haruka_bot`、`频道适配补丁` 均用 `脚手架` 或 `NoneBot2 插件商店` 安装 
    - 在虚拟环境 `venv` -> `Lib` -> `site-packages` -> `haruka_bot` 依次替换文件
    - `utils` -> `__init__.py`
      - pip 安装
          - `from nonebot.adapters.onebot.v11.exception import ActionFailed, NetworkError`
          - 改为
          - `from nonebot.adapters.onebot.v11 import ActionFailed, NetworkError`
  
  - 推送方法修改，重写频道推送逻辑

  - 权限判断重写，一并挪至 `utils` -> `__init__.py`
  
  - 管理员操作调整

  - 频道超级用户ID
    - 安装方法改动，为方便管理，将插件目录下 `GuildSuperUsers.py` 删除
    - 在配置文件中通过 `Haruka_Guild_Super_User_List = ["xxx"]` 设置频道超级用户ID

  - FASTAPI_RELOAD
    - `Windows` 必须设置 `FASTAPI_RELOAD=false` 才能正常运行 `HarukaBot`
    - 在配置文件，如 `.env.dev`
    - 将 `FASTAPI_RELOAD=true` 改为 `FASTAPI_RELOAD=false`
    
  - `utils` 目录中 `__init__.py`
    - `from nonebot.adapters.onebot.v11.exception`
    - 改为
    - `from nonebot.adapters.onebot.V11`


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

---

## 更新 & 问题记录

### *2022 / 8 / 9：*

- **新增：**
  - 将 `频道ID + 子频道ID` 字段分割成两个字段
  - 配置文件设置 `超级用户ID` 与 `管理员身份组`
    
- **改动：**
  - 安装方法改动
    - 原版 `haruka_bot`、`频道适配补丁` 均用 `脚手架` 或 `NoneBot2 插件商店` 安装 
    - 在虚拟环境 `venv` -> `Lib` -> `site-packages` -> `haruka_bot` 依次替换文件
    - `utils` -> `__init__.py`
      - pip 安装
          - `from nonebot.adapters.onebot.v11.exception import ActionFailed, NetworkError`
          - 改为
          - `from nonebot.adapters.onebot.v11 import ActionFailed, NetworkError`
  
  - 推送方法修改，重写频道推送逻辑

  - 权限判断重写，一并挪至 `utils` -> `__init__.py`
  
  - 管理员操作调整

  - 频道超级用户ID
    - 安装方法改动，为方便管理，将插件目录下 `GuildSuperUsers.py` 删除
    - 在配置文件中通过 `Haruka_Guild_Super_User_List = ["xxx"]` 设置频道超级用户ID

  - FASTAPI_RELOAD
    - `Windows` 必须设置 `FASTAPI_RELOAD=false` 才能正常运行 `HarukaBot`
    - 在配置文件，如 `.env.dev`
    - 将 `FASTAPI_RELOAD=true` 改为 `FASTAPI_RELOAD=false`
    
  - `utils` 目录中 `__init__.py`
    - `from nonebot.adapters.onebot.v11.exception`
    - 改为
    - `from nonebot.adapters.onebot.V11`

---

### *2022 / 7 / 2：*

- **新增：**
    - 支持`通过频道身份组` 设置 `Bot 管理员`
    - 支持`自定义身份组名称`
    - 支持`自定义多个身份组`
    - `身份组权限 Bug` 修复，现已支持


- **改动：**
    - 现已可以开启 `@ 机器人命令`，在最新版频道补丁中已实现 `@消息`
        - `Haruka_TO_ME=True` 或 `删除` 这一行代码


- **无改动：**
    - 频道超级用户列表：
        - 在频道命令中添加判定 `用户频道 ID` 是否在列表中，以暂时解决权限问题。
        - 该组用于管理对数据库中的管理员，将继续保留。
    - 指令添加频道管理员功能：
        - 频道超级用户可在频道中使用 `添加 / 取消 @ 频道用户` 来设置频道 `Bot 管理员`。
        - 管理员只能使用机器人的 `关注 / 取关` 功能，没有其他权限。


- **建议推送频道设为只读：**
    - 虽然暂时解决了权限问题，但频道主/频道管理员，你也不想让你的推送子频道充斥各种聊天信息吧。
    - ~~由于频道用户ID不同于QQ号，猜测超级用户不会生效~~ 已通过设置频道超级用户暂时解决。

---

### *2022 / 6 / 9_2*

- **新增：**
    - ~~支持通过频道身份组设置 `Bot 管理员`~~
    - ~~支持`自定义身份组名称`~~
    - ~~支持`自定义多个身份组`~~
    - 因为某些问题，发现 `Bug`，已取消


- **改动：**
    - 指令添加频道管理员功能：
        - 在超级用户使用 `管理员增减`、`管理列表` 操作时候，会将该用户的 `频道 ID` ~~展示出来~~替换为频道昵称，保护隐私。


- **无改动：**
    - 频道超级用户列表：
        - 在频道命令中添加判定 `用户频道 ID` 是否在列表中，以暂时解决权限问题。
        - 该组用于管理对数据库中的管理员，将继续保留。
    - 指令添加频道管理员功能：
        - 频道超级用户可在频道中使用 `添加 / 取消 @ 频道用户` 来设置频道 `Bot 管理员`。
        - 管理员只能使用机器人的 `关注 / 取关` 功能，没有其他权限。


- **仍旧建议：**
    - 关闭@机器人命令，因为不清楚频道与群的@方式是否相同 `Haruka_TO_ME=False`


- **建议推送频道设为只读：**
    - 虽然暂时解决了权限问题，但频道主/频道管理员，你也不想让你的推送子频道充斥各种聊天信息吧。
    - ~~由于频道用户ID不同于QQ号，猜测超级用户不会生效~~ 已通过设置频道超级用户暂时解决。

---

### *2022 / 6 / 9_1*

- **改动：**
    - 指令添加频道管理员功能：
        - 频道超级用户可在频道中使用 `添加 / 取消 @ 频道用户` 来设置频道Bot管理员。(非常方便)
        - 在超级用户使用 `管理员增减`、`管理列表` 操作时候，会将该用户的 `频道 ID` 展示出来。
        - 管理员只能使用机器人的 `关注 / 取关` 功能，没有其他权限。


- **无改动：**
    - 频道超级用户列表，在频道命令中添加判定 `用户频道 ID` 是否在列表中，以暂时解决权限问题。


- **仍旧建议：**
    - 关闭@机器人命令，因为不清楚频道与群的@方式是否相同 `Haruka_TO_ME=False`


- **建议推送频道设为只读：**
    - 虽然暂时解决了权限问题，但频道主/频道管理员，你也不想让你的推送子频道充斥各种聊天信息吧。
    - ~~由于频道用户ID不同于QQ号，猜测超级用户不会生效~~ 已通过设置频道超级用户暂时解决。

---

### *2022 / 6 / 8*

- **新增：**
    - 频道超级用户列表，在频道命令中添加判定 `用户频道 ID` 是否在列表中，以暂时解决权限问题。
    - 指令添加频道管理员功能：
        - 频道超级用户可在频道中使用 `添加 / 取消 用户频道ID` 来设置频道Bot管理员。
        - 管理员只能使用机器人的 `关注 / 取关` 功能，没有其他权限。


- **仍旧建议：**
    - 关闭@机器人命令，因为不清楚频道与群的@方式是否相同 `Haruka_TO_ME=False`


- **建议推送频道设为只读：**
    - 虽然暂时解决了权限问题，但频道主/频道管理员，你也不想让你的推送子频道充斥各种聊天信息吧。
    - ~~由于频道用户ID不同于QQ号，猜测超级用户不会生效~~ 已通过设置频道超级用户暂时解决。

---

## *2022 / 5 / 28*

- **新增：**
    - 频道超级用户列表，在频道命令中添加判定 `频道用户 ID` 是否在列表中，以暂时解决权限问题


- **仍旧建议：**
    - 关闭 `@ 机器人` 命令，因为不清楚频道与群的 `@ 方式` 是否相同 `Haruka_TO_ME=False`


- **建议推送频道设为只读：**
    - 虽然暂时解决了权限问题，但 `频道主 / 频道管理员`，你也不想让你的推送子频道充斥各种聊天信息吧。
    - 由于 `频道用户 ID` 不同于 `QQ 号`，猜测超级用户不会生效

---

### *2022 / 5 / 26-2*

- **建议：**
    - **关闭** `@ 机器人` 命令，因为不清楚频道与群的 `@ 方式` 是否相同 `Haruka_TO_ME=False`


- ~~建议~~ **强烈建议**推送频道设为只读：
    - 由于 `频道用户 ID` 不同于 `QQ 号`，**猜测** 超级用户不会生效
    - 经测试，频道内不存在权限系统，任何人都可以使用命令，在使用时请慎重检查频道人员成分

---

### *2022 / 5 / 26-1*

- 因为不清楚频道与群的 `@ 方式` 是否相同，建议 **关闭** `@ 机器人` 命令 `Haruka_TO_ME=False`


- 因数据库中数据类型改动，需要删除数据库重新订阅！！！！！！


- 建议推送频道设为只读，频道内权限与群内权限不一定相同（应该是不同的，在频道内输入开启权限并没有什么反应）
