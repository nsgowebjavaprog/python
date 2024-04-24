# # dict={}
# # name=input('enter  the string: ')
# # print(dict)
#
# # dict={}
# #
# # name=input("enter the string : ")
# # print(name)
# # char=input("Enter the char: ")
# # print(name.count(char))
#
# # strart--->b,end-->i
#
# dict={'balaji':'sddfdf','banana':'asasa','mango':'sjshdsdh','bass':'sdhsuf'}
# print(dict)
# for key in dict.keys():
#     print(f'{key.startswith('b')}')
#     #  3-->True
#   #  print(key)
#    # print(key.endswith('i'))  # 1-->True
#
#
# user_dict = {}
#
# num_entries = int(input("Enter the number of entries you want to add: "))
#
# for i in range(num_entries):
# 	key = input("Enter key: ")
# 	value = input("Enter value: ")
# 	user_dict[key] = value
#
# print("Dictionary after adding user input:", user_dict)
#
# dict={'balaji':'50','banana':'30','mango':'20','bass':'10'}
#
# for key,value in dict.items():
#     if key[0].lower()=='b':
#         print(f"Thhe value of '{key}' is {value}")

# list=[1,2,3,4,5,6,7,8,9,-2,-4,-6,-8,-10]
#
# for i in list:
#   if i > 0:
#
#      print(sum)
#      sum += 1
#      i+=1
#
#   elif i<=0:
#
#      print(sum)
#      sum += 1
#      i += 1
#
#   else:
#
#      print(sum)
#      sum += 1
#      i+=1

#
# num=[1,2,3,4,-1,-3]
# neg = []
# even = []
# odd = []
#
# for i in num:
#     if (i < 0):
#         neg.append(i)
#         print(neg)
#     else:
#         if (i % 2 == 0):
#             even.append(i)
#             print(even)
#         else:
#             odd.append(i)
#             print(odd)


# pos=[a<=0 for a in num]
# even=[a%2==0 for a in num]
# print(num)
# print(neg)
# print(pos)
# print(even)

'''
num=[1,2,3,4,-1,-3]
neg = []
even = []
odd = []

for i in num:
    if (i < 0):
        neg.append(i)
        print('NEG_LIST=',neg)
    elif (i % 2 == 0):
        even.append(i)
        print(even)
        print('NEG_LIST=', even)
    else:
        odd.append(i)
        print('NEG_LIST=', odd)
'''

# list=[1,23,54,67,-34,-23]
#
# neg_sum=[]
# pos_sum=[]
# even_sum=[]
#
# neg_list=(i for i in list if i<0)
# neg_sum.append(i)
# pos_list=(j for j in list if j>0)
# pos_sum.append(j)
# even_list=(k for k in list if k%2==0)
# even_sum.append(  k)
#
# print(neg_sum)
# print(pos_sum)
# print(even_sum)
# ip=bitm college's located in ballari? Is't right!!!
# ou=thgi rtsIira'l labnide ta colsege? ll'o cmtib!!!
#
# special char are same position don't change an dsame string '

                                                                                # LiNKED LIST
# Create a NODE

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Insertion
def Insertion_At_Begin(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node

# Insertion @ SPECIFIC position

def Insertion_At_Index(self, data, index):
    new_node = Node(data)
    current_node = self.head
    position = 0

    if position == index:
        self.Insertion_At_Begin(data)

    else:
        while (current_node != None and position+1 != index):
            position = position +1
            current_node = current_node.next

        if current_node != None:

            new_node.next = current_node.next
            current_node.next = new_node

        else:
            print("Index not present")

# 4.Insertion At End

def Insert_At_End(self,data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    current_node = self.head
    while(current_node.next):
        current_node = current_node.next

    current_node.next = new_node

# DELETE NODE

def remove_first_node(self):
    if (self.head == None):
        return

    self.head = self.head.next


# REMOVE LAST NODE

def remove_last_node(self):
    if self.head is None:
        return

    current_node = self.head
    while (current_node.next.next):
        current_node = current_node.next

    current_node.next = None


# Method to remove at given index
def remove_at_index(self, index):
    if self.head == None:
        return

    current_node = self.head
    position = 0
    if position == index:
        self.remove_first_node()
    else:
        while (current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")


# Linked List Traversal in Python

def printLL(self):
    current_node = self.head
    while(current_node):
        print(current_node.data)
        current_node = current_node.next





















