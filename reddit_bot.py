import praw
import config
import time
import sys

replied_to = [] #records comments that have already been replied to via comment ID to prevent the same comment getting replied to.

def login():    #logs in to the bot account with information from the conifg file
    print "logging in..."
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Alphabet Bot v0.1")
    return r

def run(r): #runs alphabet counting and replying section
    print "running..."
    count = 1
    try: #ignores errors suchs as parent deleted and so skips to the next comment
        for comment in r.subreddit('test').comments(limit=100):
            print "Comment " + str(count) + "/100"
            count += 1
            if comment.author.name != "alphabetbotcounter":
                if comment.id not in replied_to:
                    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    for x in comment.body.lower():
                        if x in alpha:
                            alpha.remove(x)
                    if len(alpha) > 0:
                        comment.reply("Your post contained " + str(26 - len(alpha)) + " letters from the alphabet. It did not contain \"" + ', '.join(map(str, alpha)) + "\"")
                    if len(alpha) == 0:
                        comment.reply("Your comment used every letter in the alphabet!")
                replied_to.append(comment.id)

    except Exception:
            print "Exception!"
            pass

def sleep(x):   #sleep timer w/ countdown takes arguement of length of sleep time
    print "sleeping..."
    for i in xrange(x,0,-5):
        time.sleep(5)
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()

while True: #keeps bot running on a continous loop with sleep time defining length of time between each run
    r = login()
    run(r)
    sleep(450)
