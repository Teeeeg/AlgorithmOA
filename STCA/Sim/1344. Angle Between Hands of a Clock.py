class Solution:

    def getHourAbsoluteAngle(self, hour: int, minutes: int):
        hourPos = hour % 12
        hourPos += (minutes) / 60

        return (hourPos / 12) * 360

    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = self.getHourAbsoluteAngle(hour, minutes)
        minuteAngle = (minutes / 60) * 360
        dist = abs(hourAngle - minuteAngle)

        if dist > 180:
            return 360 - dist
        return dist


hour = 8
minutes = 7
slt = Solution()
print(slt.angleClock(hour, minutes))