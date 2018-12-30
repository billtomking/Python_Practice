import random
import logging

all = ['1','2','3','4','5','6','7','8','9']

qing = []

zong = []
for a in all:
    del all[int(a)]
    for b in all:
        del all[int(b)]
        for c in all:
            del all[int(c)]
            for d in all:
                del all[int(d)]
                for e in all:
                    del all[int(e)]
                    for f in all:
                        del all[int(f)]
                        for g in all:
                            del all[int(g)]
                            for h in all:
                                del all[int(h)]
                                for i in all:
                                    zong.append(a,b,c,d,e,f,g,h,i)
                                    zong = '',join(zong)
                                    qing.append(zong)


