#练习3-4
print("练习3-4")

names = ["魏依晨","马渃宣","马云峥"]

print(f"能和我一起吃晚餐吗,{names[1]}?")
print(f"能和我一起吃晚餐吗,{names[0]}?")
print(f"能和我一起吃晚餐吗,{names[2]}?")
#______________________________________________________________________________________________________________
#练习3-5
print("\n练习3-5")

print(f"{names[0]}无法赴约，需另邀请别人。")

names[0] = '李青雨'
print(f"魏依晨已替换为{names[0]}")

print(f"能和我一起吃晚餐吗,{names[1]}?")
print(f"能和我一起吃晚餐吗,{names[0]}?")
print(f"能和我一起吃晚餐吗,{names[2]}?")
#_______________________________________________________________________________________________________________
#练习3-6
print("\n练习3-6")

print("我找到了一个更大的餐桌，需再邀请3人。")

names.insert(0,'江含')
names.insert(4,'吴田依航')
names.insert(5,'刘哲瑞')

print(f'已添加{names[0]},{names[4]},{names[5]}。')

print(f"能和我一起吃晚餐吗,{names[1]}?")
print(f"能和我一起吃晚餐吗,{names[0]}?")
print(f"能和我一起吃晚餐吗,{names[2]}?")
print(f"能和我一起吃晚餐吗,{names[3]}?")
print(f"能和我一起吃晚餐吗,{names[4]}?")
print(f"能和我一起吃晚餐吗,{names[5]}?")
#______________________________________________________________________________________________________________
#练习3-7
print('\n练习3-7')

print(names)

print(f"对不起，由于餐桌不能及时送达，所以不能邀请你来了，{names[0]}。")
names_del = names.pop(0)

print(f"对不起，由于餐桌不能及时送达，所以不能邀请你来了，{names[2]}。")
names_del = names.pop(2)

print(f"对不起，由于餐桌不能及时送达，所以不能邀请你来了，{names[3]}。")
names_del = names.pop(3)

print(f"对不起，由于餐桌不能及时送达，所以不能邀请你来了，{names[1]}。")
names_del = names.pop(1)

print(f'你还在受邀人之列{names[4]}')
print(f"你还在受邀人之列{names[5]}")
