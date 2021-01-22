# coding=utf-8

from msg.msg_cache import MsgCache
from msg.message_handler import MSG_CACHE_SIZE


class GroupCache:

    def __init__(self):
        self.cache = {}

    def insert(self, group, member, msg):
        if group not in self.cache:
            self.cache[group] = MsgCache(MSG_CACHE_SIZE)
        self.cache[group].append((msg, member))
