
class R1:
    def __init__(s1,F1):
        s1.F1 = F1
        print(f'\033[91m{s1.F1(s1)}\033[00m')
    def __call__(s1):
        s1.F1
class G1:
    def __init__(s1,F1):
        s1.F1 = F1
        print(f'\033[92m{s1.F1(s1)}\033[00m')
    def __call__(s1):
        s1.F1
class B1:
    def __init__(s1,F1):
        s1.F1 = F1
        print(f'\033[96m{s1.F1(s1)}\033[00m')
    def __call__(s1):
        s1.F1
class Y1:
    def __init__(s1,F1):
        s1.F1 = F1
        print(f'\033[93m{s1.F1(s1)}\033[00m')
    def __call__(s1):
        s1.F1
class M1:
    def __init__(s1):
        s1.m1 = '[M1] - '
    @B1
    def T1(s1):
        s1.c1 = '[M1] - 1. Edit 2. Reset'
        return s1.c1
    def T2(s1):
        s1.T1()
        s1.d1 = input('[M1] - ') 
    def T3(s1):
        s1.T2()
        while True:
            try:
                s1.t1 = int(s1.d1)
                break
            except:
                @R1
                def E1(s1):
                    s1.m2 = '[M1] - Invalid Option'
                    return s1.m2
                s1.T2()
    def T4(s1):
        s1.T3()
        while True:
            try:
                if int(s1.d1) != 1 and int(s1.d1) != 2:
                    @R1
                    def E2(s1):        
                        s1.m4 = '[M1] - Invalid Option'
                        return s1.m4
                    s1.T2()
                else:
                    def I2(s1):
                        s1.m5 = '[M1] - '
                        return s1.m5
                    break
            except:
                @R1
                def E3(s1):
                    s1.m6 = '[M1] - Invalid Option'
                    return s1.m6
                s1.T2()
    def T5(s1):
        s1.T4()
        if int(s1.d1) == 1:
            @B1
            def I3(s1):
                s1.m9 = '[M1] - Editing'
                return s1.m9
            s1.f1 = open('/data/data/com.termux/files/usr/etc/motd', 'w')
            s1.f2 = input('[M1] - ')
            s1.f1.write(s1.f2 + '\n')
            s1.f1.close() 
            @B1 
            def M1(s1):
                s1.m7 = '[M1] - Update Complete!'
                return s1.m7
            @Y1
            def M2(s1):
                s1.m8 = '[M1] - Reboot Termux To View Changes!'
                return s1.m8
        elif int(s1.d1) == 2:
            @B1
            def I4(s1):
                s1.m10 = '[M1] - Reseting'
                return s1.m10
            s1.f3 = open('M1.txt', 'r')
            s1.f4 = s1.f3.read()
            s1.f5 = open('/data/data/com.termux/files/usr/etc/motd', 'w')
            s1.f5.write(s1.f4)
            s1.f3.close()
            s1.f5.close()
            @Y1
            def M3(s1):
                s1.m11 = '[M1] - Reboot Termux To View Changes!'
                return s1.m11
m1 = M1()
m1.T5()
