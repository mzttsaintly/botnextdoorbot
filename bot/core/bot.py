# coding=utf-8

from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.friend import Friend
from graia.application.group import Group, Member

from msg.message_handler import MsgHandler
from mist import logger as log
from mist import config_util as config

import threading


class Bot:
    send_msg_flag = True

    def start(self):

        message_handler = MsgHandler()
        # message_handler.initHandler()

        loop = asyncio.get_event_loop()

        bcc = Broadcast(loop=loop)
        app = GraiaMiraiApplication(
            broadcast=bcc,
            connect_info=Session(
                host="http://localhost:12012",  # 填入 httpapi 服务运行的地址
                authKey=config.Config().get_auth_key(),  # 填入 authKey
                account=config.Config().get_account_id(),  # 你的机器人的 qq 号
                websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
            )
        )

        @bcc.receiver("FriendMessage")
        async def friend_message_listener(graia_app: GraiaMiraiApplication, friend: Friend, message: MessageChain):

            async def sender(send_msg, wait_time=1.0, wait_msg=None):
                if self.send_msg_flag:
                    if send_msg is not None:
                        result = await graia_app.sendFriendMessage(friend, MessageChain.create([send_msg]))
                        if result:
                            self.set_send_msg_flag(False)
                            threading.Timer(wait_time, self.set_send_msg_flag).start()
                    else:
                        log.e("msg is None")
                elif wait_msg is not None:
                    await graia_app.sendGroupMessage(friend, MessageChain.create([wait_msg]))

            msg = message.asDisplay()
            log.i("receive friend message: %s" % msg)
            await message_handler.handle(msg, sender, friend=friend)

        @bcc.receiver("GroupMessage")
        async def group_message_listener(graia_app: GraiaMiraiApplication, group: Group, member: Member, message: MessageChain):

            async def sender(send_msg, wait_time=1.0, wait_msg=None):
                should_respond = True
                if member.id == config.Config().get_aqiang_id():
                    should_respond = False

                if should_respond and self.send_msg_flag:
                    if send_msg is not None:
                        result = await graia_app.sendGroupMessage(group, MessageChain.create([send_msg]))
                        if result:
                            self.set_send_msg_flag(False)
                            threading.Timer(wait_time, self.set_send_msg_flag).start()
                    else:
                        log.e("msg is None")
                elif wait_msg is not None:
                    await graia_app.sendGroupMessage(group, MessageChain.create([wait_msg]))

            msg = message.asDisplay()
            log.i("receive group message: %s" % msg)
            await message_handler.handle(msg, sender)

        app.launch_blocking()

    def set_send_msg_flag(self, new_flag=True):
        lock = threading.Lock()
        lock.acquire()
        self.send_msg_flag = new_flag
        lock.release()
        log.i("set send msg flag: %s" % new_flag)
