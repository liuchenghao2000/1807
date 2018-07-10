list = []#装商品list = [["卫龙",5]]


while True:
    number = int(input("1-添加 2-删除 3--修改 3---退出"))
    if number == 1:
        l = []
        #添加商品
        #商品价格
        name = input("请输入商品名字")
        price = float(input("请输入商品价格"))
        l.append(name)
        l.append(price)
        
        list.append(l)  
        print(list)
    elif number == 3:
        break

