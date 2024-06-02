def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы
    if len(brackets_row)%2!=0:
        return False
    count_of_skobki=0

    for el in brackets_row:
        if el=='(':
            count_of_skobki+=1
        else:
            count_of_skobki -= 1
        if count_of_skobki<0:
            return False
    return count_of_skobki==0

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False


