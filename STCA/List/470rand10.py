# # The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# class Solution:

#     def rand10(self):
#         while True:
#             row = rand7()
#             col = rand7()
#             # 生成index 范围在1-40之间
#             index = (row-1) * 7 +  col
#             if index <= 40:
#                 # 对10取余数+1
#                 return (index-1) % 10 + 1
