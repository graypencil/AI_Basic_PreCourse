line_counter = 0
data_header = []
employee = []
customer_USA_only_list = []
customer = None

with open("customers.csv", "r") as customer_data:

    while True:
        data = customer_data.readline()
        if not data: 
            break
        if line_counter == 0:
            data_header = data.split(",")
        else: 
            customer = data.split(",")
            if customer[10].upper() == "USA":
                customer_USA_only_list.append(customer)
        line_counter += 1

print("Header :\t", data_header)

for i in range(0,10):
    print("Data",i,":\t\t", customer_USA_only_list[i])
print(len(customer_USA_only_list))