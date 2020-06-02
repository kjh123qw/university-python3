This program was created by Kim jeongho using python3.
<br />[output test result]

```
********************************************************************************
************************ RUNNING UNIVERSITY SYSTEM 3.0 *************************
********************************************************************************
----------------------------------------------------------------------
MAIN MENU
1.input
2.modify
3.delete
4.output
0.exit
please select a menu >> 1
----------------------------------------------------------------------
main menu > information input
 * The student number is maximum 8 letters. ex) 20200001
 * Name is minimum 2, maximum 10 letters.
student number [x:mainmenu] >> 20200010
name [x:mainmenu b:previous step] >> TESTNAME
TESTNAME's JAVA score [x:mainmenu b:previous step] >> 99
TESTNAME's Oracle score [x:mainmenu b:previous step] >> 95
TESTNAME's JSP score [x:mainmenu b:previous step] >> 96
TESTNAME's Python score [x:mainmenu b:previous step] >> 94
TESTNAME's Spring score [x:mainmenu b:previous step] >> 93
----------------------------------------------------------------------
[inputted information]
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200010 TESTNAME          99       95       96       94       93
Do you want to save TESTNAME's information? [y:save x:mainmenu b:previous step] >> y
  Msg - completed to save
----------------------------------------------------------------------
MAIN MENU
1.input
2.modify
3.delete
4.output
0.exit
please select a menu >> 1
----------------------------------------------------------------------
main menu > information input
 * The student number is maximum 8 letters. ex) 20200001
 * Name is minimum 2, maximum 10 letters.
student number [x:mainmenu] >> osifwe
  Err - wrong input
student number [x:mainmenu] >> 3r3r3
  Err - wrong input
student number [x:mainmenu] >> x
----------------------------------------------------------------------
MAIN MENU
1.input
2.modify
3.delete
4.output
0.exit
please select a menu >> 2
----------------------------------------------------------------------
main menu > information modify
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200001 KIMJH            100      100      100      100      100
20200002 Park              67       75       67       87       66
20200003 Naka              70       40       60       77       40
20200004 JEONGJH           78       58       48       78       96
20200005 JOEKJ             68       76       98       79       86
20200006 SEOJI             99       98      100       99       97
20200007 MATSUMOTO         95       96       94       93       99
20200008 YAMADA            95       96       94       93       99
20200009 BAEKSH            78       87       68       87       66
20200010 TESTNAME          99       95       96       94       93
please input student number you want to modify [x:mainmenu] >> 20200010
----------------------------------------------------------------------
[selected information]
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200010 TESTNAME          99       95       96       94       93
----------------------------------------------------------------------
main menu > information modify > target information select
1.modify name
2.modify score
please select a menu [x:main menu b:previous step] >> 1
----------------------------------------------------------------------
main menu > information modify > target information select > modify name
please input the new name [x:mainmenu b:previous step] >> TESTNAME2
  Msg - completed to change the new name [TESTNAME2]
----------------------------------------------------------------------
[selected information]
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200010 TESTNAME2         99       95       96       94       93
----------------------------------------------------------------------
main menu > information modify > target information select
1.modify name
2.modify score
please select a menu [x:main menu b:previous step] >> 2
----------------------------------------------------------------------
main menu > information modify > target information select > modify score
1.JAVA   2.Oracle   3.JSP   4.Python   5.Spring
please select a target subject [x:mainmenu b:previous step] >> 4
please input TESTNAME2's new Python score [x:mainmenu b:previous step] >> 30
  Msg - completed to modify Python'score [30]
----------------------------------------------------------------------
[selected information]
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200010 TESTNAME2         99       95       96       30       93
----------------------------------------------------------------------
main menu > information modify > target information select
1.modify name
2.modify score
please select a menu [x:main menu b:previous step] >> 1
----------------------------------------------------------------------
main menu > information modify > target information select > modify name
please input the new name [x:mainmenu b:previous step] >> TESTNAME3
  Msg - completed to change the new name [TESTNAME3]
----------------------------------------------------------------------
[selected information]
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200010 TESTNAME3         99       95       96       30       93
----------------------------------------------------------------------
main menu > information modify > target information select
1.modify name
2.modify score
please select a menu [x:main menu b:previous step] >> x
----------------------------------------------------------------------
MAIN MENU
1.input
2.modify
3.delete
4.output
0.exit
please select a menu >> 3
----------------------------------------------------------------------
main menu > information delete
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200001 KIMJH            100      100      100      100      100
20200002 Park              67       75       67       87       66
20200003 Naka              70       40       60       77       40
20200004 JEONGJH           78       58       48       78       96
20200005 JOEKJ             68       76       98       79       86
20200006 SEOJI             99       98      100       99       97
20200007 MATSUMOTO         95       96       94       93       99
20200008 YAMADA            95       96       94       93       99
20200009 BAEKSH            78       87       68       87       66
20200010 TESTNAME3         99       95       96       30       93
please input a target studnet number [x:mainmenu] >> 20200009
----------------------------------------------------------------------
[selected information]
   ID       Name       JAVA    Oracle    JSP     Python   Spring
20200009 BAEKSH            78       87       68       87       66
----------------------------------------------------------------------
do you want to delete this information? [y:delete x:mainmenu b:previous step] >> y
  Msg - completed to delete [20200009]
please input a target studnet number [x:mainmenu] >> x
----------------------------------------------------------------------
MAIN MENU
1.input
2.modify
3.delete
4.output
0.exit
please select a menu >> 4
----------------------------------------------------------------------
main menu > score output
1.score output by subject
2.whole score
please select a menu [x:mainmenu] >> 2
----------------------------------------------------------------------
[whole score output]
   ID       Name       JAVA    Oracle    JSP     Python   Spring   Total   Average  Rank
20200001 KIMJH            100      100      100      100      100      500   100.0     1
20200002 Park              67       75       67       87       66      362    72.4     7
20200003 Naka              70       40       60       77       40      287    57.4     9
20200004 JEONGJH           78       58       48       78       96      358    71.6     8
20200005 JOEKJ             68       76       98       79       86      407    81.4     6
20200006 SEOJI             99       98      100       99       97      493    98.6     2
20200007 MATSUMOTO         95       96       94       93       99      477    95.4     3
20200008 YAMADA            95       96       94       93       99      477    95.4     3
20200010 TESTNAME3         99       95       96       30       93      413    82.6     5
----------------------------------------------------------------------
main menu > score output
1.score output by subject
2.whole score
please select a menu [x:mainmenu] >> 1
----------------------------------------------------------------------
main menu > score output > score output by subject
1.JAVA   2.Oracle   3.JSP   4.Python   5.Spring
please select a subject [x:mainmenu b:previous step] >> 4
----------------------------------------------------------------------
[Python score output]
   ID       Name      Python    Rank   Average
20200001 KIMJH            100        1     81.8
20200002 Park              87        5     81.8
20200003 Naka              77        8     81.8
20200004 JEONGJH           78        7     81.8
20200005 JOEKJ             79        6     81.8
20200006 SEOJI             99        2     81.8
20200007 MATSUMOTO         93        3     81.8
20200008 YAMADA            93        3     81.8
20200010 TESTNAME3         30        9     81.8
----------------------------------------------------------------------
main menu > score output > score output by subject
1.JAVA   2.Oracle   3.JSP   4.Python   5.Spring
please select a subject [x:mainmenu b:previous step] >> x
----------------------------------------------------------------------
MAIN MENU
1.input
2.modify
3.delete
4.output
0.exit
please select a menu >> 0
Thank you~!.
```
