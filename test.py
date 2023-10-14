brands = []
with open("brands.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    brand = "".join(line.split("—")[0]).strip()
    print(brand)
    brands.append(brand)
