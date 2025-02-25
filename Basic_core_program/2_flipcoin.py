import random

def flip_coin(num_flips):
    if num_flips <= 0:
        print("Please enter a positive integer for the number of flips.")
        return

    

    heads = 0
    tails = 0

    for _ in range(num_flips):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    head_percentage = (heads / num_flips) * 100
    tail_percentage = (tails / num_flips) * 100
    print(f"Flips: {num_flips}")
    print(f"Heads: {heads} ({head_percentage:}%)")
    print(f"Tails: {tails} ({tail_percentage:}%)")

    


num_flips = int(input("number of times coin is fliped"))
 
flip_coin(num_flips)
