import sys
print('\n----حساب المعدل الموزون لشهادة البكالوريا----\n\n--- المواد الاساسية للتخصص ---')
print('1- رياضيات\n2- فيزياء\n3- علوم طبيعية\n4- رياضيات + فيزياء\n5- لغات')
sub = int(input('\nاختر 1-5: '))
bac = (float(input(('معدل شهادة البكالوريا: '))))
#math
if sub == 1:
    math = (float(input('نتيجة الرياضيات: ')))
    res1 = round((bac * 2 + math) / 3, 2)
    print(f'المعدل الموزون لمادة الرياضيات:{res1}')
    print("congrats!!!!!!!!!!!!!!")
    sys.exit()
#phy
if sub == 2:
    phy = (float(input('نتيجة الفيزياء: ')))
    res2 = round((bac * 2 + phy) / 3, 2)
    print(f'المعدل الموزون لمادة الفيزياء:{res2}')
    print("congrats!!!!!!!!!!!!!!")
    sys.exit()
#science
if sub == 3:
    sci = (float(input('نتيجة العلوم: ')))
    res3 = round((bac * 2 + sci) / 3, 2)
    print(f'المعدل الموزون لمادة العلوم:{res3}')
    print("congrats!!!!!!!!!!!!!!")
    sys.exit()
#math
if sub == 4:
    math1 = (float(input('نتيجة الرياضيات: ')))
    phy1 = (float(input('نتيجة الفيزياء: ')))
    res4 = round(((bac * 2) + (math1 + phy1) / 2) / 3, 2)
    print(f'المعدل الموزون لمادة الرياضيات و الفيزياء:{res4}')
    print("congrats!!!!!!!!!!!!!!")
    sys.exit()
#language
if sub == 5:
    lgh = (float(input('نتيجة اللغة المحددة او معدل اللغات المعينة: ')))
    res5 = round((bac * 2 + lgh) / 3, 2)
    print(f'المعدل الموزون للغات المعينة{res5}')
    print("congrats!!!!!!!!!!!!!!")
    sys.exit()