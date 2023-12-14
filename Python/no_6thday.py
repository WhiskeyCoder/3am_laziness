with open('duplicates.txt', 'r') as file:
    data = file.read()
    data_list = data.split('\n')
    unique_list = list(set(data_list))
    unique_data = "\n".join(unique_list)
with open('unique.txt', 'w') as file:
    file.write(unique_data)
