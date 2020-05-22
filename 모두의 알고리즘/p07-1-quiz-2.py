"""
입력:
    학생 번호 number
출력:
    학생 이름 student_name
"""


def search_student(number):
    """
    :param number: 학생 번호
    :return:
    """

    student_number_list = [39, 14, 67, 105]
    student_name_list = ["Justin", "John", "Mike", "Summer"]

    n = len(student_name_list)

    for i in range(0, n):
        if student_number_list[i] == number:
            return student_name_list[i]

    return "?"


print(search_student(39))
print(search_student(42))
print(search_student(14))