"""a = 10
print(a)
type(a)
id(a)
print(a,type(a),id(a))"""

"""a = 10
b = 20 
c = a+b 
print(a,type(a),id(a))
print(b,type(b),id(b))"""

#binary data
# a = 0b1001
# print(a,type,(a))
# a = 0b1111
# print(a,type,(a))
# a = 0B10000
# print(a,type,(a))

#octel data
"""a = 0o17
print(a,type,(a))
a = 0o14
print(a,tuple,(a))
a = 0o123
print(a,type,(a))"""

#hexa decimal data
"""a = 0xac
print(a,type,(a))
a = 0xBEE
print(a,type,(a))
a = 0x1B
print(a,type,(a))"""

#varname=bin

"""a = 10
print(a)
b = bin(a)
print(b)

a = 0o12
b = bin(a)
print(b)

a = 0xf
b = bin(a)
print(b)"""


#varname=oct
"""a = 15 
b = oct(a)
print(b)

a = 0b1110
b = oct(a)
print(b)

a = 0xd
b = oct(a)
print(b)"""

#vername=hexa
"""a = 15
b = hex(a)
print(b)

a = 0b1110
b = hex(a)
print(b)

a = 0o123
b = hex(a)
print(b)"""

#float data type
"""a = 1.2
print(a, type,(a))

a = 2.2
b = 2.3
c = a+b
print(a,type,(a))
print(b,type,(b))
print(c,type,(c))

a = 2 
b = 2.5
c = a+b
print(a,type,(a))
print(b,type,(b))
print(c,type,(c))

a = 3e2
print(a,type,(a))
b = 10e2
print(b,type,(b))"""

#bool data type
"""a = True
b = False
print(a,type,(a))
print(b,type,(b))

a = True
b = False
c = a+b
print(c,type,(c))
print(2+True-False)
print(2+True*4)

print(0b1111-True)
print(0xf+True)
print(0o7+True)

print(True/True)
print(False/True)"""

#complex data type
"""a = 2+3j
print(a,type,(a))
b = -2.3-5j
print(b,type,(b))
c = -1.5-4.5j
print(c,type,(c))
d = 3j
print(d,type,(d))
e = 3.5j
print(e,type(e))"""


# #singl line and multi line string data
# s1="python"
# print(s1,type,(s1))
# s2='python'
# print(s2,type(s2))
# s3="A"
# print(s3,type,(s3))
# s4='A'
# print(s4,type,(s4))
# s5="12345"
# print(s5,type,(s5))
# s6='12345'
# print(s6,type,(s6))
# s7="123_abc"
# print(s7,type,(s7))
# s8='123_abc'
# print(s8,type,(s8))
# addr1="""guid van rossum FNO:3-4,hill side python softwar foundation nther lands -56
# print(addr1,type,(addr1))"""
# s1="""python programming"""
# print(s1,type,(s1))
# s2='''python programming'''
# print(s2,type,(s2))
# s3="""A"""
# print(s3,type,(s3))
# s4='''A'''
# print(s4,type,(s4))

# lst1=[10, 20, 30, 12.34, 10, 20, -45, 67]
# print(lst1, type(lst1))
# len(lst1)
# lst2 = [100, "Rossum", 45.67, 2 + 3j, True]    
# print(lst2, type(lst2), id(lst2))
# print(lst2[1], type(lst2[1]))
# len(lst2)
# print(lst2[-5], type(lst2[-5]))

# lst2 = [100, "Rossum", 45.67, 2 + 3j, True]
# print(lst2, type(lst2), id(lst2))
# lst2[0]=5555  #index based update
# print(lst2[0], type(lst2[0]))
# lst2[1:3]  #slice based update
# print(lst2[1:3], type(lst2[1:3]))   
# lst2[1] = ["Guido", 99.88]  #list based update
# print(lst2, type(lst2), id(lst2))

# lst=[10,'ROSSUM',[30,35,25],[70,65,60],'JNTU']
# print(lst, type(lst), id(lst))
# for val in lst:
#     print(val,"--->", type(val),"--->",type(lst))

# print(lst,type(lst))
# lst[2].append(38)
# print(lst, type(lst))

# lst[2].append(38)
# lst[2].append(58)
# lst[-2].insert(1,58)
# lst[2].insert(1,58)
# lst[-2][::3]
# lst[2].append(35)
# lst[2]+lst[3]
# lst[2].extend(lst[3])
# lst.insert(-1,lst[2]+lst[3])
# lst[2].extend(lst[3])
# lst[-2].pop()
# lst[2].remove(35)
# del lst[2:4]
# lst.append(100)
# lst.insert(-1,[10,30,50])
# print(lst, type(lst), id(lst))

# lst=[100,"RS",[18,19,17],[67,80,76], "JNTU"]
# for val in lst:
#     print(val, "--->", type(val), "--->",type(lst))
#     lst[2]
#     print(lst[2], type(lst[2]))
#     lst[-3]
#     print(lst[-3], type(lst[-3]))
#     lst[3]
#     print(lst[3], type(lst[3]))
#     lst[-2]
#     print(lst[-2], type(lst[-2]))
#     lst[2][-2]
#     print(lst[2][-2], type(lst[2][-2]))
#     lst[-3][1]
#     print(lst[-3][1], type(lst[-3][1]))
#     lst[-3][-2]
#     print(lst[-3][-2], type(lst[-3][-2]))
#     lst[3][1]
#     print(lst[3][1], type(lst[3][1]))


# lst=[100,'RS',[18,19,17],[67,80,76], 'JNTU']
# print(lst)
# lst[2].append(15)
# print(lst, type(lst))   
# lst[-2].insert(1,72)
# print(lst, type(lst))
# lst[-3].sort()
# print(lst, type(lst))
# lst[-2].sort(reverse=True)
# print(lst, type(lst))
# lst.append([1.2, 3.4, 5.6])
# print(lst, type(lst))
# lst[-1].clear()
# print(lst, type(lst))
# del lst[-1]
# print(lst, type(lst))
# lst.remove([15,17,18,19])
# print(lst, type(lst))
# del lst[2][3]
# print(lst, type(lst))

# lst=[[[10,20,30],[40,50,60],[70,80,90],[1,2,3],[4,5,6],[6,7,8]]]
# print(lst, type(lst), id(lst))
# for val in lst:
#     print(val)
    
#     for matrix in lst:
#         print(matrix)
        
#         for row in matrix:
#             print(row)
#             print(row[0], type(row[0]))
#             print(row[1], type(row[1]))
#             print(row[2], type(row[2]))
#             print(row[-1], type(row[-1]))

# lst=[[[10,20,30],[40,50,60],[70,80,90],]]
# print(lst, type(lst), id(lst))

# a = True
# b = False
# c = a+b
# print(c,type(c))
# print(2+True-False)
# print(2+True*4)
    





