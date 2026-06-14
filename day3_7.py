for num in range(1, 100):
    if num > 1:
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2 and num % 2 == 0:
            print(num)