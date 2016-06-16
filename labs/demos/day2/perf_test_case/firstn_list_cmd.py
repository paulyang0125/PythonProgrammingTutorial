
# Build and return a list
import sys

@profile
def firstn_list(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

#sum_of_first_n = sum(firstn(100000000))



if __name__ == '__main__':
	num = int(sys.argv[1]) # stand for first argument 
	firstn_list(num)


