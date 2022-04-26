import time

print("hello would")
print("你的名字是什么？（what is your name）")
myname = input()
print("很高兴见到你，（it is good to meet you,）" + myname)
print("你名字里的字数是：（the length of your name is:）")
print(len(myname))
print("你的年龄是什么？（what is your age）")
age = input()
print("你会在一年里长到 "+str(int(age) + 1)+"岁。 ")
print("（your will be " + str(int(age) + 1) + " in a year.）")
time.sleep(5)
