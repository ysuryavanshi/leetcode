class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef = 0
        wait = 0
        for arrival, time in customers:
            if chef <= arrival:
                chef = arrival + time
                wait += time
            else:
                chef = chef + time
                wait += chef - arrival
        return wait/len(customers)
