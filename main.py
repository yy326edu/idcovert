# -*- coding:utf-8 -*-
print "Developed by YangYi"


def qu0x(a, b):
    n_a = str(a)[2:]
    n_b = str(b)[2:]
    if len(n_b) == 3:
        n_all = n_a + "0" + n_b
        return n_all
    elif len(n_b) == 2:
        n_all = n_a + "00" + n_b
        return n_all
    else:
        n_all = n_a + n_b
        return n_all


def covert8_10(cardstr):
    i = 8 - len(cardstr)
    if len(cardstr) <= 5:
        print "Input wrong card number!"

    else:
        aft_five = cardstr[-5:]
        bef_three = cardstr[0:3 - i]
        q3 = hex(int(bef_three))
        h5 = hex(int(aft_five))
        hb8 = qu0x(q3, h5)
        return int(hb8, 16)


while True:
    card_num = raw_input("Please input old card number:")
    print 'New ID card number is '+str(covert8_10(card_num))
