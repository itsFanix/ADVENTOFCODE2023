import re

res = 0
digits = {"one": "1", "two" : "2", "three" : "3","four" : "4","five" : "5","six" : "6","seven" : "7", "eight" : "8", "nine" : "9"}
with open('dayOneData.txt') as dataSource:
    
    ##############PartTwo##############
    for line in dataSource:
        pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
        value = re.findall(pattern, line)
        val=""
    #value = re.findall("[0-9]", line)
    #     val = value[0] + value[-1]
    #     print(val)
    #     res += int(val)


    ##PART TWO 
        if value[0] in digits:
            val+= digits[value[0]]
        else:
            val += value[0]
        if value[-1] in digits:
            val += digits[value[-1]]
        else:
            val += value[-1]
        res += int(val)
print(res)

        