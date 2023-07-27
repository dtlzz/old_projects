import sys
import pickle
set1 = input('do you wanna set/reset your email (y for yes): ')
if set1 == 'y':
    print("it's always optimal to back your accounts with more than one email")
    print('please insert emails you wanna use as a personal email (s for skip):\n')
    pmail1 = input('1- email 1: ')
    pmail2 = input('2- email 2: ')
    print('please insert emails you wanna use for a throwaway account (s for skip):\n')
    thr1 = input('1- email 1: ')
    thr2 = input('2- email 2: ')
    print('\nplease insert emails you wanna use for ultra sensitive account (s for skip):\n')
    vs1 = input('1- email 1: ')
    vs2 = input('2- email 2: ')

    with open('.mydata.pkl', 'wb') as f:
        pickle.dump(pmail1, f)
        pickle.dump(pmail2, f)
        pickle.dump(thr1, f)
        pickle.dump(thr2, f)
        pickle.dump(vs1, f)
        pickle.dump(vs2, f)

else:

    with open('.mydata.pkl', 'rb') as f:
        pmail1 = pickle.load(f)
        pmail2 = pickle.load(f)
        thr1 = pickle.load(f)
        thr2 = pickle.load(f)
        vs1 = pickle.load(f)
        vs2 = pickle.load(f)


    account = input("welcome big boy what account you are creating?:\n"
                    "1- personal\n2- throwaway\n3- ultra sensitive\n- insert the type of account: ")

    if account == '1':
        if pmail1 == 's':
            if pmail2 == 's':
                print("sorry you didn't provide any email")
                sys.exit()
            else:
                print(f'good your email is:\n1- {pmail2} ')
                sys.exit()
        else:
            if pmail2 == 's':
                print(f'good your email is\n1- {pmail1}')
                sys.exit()
            else:
                print(f'good your emails are:\n1- {pmail1}\n2- {pmail2}')
                sys.exit()


    elif account == '2':
        if thr1 == 's':
            if thr2 == 's':
                print("sorry you didn't provide any email")
                sys.exit()
            else:
                print(f'good you email is:\n1- {thr2}')
                sys.exit()
        else:
            if thr2 == 's':
                print(f'good your email is\n1- {thr1}')
                sys.exit()
            else:
                print(f'good your emails are:\n1- {thr1}\n2- {thr2}')
                sys.exit()
    elif account == '3':
        if vs1 == 's':
            if vs2 == 's':
                print("sorry you didn't provide any email")
                sys.exit()
            else:
                print(f'good your email is:\n1- {vs2}')
                sys.exit()
        else:
            if vs2 == 's':
                print(f'good your email is:\n1- {vs1}')
                sys.exit()
            else:
                print(f'good your emails are:\n1- {vs1}\n2- {vs2}')