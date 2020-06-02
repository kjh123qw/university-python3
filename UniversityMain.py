# -*- coding:utf-8 -*-
'''
Created on 2020. 1. 30.

@author: kosmo-18
'''

import pickle

studentList = {}


def main():
    """main method"""
    print("*" * 80)
    print("*" * 24, "RUNNING UNIVERSITY SYSTEM 3.0", "*" * 25)
    print("*" * 80)
    loadInfo()
    while 1:
        print("-" * 70)
        print("MAIN MENU")
        print("{:12}\n{:12}\n{:12}\n{:12}\n{:12}".format(
            "1.input", "2.modify", "3.delete", "4.output", "0.exit"))
        print("please select a menu >> ", end="")
        inp = input()
        if(valInput(inp, int, 4)):
            if(inp.__eq__("1")):
                inputInfo()
            elif(inp.__eq__("2")):
                modifyInfo()
            elif(inp.__eq__("3")):
                deleteInfo()
            elif(inp.__eq__("4")):
                printInfo()
            elif(inp.__eq__("0")):
                print("Thank you~!.")
                break
        else:
            print("wrong input")


def inputInfo():
    """input method"""
    global studentList

    step = 0
    idNum = 0
    name = ""
    pJava = 0
    pOracle = 0
    pJsp = 0
    pPython = 0
    pSpring = 0

    print("-" * 70)
    print("main menu > information input")
    print(" * The student number is maximum 8 letters. ex) 20200001")
    print(" * Name is minimum 2, maximum 10 letters.")
    while 1:
        if(step == 0):
            print("student number [x:mainmenu] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            else:
                if(valInput(inp, int, 99999999, 20200001)):
                    if(len(studentList) == 0 or not int(inp) in studentList.keys()):
                        idNum = int(inp)
                        step = 1
                    else:
                        print("  Err - already exist same sutudent number")
                else:
                    print("  Err - wrong input")
        elif(step == 1):
            print("name [x:mainmenu b:previous step] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 0
            else:
                if(valInput(inp, str, 10, 1)):
                    name = inp
                    step = 2
                else:
                    print("  Err - wrong input")
        elif(step == 2):
            print(
                "{:}'s JAVA score [x:mainmenu b:previous step] >> ".format(name), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 1
            else:
                if(valInput(inp, int, 100)):
                    pJava = int(inp)
                    step = 3
                else:
                    print("  Err - wrong input")
        elif(step == 3):
            print(
                "{:}'s Oracle score [x:mainmenu b:previous step] >> ".format(name), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 2
            else:
                if(valInput(inp, int, 100)):
                    pOracle = int(inp)
                    step = 4
                else:
                    print("  Err - wrong input")
        elif(step == 4):
            print(
                "{:}'s JSP score [x:mainmenu b:previous step] >> ".format(name), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 3
            else:
                if(valInput(inp, int, 100)):
                    pJsp = int(inp)
                    step = 5
                else:
                    print("  Err - wrong input")
        elif(step == 5):
            print(
                "{:}'s Python score [x:mainmenu b:previous step] >> ".format(name), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 4
            else:
                if(valInput(inp, int, 100)):
                    pPython = int(inp)
                    step = 6
                else:
                    print("  Err - wrong input")
        elif(step == 6):
            print(
                "{:}'s Spring score [x:mainmenu b:previous step] >> ".format(name), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 5
            else:
                if(valInput(inp, int, 100)):
                    pSpring = int(inp)
                    step = 7
                else:
                    print("  Err - wrong input")
        elif(step == 7):
            print("-" * 70)
            print("[inputted information]")
            print("{:^8} {:^11} {:^8} {:^8} {:^8} {:^8} {:^8}".format
                  ("ID", "Name", "JAVA", "Oracle", "JSP", "Python", "Spring"))
            print("{:8} {:11} {:8,d} {:8,d} {:8,d} {:8,d} {:8,d}".format
                  (idNum, name, pJava, pOracle, pJsp, pPython, pSpring))
            print(
                "Do you want to save {:}'s information? [y:save x:mainmenu b:previous step] >> ".format(name), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 6
            elif(inp == "y"):
                step = 8
            else:
                print("  Err - wrong input")
        elif(step == 8):
            print("  Msg - completed to save")
            std = Student(idNum, name, pJava, pOracle, pJsp, pPython, pSpring)
            studentList[idNum] = std
            saveInfo()
            break


def modifyInfo():
    """modify method"""
    global studentList
    idNum = 0
    step = 0
    mdfSubj = ""
    targetStd = Student

    print("-" * 70)
    print("main menu > information modify")
    print("{:^8} {:^11} {:^8} {:^8} {:^8} {:^8} {:^8}".format
          ("ID", "Name", "JAVA", "Oracle", "JSP", "Python", "Spring"))
    for idNum in studentList:
        print(studentList[idNum])
    while 1:
        if(step == 0):
            print(
                "please input student number you want to modify [x:mainmenu] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            else:
                if(valInput(inp, int, 99999999, 20200001)):
                    if(int(inp) in studentList.keys()):
                        idNum = int(inp)
                        targetStd = studentList[idNum]
                        step = 1
                    else:
                        print("  Err - there is no student number")
                else:
                    print("  Err - wrong input")
        elif(step == 1):
            print("-" * 70)
            print("[selected information]")
            print("{:^8} {:^11} {:^8} {:^8} {:^8} {:^8} {:^8}".format
                  ("ID", "Name", "JAVA", "Oracle", "JSP", "Python", "Spring"))
            print(targetStd)
            print("-" * 70)
            print("main menu > information modify > target information select")
            print("1.{:}\n2.{:}".format("modify name", "modify score"))
            print(
                "please select a menu [x:main menu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 0
            elif(valInput(inp, int, 2, 1)):
                if(inp.__eq__("1")):
                    step = 2
                elif(inp.__eq__("2")):
                    step = 3
            else:
                print("  Err - wrong input")
        elif(step == 2):
            print("-" * 70)
            print(
                "main menu > information modify > target information select > modify name")
            print(
                "please input the new name [x:mainmenu b:previous step] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 1
            else:
                if(valInput(inp, str, 10, 1)):
                    targetStd.name = inp
                    print(
                        "  Msg - completed to change the new name [{:}]".format(inp))
                    saveInfo()
                    step = 1
                else:
                    print("  Err - wrong input")
        elif(step == 3):
            print("-" * 70)
            print(
                "main menu > information modify > target information select > modify score")
            print("{:}   {:}   {:}   {:}   {:}".format
                  ("1.JAVA", "2.Oracle", "3.JSP", "4.Python", "5.Spring"))
            print(
                "please select a target subject [x:mainmenu b:previous step] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 1
            elif(valInput(inp, int, 5, 1)):
                if(inp.__eq__("1")):
                    mdfSubj = "JAVA"
                elif(inp.__eq__("2")):
                    mdfSubj = "Oracle"
                elif(inp.__eq__("3")):
                    mdfSubj = "JSP"
                elif(inp.__eq__("4")):
                    mdfSubj = "Python"
                elif(inp.__eq__("5")):
                    mdfSubj = "Spring"
                step = 4
            else:
                print("  Err - wrong input")
        elif(step == 4):
            print("please input {:}'s new {:} score [x:mainmenu b:previous step] >> ".format(
                targetStd.name, mdfSubj), end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 3
            else:
                if(valInput(inp, int, 100)):
                    score = int(inp)
                    if(mdfSubj.__eq__("JAVA")):
                        targetStd.pJava = score
                    elif(mdfSubj.__eq__("Oracle")):
                        targetStd.pOracle = score
                    elif(mdfSubj.__eq__("JSP")):
                        targetStd.pJsp = score
                    elif(mdfSubj.__eq__("Python")):
                        targetStd.pPython = score
                    elif(mdfSubj.__eq__("Spring")):
                        targetStd.pSpring = score
                    print(
                        "  Msg - completed to modify {:}'score [{:,d}]".format(mdfSubj, score))
                    step = 1
                    saveInfo()
                else:
                    print("  Err - wrong input")


def deleteInfo():
    """delete method"""
    global studentList
    idNum = 0
    step = 0
    targetStd = ""
    print("-" * 70)
    print("main menu > information delete")
    print("{:^8} {:^11} {:^8} {:^8} {:^8} {:^8} {:^8}".format
          ("ID", "Name", "JAVA", "Oracle", "JSP", "Python", "Spring"))
    for idNum in studentList:
        print(studentList[idNum])
    while 1:
        if(step == 0):
            print(
                "please input a target studnet number [x:mainmenu] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            else:
                if(valInput(inp, int, 99999999, 20200001)):
                    if(int(inp) in studentList.keys()):
                        idNum = int(inp)
                        targetStd = studentList[idNum]
                        step = 1
                    else:
                        print("  Err - there is no student number")
                else:
                    print("  Err - wrong input")
        elif(step == 1):
            print("-" * 70)
            print("[selected information]")
            print("{:^8} {:^11} {:^8} {:^8} {:^8} {:^8} {:^8}".format
                  ("ID", "Name", "JAVA", "Oracle", "JSP", "Python", "Spring"))
            print(targetStd)
            print("-" * 70)
            print(
                "do you want to delete this information? [y:delete x:mainmenu b:previous step] >> ", end="")
            inp = input()
            if(inp.__eq__("x")):
                break
            elif(inp.__eq__("b")):
                step = 0
            elif(inp.__eq__("y")):
                print("  Msg - completed to delete [{:}]".format(idNum))
                studentList.pop(idNum)
                saveInfo()
                step = 0
            else:
                print("  Err - wrong input")


def printInfo():
    """score output method"""
    global studentList
    step = 0
    while 1:
        if(step == 0):
            print("-" * 70)
            print("main menu > score output")
            print("{:}\n{:}".format("1.score output by subject", "2.whole score"))
            print("please select a menu [x:mainmenu] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            elif(valInput(inp, int, 2, 1)):
                if(inp.__eq__("1")):
                    step = 1
                elif(inp.__eq__("2")):
                    step = 2
            else:
                print("  Err - wrong input")
        elif(step == 1):
            print("-" * 70)
            print("main menu > score output > score output by subject")
            print("{:}   {:}   {:}   {:}   {:}".format
                  ("1.JAVA", "2.Oracle", "3.JSP", "4.Python", "5.Spring"))
            print(
                "please select a subject [x:mainmenu b:previous step] >> ", end="")
            inp = input()
            if(inp == "x"):
                break
            elif(inp == "b"):
                step = 0
            elif(valInput(inp, int, 5, 1)):
                if(inp.__eq__("1")):
                    printSub(Student.getpJava, "JAVA")
                elif(inp.__eq__("2")):
                    printSub(Student.getpOracle, "Oracle")
                elif(inp.__eq__("3")):
                    printSub(Student.getpJsp, "JSP")
                elif(inp.__eq__("4")):
                    printSub(Student.getpPython, "Python")
                elif(inp.__eq__("5")):
                    printSub(Student.getpSpring, "Spring")
            else:
                print("  Err - wrong input")
        elif(step == 2):
            if(len(studentList) == 0):
                print("there is information")
            else:
                print("-" * 70)
                print("[whole score output]")
                print("{:^8} {:^11} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^5}".format
                      ("ID", "Name", "JAVA", "Oracle", "JSP", "Python", "Spring", "Total", "Average", "Rank"))
                sumValue = {}
                avgValue = {}
                rank = {}
                for idNum in studentList:
                    sumValue[idNum] = Student.getpJava(studentList[idNum]) + Student.getpOracle(studentList[idNum]) + \
                        Student.getpJsp(studentList[idNum]) + Student.getpPython(studentList[idNum]) + \
                        Student.getpSpring(studentList[idNum])
                    avgValue[idNum] = float(sumValue[idNum] / 5.0)
                for idNum in studentList:
                    rank[idNum] = 1
                    for idNum2 in studentList:
                        if(sumValue[idNum] < sumValue[idNum2]):
                            rank[idNum] += 1
                for idNum in studentList:
                    print(studentList[idNum], "{:8,d} {:7.1f} {:5,d}".format(
                        sumValue[idNum], avgValue[idNum], rank[idNum]))
                step = 0


def printSub(func, subj):
    """score output method
    func: method address / subj: output subject"""
    print("-" * 70)
    print("[{:} score output]".format(subj))
    print("{:^8} {:^11} {:^8} {:^8} {:^8}".format(
        "ID", "Name", subj, "Rank", "Average"))
    seq = len(studentList)
    avg = 0
    for idNum in studentList:
        avg += func(studentList[idNum])
    avg = avg / seq
    for idNum in studentList:
        rank = 1
        std = studentList[idNum]
        for idNum2 in studentList:
            std2 = studentList[idNum2]
            if(func(std) < func(std2)):
                rank += 1
        print("{:8} {:11} {:8,d} {:8,d} {:8.1f}".format
              (std.getidNum(), std.getName(), func(std), rank, avg))


def saveInfo():
    """save method"""
    global studentList
    saveDict = {}

    if(len(studentList) == 0):
        print("there is no information to save")
    else:
        for idNum in studentList:
            saveDict[idNum] = studentList[idNum].returnInfo()
        f = open('dbHaksa.txt', 'wb')
        pickle.dump(saveDict, f)
        f.close()


def loadInfo():
    """load method"""
    global studentList
    try:
        f = open('dbHaksa.txt', 'rb')
        loadData = pickle.load(f)
        for idNum in loadData:
            studentList[idNum] = Student(loadData[idNum][0], loadData[idNum][1], loadData[idNum]
                                         [2], loadData[idNum][3], loadData[idNum][4], loadData[idNum][5], loadData[idNum][6])
    except:
        pass


def valInput(inp, ty, limit, less=0):
    """input value check method
    inp: input value / ty: check type / [ty(int)]limit: limit by the number / [ty(str)]limit: limit by the letter"""
    retVal = False
    if(ty == int):
        try:
            inpNum = int(inp)
            if(less <= inpNum and inpNum <= limit):
                retVal = True
        except:
            pass
    elif(ty == str):
        if(less < len(inp) and len(inp) <= limit):
            retVal = True
    return retVal


class Student:
    def __init__(self, idNum, name, pJava, pOracle, pJsp, pPython, pSpring):
        self.idNum = int(idNum)
        self.name = name
        self.pJava = int(pJava)
        self.pOracle = int(pOracle)
        self.pJsp = int(pJsp)
        self.pPython = int(pPython)
        self.pSpring = int(pSpring)

    def __str__(self):
        return "{:8} {:11} {:8,d} {:8,d} {:8,d} {:8,d} {:8,d}".format(self.idNum, self.name, self.pJava, self.pOracle, self.pJsp, self.pPython, self.pSpring)

    def returnInfo(self):
        return self.idNum, self.name, self.pJava, self.pOracle, self.pJsp, self.pPython, self.pSpring

    def getidNum(self):
        return self.idNum

    def getName(self):
        return self.name

    def getpJava(self):
        return self.pJava

    def getpOracle(self):
        return self.pOracle

    def getpJsp(self):
        return self.pJsp

    def getpPython(self):
        return self.pPython

    def getpSpring(self):
        return self.pSpring


main()
