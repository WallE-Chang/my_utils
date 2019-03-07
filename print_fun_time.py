# -*- coding: utf-8 -*-
# @Author: wanli
# @Date:   2019-03-07 18:03:00
# @Last Modified by:   wanli
# @Last Modified time: 2019-03-07 18:05:50


def print_func_time(func):
    from line_profiler import LineProfiler
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        lp = LineProfiler()
        lp_wrapper = lp(func)
        result=lp_wrapper(*args, **kwargs)
        lp.print_stats()
        return result
    return wrapper  # 返回


if __name__ == '__main__':

    @print_func_time                  ## 把修饰器加到你的函数上面，每次调用函数都会打印时间
    def is_addable(l, t):
        for i, n in enumerate(l):
            for m in l[i:]:
                if n + m == t:
                    return True
        return False


    assert is_addable(range(20), 25) == True