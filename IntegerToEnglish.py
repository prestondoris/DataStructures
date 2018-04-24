# LeetCode Question Integer to English Words
#Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# This was my original answer, but after looking through other solutions, I found a solution in Java
# by user "iuri.srb". That version is below this block comment.
#def numberToWords(self, num):
#     """
#     :type num: int
#     :rtype: str
#     """
#     zeroToTwenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten','Eleven', 'Twelve',                          'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
#     tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
#     numStr = str(num)
#     ans = ''
#     nextPlace = ''
#     if len(numStr) == 1:
#         if int(numStr[0]) == 0:
#             ans = 'Zero'
#         else:
#             ans = '%s' % zeroToTwenty[int(numStr[0])]
#
#     elif len(numStr) == 2:
#         remainder = num % 10
#         if num >= 20:
#             if remainder > 0:
#                 ans = '%s ' % tens[int(numStr[0])] + '%s' % zeroToTwenty[remainder]
#             else:
#                 ans = '%s' % tens[int(numStr[0])]
#         else:
#             ans = '%s' % zeroToTwenty[num]
#
#     elif len(numStr) == 3:
#         remainder = num % 100
#         if remainder > 0:
#             nextPlace = self.numberToWords(remainder)
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Hundred' + '%s' % nextPlace
#         else:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s' % 'Hundred'
#
#     elif len(numStr) == 4:
#         remainder = num % 1000
#         if remainder > 0:
#             nextPlace = self.numberToWords(remainder)
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Thousand' + '%s' % nextPlace
#         else:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s' % 'Thousand'
#
#     elif len(numStr) == 5:
#         remainder = num % 1000
#         if remainder > 0:
#             nextPlace = self.numberToWords(remainder)
#             if int(numStr[:2]) >= 20:
#                 tensPlace = int(numStr[:2]) % 10
#                 if tensPlace:
#                     ans = '%s ' %tens[int(numStr[0])] + '%s ' %zeroToTwenty[tensPlace] + '%s ' %'Thousand' + '%s' %nextPlace
#                 else:
#                     ans = '%s ' % tens[int(numStr[0])] + '%s ' % 'Thousand' + '%s' % nextPlace
#
#             else:
#                 ans = '%s ' % zeroToTwenty[int(numStr[:2])] + '%s ' % 'Thousand' + '%s' % nextPlace
#         else:
#             if int(numStr[:2]) >= 20:
#                 tensPlace = int(numStr[:2]) % 10
#                 if tensPlace:
#                     ans = '%s ' %tens[int(numStr[0])] + '%s ' % zeroToTwenty[tensPlace] + '%s' % 'Thousand'
#                 else:
#                     ans = '%s ' %tens[int(numStr[0])] + '%s' % 'Thousand'
#             else:
#                 ans = '%s ' %zeroToTwenty[int(numStr[:2])] + '%s' % 'Thousand'
#
#     elif len(numStr) == 6:
#         remainder = num % 100000
#         nextPlace = self.numberToWords(remainder)
#         if remainder > 1000:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] +'%s ' % 'Hundred' + '%s' % nextPlace
#         elif 0 < remainder < 1000:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Hundred Thousand' + '%s' % nextPlace
#         else:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s' % 'Hundred Thousand'
#
#     elif len(numStr) == 7:
#         remainder = num % 1000000
#         if remainder > 0:
#             nextPlace = self.numberToWords(remainder)
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Million' + '%s' % nextPlace
#         else:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s' % 'Million'
#
#     elif len(numStr) == 8:
#         remainder = num % 1000000
#         if remainder > 0:
#             nextPlace = self.numberToWords(remainder)
#             if int(numStr[:2]) >= 20:
#                 tensPlace = int(numStr[:2]) % 10
#                 if tensPlace:
#                     ans = '%s ' %tens[int(numStr[0])] + '%s ' %zeroToTwenty[tensPlace] + '%s ' %'Million' + '%s' %nextPlace
#                 else:
#                     ans = '%s ' %tens[int(numStr[0])] + '%s ' %'Million' + '%s' %nextPlace
#             else:
#                 ans = '%s ' %zeroToTwenty[int(numStr[:2])] + '%s ' %'Million' + '%s' %nextPlace
#         else:
#             if int(numStr[:2]) >=20:
#                 tensPlace = int(numStr[:2]) % 10
#                 if tensPlace:
#                     ans = '%s '% tens[int(numStr[0])] + '%s ' %zeroToTwenty[tensPlace] + '%s' % 'Million'
#                 else:
#                     ans = '%s '% tens[int(numStr[0])] + '%s' % 'Million'
#             else:
#                 ans = '%s '% zeroToTwenty[int(numStr[:2])] + '%s' % 'Million'
#
#
#     elif len(numStr) == 9:
#         remainder = num % 100000000
#         nextPlace = self.numberToWords(remainder)
#         if remainder > 1000000:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Hundred' + '%s' % nextPlace
#         elif 0 < remainder < 1000000:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Hundred Million' + '%s' % nextPlace
#         else:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s' % 'Hundred Million'
#
#     elif len(numStr) == 10:
#         remainder = num % 1000000000
#         if remainder > 0:
#             nextPlace = self.numberToWords(remainder)
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s ' % 'Billion' + '%s' % nextPlace
#         else:
#             ans = '%s ' % zeroToTwenty[int(numStr[0])] + '%s' % 'Billion'
#
#
#     return ans



def numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return 'Zero'
    else:
        return self.convert(num)


def convert(self, num):
    zeroToTwenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten','Eleven', 'Twelve',
                    'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    ans = ''

    if num < 20:
        ans = zeroToTwenty[num]
    elif num < 100:
        if num % 10:
            ans = tens[num/10] + ' ' + self.convert(num % 10)
        else:
            ans = tens[num/10] + '' + self.convert(num % 10)

    elif num < 1000:
        if num % 100:
            ans = self.convert(num/100) + ' Hundred ' + self.convert(num % 100)
        else:
            ans = self.convert(num/100) + ' Hundred'

    elif num < 1000000:
        if num % 1000:
            ans = self.convert(num/1000) + ' Thousand ' + self.convert(num % 1000)
        else:
            ans = self.convert(num/1000) + ' Thousand'

    elif num < 1000000000:
        if num % 1000000:
            ans = self.convert(num/1000000) + ' Million ' + self.convert(num % 1000000)
        else:
            ans = self.convert(num/1000000) + ' Million'
    else:
        if num % 1000000000:
            ans = self.convert(num/1000000000) + ' Billion ' + self.convert(num % 1000000000)
        else:
            ans = self.convert(num/1000000000) + ' Billion'
    return ans
