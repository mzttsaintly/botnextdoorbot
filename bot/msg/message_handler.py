# coding=utf-8
from graia.application import MessageChain

from mist import logger as log
from command.img import EroImage
from command.application import Arknights
from msg.corpus import Corpus
from mist.config_util import Config
import mist.config_util as config
from graia.application.message.elements.internal import Plain

import re

MSG_CACHE_SIZE = 10


class MsgHandler:
    groups_cache = []

    def __init__(self):
        self.corpus = Corpus()
        self.ero_image = EroImage()
        return

    async def handle(self, message: MessageChain, sender, friend=None, group=None, member=None):
        plain = message.asDisplay()
        if friend is not None:
            log.i(friend.id, Config().get_manager_id())
            if friend.id in Config().get_manager_id():
                await self.handle_manager_msg(message, sender, friend)
                return

        for cmd in EroImage.cmd:
            if re.search(cmd, plain):
                img = EroImage().get_rand_img()
                log.i("img: %s" % img)
                await sender(img, 10.0, Plain("别冲了别冲了"))
                return

        reply = self.corpus.compile(plain, None)
        log.i("answer: %s", reply)
        await sender(Plain(reply))

    async def handle_manager_msg(self, message: MessageChain, sender, friend):
        reply = await self.ero_image.solve_receive_msg(message)
        if reply is not None:
            await sender(Plain(reply))
            return

        if config.SERVER_FLAG:
            for cmd in Arknights.cmd:
                if re.search(cmd, message.asDisplay()):
                    await Arknights().run(sender)
                    return
