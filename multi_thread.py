import threading


class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
'''

"""测试函数，计算两个数之和"""
def fun(a,b):
    time.sleep(1)
    return a+b
li = []
for i in range(4):
    t = MyThread(fun,args=(i,i+1))
    li.append(t)
    t.start()
for t in li:
    t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
    print (t.get_result())
'''
