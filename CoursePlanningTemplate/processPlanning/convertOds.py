# prerequisites: requires python 3.x (or higher)
# open cmd
# browse to this directory
# install pyexcel with:
# python -m pip install pyexcel
# python -m pip install pyexcel-ods (outdated)
# python -m pip install pyexcel-ods3 (outdated)
# python -m pip install pyexcel-xlsx
# python -m pip install pyexcel-xlsxw (ignored)
# run this script with:
# python convertOds.py
import pyexcel
import glob
import os
import subprocess

def convert_to_xlxs():
    os.chdir(".")
    for file in glob.glob("../*.ods"):
        #for sheet in file:
         #   print(sheet)
        #sheet = pyexcel.get_sheet(file_name = file)
        sheet = pyexcel.get_sheet(file_name = file,sheet_name = "Course")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Lectures")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Assignments")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "OldExams")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Exercises")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "StudyMaterial")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Exam")

        #print(sheet)
        sheet.save_as(file + '.xlsx')

def run_excel_module_from_python():
    import os, os.path
    import win32com.client

    if os.path.exists("GenerateTwCommandsAndLatexTemplates.xlsm"):
        xl=win32com.client.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath("GenerateTwCommandsAndLatexTemplates.xlsm"), ReadOnly=1)
        xl.Application.Run("GenerateTwCommandsAndLatexTemplates.xlsm!Module1.main")
        ##    xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
        xl.Application.Quit() # Comment this out if your excel script closes
        del xl

def create_latex_exam_solution_templates():
    import os, os.path
    import win32com.client

    if os.path.exists("GenerateTwCommandsAndLatexTemplates.xlsm"):
        xl=win32com.client.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath("GenerateTwCommandsAndLatexTemplates.xlsm"), ReadOnly=1)
        xl.Application.Run("GenerateTwCommandsAndLatexTemplates.xlsm!Module2.createExamSolutionTemplates")
        ##    xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
        xl.Application.Quit() # Comment this out if your excel script closes
        del xl

subprocess.call("cscript CsvTasks/readCSV.vbs") # works

#subprocess.call("cmd /c 19112944.vbs") # works
                                       # have shell, can associate .vbs with c|wscript.exe

convert_to_xlxs()
print("Converted .ods to .xlxs in parentfolder.")
run_excel_module_from_python()
print("Completed evaluation of excel subroutine")