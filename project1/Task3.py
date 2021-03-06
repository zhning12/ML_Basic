"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""


call_pes_list = []

#主
opt_phone_080_count = 0
#被
pes_phone_080_count = 0


for phone_info in calls:
    opt_phone = phone_info[0]
    pes_phone = phone_info[1]
    if "(080)" in opt_phone:
        # 主叫电话
        opt_phone_080_count += 1
        #固定电话以"(0"开头
        if pes_phone.startswith("(0"):
            tmp = pes_phone[0:pes_phone.index(")")+1]
            call_pes_list.append(tmp)
            pass
        #移动电话
        if (" " in pes_phone) and (pes_phone.startswith("7") \
            or pes_phone.startswith("8") \
            or pes_phone.startswith("9")):
            tmp = pes_phone[0:4]
            call_pes_list.append(tmp)
            pass
        if pes_phone.startswith("140"):
            pass
            
        if "(080)" in pes_phone:
            pes_phone_080_count += 1
    
# 被叫去重
unique_list = set(call_pes_list)
# 去重后的电话列表排序
sorted_unique_list = sorted(unique_list)

print("The numbers called by people in Bangalore have codes:")
for itm in sorted_unique_list:
    print(itm)

percent = round(pes_phone_080_count*100/opt_phone_080_count, 2)
print("{} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(percent))