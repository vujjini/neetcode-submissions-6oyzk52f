class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 1
        news = []
        for i in reversed(range(len(self.tweets))):
            if k > 10:
                break
            if userId in self.follow_map:
                if self.tweets[i][0] in self.follow_map[userId]:
                    news.append(self.tweets[i][1])
                    k+=1
            elif self.tweets[i][0] == userId:
                news.append(self.tweets[i][1])
                k+=1

        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].add(followeeId)
        else:
            self.follow_map[followerId] = {followerId, followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
