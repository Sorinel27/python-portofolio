from instaloader import Instaloader, Profile
from insta_users import users

total_followers = []

for user in users:
    L = Instaloader()
    profile = Profile.from_username(L.context, user)
    total_followers.append(profile.followers)
