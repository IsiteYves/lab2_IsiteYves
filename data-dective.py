import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    clean_tweets = []
    bad_rows = 0
    
    for tweet in tweets:
        if not tweet.get('Text') or tweet['Text'].strip() == '':
            bad_rows += 1
            continue
            
        if not tweet.get('Likes') or tweet['Likes'].strip() == '':
            tweet['Likes'] = '0'
            bad_rows += 1
            
        if not tweet.get('Retweets') or tweet['Retweets'].strip() == '':
            tweet['Retweets'] = '0'
            bad_rows += 1
            
        clean_tweets.append(tweet)
    
    print(f"Fixed or removed {bad_rows} bad rows.")
    return clean_tweets

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    if not tweets:
        print("No tweets available.")
        return None
        
    viral_tweet = tweets[0]
    max_likes = int(viral_tweet['Likes']) if viral_tweet['Likes'].isdigit() else 0
    
    for tweet in tweets:
        likes = int(tweet['Likes']) if tweet['Likes'].isdigit() else 0
        if likes > max_likes:
            max_likes = likes
            viral_tweet = tweet
    
    print(f"Viral Tweet - Username: {viral_tweet['Username']}, Likes: {max_likes}")
    print(f"Text: {viral_tweet['Text'][:100]}...")
    return viral_tweet

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    n = len(tweets)
    sorted_tweets = tweets.copy()
    
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            likes1 = int(sorted_tweets[max_idx]['Likes']) if sorted_tweets[max_idx]['Likes'].isdigit() else 0
            likes2 = int(sorted_tweets[j]['Likes']) if sorted_tweets[j]['Likes'].isdigit() else 0
            
            if likes2 > likes1:
                max_idx = j
        
        if max_idx != i:
            sorted_tweets[i], sorted_tweets[max_idx] = sorted_tweets[max_idx], sorted_tweets[i]
    
    return sorted_tweets

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matching_tweets = []
    keyword_lower = keyword.lower()
    
    for tweet in tweets:
        text = tweet.get('Text', '').lower()
        if keyword_lower in text:
            matching_tweets.append(tweet)
    
    print(f"Found {len(matching_tweets)} tweets containing '{keyword}':")
    for tweet in matching_tweets:
        print(f"- {tweet['Username']}: {tweet['Text'][:80]}...")
    
    return matching_tweets

if __name__ == "__main__":
    try:
        # Load the messy data
        dataset = load_raw_data("twitter_dataset.csv")
        print(f"Loaded {len(dataset)} raw tweets.\n")
        
        # Quest 1: Clean the data
        clean_dataset = clean_data(dataset)
        print(f"After cleaning: {len(clean_dataset)} tweets remain.\n")
        
        # Quest 2: Find viral tweet
        print("=== QUEST 2: VIRAL TWEET ===")
        viral = find_viral_tweet(clean_dataset)
        print()
        
        # Quest 3: Sort and show top 10
        print("=== QUEST 3: TOP 10 MOST LIKED TWEETS ===")
        sorted_tweets = custom_sort_by_likes(clean_dataset)
        top_10 = sorted_tweets[:10]
        for i, tweet in enumerate(top_10, 1):
            likes = int(tweet['Likes']) if tweet['Likes'].isdigit() else 0
            print(f"{i}. {tweet['Username']}: {likes} likes - {tweet['Text'][:60]}...")
        print()
        
        # Quest 4: Search functionality
        print("=== QUEST 4: KEYWORD SEARCH ===")
        keyword = input("Enter a keyword to search for: ")
        matches = search_tweets(clean_dataset, keyword)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting gracefully...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)