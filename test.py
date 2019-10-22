with open('csv_src/Basic.txt', 'r') as f:
    basic_list = list()
    for basic in f.readlines()[1:]:
        basic_list.append(int(basic.rstrip()))

    total_basic_revenue = sum(basic_list) * 5

print(basic_list)
print(total_basic_revenue)