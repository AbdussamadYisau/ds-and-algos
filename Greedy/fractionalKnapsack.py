# Uses python3
import sys
from time import time

def get_optimal_value(capacity, weights, values):
    #value = 0.
    # write your code here
    value_weights =  zip(values, weights)
    weights_value_dict = {w:v for v,w in value_weights}
    units = [weights_value_dict[w]/w for w in weights_value_dict]
    units_weights =  zip(units, weights)
    units_weights_dict = {u:w for u,w in units_weights}
    units = sorted(units, reverse=True)
    knapsack = []
    value_sum = []
    i = 0
    v = 0
    check = 0


    while True:
        if sum(knapsack) == capacity:
            return(sum(value_sum))

        if units_weights_dict[units[i]] <= capacity:
            knapsack.append(units_weights_dict[units[i]])
            value_sum.append(weights_value_dict[units_weights_dict[units[i]]])
            i += 1

        if units_weights_dict[units[i]] > capacity:
            v += units[i]
            check += 1
            if check == capacity:
                return(v)

            
    #return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    #t0 = time()
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    #print(time()-t0)