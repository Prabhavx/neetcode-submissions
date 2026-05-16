class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            while stk and stk[-1] > 0 and ast < 0:
                if stk[-1] < abs(ast):
                    stk.pop()
                    continue
                elif stk[-1] == abs(ast):
                    stk.pop()
                break
            else:
                stk.append(ast)
                
        return stk