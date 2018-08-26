class QQ():
    def __openvip(self):
        print('开通成功')

    def checkqq(self,money):
        if money >= 10:
            self.__openvip()
        else:
            print('余额不足')


qq = QQ()
qq.checkqq(5)


qq1 = QQ()
qq1.checkqq(15)
        
