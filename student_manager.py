"""
@File       :   student_manager.py
@Time       :   2020/8/5 16:30
@Author     :   Wang
@Version    :   2.01
@Description:   控制台操作学生信息的CRUD-数据库版
"""
import pymysql


def add_stu(cursor):
    name = input("请输入学生姓名:")
    sex = input("请输入学生性别:")
    age = input("请输入学生年龄:")
    salary = input("请输入学生薪资:")
    advice = input("请输入学生建议:")
    cursor.execute("insert into t_student values (null, %s, %s, %s, %s, %s)",
                   (name, sex, int(age), float(salary), advice))
    cursor.connection.commit()
    if cursor.rowcount:
        print(f"新增学生信息成功")
    else:
        print(f"新增学生信息失败")


def delete_stu(cursor):
    sid = input("请输入需要删除信息的学生ID:")
    cursor.execute("delete from t_student where sid = %s", (int(sid),))
    cursor.connection.commit()
    if cursor.rowcount:
        print(f"删除学生信息成功")
    else:
        print(f"删除学生信息失败,不存在ID为{sid}的学生信息")


def update_stu(cursor):
    sid = input("请输入需要更新信息的学生ID:")
    cursor.execute("select * from t_student where sid = %s", (int(sid),))
    if not cursor.rowcount:
        print(f"更新学生信息失败,不存在ID为{sid}的学生信息")
    else:
        name = input("请输入学生姓名:")
        sex = input("请输入学生性别:")
        age = input("请输入学生年龄:")
        salary = input("请输入学生薪资:")
        advice = input("请输入学生建议:")
        cursor.execute("update t_student set name = %s, sex = %s, age = %s"
                       ", salary = %s, advice = %s where sid = %s",
                       (name, sex, int(age), float(salary), advice, int(sid)))
        cursor.connection.commit()
        if cursor.rowcount:
            print(f"更新学生信息成功")
        else:
            print(f"更新学生信息失败")


def retrieve_stu(cursor):
    sid = input("请输入需要查找信息学生ID:")
    cursor.execute("select * from t_student where sid = %s", (int(sid),))
    if cursor.rowcount == 0:
        print(f"查找学生信息失败,不存在ID为{sid}的学生信息")
    else:
        for column in cursor.description:
            print(column[0], end="\t\t")
        print("")
        for line in cursor.fetchall():
            for value in line:
                print(value, end="\t\t")
        print("")


def list_stu(cursor):
    cursor.execute("select * from t_student")
    if cursor.rowcount == 0:
        print("当前无学生信息")
    else:
        print(f"当前存在{cursor.rowcount}个学生信息,如下:")
        for column in cursor.description:
            print(column[0], end="\t\t")
        print("")
        for line in cursor.fetchall():
            for value in line:
                print(value, end="\t\t")
            print("")


def main():

    my_connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="py"
    )
    my_cursor = my_connect.cursor()
    while True:
        operation = input("请输入操作:(1:新增学生信息 2:删除学生信息 3:更新学生信息"
                          " 4:查找学生信息 5:列出所有学生信息 0:退出)")
        try:
            operation = int(operation)
        except ValueError:
            print("请输入数字选项")
            continue
        if operation == 1:
            add_stu(my_cursor)
        elif operation == 2:
            delete_stu(my_cursor)
        elif operation == 3:
            update_stu(my_cursor)
        elif operation == 4:
            retrieve_stu(my_cursor)
        elif operation == 5:
            list_stu(my_cursor)
        elif operation == 0:
            print("再见")
            my_cursor.close()
            my_connect.close()
            return
        else:
            continue
        while True:
            continue_flag = input("继续操作?(Y/N)")
            if continue_flag.lower() == "y":
                break
            elif continue_flag.lower() == "n":
                print("再见")
                my_cursor.close()
                my_connect.close()
                return


if __name__ == "__main__":
    main()
