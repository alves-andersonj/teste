import re

with open('/tmp/output_1.txt', 'r') as f:
    lines = f.readlines()

for tag in lines:
    tag = re.sub(' +', '   ', tag)
    s = tag
    s = s.split("   ", 1)
    row = ""
    for side in s:
        row = row + "     " + side
    print(row.strip())
    with open('/tmp/output_2.txt', 'a') as fw:
        fw.write(row.strip() + '\n')
    fw.close()