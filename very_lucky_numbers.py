list = []
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            for a4 in range(1,10):
                for b1 in range(10):
                    for b2 in range(10):
                        for b3 in range(10):
                            for b4 in range(1,10):
                                if (a1 + a2 == a3 + a4) and (b1 + b2 == b3 + b4):
                                    a = int(str(a1) + str(a2) + str(a3) + str(a4))
                                    b = int(str(b1) + str(b2) + str(b3) + str(b4))
                                    if a > b:
                                        print(a,b)
                                        if a - b == 2016:
                                            list.append([a,b])
                                            print(f"{a} - {b} = 2016")
print(f"Кол-во результатов: {len(list)}")
if len(list) > 0:
    print(f"Результаты: {list}")
