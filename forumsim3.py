# posts are 1-10 posts, and 0-2x the amount of posts for likes and dislikes
# reposts are 2-8 posts, and 0-2x the amount of posts for likes and dislikes
# profile posts are 1 post, 0-10 likes and 0-3 dislikes
# postfarm is 30-110 posts.

#importing functions
import math
import random

#input
print("input like percent")
like_percent = int(input())
print("input dislike percent")
dislike_percent = int(input())
print("insert /post name")
command_1 = input()
print("insert post content (if any)")
content = input()
print("insert /post-pf name")
command_2 = input()
print("insert /repost name")
command_3 = input()
print("input repost number")
repost_number = input()
print("input replying thread name")
command_4 = input()
print("enter reply content")
command_5 = input()
print("input like count of replying thread")
replylike = int(input())
print("input dislike count of replying thread")
replydislike = int(input())
print("input the number of replies of replying thread")
replyreply = int(input())

#special sections like bonus
likebonus = 35
boosted_section = 2

sp_likebonus = 40
sp_boosted_section = 6

#outlining posts section
post_type = [("/post-sb", 1), ("/post-hy", 2), ("/post-gh", 3), ("/post-fg", 4), ("/post-ot", 5), ("/post-sp", 6)]
profile_post_type = ("/post-pf", 0)
repost_post_type = [("/repost-sb", 1), ("/repost-hy", 2), ("/repost-gh", 3), ("/repost-fg", 4), ("/repost-ot", 5), ("/repost-sp", 6)]
reply_post_type = [("reply-pf", 0), ("/reply-sb", 1), ("/reply-hy", 2), ("/reply-gh", 3), ("/reply-fg", 4), ("/reply-ot", 5), ("/reply-sp", 6)]
section = ["0 not occupied", "Suggestion Box", "Hypixel Minigames Discussions", "Guides/Help", "Forum Games", "Off Topic", "Special"]

#defining functions
def postfarm():
    posts = random.randint(30,110)
    print(f"You farmed {posts} posts!")
    
def post_posting (command_1, post_type, boosted_section, sp_boosted_section):
    tmplikepercent = like_percent
    valid = -1
    for postSection, sectionNum in post_type:
        if postSection in command_1:
            valid = 1
            break
    sectionName = section[sectionNum]
    if boosted_section == sectionNum:
        tmplikepercent += likebonus
    elif sp_boosted_section == sectionNum:
        tmplikepercent += sp_likebonus
    if valid == -1:
        return
        
    #calculation
    post_post = random.randint(1,10)
    like_count = random.randint(0,(2*post_post))
    post_like_count = math.floor(like_count * tmplikepercent / 100)
    dislike_count = random.randint(0,(2*post_post))
    post_dislike_count = dislike_count * dislike_percent / 100
    if (dislike_count > 1 and post_dislike_count < 1):
        post_dislike_count = 1
    else:
        post_dislike_count = math.floor(post_dislike_count)
        
    #printing
    if (content != ""):
        post_like_count += 3
        print(f"You posted '{command_1[9:]}' in the {sectionName} section with the content [{content}].")
        print(f"Post count: {post_post}")
        print(f"Like count: {post_like_count} ({like_count}*{tmplikepercent}%+3)")
        print(f"Dislike count: {post_dislike_count} ({dislike_count}*{dislike_percent}%)")
    else:
        print(f"You posted '{command_1[9:]}' in the {sectionName} Section.")
        print(f"Post count: {post_post}")
        print(f"Like count: {post_like_count} ({like_count}*{tmplikepercent}%)")
        print(f"Dislike count: {post_dislike_count} ({dislike_count}*{dislike_percent}%)")

def profile_post_posting (command_2, profile_post_type):
    profile_post, section = profile_post_type
    if profile_post in command_2:
        
        #calculation
        profile_post = 1
        like_count = random.randint(0,10)
        post_like_count = math.floor(like_count * like_percent / 100)
        dislike_count = random.randint(0,3)
        post_dislike_count = math.floor(dislike_count * dislike_percent / 100)
        if (dislike_count > 1 and post_dislike_count < 1):
            post_dislike_count = 1
        else:
            post_dislike_count = math.floor(post_dislike_count)
        
        #printing
        print(f"You posted '{command_2[9:]}' on your profile.")
        print(f"Post count: {profile_post}")
        print(f"Like count: {post_like_count} ({like_count}*{like_percent}%)")
        print(f"Dislike count: {post_dislike_count} ({dislike_count}*{dislike_percent}%)")
        
def repost_posting (command_3, repost_type, boosted_section, sp_boosted_section):
    tmplikepercent = like_percent
    valid = -1
    for postSection, sectionNum in repost_type:
        if postSection in command_3:
            valid = 1
            break
    sectionName = section[sectionNum]
    if boosted_section == sectionNum:
        tmplikepercent += likebonus
    elif sp_boosted_section == sectionNum:
        tmplikepercent += sp_likebonus
    if valid == -1:
        return
        
    #calculation
    repost_post = random.randint(2,8)
    like_count = random.randint(0,(2*repost_post))
    post_like_count = math.floor(like_count * tmplikepercent / 100)
    dislike_count = random.randint(0,(2*repost_post))
    post_dislike_count = math.floor(dislike_count * dislike_percent / 100)
    if (dislike_count > 1 and post_dislike_count < 1):
        post_dislike_count = 1
    else:
        post_dislike_count = math.floor(post_dislike_count)
        
    #printing
    print(f"You posted '{command_3[11:]}' in the {sectionName} section. This is the {repost_number} repost.")
    print(f"Post count: {repost_post}")
    print(f"Like count: {post_like_count} ({like_count}*{tmplikepercent}%)")
    print(f"Dislike count: {post_dislike_count} ({dislike_count}*{dislike_percent}%)")

def reply_posting (command_4, reply_post_type):
    valid = -1
    for postSection, sectionNum in reply_post_type:
        if postSection in command_4:
            valid = 1
            break
    if valid == -1:
        return
    sectionName = section[sectionNum]
    reply_post = 1
    like_count = round(random.randint(0, replylike) / (replyreply + 1))
    dislike_count = random.randint(0, replydislike)
        
    #printing
    if sectionNum == 0:
        print(f"You posted '{command_5}' in response to '{command_4[10:]}' on a profile, this is the {replyreply}th reply.")
    else:
        print(f"You posted '{command_5}' in response to '{command_4[10:]}' in the {sectionName} section, this is the {replyreply}th reply.")
    print(f"Post count: {reply_post}")
    print(f"Like count: {like_count}")
    print(f"Dislike count: {dislike_count}")
        
#regular posting
post_posting(command_1, post_type, boosted_section, sp_boosted_section)
#spacing
print()
print()
#profile posts
profile_post_posting(command_2, profile_post_type)
#spacing
print()
print()
#repost
repost_posting(command_3, repost_post_type, boosted_section, sp_boosted_section)
#spacing
print()
print()
#reply
reply_posting(command_4, reply_post_type)
#spacing
print()
print()
postfarm()
