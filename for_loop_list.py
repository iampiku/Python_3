# sum of all the elements of the list
def sum_elem():
    num_elem = int(input())
    prices = []
    prices.append(num_elem)
    sum = 0
    for items in prices :
        sum += items
    print(sum)

ob = sum_elem()