from collections import deque


class Solution:
    # 贪心
    # 一有权利就消灭后面的敌对方

    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Radiant = deque()
        Dire = deque()

        # 统计每个参议员出现的位置
        for i, ch in enumerate(senate):
            if ch == 'R':
                Radiant.append(i)
            else:
                Dire.append(i)

        # 比较每个阵营谁在先
        while Radiant and Dire:
            # 在先的消灭其后面的
            radiant = Radiant.popleft()
            dire = Dire.popleft()
            if radiant < dire:
                # 再次+n加入队列进入下一个循环
                Radiant.append(radiant + n)
            else:
                Dire.append(dire + n)

        return 'Radiant' if Radiant else 'Dire'


senate = 'RDD'
slt = Solution()
print(slt.predictPartyVictory(senate))