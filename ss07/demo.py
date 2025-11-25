import pandas as pd
# Series
#Thao tac khoi tao tu list
myList = [10,20,30,40,50]
serires = pd.Series(myList)

print(f"{serires}")

#Tạo series với chỉ số tuỳ chỉnh
seriresCustomIndex = pd.Series(myList, index=['a', 'b', 'c', 'd', 'e'])
print(f"{seriresCustomIndex}")

#Khởi tạo series từ dictionary
seriesDictionary = pd.Series({
    'name':'Le Dien Tien',
    'gender': 'Nam'
})
print(f"Serires vowis dictionary:\n {seriesDictionary}")

# 1.Lay giu lieu. thong qua vi tri
print(f"Gia tri tai vi tri 1 trong list: {serires[0]}")
print(f"Gia tri tai vi tri 1 trong list: {seriresCustomIndex['b']}")

# 2.Thao tác thêm phần tử vào trong series
seriresCustomIndex['t'] = 2005
print(f"{seriresCustomIndex}")

#3. thao tac cap nhat phan tu
seriresCustomIndex['t'] = 2009
print(f"{seriresCustomIndex}")

#4. Xoá phần tử
del(seriresCustomIndex['t'])
print(f"{seriresCustomIndex}")

# XỬ lý dữ liệu thiếu 
s = pd.Series([2,3,4,5,3])