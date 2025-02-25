import random

#function for generating random number
def random_coupon(n):
    return random.randint(1,n)

#Collects coupon numbers and counts random numbers needed.
def distinct_coupon(n):
    collected_coupons = set()
    random_num =0

    while len(collected_coupons) < n:
        new_coupon = random_coupon(n)
        random_num +=1

        if new_coupon not in collected_coupons:
            collected_coupons.add(new_coupon)

    return random_num ,collected_coupons


Num  = int(input("enter number of distinct  coupon number"))

print(f"Number of coupons needed is{Num}")
total_random_number, coupons = distinct_coupon(Num)


print(f"random number generated is {total_random_number}")
print(f"coupon numbers generated : {list(coupons)}")




