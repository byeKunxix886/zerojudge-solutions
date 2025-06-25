#矩陣的翻轉(轉置矩陣程式)
#何坤璋

while True:
    try:
        two_num = input().split() 

        matrix = []

        # 將矩陣看作多個向量組成，每個 row 是一個向量
        for i in range(int(two_num[0])): 
            vector = list(map(int,input().split())) # 把一列變成向量
            matrix.append(vector) # 把這列加進矩陣中
        

        n = len(matrix) 
        m = len(matrix[0]) 

        #原矩陣為n * m n列m行 故 轉置矩陣為m*n m列n行
        #建立一個「共有 m 列（外層），每列有 n 個元素（內層）」的二維 list，也就是矩陣！
        B = [[0 for _ in range(n)] for _ in range(m)] #建立一個空矩陣的方法

        '''
        B = []
        for _ in range(m):             # 建立 m 個 row
            inner_list = []
            for _ in range(n):         # 每個 row 裡放 n 個 0
                inner_list.append(0)
            B.append(inner_list)
        '''

        #由於前面有建立空矩陣，故這裡可以直接去交換兩矩陣的值
        for i in range(n):
            for j in range(m):
                B[j][i] = matrix[i][j]


        #格式化一列一列輸出
        for _ in B:
            print(" ".join((map(str,_))))

    except:
        break
