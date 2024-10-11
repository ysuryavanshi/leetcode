class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key=lambda x: times[x][0])
        empty_seats, taken_seats = list(range(len(times))), []

        for i in order:
            a, l = times[i]

            while taken_seats and taken_seats[0][0] <= a:
                heappush(empty_seats, heappop(taken_seats)[1])
            seat = heappop(empty_seats)

            if i == targetFriend: return seat
            heappush(taken_seats, (l, seat))