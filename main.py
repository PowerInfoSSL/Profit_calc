#!/usr/bin/python
#Need python3, Matplotlib,Pandas



from matplotlib import pyplot as plt
import pandas as pd
import os



days=[]
f_price=[]
lst=[]
from matplotlib.axes import Axes

def mony_3(price):
    q=0
    ret='{:,.0f}'.format(price)
    return ret



def calc(price,present=5,month=1):
    price =price *1000000
    import os
    os.system('rm profit.txt')
    if price ==0:
        return 0
    global  days,f_price
    temp_price=price
    temp_sum=0
    file_prof=open('profit.txt','w')
    for i in range(month*30+1):
        days.append(i)
        profit=int((temp_price/100) *present)
        lst.append(profit)
        temp_price =temp_price + ((temp_price/100) *present)
        f_price.append(float(temp_price))
        temp_sum +=profit
        ps='\n[+]' + str(i+1) + ' - TODAY Profit: ' + str(mony_3(profit)) + ' SUM Profit: %s' %mony_3(temp_sum) + ' ----  Your Investment: %s' %mony_3(temp_price)
        file_prof.writelines(ps)
        print('[+]' + str(i+1) + ' - TODAY Profit: ' + str(profit) + ' SUM Profit: %s' %temp_sum)
        #print('\n [+] %d-Day %d You have %s' % (i,i,temp_price))
    plt.plot(days,f_price)
    file_prof.close()
    os.system('open profit.txt')
    s=str(temp_price)
    s2='%s can be ---> ' % mony_3(price)
    s3=0
    s2 +=mony_3(temp_price)
    plt.title(s2)
    plt.savefig('1.pdf')
    print(temp_price)
    import os
    os.system('open 1.pdf')
    print('\n           THE End\n____________')


calc(20,2,10)
