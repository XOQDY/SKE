x = int(input())
dic = {}
dic2 = {}
for i in range(x):
    itim, price = input().split()
    dic[itim] = int(price)
y = int(input())
for i in range(y):
    itim, price = input().split()
    if itim in dic:
        if itim not in dic2:
            dic2[itim] = dic[itim] * int(price)
        elif itim in dic:
            dic2[itim] += dic[itim] * int(price)
if dic2 == {}:
    print("No ice cream sales")
else:
    sales = sum(dic2.values())
    top_sale = max(dic2.values())
    list_top_sale = []
    for i in dic2:
        if dic2[i] == top_sale:
            list_top_sale.append(i)
    list_top_sale.sort()
    list_top_sale_str = ', '.join([str(elem) for elem in list_top_sale])
    print(f"Total ice cream sales: {sales:.1f}")
    print(f"Top sales: {list_top_sale_str}")