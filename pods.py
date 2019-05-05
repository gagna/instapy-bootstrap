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

from basic_settings import insta_password, insta_username, pods_comments_list

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
    """ InstaPy Pods
    """
    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(pods_comments_list, media="Photo")
    session.join_pods()
