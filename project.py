name = ['Anas', 'Vaishali', 'Dev', 'Roshni']
mark = [240, 260, 270, 250]

def update():
    n = input("Enter Name: ")

    if n in name:
        index = name.index(n)
        m = int(input("Enter Marks: "))
        mark[index] = m
        print("Marks updated successfully")
    else:
        print("Write valid name to update marks")

x = update()

def delete():
    n = input("Enter Name: ")
    if n in name:
        index = name.index(n)
        name[index:index+1] = []
        
    else:
        print("Write valid name to delete")
y = delete()


def insert():
    while True:
        n = input("Enter Name: ")
        p = int(input("Enter Marks:"))
        if n not in name:
            name.append(n)
            mark.append(p)
        else:
            print("Name already exist")
            break

c = insert()

        

def showall():
        print('.'*50)
        for j in range(len(mark)):
            
            print(f"| {name[j]} | {mark[j]} |".center(30, " "))
        print('.'*50)
        
        
b = showall()


def show():
    n = input("Enter name")
    if n in name:
        i = name.index(n)
        print('.'*50)
        print(f"| {name[i]} | {mark[i]} |".center(30, " "))
        print('.'*50)
    else:
        print("Name not exist")

a = show()
        

