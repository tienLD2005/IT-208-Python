#các thao. tác làm việc với file(read, write, close)
# cac thao tac doc file
file_path = "./ss05/demo.txt"

file = open(file_path, "r", encoding="utf-8") 
content = file.read()

print(f"COntent: {content}")

file.close()

create_file = open("./ss05/demo.md", 'w', encoding="utf-8")
create_file.write("Helo cac con vo cua a")

import csv

data = [
    ["name", "age", "city"],
    ["Tien", 20, "Hanoi"],
    ["Minh", 22, "Danang"]
]

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name","price"])
    writer.writerow(["1", "tien",1200])

