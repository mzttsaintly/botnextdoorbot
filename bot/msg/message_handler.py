# coding=utf-8

from mist import logger as log
from command.img import EroImage
from command.application import Arknights
from graia.application.message.elements.internal import Plain

import re

MSG_CACHE_SIZE = 10


class MsgHandler:
    corpus = []
    groups_cache = []

    def __init__(self):
        # todo: init corpus file
        return

    async def handle(self, msg: str, sender, friend=None, group=None, member=None):
        if friend is not None and friend.id == 986562745:
            for cmd in Arknights.cmd:
                if re.search(cmd, msg):
                    await Arknights().run(sender)

        for cmd in EroImage.cmd:
            if re.search(cmd, msg):
                img = EroImage().get_rand_img()
                log.i("img: %s" % img)
                await sender(img, 10.0, Plain("别冲了别冲了"))


