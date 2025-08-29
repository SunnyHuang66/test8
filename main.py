# 这是一个简单的Python程序，计算斐波那契数列并打印结果

def fibonacci(n):
    """生成斐波那契数列的前n个数字"""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    # 获取用户输入
    try:
        num_terms = int(input("请输入要生成的斐波那契数列项数: "))
        if num_terms <= 0:
            print("请输入一个正整数。")
            return
        
        # 生成并打印斐波那契数列
        result = fibonacci(num_terms)
        print(f"斐波那契数列的前{num_terms}项是:")
        print(result)
        
    except ValueError:
        print("输入无效，请输入一个整数。")

if __name__ == "__main__":
    main()