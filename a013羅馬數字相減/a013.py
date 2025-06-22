#羅馬數字相減

#function羅馬數字轉阿拉伯數字
def rome_to_number(str1):
    number = 0

    rome_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1] #一對一
    num_list = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    
   
    for i in range(len(str1)-1): #從開頭到字串的倒數第二位
            #rome_list[num_list.index(str1[i])]) #先看str1目前的元素是什麼，對應到該羅馬數字list中的那個
            #因為羅馬數字上的代表著位置，即羅馬數字的list是map，去對應阿拉伯數字
        current = rome_list[num_list.index(str1[i])]
        nextone = rome_list[num_list.index(str1[i + 1])]
        
        if nextone <= current:
            number += current
        else:
            number -= current
        

    number += rome_list[num_list.index(str1[len(str1)-1])] #必須手動加上最後一位，或著每一次判斷現在是否是最後一位，因為我設定讓i不跑到最後一位，以免現在位的元素值沒人可以比
    return number


#function阿拉伯數字轉羅馬數字
def number_to_rome(num1):
    ans_strlist = []

    coins = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    rome = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    for coin in coins:
        if num1 >= coin:
            count = num1 // coin
            ans_strlist.append(count * rome[coins.index(coin)])
            num1 %= coin



    return "".join(ans_strlist)


two_rome_list = [ ]

#分組放羅馬數字
while True:
    rome = input()
    if rome == '#':
        break
    else:
        rome = rome.split()
        two_rome_list.append(rome) #串列包n個兩羅馬數字的子串列


ans = 0
#羅馬數字相減
#一組一組access，然後用函數去相減

for s in two_rome_list:
    num1 = rome_to_number(s[0])
    num2 = rome_to_number(s[1])

    ans = abs(num1 - num2)  # 直接取絕對值，不用比較大小

    if ans != 0:
        print(number_to_rome(ans))
    else:
        print('ZERO')


