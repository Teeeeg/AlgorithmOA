from heapq import heappop, heappush
from typing import List


class User:

    def __init__(self, userId) -> None:
        self.follower = set()
        self.followee = set([userId])
        self.twit = []


class Twitter:

    def __init__(self):
        self.data = {}
        self.count = 0

    def getOrCreate(self, userId) -> User:
        if userId not in self.data:
            self.data[userId] = User(userId)
        return self.data[userId]

    def postTweet(self, userId: int, twitId: int) -> None:
        user = self.getOrCreate(userId)
        user.twit.append((-self.count, twitId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.getOrCreate(userId)
        followees = user.followee
        res = []
        maxHeap = []

        for followeeId in followees:
            followee = self.data[followeeId]
            for twitId in followee.twit:
                heappush(maxHeap, twitId)

        count = 10
        while maxHeap and count > 0:
            res.append(heappop(maxHeap)[1])
            count -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.getOrCreate(followerId)
        followee = self.getOrCreate(followeeId)
        follower.followee.add(followeeId)
        followee.follower.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.getOrCreate(followerId)
        followee = self.getOrCreate(followeeId)
        if followeeId in follower.followee:
            follower.followee.remove(followeeId)

        if followerId in followee.follower:
            followee.follower.remove(followerId)


twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))