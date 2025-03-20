import os 
a = 'a'
with open("C:\\Users\\meir.stroh\\OneDrive\\new\\unsubscribeLinks\\links.html", "r+") as f:
    file = f.read()
    if a not in file:
        f.write("\n a is not in file")
        print('a is not in file')
    else:
        print("a is in file")
    print(file)