"""
Settings

Be sure to insert the right credentials
"""
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
white_list = [line.rstrip("\n") for line in open("txt_files/whitelist.txt")]
