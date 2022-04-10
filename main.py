from functions import *
from credentials import USERNAME, PASSWORD
from instaloader import ProfileNotExistsException

if __name__=="__main__":

    L = instaloader.Instaloader()
    L.login(USERNAME, PASSWORD)
    input_profile = input('Insert Username of Giveaway Account')

    try:
        profile = instaloader.Profile.from_username(L.context, input_profile)
    except ProfileNotExistsException:
        print('Profile entered does not exist, restart and enter a new profile')

    winner = False
    while winner == False:

        insta_post = specify_post(L)

        users = get_comments(insta_post, L, profile)

        winner = pick_comment(users)

    print(winner)


