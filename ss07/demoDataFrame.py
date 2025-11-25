import pandas as pd
#Khởi tạo dataFrame
userData = {'name': ['Nguyen van a', 'Le Dien T'],
            'age' : [10,20],
            'address': ['Hn', 'TN']
            }
#In ra du lieu
data = pd.DataFrame(userData)
print(data)

#Truy cap vao 1 cot
print(f"COt name trong data:\n {data['name']}")

print()