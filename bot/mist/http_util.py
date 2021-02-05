# coding=utf-8

import requests
from mist import logger as log


async def download_img(img_url, save_path, api_token=None):
    log.i("img url: %s" % img_url)
    header = {"Authorization": "Bearer " + api_token} if api_token else None
    r = requests.get(img_url, headers=header, stream=True)
    log.i(r.status_code)
    if r.status_code == 200:
        open(save_path, 'wb').write(r.content)
    flag = r.status_code == 200
    del r
    return flag

