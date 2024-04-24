from string import punctuation
string="bitm college's located in ballari? Is't right!!!"
print(string[::-1])
# special char & space not change the position
space_special_chars=(i for i in string if i==" " or i==punctuation)
print(space_special_chars)
print(string)
