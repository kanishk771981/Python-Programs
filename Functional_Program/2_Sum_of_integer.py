def zero_triplets(arr, Num):
    triplets = []
    count = 0

    for i in range(Num - 2):
        for j in range(i + 1, Num - 1):
            for k in range(j + 1, Num):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = list(sorted([arr[i], arr[j], arr[k]]))
                    if triplet not in triplets:
                        triplets.append(triplet)
                        count += 1
    return count, triplets

# Input handling
Num = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

# Calling the function
count, triplets = zero_triplets(arr, Num)

# Output
if count > 0:
    print(f"\nNumber of distinct triplets: {count}")
    print("Triplets are:")
    for triplet in triplets:
        print(triplet)
else:
    print("\nNo triplets found.")
