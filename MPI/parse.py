with open('file', r) as file:
    list = file.readlines()
    for str in list:
        if "MPI" == str[0:3]:
            print(str[8:-1])
