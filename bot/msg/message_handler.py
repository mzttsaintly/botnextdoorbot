# coding=utf-8

from mist import logger as log
from command.img import EroImage
from command.application import Arknights
from msg.corpus import Corpus
from mist.config_util import Config
from graia.application.message.elements.internal import Plain

import re

MSG_CACHE_SIZE = 10


class MsgHandler:
    groups_cache = []

    def __init__(self):
        self.corpus = Corpus()
        return

    async def handle(self, msg: str, sender, friend=None, group=None, member=None):
        if friend is not None and friend.id == Config().get_aqiang_id():
            for cmd in Arknights.cmd:
                if re.search(cmd, msg):
                    await Arknights().run(sender)
                    return

        for cmd in EroImage.cmd:
            if re.search(cmd, msg):
                img = EroImage().get_rand_img()
                log.i("img: %s" % img)
                await sender(img, 10.0, Plain("别冲了别冲了"))
                return

        answer = self.corpus.compile(msg, None)
        log.i("answer: %s", answer)
        await sender(Plain(answer))


