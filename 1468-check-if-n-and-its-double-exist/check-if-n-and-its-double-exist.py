class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i+1,len(arr)):
                if (i != j) and (0 <= i and j < len(arr)) and (arr[i] == 2*arr[j] or arr[j] == 2 * arr[i]):
                    return True
        return False