class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef = wait = 0
        for arrival, time in customers:
            chef = max(arrival, chef) + time
            wait += chef - arrival
        return wait/len(customers)
