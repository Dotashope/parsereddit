import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="o3LEH7uPOUluslvEE26CHw",         
                               client_secret="17nxFhV1Pzj0kOrgZhSAHx9zmMrFCA",   
                               user_agent="okonomioki") 

sub = input("Where you want to look?")

subreddit = reddit_read_only.subreddit(sub)
 
posts = subreddit.hot(limit=10)
# Scraping the top posts of the current month

#posts_dict = {"Title": [], "Post Text": [],
#              "ID": [], "Score": [],
#              "Total Comments": [], "Post URL": []
#              }
#getting all the info from posts 

posts_dict = {"Title": [], "Post Text": [],
              "Post_id": [], "Comments": []
              }
for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["Post_id"].append(post.id)
     
    # The score of a post
    #posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    #posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    #posts_dict["Post URL"].append(post.url)
    for ID in ["Post_id"]:
        posts_dict["Comments"].append(subreddit.submission(id=ID))
# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts

top_posts.to_csv("Top Post.csv", index=True)

# python3 "C:\Users\Shidingdingding\Desktop\新建文件夹\reddit.py"