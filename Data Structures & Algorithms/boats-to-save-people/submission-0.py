class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0
        right = len(people) - 1
        while right >= 0 and people[right] == limit:
            right -= 1
            count += 1
        while left <= right:
            if left == right:
                count += 1
                left += 1
                right -= 1
                break
            leftN = people[left]
            rightN = people[right]
            if leftN + rightN <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                right -= 1
        return count
        