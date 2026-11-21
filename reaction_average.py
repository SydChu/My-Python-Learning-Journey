times = 0         # 已录入次数
valid_count = 0   # 有效数据数量
total = 0         # 有效反应时的总和

while times < 6:
    reaction_time = float(input("请输入第" + str(times+1) + "次反应时（毫秒）"))
    times += 1    # 每次输入都计数，包括无效数据
    if reaction_time < 100 or reaction_time > 1500:
        print("本次数据无效，跳过统计")
        continue
    valid_count += 1
    total += reaction_time

print("有效数据数量"+str(valid_count))

if valid_count > 0:
    average = total / valid_count
    print("平均反应时:" + str(average) +"毫秒")
else:
    print("没有有效数据")
