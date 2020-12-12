def command_input():
    import os
    command = str(input())
    x = 0
    b = False
    i = False
    folder_name = ""
    names = []
    #command evaluation begins
    while x < len(command):
        cl = command[x]
        if b == True and i == False:
            i = True
            u = x
            while x < len(command):
                if command[x] == " ":
                    break
                else:
                    pass
                x += 1
            n = command[u:x]
            i = True
            break
        elif cl == " " and b == False:
            folder_name = command[:x]
            u = x
            b = True
        x += 1
    x += 1 # x = length
    file_exist = False
    if x < len(command):
        file_exist = True
        while x < len(command):
            #print(x)
            name = command[(x)]
            names.append(name)
            #print(name)
            x += 2
    #print(folder_name)
    #print(int(n))
    number = int(n)
    folder = os.mkdir(folder_name)
    x = 0
    if file_exist == True:
        while x < len(names):
            file = open((str(os.getcwd()) + '\\' + str(folder_name) + '\\' + str(names[x]) + '.cpp'), 'x')
            x += 1
    else:
        while x < number:
            x += 1
            file = open((str(os.getcwd()) + '\\' + str(folder_name) + '\\' + str(x) + '.cpp'), 'x')
command_input()