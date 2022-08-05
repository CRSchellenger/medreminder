from sqlite3 import Time
from datetime import datetime,timedelta
import time
global nm
while True:
    ad = input('What would you like to do? ')
    if ad.lower() == 'admin meds':
        fr = open('/Users/bubba/medlist.txt', 'r')
        content = fr.read()
        print ('------Med list -------- \n '+ content)
        fr.close()
        i = input('Please enter a med name: ')
        if i == 'xanax':
            x = input('Please enter your name: ')
            ct = time.strftime('%Y-%m-%d %H:%M:%S')
            mt = time.strftime('%H:%m')
            xtt = datetime.now() + timedelta(hours=5)

            r = '\n' + x +' has administered '+ i +' at '+ ct

            medfile = open('/Users/bubba/medfile.txt', 'a')
            medfile.writelines(r)
            medfile.close()
            medfile = open('/Users/bubba/medfile.txt','r+')

            print('Xanax has been administered')
            print(r)
            print('next pill to be administered at '+ str(xtt))

            xsr = '\n' + str(xtt) +' xanax'
            xs = open('/Users/bubba/medschedule', 'a')
            xs.writelines(xsr)
            xs.close()
            xs = open('/Users/bubba/medschedule', 'r+')

        elif i == 'oxycodone':
            o = input('Please enter your name: ')
            rt = time.strftime('%Y-%m-%d %H:%M:%S')
            ot = time.strftime('%H:%m')
            ott = datetime.now() + timedelta(hours=4)

            oi = '\n' + o +' has administered '+ i +' at '+ rt

            medfile = open('/Users/bubba/medfile.txt', 'a')
            medfile.writelines(oi)
            medfile.close()
            medfile = open('/Users/bubba/medfile.txt','r+')

            print('oxycodone has been administered')
            print(oi)
            print('next pill to be administered at '+ str(ott))

            osr = '\n' + str(ott) + ' oxycodone'
            os = open('/Users/bubba/medschedule', 'a')
            os.writelines(str(osr))
            os.close()
            os = open('/Users/bubba/medschedule.txt', 'r+')

        elif i == 'loratadine':
            ln = input('Please enter your name: ')
            lt = time.strftime('%Y-%m-%d %H:%M:%S')
            ltq = time.strftime('%H:%m')
            ltt = datetime.now() + timedelta(hours=24)

            li = '\n' + ln +' has administered '+ i +' at '+ lt

            medfile = open('/Users/bubba/medfile.txt', 'a')
            medfile.writelines(li)
            medfile.close()
            medfile = open('/Users/bubba/medfile.txt','r+')

            print('oxycodone has been administered')
            print(li)
            print('next pill to be administered at '+ str(ltt))

            lsr = '\n' + str(ltt) + ' loratadine'
            ls = open('/Users/bubba/medschedule', 'a')
            ls.writelines(str(lsr))
            ls.close()
            ls = open('/Users/bubba/medschedule.txt', 'r+')

        elif i == 'tramadol':
            tn = input('Please enter your name: ')
            tt = time.strftime('%Y-%m-%d %H:%M:%S')
            ttq = time.strftime('%H:%m')
            ttt = datetime.now() + timedelta(hours=6)

            ti = '\n' + tn +' has administered '+ i +' at '+ tt

            medfile = open('/Users/bubba/medfile.txt', 'a')
            medfile.writelines(ti)
            medfile.close()
            medfile = open('/Users/bubba/medfile.txt','r+')

            print('oxycodone has been administered')
            print(ti)
            print('next pill to be administered at '+ str(ttt))

            tsr = '\n' + str(ttt) + ' tramadol'
            ts = open('/Users/bubba/medschedule', 'a')
            ts.writelines(str(tsr))
            ts.close()
            ts = open('/Users/bubba/medschedule.txt', 'r+')


        elif i == 'temazepam':
                ten = input('Please enter your name: ')
                tet = time.strftime('%Y-%m-%d %H:%M:%S')
                tte = time.strftime('%H:%m')
                tte = datetime.now() + timedelta(hours=24)

                te = '\n' + ten +' has administered '+ i +' at '+ tet

                medfile = open('/Users/bubba/medfile.txt', 'a')
                medfile.writelines(te)
                medfile.close()
                medfile = open('/Users/bubba/medfile.txt','r+')

                print('oxycodone has been administered')
                print(te)
                print('next pill to be administered at '+ str(tte))

                tse = '\n' + str(tte) + ' temazepam'
                te = open('/Users/bubba/medschedule', 'a')
                te.writelines(str(tse))
                te.close()
                te = open('/Users/bubba/medschedule.txt', 'r+')


        elif i == 'senokot':
                sen = input('Please enter your name: ')
                set = time.strftime('%Y-%m-%d %H:%M:%S')
                ste = time.strftime('%H:%m')
                ste = datetime.now() + timedelta(hours=12)

                se = '\n' + sen +' has administered '+ i +' at '+ set

                medfile = open('/Users/bubba/medfile.txt', 'a')
                medfile.writelines(se)
                medfile.close()
                medfile = open('/Users/bubba/medfile.txt','r+')

                print('oxycodone has been administered')
                print(se)
                print('next pill to be administered at '+ str(ste))

                sse = '\n' + str(ste) + ' senokot'
                se = open('/Users/bubba/medschedule', 'a')
                se.writelines(str(sse))
                se.close()
                se = open('/Users/bubba/medschedule.txt', 'r+')


        elif i == 'fentanyl':
                fen = input('Please enter your name: ')
                fet = time.strftime('%Y-%m-%d %H:%M:%S')
                fte = time.strftime('%H:%m')
                fre = datetime.now() + timedelta(hours=24)

                fe = '\n' + fen +' has administered '+ i +' at '+ fet

                medfile = open('/Users/bubba/medfile.txt', 'a')
                medfile.writelines(fe)
                medfile.close()
                medfile = open('/Users/bubba/medfile.txt','r+')

                print('oxycodone has been administered')
                print(fe)
                print('next pill to be administered at '+ str(fre))

                fse = '\n' + str(fre) + ' fentanyl'
                fe = open('/Users/bubba/medschedule', 'a')
                fe.writelines(str(fse))
                fe.close()
                fe = open('/Users/bubba/medschedule.txt', 'r+')



        else:
            print('Please enter med name' + '\n' + '-error 1')
    elif ad.lower() == 'add meds':
        nm= input('Please enter med name that you would like to add to the system: ')
        medlist =open('/Users/bubba/medlist.txt', 'a')
        medlist.writelines('\n' + nm)
        medlist.close()
        medlist = open('/Users/bubba/medlist.txt','r+')

    elif ad.lower() == 'med info':
        print('welcome to the med information section')
        di = input('Please enter med name that you would like to learn about: ')
        di.lower()
        if di == 'xanax' or di == 'alprazolam':
            xi = open('/Users/bubba/xanax drug info', 'r')
            xc = xi.read()
            print(xc)
            xi.close()

        elif di == 'oxycodone':
            oi = open('/Users/bubba/oi.text', 'r')
            oc = oi.read()
            print(oc)
            oi.close()

        elif di == 'loratadine':
            li = open('/Users/bubba/li.txt', 'r')
            lc = li.read()
            print(lc)
            li.close()

        elif di == 'tramadol':
            ti = open('/Users/bubba/ti.txt', 'r')
            tc = ti.read()
            print(tc)
            ti.close()

        elif di == 'temazepam':
            te = open('/Users/bubba/te.txt', 'r')
            tc = te.read()
            print(tc)
            te.close()


        elif di == 'senokot':
            si = open('/Users/bubba/si.txt', 'r')
            sc = si.read()
            print(sc)
            si.close()


        elif di == 'fentanyl':
            fi = open('/Users/bubba/fi.txt', 'r')
            fc = fi.read()
            print(fc)
            fi.close()


    elif ad.lower() == 'note':
        ntd = time.strftime('%Y-%m-%d %H:%M:%S')
        nt = input('Title: ')
        ntb = input('Note: ')

        n = '\n-------------------------------------------' +'\n'+ ntd + '\n' + nt + '\n' + ntb +'\n-------------------------------------------'

        note = open('/Users/bubba/notes.txt', 'a')
        note.writelines(n)
        note.close()
        note = open('/Users/bubba/notes.txt','r+')


    elif ad.lower() == 'print notes':
        ni = open('/Users/bubba/notes.txt', 'r')
        nc = ni.read()
        print(nc)
        ni.close()

    elif ad.lower() == 'vitials':
        bp = input('Enter Blood pressure: ')
        hr = input('Enter heart rate: ')
        sp = input('Enter SP02 rate: ')
        ctd = time.strftime('%Y-%m-%d %H:%M:%S')

        v = '\n-------------------------------------------'+'\n' +ctd +'\nBlood Pressure: '+ bp + '\nHeart Rate: '+hr + '\nSP02: ' + sp +'\n-------------------------------------------'

        note = open('/Users/bubba/vitals.txt', 'a')
        note.writelines(v)
        note.close()
        note = open('/Users/bubba/vitals.txt','r+')
    elif ad.lower() == 'print vitals':
        vi = open('/Users/bubba/vitals.txt', 'r')
        vc = vi.read()
        print(vc)
        vi.close()
    
    
    elif ad.lower() == 'nurse':
        ny = input('Please enter your name: ')
        ni = input('Would you like to add any notes about todays visit?: ')
        td = time.strftime('%Y-%m-%d %H:%M:%S')
        if ni == 'yes':
            nn = input('Enter your notes now: ')
            d= '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse Notes: '+ nn + '\n-------------------------------------------'
            nv = open('/Users/bubba/nurse.txt', 'a')
            nv.writelines(d)
            nv.close()
            nv = open('/Users/bubba/nurse.txt','r+')
        else:

            e = '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse did not enter any notes'+'\n-------------------------------------------'

            nv1 = open('/Users/bubba/nurse.txt', 'a')
            nv1.writelines(e)
            nv1.close()
            nv1 = open('/Users/bubba/nurse.txt','r+')
            
    


    elif ad.lower() == 'covid test':
        print('Types of tests are Anitgen and PCR')
        pn = input('Please enter the name of the person this test was performed on: ')
        ctt = input ('Please enter the the type of test you have taken: ')
        print('--------------------------------')
        print('pos,neg')
        ttr = input('Please enter the result of the test: ')
        if ttr == 'pos':
            print('Please isolate for 5 days to ensure the diaease does note spread')
        else:
            pass
        tdd = time.strftime('%Y-%m-%d %H:%M:%S')

        cttr = '\n-------------------------------------------'+'\n' +tdd +'\nName of the person this test was performed on: ' + pn +'\ntype of test taken: ' + ctt + '\nResult of the test: ' + ttr +'\n-------------------------------------------'

        covid = open('/Users/bubba/ct.txt', 'a')
        covid.writelines(cttr)
        covid.close()
        covid = open('/Users/bubba/ct.txt','r+')


    elif ad.lower() == 'quit':
        break
        