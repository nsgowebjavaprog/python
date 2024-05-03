if __name__ == '__main__':
    dict={}
    s = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #2nd gtreatest marks/percent
        if score in dict:
            dict[score].append(name)
        else:
            dict[score]=[name]
            
        if score not in s:
            s.append(score)
            
    m=min(s)
    s.remove(m)
    m1 = min(s) 
    
    dict[m1].sort()
    for i in dict[m1]:
        print(i)
    