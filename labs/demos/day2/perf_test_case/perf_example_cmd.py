import sys

@profile
def my_func_t(n):
    a = [1] * (10 ** 6) * n
    b = [2] * (2 * 10 ** 7) * n
    del b
    return a
#@profile
def my_func_y(n):
    a = [1] * (10 ** 6) * n
    b = [2] * (2 * 10 ** 7) * n
    del b
    return a

if __name__ == '__main__':
	num = int(sys.argv[1]) # stand for first argument 
	my_func_t(num)
	my_func_y(num)