lst = []
all_num_list = []
for i in range(28): lst.append(int(input()))
for i in range(30): all_num_list.append(i+1)
diff = list(set(all_num_list) - set(lst))
diff.sort()
print(diff[0])
print(diff[1])
