# def upper_case(string):
#     assert type(string)==str, f"The value {string} passed is not a string"
#     if isinstance(string,str):
#         sting_list = []
#         for i in string:
#             up = i.upper()
#             sting_list.append(up)
#         for i in sting_list:
#             st    

s=input("Input lowercased string:" )
a=list((map(str.upper,s)))
for i in a:
    print(i,end="")
