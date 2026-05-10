class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque

        def isEdge(s1,s2,n):
            ans=0
            for i in range(n):
                if s1[i]!=s2[i]: ans+=1
            if ans==1: return True
            else: return False

        def bfs(G,source):
            vis=set([source])
            q=deque([source])
            dist={source:1}
            while q:
                cur=q.popleft()
                for neighbor in G[cur]:
                    if neighbor not in vis:
                        dist[neighbor]=dist[cur]+1
                        vis.add(neighbor)
                        q.append(neighbor)
            return dist
        
        n=len(wordList)+1
        word_len=len(beginWord)
        wordList.append(beginWord)
        G={}
        for i in range(n):
            G[wordList[i]]=[]
            s1=wordList[i]
            for j in range(n):
                s2=wordList[j]
                if isEdge(s1,s2,word_len):
                    G[s1].append(s2)

        dist=bfs(G,beginWord)
        if endWord not in dist: return 0
        else: return dist[endWord]
                
            

        
