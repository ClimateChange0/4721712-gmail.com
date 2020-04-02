import random
secret = random.randint(1,100)
print("---------geam------------")
temp = input("来猜一猜我心里的数字1-100之间：")
guess = int(temp)
if guess == secret:
        print("我艹,你猜中了")
        print("猜中了也没什么！")
else:
    if guess > secret:
        print("大了大了")
    else:
        print("小了小了")
while guess != secret:
    temp = input("猜错了在重新猜一次吧：")
    guess = int(temp)
    if guess == secret:
        print("我艹,你猜中了")
        print("猜中了也没什么！")
    else:
        if guess > secret:
            print("大了大了")
        else:
            print("小了小了")
print("geam over")
