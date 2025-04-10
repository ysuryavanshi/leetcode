class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def helper(num: int) -> int:
            num_str = str(num)
            suffix_len = len(s)
            prefix_len = len(num_str) - suffix_len

            if prefix_len < 0:
                return 0

            dp = [[0] * 2 for _ in range(prefix_len + 1)]

            dp[prefix_len][0] = 1
            suffix_from_num = num_str[prefix_len:]
            dp[prefix_len][1] = int(suffix_from_num) >= int(s)

            for i in range(prefix_len - 1, -1, -1):
                digit = int(num_str[i])
                dp[i][0] = (limit + 1) * dp[i + 1][0]
                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]

        return helper(finish) - helper(start - 1)