products = {
    "A": 120,
    "B": 80,
    "C": 300
}

items_list = list(products.items())

def get_price(item):
    print(f"Python gọi get_price({item}) → {item[1]}")
    return item[1]

print("Bắt đầu gọi sorted...\n")
sorted_list = sorted(items_list, key=get_price)

print("\nKết quả sau khi sắp xếp:")
print(sorted_list)
