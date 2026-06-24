class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleet = [[position[i], speed[i]] for i in range(n)]
        fleet.sort()    # to sort on the basis of positions
        stack = [fleet[0]]

        for i in range(1,n):
            pos, spd = fleet[i]
            if stack and (stack[-1])[1] <= spd: stack.append(fleet[i])
            else:
                while stack and (stack[-1])[1] > spd and pos + ((pos - (stack[-1])[0])/((stack[-1])[1] - spd)) * spd <= target: # required time for the cars to meet * speed + pos -> pos of meet
                    stack.pop()
                stack.append(fleet[i])

        return len(stack)