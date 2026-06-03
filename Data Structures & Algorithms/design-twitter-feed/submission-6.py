from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                indx = len(self.tweetMap[followeeId])-1
                time, tweetId = self.tweetMap[followeeId][indx]
                heap.append([time, tweetId, followeeId, indx-1])

        heapq.heapify(heap)
        while heap and len(ans)<10:
            time, tweetId, followeeId, indx = heapq.heappop(heap)
            ans.append(tweetId)
            if indx >= 0:
                time, tweetId = self.tweetMap[followeeId][indx]
                heapq.heappush(heap, [time, tweetId, followeeId, indx-1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
