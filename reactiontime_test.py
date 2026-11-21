# 简单反应时实验：数据录入与初筛
# 运行时依次输入：被试编号、年龄、三次反应时(ms)

sub_id = input("被试编号：")
age = int(input("被试年龄："))
rt1 = float(input("第 1 次反应时(ms)："))
rt2 = float(input("第 2 次反应时(ms)："))
rt3 = float(input("第 3 次反应时(ms)："))

mean_rt = (rt1 + rt2 + rt3) / 3
range_rt = max(rt1, rt2, rt3) - min(rt1, rt2, rt3)
mean_rt_sec = mean_rt / 1000

is_valid = (18 <= age <= 35) and (200 <= mean_rt <= 1000) and (range_rt < 300)

print("========== 被试 " + sub_id + " 数据摘要 ==========")
print("平均反应时：" + str(mean_rt) + "ms")
print("反应时极差：" + str(range_rt) + "ms")
print("换算为秒  ：" + str(mean_rt_sec) + "s")
print("数据有效性：" + str(is_valid))
