import schedule
import praw
import pandas as pd
import time 

def job():
    
   #Authenticating with reddit servers with the access tokens
    reddit = praw.Reddit(client_id='GS6scCoMSNomkI78L8nglQ',
                             client_secret='D3O0SzMJ8ZIz4IfTL4lAJOHy_fakJA',
                             password='A2d4i0t6y4a@',
                             user_agent='Diss',
                             username='info_scientist')
    
    #Creating an instance of reddit object specifying the subreddit to scrape from
    subreddits=reddit.subreddit('CryptoCurrency')
    
    #Extracting top 50 hot posts from the hot section of reddit
    hot_news=subreddits.new(limit=50)

    #Creating a dictionary to append the values extracted from the api 
    topics_dict={
             "title":[],\
             "score":[],\
             "id":[],\
             "url":[],\
             "comms_num":[],\
             "author":[],\
             "upvote_ratio":[],\
             "flair":[],\
             "created_utc":[],\
             "clicked":[],
             "edited":[],
             "no_crossposts":[],\
             "domain":[],\
             "is_crosspostable":[],\
             "view_count":[],\
             "visited":[],\
             "upvote":[],\
             "ups":[],\
             "is_video":[],\
             "link_flair_text":[],\
             "gilded":[],
           
    
             }
    
    for submission in hot_news:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["author"].append(submission.author)
        topics_dict["upvote_ratio"].append(submission.upvote_ratio)
        topics_dict["flair"].append(submission.author_flair_text)
        topics_dict["created_utc"].append(submission.created_utc)
        topics_dict["clicked"].append(submission.clicked)
        topics_dict["edited"].append(submission.edited)
        topics_dict["no_crossposts"].append(submission.num_crossposts)
        topics_dict["is_crosspostable"].append(submission.is_crosspostable)
        topics_dict["view_count"].append(submission.view_count)
        topics_dict["visited"].append(submission.visited)
        topics_dict["domain"].append(submission.domain)
        topics_dict["ups"].append(submission.ups)
        topics_dict["upvote"].append(submission.upvote)
        topics_dict["is_video"].append(submission.is_video)
        topics_dict["link_flair_text"].append(submission.link_flair_text)
        topics_dict["gilded"].append(submission.gilded)
  


      
     
    df = pd.DataFrame(topics_dict)
    with open('new_crypto1.csv', 'a') as f:
        df.to_csv(f, header=True)
    


schedule.every().day.at("07:30").do(job)
schedule.every().day.at("13:30").do(job)
schedule.every().day.at("19:30").do(job)
schedule.every().day.at("21:30").do(job)

while True:
        schedule.run_pending()
    
        time.sleep(60)
    
    
    
