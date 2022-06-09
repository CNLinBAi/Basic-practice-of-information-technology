students = []  # 存储所有学生的列表（实际项目，数据存储到数据库中）
# 根据学号查询学生是否存在
def is_exists(sid):
    for student_dict in students:
        stu_id = student_dict.get("stu_id")   # 通过字典的key，获取对应的value(学号)
        if sid == stu_id:   # 如果查到了，返回True
            return True
    return False   # 如果系统没有查询到，则返回False
# 添加学生的函数
def add_student(sid,name,score):
    # 添加学生之前先检查是否存在该生（根据学号查询）
    is_have = is_exists(sid)
    if is_have:
        return False  # 如果已经存在该生，则添加失败，返回False

    # 创建新生字典
    new_student = {
        "stu_id":sid,
        "stu_name":name,
        "stu_score":score
    }
    students.append(new_student)  # 添加新生字典到学生列表容器中
    return True
def delete_student(new_sid):

    for i in students:
        if i['stu_id'] == new_sid:
            students.remove(i)
            return True

    return False

def find_student(new_sid):
    for i in students:
        if i['stu_id'] == new_sid:
            print("学号为" ,i['stu_id'])
            print("姓名为", i['stu_name'])
            print("成绩为", i['stu_score'])
            return True
    return False




# 查询所有学生信息
def showAll():
    for student_dict in students:
        print(student_dict.get("stu_id"),student_dict.get("stu_name"),student_dict.get("stu_score"))


if __name__ == '__main__':   # 只有直接执行当前文件，__name__变量的值才是'__main__'（防止其他文件导入时执行下面的代码）
    while True:
        # input()函数阻塞执行，等待键盘输入，输入的内容会作为字符串返回
        choice = input("1 添加新生 2 删除学生 3 查询某个学生 4 查询所有学生 5 退出系统")
        if choice == "1":
            new_sid = input("请输入新生学号：")
            new_name = input("请输入新生姓名：")
            new_score = float(input("请输入新生成绩："))   # 如果输入的是非数字，则float()函数转换会出错
            is_success = add_student(new_sid,new_name,new_score)  # 调用添加学生方法
            if is_success:
                print("新生添加成功~~~~")
            else:
                print("系统已经存在该生，添加失败！")
        elif choice == "2":
            new_sid = input("请输入新生学号：")
            is_success = delete_student(new_sid)
            if is_success:
                print("学生删除成功~~~~")
            else:
                print("不存在该学生")
        elif choice == "3":
            new_sid = input("请输入新生学号：")
            is_success = find_student(new_sid)
            if is_success:
                print("查询完毕1")
            else:
                print("不存在该学生")
        elif choice == "4":
            print("学号：\t姓名：\t成绩：\t")
            showAll()
        elif choice == "5":
            break
        else:
            print("选择错误，请重新选择")