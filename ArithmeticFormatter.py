def arithmetic_arranger(problems, show_answers=False):
    #初始化解答四行
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []
    
    #確認problems是否大於5個
    if len(problems) > 5:
        return'Error: Too many problems.'
    
    #迴圈problems以分解
    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts[0], parts[1], parts[2]
        #驗證運算符號
        if operator not in ['+' , '-']:
            return"Error: Operator must be '+' or '-'."
        #驗證第0位和第2位是否為數字
        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        #驗證第0位和第2位是否超過四位數
        if len(operand1) >4 or len(operand2)>4:
            return'Error: Numbers cannot be more than four digits.'
    
        #計算每個算式的寬度
        width= max(len(operand1), len(operand2))+2

        #建構最終輸出的前3行並向右對齊
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width-1))
        dashes_line.append("-"*width)
    
         # 如果需要顯示答案，計算並加入
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers_line.append(answer.rjust(width))
    # 將各行組合成輸出
    
    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes_line)
    
     
    # 如果需要顯示答案，添加答案行
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers_line)
    
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
