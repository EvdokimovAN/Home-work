def city(spisok):
    start = [0]*26
    end = [0]*26
    for city in spisok:
        s = city[0]
        e = city[-1]
        start[ord(s)-ord('a')]+=1
        end[ord(e)-ord('a')]+=1
    k = 0
    l = 0
    for i in range(26):
        if start[i] != end[i]:
            if start[i] == end[i] + 1:
                k += 1
            elif end[i] == start[i] + 1:
                l += 1
            else:
                return False 
    return (k == 0 and l == 0) or (k == 1 and l == 1)
cities1 = ["london", "newyork", "klin", "vienna"]  
cities2 = ["paris", "sydney", "york", "kyoto","gog"]  
cities3 = ["paris", "london", "moscow"] 
cities4 = ["a", "b", "c"]  

print(city(cities1)) 
print(city(cities2)) 
print(city(cities3))