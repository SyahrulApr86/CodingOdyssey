# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big_cap = big
        self.medium_cap = medium
        self.small_cap = small
        self. big_now, self.medium_now, self.small_now = 0, 0, 0

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1 and self.big_now < self.big_cap:
            self.big_now += 1
            return True
        elif carType == 2 and self.medium_now < self.medium_cap:
            self.medium_now += 1
            return True
        elif carType == 3 and self.small_now < self.small_cap:
            self.small_now += 1
            return True

        return False

# class ParkingSystem:
#
#     def __init__(self, big, medium, small):
#         self.capacity = {1: big, 2: medium, 3: small}
#         self.current = {1: 0, 2: 0, 3: 0}
#
#     def addCar(self, carType):
#         if self.current[carType] < self.capacity[carType]:
#             self.current[carType] += 1
#             return True
#         return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)