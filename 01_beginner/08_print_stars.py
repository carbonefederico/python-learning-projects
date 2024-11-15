def square (size):
    line = ""
    for i in range (0,size):
        line+="#"

    for j in range (0,size):
        print (line)

def list_of_stars (list):
    for element in list:
        current_row = ""
        for j in range (element):
            current_row += "*"
        print (current_row)

list_of_stars ([4,4,4,4])

