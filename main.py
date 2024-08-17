from item import Item

items = {}
total_quantity = 0
with open("input1.csv", "r") as file:
    for i, line in enumerate(file):
        if i == 0:
            continue
        else:
            cols = line.split(",")
            name = cols[0]
            quantity = int(cols[1].replace("\n", ''))
            total_quantity += quantity
            if name in items:
                items[name].add_quantity(quantity)
            else:
                item = Item(name)
                item.add_quantity(quantity)
                items[name] = item

quantity_per_item = {}
count_per_item = {}
max_per_item = {}
min_per_item = {}
avg_per_item = {}
median_per_item = {}

for item_name in items:
    item = items[item_name]
    quantity_per_item[item.name] = item.get_sum()
    count_per_item[item.name] = item.count()
    max_per_item[item.name] = item.get_max()
    min_per_item[item.name] = item.get_min()
    avg_per_item[item.name] = item.get_avg()
    median_per_item[item.name] = item.get_median()


print("Total quantity per item: ", quantity_per_item)
print("Count per item: ", count_per_item)
print("Median per item: ", median_per_item)
print("Max per item: ", max_per_item)
print("Min per item: ", min_per_item)
print("Avg per item: ", avg_per_item)
print("Total quantity of all items: ", total_quantity)


asc_sorted = sorted(items.items(), key=lambda x: x[1].get_min())
desc_sorted = sorted(items.items(), key=lambda x: x[1].get_max())

bottom_items = [(x[0], x[1].get_min()) for x in asc_sorted[0:5]]
top_items = [(x[0], x[1].get_max()) for x in asc_sorted[0:5]]

print("Top 5 quantities: ", top_items)
print("Bottom 5 quantities: ", bottom_items)

max_quantity = top_items[0][1]
start = 0
while (start < max_quantity):
    low, high = start, start+10
    groups = {}
    for item_name in items:
        item = items[item_name]
        quantities = item.get_quantities_between(low, high)
        if len(quantities) > 0:
            groups[item.name] = quantities
    print(f"Range {start+1}-{start+10}: ", groups)
    start += 10
