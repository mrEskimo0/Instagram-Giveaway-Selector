import random
import instaloader

def specify_post(L):
    # get post that we want to pick comments from_username
    shortcode = input('what is the shortcode?')
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    return post

def get_comments(post, L, profile):
    # get comments from post into list
    post_comments = post.get_comments()
    user_comments = []

    for comment in post_comments:
        if len(comment.text.split('@')) < 2 and comment.owner.username not in user_comments:
            comment_followees = instaloader.Profile.from_username(L.context, comment.owner.username)
            follow_flag = False
            for account_followed in comment_followees.get_followees():
                if follow_flag:
                    break
                if account_followed == profile.username:
                    follow_flag = True
            if follow_flag:
                user_comments.append(comment.owner.username)
                
    return user_comments

def pick_comment(user_set):
    # pick a comment from list
    return random.choice(user_set)
