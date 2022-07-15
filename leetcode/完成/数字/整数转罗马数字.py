class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {
            4:{"1":"M","2":"MM","3":"MMM","4":"MD","5": "D","6":"DM","7":"DM","8":"DMMM","9":"MM"},
            3:{"0":"","1":"C","2":"CC","3":"CCC","4":"CD","5": "D","6":"DC","7":"DCC","8":"DCCC","9":"CM"},
            2: {"0":"","1":"X","2":"XX","3":"XXX","4":"XL","5": "L","6":"LX","7":"LXX","8":"LXXX","9":"XC"},
            1:{"0":"","1":"I","2":"II","3":"III","4":"IV","5": "V","6":"VI","7":"VII","8":"VIII","9":"IX"},
        }
        num_str = str(num)
        long = len(num_str)
        res_list = []
        for count,n in enumerate(num_str):
            pos = long - count
            res_list.append(dic[pos][n])
        return "".join(res_list)

test = Solution()
print(test.intToRoman(70))