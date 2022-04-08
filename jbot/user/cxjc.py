#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import os
import sys

from telethon import events
from .login import user
from .. import chat_id, logger, ch_name, BOT_SET

@user.on(events.NewMessage(from_users=chat_id, pattern=r'^-cx$'))
#@jdbot.on(events.NewMessage(from_users=chat_id, pattern=r'^/cx$'))
async def cxjc(event):
    try:        
        cmd = "ps -ef"
        f = os.popen(cmd)
        txt = f.readlines() 
        strReturn=""
        intcount=0
        if txt:
            for line in txt:
                if "timeout" in line:
                    continue
                if "/ql/build" in line:
                    continue
                if "backend" in line:
                    continue
                if "node" in line and ".js" in line :
                    pid = line.split()[0].ljust(10,' ')
                    pid_name = line.split()[4]
                    res ="/kill"+pid+'文件名: '+pid_name+'\n\n'
                    strReturn=strReturn+res
                    intcount=intcount+1
                if "python3" in line and ".py" in line:
                    pid = line.split()[0].ljust(10,' ')
                    pid_name = line.split()[4]
                    res ="/kill"+pid+'文件名: '+pid_name+'\n\n'
                    strReturn=strReturn+res
                    intcount=intcount+1
                if intcount==35:
                    intcount=0
                    if strReturn:
                        msg = await event.edit(strReturn)
                        await asyncio.sleep(10)
                        await msg.delete()
                    strReturn=""
            if strReturn:
                msg = await event.edit(strReturn)
                await asyncio.sleep(10)
                await msg.delete()
            else:
                msg = await user.send_message(event.chat_id,'当前系统未执行任何脚本')
                await asyncio.sleep(5)
                await msg.delete()
        else:
            msg = await user.send_message(event.chat_id,'当前系统未执行任何脚本')
            await asyncio.sleep(5)
            await msg.delete()
        
    except Exception as e:
        title = "【💥错误💥】"
        name = "文件名：" + os.path.split(__file__)[-1].split(".")[0]
        function = "函数名：" + sys._getframe().f_code.co_name
        tip = '建议百度/谷歌进行查询'
        await jdbot.send_message(chat_id, f"{title}\n\n{name}\n{function}\n错误原因：{str(e)}\n\n{tip}")
        logger.error(f"错误--->{str(e)}")


if ch_name:
    jdbot.add_event_handler(cxjc, events.NewMessage(from_users=chat_id, pattern=BOT_SET['命令别名']['cron']))