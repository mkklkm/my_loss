def calculate_my_loss(real_values, my_status):
    """
    计算你人生的均方误差 (MSE)
    real_values: 理想中的目标列表
    my_status:   你现在的垃圾表现列表
    """
    if len(real_values) != len(my_status):
        return "连列表长度都不一样，你的人生逻辑已经彻底崩了。"

    n = len(real_values)
    total_error = 0

    for i in range(n):
        # 算出每一项的差距并平方（平方是为了消除负号，并放大严重的偏差）
        error = (real_values[i] - my_status[i]) ** 2
        total_error += error

    mse = total_error / n
    return mse


# 案例测试：
# 假设理想状态是 [10, 10, 10] (满分努力)
# 你现在的状态是 [1, 0, 2] (11点起床, 刷抖音, 撸管)
targets = [10, 10, 10]
me_now = [1, 0, 2]

loss = calculate_my_loss(targets, me_now)
print(f"你目前的 Loss (损失值) 是: {loss}")
print("I'm a loser.")