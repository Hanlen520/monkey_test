import os
import xlsxwriter
from Base import BaseReport
import xlrd


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def report(info):
    #run_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    #workbook = xlsxwriter.Workbook('report.' + run_time + '.xlsx')
    workbook = xlsxwriter.Workbook('performance_report.xlsx')
    bo = BaseReport.OperateReport(workbook)
    bo.monitor(info)
    bo.crash()
    bo.analysis(info)
    bo.close()

def readExcel():
    workbook = xlrd.open_workbook("D:\monkey_test\performance_report.xlsx")
    for item in workbook.sheet_by_name("性能数据详情")._cell_values[2]:
        print(item)
    # for item in workbook.sheet_by_name("崩溃日志")._cell_values:
    #     print(item)

if __name__=="__main__":
    readExcel()
