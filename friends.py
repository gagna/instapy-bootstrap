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
friendship = InstaPy(
    username=insta_username,
    password=insta_password,
    disable_image_load=True,
    headless_browser=True,
    multi_logs=True,
)

with smart_run(friendship):
    friendship.set_quota_supervisor(
        enabled=True,
        sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=True,
        peak_likes=(57, 585),
        peak_comments=(21, 182),
        peak_follows=(48, None),
        peak_unfollows=(35, 402),
        peak_server_calls=(None, 4700),
    )
    friendship.set_relationship_bounds(enabled=False)
    friendship.set_skip_users(skip_private=False)
    friendship.set_do_like(True, percentage=100)
    friendship.follow_by_list(friends_list, times=1, sleep_delay=60, interact=False)
    friendship.interact_by_users(friends_list, amount=2, randomize=False)
