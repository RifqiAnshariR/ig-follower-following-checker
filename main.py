import json
from datetime import datetime

# Load data followers
with open('./connections/followers_and_following/followers_1.json', 'r') as f:
    followers_data = json.load(f)
    followers = set()
    followers_time = {}
    for e in followers_data:
        u = e['string_list_data'][0]['value']
        t = e['string_list_data'][0]['timestamp']
        dt = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        followers.add(u)
        followers_time[u] = dt

# Load data following
with open('./connections/followers_and_following/following.json', 'r') as f:
    data = json.load(f)
    following_data = data['relationships_following']
    following = set()
    following_time = {}
    for e in following_data:
        u = e['string_list_data'][0]['value']
        t = e['string_list_data'][0]['timestamp']
        dt = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        following.add(u)
        following_time[u] = dt

not_follow_you_back = sorted(following - followers)
not_follow_by_you = sorted(followers - following)

with open('followers.txt', 'w') as f:
    f.write("People follows you:\n")
    for u, t in followers_time.items():
        f.write(f"- username: {u}, time: {t}\n")

with open('following.txt', 'w') as f:
    f.write("People you follow:\n")
    for u, t in following_time.items():
        f.write(f"- username: {u}, time: {t}\n")

with open('not_follow_you_back.txt', 'w') as f:
    f.write("People not following you back:\n")
    for u in not_follow_you_back:
        t = following_time[u]
        f.write(f"- username: {u}, time: {t}\n")

with open('not_follow_by_you.txt', 'w') as f:
    f.write("People not followed by you:\n")
    for u in not_follow_by_you:
        t = followers_time[u]
        f.write(f"- username: {u}, time: {t}\n")

print("Done. File saved!")
