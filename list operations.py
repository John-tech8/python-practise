my_list=["p","e","r","m","i","t"]
print(f"Original List: {my_list}")
print(f"First Element: {my_list[0]}")
print(f"Last Element: {my_list[5]}")
print(f"First four  Elements: {my_list[0:4]}")
my_list[0:2]=["k","l"]
print(f" List after changing first  3 index : {my_list}")
my_list[3]="j"
print(f" List after changing  : {my_list}")
my_list.remove("i")
print(f" List after removing i  : {my_list}")
del my_list[4]
print(f" List after deleting t  : {my_list}")
