lst = ["33%", "98.1%", "56.44%", "100%"]

def convert_to_decimal(lst):
     lst1 = []
     for item in lst:
          lst1.append(float((item.strip("%")))/100)
     print(lst1)




convert_to_decimal(lst)