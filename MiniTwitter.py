'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.users = dict()
        self.timestamp = dict()
        
    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        if user_id in self.users:
            self.timestamp[user_id].append(tweet_text)
        else:
            self.users[user_id] = list()
            self.timestamp[user_id] = list()
            self.timestamp[user_id] = [tweet_text] + self.timestamp[user_id] # Add to the front of the list
        # print self.timestamp[user_id]
        return self.timestamp[user_id]

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        ret = []
        bound = 10 if 10 < len(self.timestamp[user_id]) else len(self.timestamp[user_id])
        for i in range(0, bound):
            ret = ret + [self.timestamp[user_id][i]]
        print ret
        return ret
        
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    # def getTimeline(self, user_id):
        # Write your code here


    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    # def follow(self, from_user_id, to_user_id):
        # Write your code here


    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    # def unfollow(self, from_user_id, to_user_id):
        # Write your code here




    
