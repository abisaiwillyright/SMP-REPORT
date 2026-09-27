# This is what the X Api vs returns when you fetch a post
# Structure: data (the post) + include (the auther details)

import requests, json, datetime, os, tweepy, math

x_response = {
    "data": {
        "id": "2076589716036608320",
        "text": "Live by a code:\n\n* Loyalty.\n* Strength.\n* Honour.\n* Discipline.\n\nIf you stand for nothing, you fall for anything.",
        "created_at": "2026-07-14T05:30:00Z",
        "author_id": "748352990",
        "public_metrics": {
            "retweet_count": 2104,
            "reply_count":    487,
            "like_count":   11380,
            "quote_count":    319,
            "bookmark_count": 4251
        }
    },
    "includes": {
        "users": [
            {
                "id": "748352990",
                "name": "Amerix",
                "username": "amerix",
                "public_metrics": {
                    "followers_count": 1200000,
                    "following_count": 487
                }
            }
        ]
    }
}

# Parse it exactly as you have been parsing all lesson
post    = x_response["data"]
author  = x_response["includes"]["users"][0]
metrics = post["public_metrics"]

print('POST')
print(f' Auther: @{author['username']} ({author['name']})')
print(f' Text: {post['text'][:60]}...')
print()

print('ENGEGEMENT')
print(f"Likes: {metrics['like_count']:,} \nRetweets: {metrics['retweet_count']:,} \nReplies: {metrics['reply_count']:,} \nBookmarks: {metrics['bookmark_count']:,}\n")

print(f"AUTHOR: @{author['username']} has {author['public_metrics']['followers_count']:,} followers")



print(f"Read more at: https://x.com/{author['username']}\n")