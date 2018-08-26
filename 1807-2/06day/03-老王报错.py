class showError(Exception):
    def __init__(self,name):
        self.name = name 
        #self.name1 != '老王'
class InputManger():
    def my_input(self):
        self.name = input('请输入姓名:')
        try:
            if self.name == '老王':
                raise showError(self.name)
        except showError as ret:
            print('不能输入%s'%ret.name)


im = InputManger()
im.my_input()
