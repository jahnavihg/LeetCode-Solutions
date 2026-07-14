def containsDuplicates(num):
    for i in range(len(num)):
        for j in range(i+1, len(Num)):
            if num[i]==num[j]:
                return True
    return False