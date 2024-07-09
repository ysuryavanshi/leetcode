class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef = 0
        wait = []
        for arrival, time in customers:
            if chef <= arrival:
                chef = arrival + time
                wait.append(time)
            else:
                chef = chef + time
                wait.append(chef - arrival)
        return sum(wait)/len(wait)
