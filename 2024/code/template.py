with open('../data/template_data.txt', 'r') as file:
    data = [[character for character in line.strip()] for line in file]
    
print(data)