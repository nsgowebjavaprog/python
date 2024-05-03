def minion_game(string):
    # your code goes here
    s=len(string)
    con,vow=0,0
    
    for i in range(s):
        if string[i] in 'AEIOU':
            vow = vow+(s-i)
        else:
            con=con+(s-i)
    if con>vow:        
        print('Stuart {}'. format(con))  
    elif con == vow:
        print("Draw")
         
    else:
        print('Kevin {}'. format (vow))       
 
if __name__ == '__main__':
    s = input()
    minion_game(s)