'''import json
#2
class User:

    def __init__(self,name,age):
        self.name=name
        self.age=age

user = User('Max',21)

def encoder_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of type is not JSON serializable')

userJSON = json.dumps(user,dufault=encoder_user)
print(userJSON)'''

# 1
# student={'name':'coder','age':21,'city':'bijapur','has_college':False,'titles':['coder','programmer']}
#
# studentJSON = json.dumps(student, indent=4,sort_keys=True)
# print(studentJSON)
#
# # store in file
# # with open('FREE_JSON_EXAMPLE.txt','w') as file:
# #     json.dump(student,file)

