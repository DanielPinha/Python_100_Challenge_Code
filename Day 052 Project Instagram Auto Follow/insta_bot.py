import os
from InstaFollower import InstaFollower

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')

insta = InstaFollower(EMAIL, PASSWORD)

insta.login_insta()
insta.find_followers('chefsclub')
insta.follow()
