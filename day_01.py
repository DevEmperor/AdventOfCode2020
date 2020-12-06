with open("/media/veracrypt3/Developement/Python/AdventOfCode2020/text_01.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for i in content:
    for j in content:
        for k in content:
            if int(i) + int(j) + int(k) == 2020:
                print(f"I: {i} J: {j} K: {k} Result: {int(i) * int(j) * int(k)}")
