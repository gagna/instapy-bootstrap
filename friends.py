"""
This template is written by gagna

"""
# imports
import random
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# login credentials
insta_username = ""  # <- enter username here
insta_password = ""  # <- enter password here

# populate list from file
friends_list = [line.rstrip("\n") for line in open("txt_files/friends.txt")]
influencers_list = [line.rstrip("\n") for line in open("txt_files/influencers.txt")]
blacktags_list = [line.rstrip("\n") for line in open("txt_files/blacktags.txt")]
locations_list = [line.rstrip("\n") for line in open("txt_files/locations.txt")]
hashtags_list = [line.rstrip("\n") for line in open("txt_files/hashtags.txt")]
smart_hashtags_list = [line.rstrip("\n") for line in open("txt_files/smart_hashtags.txt")]
smart_locations_list = [line.rstrip("\n") for line in open("txt_files/smart_locations.txt")]
pic_comments_list = [line.rstrip("\n") for line in open("txt_files/pic_comments.txt")]
vid_comments_list = [line.rstrip("\n") for line in open("txt_files/vid_comments.txt")]
mandatory_words_list = [line.rstrip("\n") for line in open("txt_files/mandatory_words.txt")]
pods_comments_list = [line.rstrip("\n") for line in open("txt_files/pods_comments.txt")]
# ------------------------------------------------------------------------

"""
Like the last two post of your friends
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

# ------------------------------------------------------------------------
