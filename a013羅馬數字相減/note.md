>Everyday Code
---


Q: 若用迴圈跑到某一位或最後一位會出錯怎辦？那就不要跑到那一位呀，略過它即可


**筆記**
*比大小時，要確定到底要比較什麼？是整數大小嗎或著是字元長度...，因為Python不會提醒你，有時會比較錯。


### String 方法
str*數，表示str重複出現數次


### 取相減的值、取差值 -> 直接取相減的絕對值(Absolute value)
可讀性好、語意明確。絕對值就是兩點差距，不管誰大誰小、沒有方向
x = abs(num1 - num2)  直接取絕對值


### 數值和羅馬字串 的一對一對應 -> 索引映射
rome_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
num_list  = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
因為羅馬數字本身沒有意義，必須去對應才有意義。

### 分組放羅馬數字處理 <-> 串列裡包子串列
two_rome_list = [ ]

while True:
    rome = input()
    if rome == '#':
        break
    else:
        rome = rome.split()
        two_rome_list.append(rome) #串列包n個兩羅馬數字的子串列











