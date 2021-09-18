string = "ABABBAABAA"
LCP = [0]

arr = [string[i:] for i in range(len(string))]
arr = sorted(arr)

print("Sorted Sufix Array:",arr,sep="\n")

for i in range(len(arr)-1):
    count = 0
    for j in range(len(arr[i])):
        if arr[i][j] == arr[i+1][j]:
            count+=1
        else:
            break
    LCP.append(count)

print("\nLongest Common Prefix Array:",LCP,sep="\n")

max_val = max(LCP)
longest_indexes = [i for i,x in enumerate(LCP) if x==max_val]
my_subs = [arr[i-1] for i in longest_indexes]
subs = [my_subs[i][:max_val] for i in range(len(my_subs))] 

print("\nMy longest substring interval is:", *subs)
