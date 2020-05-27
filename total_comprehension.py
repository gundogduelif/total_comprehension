# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]

print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")


maplist = [n * 100 for n in my_numbers]

print("--------------") 
print("MAPPED LIST:", maplist)

greater_than_three = [n for n in my_numbers if n > 3]

print("--------------") 
print("FILTERED LIST W/ MATCHES:", greater_than_three)

greater_than_eight = [n for n in my_numbers if n > 8]

print("--------------") 
print("FILTERED LIST W/O MATCHES:", greater_than_eight)

mapped_filtered = [ n * 100 for n in my_numbers if n > 3 ]

print("--------------") 
print("MAPPED AND FILTERED LIST:", mapped_filtered)


# --------------
# ORIGINAL LIST: [1, 2, 3, 4, 5, 6, 7]
# --------------
# TOTAL COMPREHENSION...
# --------------
# MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
# --------------
# FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
# --------------
# FILTERED LIST W/O MATCHES: []
# --------------
# MAPPED AND FILTERED LIST: [400, 500, 600, 700]