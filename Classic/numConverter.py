EN_ONES = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
EN_TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
EN_DOZENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
EN_BASE = ["", "Thousand", "Million", "Billion"]

CN_ONES = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
CN_BASE = ["", "十", "百", "千", "万", "亿"]


class Solution:

    def hundredsToEnglishStr(self, num: int):
        res = ''

        if num >= 100:
            index = num // 100
            res += EN_ONES[index] + ' Hundred '
            num %= 100

        if num >= 20:
            index = num // 10
            res += EN_TENS[index] + ' '
            num -= (num // 10) * 10

        if num >= 10:
            index = num - 10
            res += EN_DOZENS[index] + ' '
            num = 0

        if num > 0:
            index = num
            res += EN_ONES[index] + ' '

        return res

    def ArabicNumeralToEnglish(self, num: int):
        if num == 0:
            return 'Zero'

        base = 1000000000
        index = 3
        res = ''

        while base > 0:
            prefix = num // base
            num %= base

            if prefix != 0:
                res += self.hundredsToEnglishStr(prefix) + EN_BASE[index] + ' '
            index -= 1
            base //= 1000

        return res.rstrip(' ')

    def thousandToChineseStr(self, num: int):
        res = ''

        if num >= 1000:
            index = num // 1000
            res += CN_ONES[index] + CN_BASE[3]
            num %= 1000
            # 多少 零 多少
            if num < 100:
                res += CN_ONES[0]

        if num >= 100:
            index = num // 100
            res += CN_ONES[index] + CN_BASE[2]
            num %= 100
            if num < 10:
                res += CN_ONES[0]

        if num >= 10:
            index = num // 10
            res += CN_ONES[index] + CN_BASE[1]
            num %= 10

        if num > 0:
            index = num
            res += CN_ONES[index]

        return res

    def ArabicNumeralToChinese(self, num):
        if num == 0:
            return '零'

        res = ''
        base = 100000000
        index = 5

        while base > 0:
            prefix = num // base
            num %= base

            if prefix != 0:
                unit = CN_BASE[index]
                if index == 3:
                    unit = ''
                res += self.thousandToChineseStr(prefix) + unit
                # 补零
                if num < base // 10:
                    res += CN_ONES[0]
            index -= 1
            base //= 10000

        return res


num = 412021
slt = Solution()
print(slt.ArabicNumeralToChinese(num))