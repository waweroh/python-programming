tree_height = input("how many tall: ")
tree_height = int(tree_height)
spaces = tree_height - 1 
hashes = 1
#stump_spaces = tree_height - 1
for i in range(spaces):
    print(" ", end='')
 
    for i in range(hashes):
        print("#", end='')

    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
print("#")


#for i in range(stump_spaces):
 #   print(' ', end='')


