
# a generator that yields items instead of returning a list
import sys

@profile
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

#sum_of_first_n = sum(firstn(100000000))


if __name__ == '__main__':
	num = int(sys.argv[1]) # stand for first argument 
	firstn_generator(num)