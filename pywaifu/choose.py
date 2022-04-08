import random
from pywaifu.waifu_api import pics


def waifu():
    """Returns a random image link"""
    waifu_pic = random.choice(pics)
    return waifu_pic
