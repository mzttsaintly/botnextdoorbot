# coding=utf-8

import os
import re
import json
from random import randint

from graia.application import MessageChain
from graia.application.message.elements.internal import Image
from mist import logger as log
from mist.http_util import download_img

res_path = os.path.abspath(
    os.path.dirname(os.path.abspath(__file__))
    + os.path.sep + ".." +
    os.path.sep + ".." +
    os.path.sep + "res"
)


class Img(object):
    ext = ['.jpg', ".png", ".gif", ".bmp", ".jpeg"]
    sent_list = []
    IMAGE_CACHE_NUM = 50

    def __init__(self):
        self.path = res_path + "\\img"

    async def send_rand_img(self, sender):
        await sender(self.get_rand_img())

    def get_rand_img(self):
        if self.path is None:
            return None
        elif os.path.isdir(self.path):
            img_list = []
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if os.path.splitext(file)[1] in self.ext:
                        img_list.append(file)

            size = len(img_list)
            if size > 0:
                img_path = os.path.join(self.path, img_list[self.get_available_index(size)])
                img = Image.fromLocalFile(img_path)
                return img
        elif os.path.isfile(self.path):
            return self.path

        return None

    def get_available_index(self, img_num) -> int:
        index = randint(0, img_num - 1)
        if img_num > self.IMAGE_CACHE_NUM:
            while index in self.sent_list:
                index = randint(0, img_num - 1)
        self.sent_list.append(index)
        while len(self.sent_list) > self.IMAGE_CACHE_NUM:
            del self.sent_list[0]
        log.i("image index: %d" % index)
        return index


class EroImage(Img):
    cmd = [".*[来搞整].*[瑟色涩]图.*"]
    cmd_receive = "吃点[瑟色涩]图"
    cmd_receive_done = "可以拉了"
    msg_receive = "你倒是发啊"
    msg_receive_done = "不用你提醒我"
    msg_download_success = "吃了"
    msg_download_failure = "吃了个虚空涩图"

    def __init__(self):
        super().__init__()
        self.receive_flag = False
        self.path = res_path + "\\img\\ero"

    async def solve_receive_msg(self, message: MessageChain):
        plain = message.asDisplay()
        if re.search(EroImage.cmd_receive, plain):
            self.set_receive_flag(True)
            return self.msg_receive
        elif re.search(EroImage.cmd_receive_done, plain):
            self.set_receive_flag(False)
            return self.msg_receive_done
        if self.receive_flag:
            images = message.get(Image)
            if len(images) == 0:
                return False
            else:
                return await self.receive_image(images)

    async def receive_image(self, images: list):
        flag = False
        for image in images:
            image = json.loads(image.json())
            save_path = self.path + "/" + image["imageId"]
            if await download_img(image["url"], save_path):
                flag = self.msg_download_success
            else:
                flag = self.msg_download_failure
        return flag

    def set_receive_flag(self, flag: bool):
        log.i("set receive flag: %s" % flag)
        self.receive_flag = flag
