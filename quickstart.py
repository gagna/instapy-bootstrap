"""
This template is written by gagna

"""
# imports
import random

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

# ------------------------------------------------------------------------

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

    bottingSession.set_skip_users(skip_private=False)
    bottingSession.set_simulation(enabled=False)
    # ------------------------------------------------------------------------

    # mandatory language, skip post f any character of the description
    # is outside of the character set selected
    # Available character sets:
    # LATIN, GREEK, CYRILLIC, ARABIC,
    # HEBREW, CJK, HANGUL, HIRAGANA,
    # KATAKANA and THAI
    # bottingSession.set_mandatory_language(enabled=True, character_set='LATIN')

    # like the image if any of passed words are in there

    # bottingSession.set_mandatory_words(mandatory_words_list)

    # prevent commenting and unfollowing your friends
    bottingSession.set_dont_include(friends_list)

    # ignore liking your friends post
    bottingSession.set_ignore_users(friends_list)

    # won't like the image if one of those hashtags are in there
    bottingSession.set_dont_like(blacktags_list)
    # ------------------------------------------------------------------------

    # liking
    bottingSession.set_delimit_liking(enabled=True, max=1000, min=20)
    # ------------------------------------------------------------------------

    # following

    bottingSession.set_do_follow(enabled=True, percentage=30, times=2)
    # ------------------------------------------------------------------------

    # commenting, append @{} to tag post owners

    # session.set_do_comment(enabled=True, percentage=15)
    # session.set_comments(pic_comments_list, media='Photo')
    # session.set_comments(vid_comments_list, media='Video')
    # ------------------------------------------------------------------------

    # user interact settings

    bottingSession.set_user_interact(amount=3, randomize=True, percentage=40)
    bottingSession.set_do_like(enabled=True, percentage=100)
    # ------------------------------------------------------------------------

    # smart hashtags

    # bottingSession.set_smart_hashtags(smart_hashtags_list, limit=3, sort='top', log_tags=True)
    # bottingSession.set_smart_location_hashtags(smart_locations_list, radius=20, limit=10)
    # ------------------------------------------------------------------------

    """
    Actions
    """
    # action by smart hashtags

    # bottingSession.like_by_tags(amount=10, use_smart_hashtags=True)
    # bottingSession.like_by_tags(amount=10, use_smart_location_hashtags=True)
    # ------------------------------------------------------------------------

    # actions by tags

    # bottingSession.like_by_tags(hashtags_list, amount=300)
    # session.follow_by_tags(['tag1', 'tag2'], amount=10)
    # ------------------------------------------------------------------------

    # like by feed

    # bottingSession.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)

    # ------------------------------------------------------------------------

    # actions by locations

    bottingSession.like_by_locations(
        random.choices(locations_list, k=3), amount=random.randint(10, 120), skip_top_posts=False
    )
    bottingSession.follow_by_locations(random.choices(locations_list, k=3), amount=100)

    # session.comment_by_locations(random.choices(locations_list, k=3), amount=100)

    # ------------------------------------------------------------------------

    # follow someone else's followers

    bottingSession.follow_user_followers(
        random.choices(influencers_list, k=3),  # get 3 random user from list
        amount=random.randint(25, 50),
        randomize=False,
        sleep_delay=600,
        interact=True,
    )

    # ------------------------------------------------------------------------

    """ 
    InstaPy Pods
    """
    bottingSession.set_comments(pods_comments_list, media="Photo")
    bottingSession.join_pods()

    # ------------------------------------------------------------------------

    # unfollowing

    bottingSession.unfollow_users(
        amount=random.randint(50, 100),
        InstapyFollowed=(True, "nonfollowers"),
        style="FIFO",
        unfollow_after=7 * 24 * 60 * 60,
        sleep_delay=600,
    )

    bottingSession.unfollow_users(
        amount=random.randint(75, 150),
        InstapyFollowed=(False, "all"),
        style="LIFO",
        unfollow_after=48 * 60 * 60,
        sleep_delay=600,
    )

    # ------------------------------------------------------------------------
