A_B = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
TO_NUM = [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
    
sum_id = 0
identi = input()

# print(TO_NUM[A_B.index(identi[0])]) # x -> index -> y[index] -> y

num_firstletter = TO_NUM[A_B.index(identi[0])]
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
