#coding=utf-8
import pymysql
import os
import time
import re


def readcasestep():
    sql1= "SELECT webtestlocation,webfindmethod,webkwargesone,webkwargestwo,webkwargesthree,webkwargesfour,b.task_casename,b.case_id FROM webtest_webcasestep AS a LEFT JOIN webtest_webtest_task AS b ON a.Webcase_id=b.case_id;"
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    webcasestepcheck = cursor.execute(sql1)  # 读取页面上的执行步骤
    get_selectresult = cursor.fetchmany(webcasestepcheck)  # 获取所有的查询结果
    case_count = 0
    for one_result in get_selectresult:
        case_list = []
        case_list.append(one_result)
        case_count += 1  # 查看读取用例了多少次，即一遍一遍的读取数据库中的步骤
        run_webcasestep_intask(case_list, case_count)
        # readSQLCounts()
    coon.ping(reconnect=True)
    coon.commit()
    cursor.close()
    coon.close()


#获取总共有多少条step:
def readSQLCounts():
    sql2 = "SELECT count(*) FROM webtest_webcasestep AS a LEFT JOIN webtest_webtest_task AS b ON a.Webcase_id=b.case_id;"
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    get_counts = cursor.execute(sql2)                                   # 读取页面上的执行步骤数量
    get_countsnumber = cursor.fetchmany(get_counts)                     # 获取所有的查询结果数量
    coon.ping(reconnect=True)
    coon.commit()
    cursor.close()
    coon.close()
    return get_countsnumber



def run_webcasestep_intask(case_list, case_count):
    get_case_count = case_count
    counts = readSQLCounts()
    new_count = list(counts)  # 将元祖转换为列表
    step_counts = new_count[0][0]  # 将数据库查询到的步骤数量取出
    taskcasesuit = "test.txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, taskcasesuit)  # 加入完整的目录和文件名称
    for case in case_list:
        try:
            webtestlocation = case[0]
            webfindmethod = case[1]
            webkwargesone = case[2]
            webkwargestwo = case[3]
            webkwargesthree = case[4]
            webkwargesfour = case[5]
            taskcasename = case[6]
            case_id = case[7]
        except Exception as e:
            return '测试用例格式不正确！！%s' % e
        with open(project_path, 'a+',encoding="GBK") as txtfile:
            txtfile.seek(0)
            r = txtfile.readlines()
            str1 ="Test0"+case_id + "\n"
            str2 = "\t"+"[Documentation]"+"\t"+"\t"+taskcasename+"\n"
            if str1 in r:
                print("已经写入了")
            else:
                txtfile.write("\r"+str1)
            if str2 in r:
                print("也已经写入了")
            else:
                txtfile.write(str2)
            try:                                                                            # 判断参数的长度 并分别写入
                if webkwargesone == "":
                    txtfile.write("\t" + webfindmethod + "\n")
                elif webkwargestwo == "":
                    txtfile.write("\t" + webfindmethod + "\t" + webkwargesone + "\n")
                elif webkwargesthree == "":
                    txtfile.write("\t" + webfindmethod + "\t" + webkwargesone + "\t" + webkwargestwo + "\n")
                elif webkwargesfour == "":
                    txtfile.write(
                        "\t" + webfindmethod + "\t" + webkwargesone + "\t" + webkwargestwo + "\t" + webkwargesthree + "\n")
                else:
                    txtfile.write(
                        "\t" + webfindmethod + "\t" + webkwargesone + "\t" + webkwargestwo + "\t" + webkwargesthree + "\t" + webkwargesfour + "\n")
            except Exception as e:
                print("Failed,please retry.....")
            txtfile.close()
            print("over")
            if get_case_count == step_counts:
                print(get_case_count)
                time.sleep(2)
                # run_in_terminal(taskcasename)
                print("正在运行脚本")
            else:
                print("数据正在写入中")

if __name__ == '__main__':
    readcasestep()