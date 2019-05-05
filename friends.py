"""
This template is written by @il.gagna

Please configure basic_settings.py first
"""

""" Imports
"""
import random

from instapy import set_workspace
from instapy import InstaPy
from instapy import smart_run

from basic_settings import (
    insta_password,
    insta_username,
    friends_list,
    influencers_list,
    blacktags_list,
    locations_list,
    hashtags_list,
    smart_hashtags_list,
    smart_locations_list,
    pic_comments_list,
    vid_comments_list,
    mandatory_words_list,
    pods_comments_list,
    white_list,
)

""" InstaPy workspace settings
"""
set_workspace(path=None)

""" Like the last two post of your friends
"""
session = InstaPy(
    username=insta_username,
    password=insta_password,
    disable_image_load=True,
    headless_browser=True,
    multi_logs=True,
)

with smart_run(session):
    session.set_relationship_bounds(enabled=False)
    session.set_skip_users(skip_private=False)
    session.set_do_like(True, percentage=100)
    session.follow_by_list(friends_list, times=1, sleep_delay=60, interact=False)
    session.interact_by_users(friends_list, amount=2, randomize=False)
