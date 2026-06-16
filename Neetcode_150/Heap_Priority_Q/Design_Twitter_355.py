from collections import defaultdict
import heapq 

class Twitter:

    def __init__(self):

        #hashmap which stores UserId as key and following as value
        self.following = defaultdict(set)

        #hashmap which stores UserId as key and list of tweetIds, timestamp as value pairs
        self.tweets = defaultdict(list)

        #timestamp to show when the tweet was created
        self.timestamp = 0

      

    def postTweet(self, userId: int, tweetId: int) -> None:

        #append tweetId with timestamp to dict
        self.tweets[userId].append((self.timestamp, tweetId))

        #decrement the time so latest tweet is at the top of the min heap
        self.timestamp -= 1


    def getNewsFeed(self, userId: int) -> List[int]:

        #list of tweets for result0
        self.tweet_ids = []

        #all user set for iteration
        all_users = set(self.following[userId]) 
        all_users.add(userId)

        min_heap = []

        for user in all_users:

            #check user has tweets
            if user in self.tweets and self.tweets[user]:

                #get latest tweet
                latest_idx = len(self.tweets[user]) - 1

                timestamp, tweetId = self.tweets[user][latest_idx]

                #push latest tweet information to the heap (for each user)
                heapq.heappush(min_heap, (timestamp, user, tweetId, latest_idx))

        while min_heap and len(self.tweet_ids) < 10:

            #pop the latest tweet of the heap
            timestamp, user, tweetId, latest_idx = heapq.heappop(min_heap)

            #append the tweet 
            self.tweet_ids.append(tweetId)

            #if this user has another tweet, get the tweet and push it
            if latest_idx > 0:

                next_idx = latest_idx - 1

                next_timestamp, next_tweetId = self.tweets[user][next_idx]

                heapq.heappush(min_heap, (next_timestamp, user, next_tweetId, next_idx))

        return self.tweet_ids


    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId == followeeId:
            return

        self.following[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            return

        #discard does not throw error if value already exists
        self.following[followerId].discard(followeeId)

 
