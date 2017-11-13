import praw

reddit = praw.Reddit(client_id='clientid', client_secret='secretcode,
                     password='password', user_agent='Reddit Flair Data Bot by chaseoes', username='username')
subreddit = reddit.subreddit('globaloffensive')

myData = dict()
post = 0

# Search all submissions between Jan 1 and Dec 31. Change the epoch times here to your own date range.
for submission in subreddit.submissions(1483228800, 1514678400):
    count = myData.get(submission.link_flair_text, 0)
    myData[submission.link_flair_text] = count + 1
    post += 1
    print("(#" + str(post) + ") " + submission.title)

# Write data to a CSV file.
with open('flair-stats.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in myData.items()]

# All done!
print(">>> Completed! Data saved to flair-stats.csv.")
