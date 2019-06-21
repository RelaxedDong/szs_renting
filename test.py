import re

REGION = (
    ('0', '不限'), ('1', '罗湖区'), ('2', '福田区'), ('3', '南山区'), ('4', '龙岗区'), ('5', '盐田区'),
    ('6', '宝安区'), ('7', '光明新区'), ('8', '坪山新区'), ('9', '龙华新区'), ('10', '大鹏新区'),)

regions = [r[1] for r in REGION]
com = r'%s'%regions
text = re.findall(com,'坪山新区')
print(''.join(text))