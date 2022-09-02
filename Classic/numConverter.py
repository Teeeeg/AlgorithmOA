EN_ONES = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
EN_TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
EN_DOZENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
EN_BASE = ["", "Thousand", "Million", "Billion"]

CN_ONES = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
CN_BASE = ["", "十", "百", "千", "万", "亿"]

EN_NUM = {
    "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Eleven": 11,
    "Twelve": 12,
    "Thirteen": 13,
    "Fourteen": 14,
    "Fifteen": 15,
    "Sixteen": 16,
    "Seventeen": 17,
    "Eighteen": 18,
    "Nineteen": 19,
    "Twenty": 20,
    "Thirty": 30,
    "Forty": 40,
    "Fifty": 50,
    "Sixty": 60,
    "Seventy": 70,
    "Eighty": 80,
    "Ninety": 90
}

EN_NUM_BASE = {"Hundred": 100, "Thousand": 1000, "Million": 1000000, "Billion": 1000000000}

CN_NUM = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}

CN_NUM_BASE = {"十": 10, "百": 100, "千": 1000, "万": 10000, "亿": 100000000}


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

        if res[-1] == '零':
            return res[:-1]

        return res

    def englishToArabicNumeral(self, enString: str):
        if not enString:
            return -1

        n = len(enString)
        stack = []
        left = 0
        right = 0

        while right < n:
            while right < n and enString[right] != ' ':
                right += 1
            token = enString[left:right]

            if token in EN_NUM:
                num = EN_NUM[token]
                stack.append(num)
            else:
                base = EN_NUM_BASE[token]
                prefix = 0

                while stack and stack[-1] < base:
                    prefix += stack.pop()

                stack.append(prefix * base)

            left = right + 1
            right += 1

        res = 0
        while stack:
            res += stack.pop()

        return res

    def chineseToArabicNumeral(self, cnString: str):
        if not cnString:
            return -1

        index = 0
        n = len(cnString)
        stack = []

        while index < n:
            cnChar = cnString[index]

            if cnChar in CN_NUM:
                num = CN_NUM[cnChar]
                stack.append(num)
            else:
                base = CN_NUM_BASE[cnChar]
                prefix = 0

                while stack and stack[-1] < base:
                    prefix += stack.pop()
                stack.append(prefix * base)

            index += 1

        res = 0
        while stack:
            res += stack.pop()

        return res


enString = 'Three Thousand Four Hundred One'
slt = Solution()
print(slt.englishToArabicNumeral(enString))
cnString = '一十二'
print(slt.chineseToArabicNumeral(cnString))
