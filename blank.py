"""
This template is written by gagna

"""

"""
Imports
"""

from basic_settings import InstaPy, smart_run, set_workspace

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
)

"""
------------------------------------------------------------------------
"""

"""
Real botting session
"""

bottingSession = InstaPy(
    username=insta_username,
    password=insta_password,
    disable_image_load=True,
    headless_browser=True,
    multi_logs=True,
)
"""
------------------------------------------------------------------------
"""

with smart_run(bottingSession):
    """
    Settings
    """
    bottingSession.set_relationship_bounds(
        enabled=True,
        potency_ratio=-0.50,
        delimit_by_numbers=True,
        max_followers=2000,
        max_following=3500,
        min_followers=25,
        min_following=25,
    )

    bottingSession.set_quota_supervisor(
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
    """
    ------------------------------------------------------------------------
    """

    """
    Actions
    """

    # ------------------------------------------------------------------------

    """ 
    InstaPy Pods
    """
    bottingSession.set_comments(pods_comments_list, media="Photo")
    bottingSession.join_pods()

    """
    ------------------------------------------------------------------------
    """
