class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        for i in bills:
            if i == 5:
                count5 += 1
            elif i == 10:
                count10 += 1
                # we have to check if we have a 5 to spare
                if count5 <= 0:
                    return False
                count5 -= 1
            elif i == 20:
                # we dont have to store 20 as we wont spare it to anyone
                # first we'll try to give 10+5, if not we'll do 5+5+5
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        return True
        