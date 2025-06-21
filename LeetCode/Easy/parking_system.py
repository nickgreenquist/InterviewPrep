class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small

        self.big_used = 0
        self.medium_used = 0
        self.small_used = 0
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big_used < self.big:
                self.big_used += 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium_used < self.medium:
                self.medium_used += 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small_used < self.small:
                self.small_used += 1
                return True
            else:
                return False
        else:
            return False