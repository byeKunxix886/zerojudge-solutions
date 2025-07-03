id_map = { 'A':10,'B':11,'C':12,'D':13,'E':14,
           'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,
           'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,
           'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,
           'X':30,'Y':31,'Z':33
}



sum_id = 0
identi = input()

# print(TO_NUM[A_B.index(identi[0])]) # x -> index -> y[index] -> y

num_firstletter = id_map[identi[0]]
#print(num_firstletter) #debug: 拿到正確的字母所對應的數字 OK
sum_id = (num_firstletter // 10) +  ((num_firstletter % 10) * 9) # /為精確商，小數點都會取，直到完全能得到被除數，商 = 被除數 ÷ 除數 。但通常我們要整數商//
# print(sum_id) #Debug: sum_id 計算正確 NO 

for i in range(1,len(identi)-1):
    # print(identi[i]) #Debug: 拿到正確的identi上的數字，且資料型態正確 OK
    sum_id += int(identi[i]) * (9 - i)


sum_id += int(identi[9])


if sum_id % 10 == 0:
    print("real")
else:
    print("fake")
