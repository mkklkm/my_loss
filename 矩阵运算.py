def matrix_multiply(A, B):
    # 这里是你写的那个三层循环函数
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("错误：左矩阵的列数必须等于右矩阵的行数！")
        return None

    # 初始化结果矩阵
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # 你的核心逻辑（把那个下标坑填好！）
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]  # 注意这里的下标！
    return result


if __name__ == "__main__":
    # 1. 在这里手动定义数据（测试用例）
    matrix_a = [
        [1, 2],
        [3, 4]
    ]
    matrix_b = [
        [5, 6],
        [7, 8]
    ]

    # 2. 调用你的函数
    print("正在计算矩阵相乘...")
    output = matrix_multiply(matrix_a, matrix_b)

    # 3. 打印结果，看看对不对
    # 应该是 [[19, 22], [43, 50]]
    if output:
        for row in output:
            print(row)