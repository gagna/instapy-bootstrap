"""
This template is written by @il.gagna

Based on like_by_tag_interact_unfollow.py by @timgrossmann

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

""" Botting session
"""

session = InstaPy(
    username=insta_username,
    password=insta_password,
    disable_image_load=True,
    headless_browser=True,
    multi_logs=True,
)


with smart_run(session):
    """ Settings
    """
    session.set_relationship_bounds(enabled=True, max_followers=15000)

    session.set_dont_include(friends_list)
    session.set_dont_like(blacktags_list)
    session.set_ignore_if_contains(white_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    """ Actions
    """
    session.like_by_tags(
        random.sample(hashtags_list, 3), amount=random.randint(50, 100), interact=True
    )

    session.unfollow_users(
        amount=random.randint(75, 150),
        InstapyFollowed=(True, "all"),
        style="FIFO",
        unfollow_after=90 * 60 * 60,
        sleep_delay=501,
    )

    """ InstaPy Pods
    """
    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(pods_comments_list, media="Photo")
    session.join_pods()
