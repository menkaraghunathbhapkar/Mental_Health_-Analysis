import tweepy 
import csv
import io

#Twitter API credentials

consumer_key = 'd7RJDeV6M1TdKnXXdY29Zud5O'
consumer_secret = '8LV35luiAco2mBnQ1W6erOnA8cbMwVgxblfHjP5zk5dmAXGwd6'
access_key = '2206645458-9qlftwQ5eiovob7GCp21VrAoFRXi7AJLGt5ts3O'
access_secret = 'Oc9ZKbHSL0reJhZYcU0Vk9UERbVvsTwerIfDUTwiRNGYf'

#with io.open(f'tweetsAll.csv', "a", encoding="utf-8") as f:

All_Users_tweets=[]
All_Tweetscount_forindividual_user=[]
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        count=0
        #alltweets=[]
        #alltweets.append(screen_name)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
        #print(alltweets)
        count=count+len(alltweets)
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str,tweet.text] for tweet in alltweets]
    All_Users_tweets.extend(outtweets)
    All_Tweetscount_forindividual_user.append(count)

    
    pass
    

#write the csv  
#with io.open(f'AllFinaltweetswithcount.csv', "a", encoding="utf-8") as f:
    #with open(f'new_{screen_name}_tweets.csv', 'w') as f:
    #writer = csv.writer(f)
    #writer.writerow(["id","text"])
    #writer.writerows(All_Users_tweets)
    
    
    
    
name=["J_tsar",'Daniel78037553','VenglishWell','ida_skibenes','GraceYeohCNA']
for i in range(len(name)):
    if __name__ == '__main__':
    #pass in the username of the account you want to download
        get_all_tweets(name[i])

