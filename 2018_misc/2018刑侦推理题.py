def say():
    print(q0)
    print(q1)
    print(q2)
    print(q3)
    print(q4)
    print(q5)
    print(q6)
    print(q7)
    print(q8)
    print(q9)
    print(b[0], b[1], b[2], b[3])

for q0 in range(4):
    for q1 in range(4):
        for q2 in range(4):
            for q3 in range(4):
                for q4 in range(4):
                    for q5 in range(4):
                        for q6 in range(4):
                            for q7 in range(4):
                                for q8 in range(4):
                                    for q9 in range(4):
                                        b = [0, 0, 0, 0]
                                        b[q0] += 1;
                                        b[q1] += 1;
                                        b[q2] += 1;
                                        b[q3] += 1;
                                        b[q4] += 1;
                                        b[q5] += 1;
                                        b[q6] += 1;
                                        b[q7] += 1;
                                        b[q8] += 1;
                                        b[q9] += 1;
                                        if((q1==0 and q4==2) or (q1==1 and q4==3)or(q1==2 and q4==0) or (q1==3 and q4==1)):
                                            if((q2==0 and q5==q1 and q1==q3 and q2!=q1) or (q2==1 and q2==q1 and q1==q3 and q5!=q1)or (q2==2 and q2==q5 and q5==q3 and q1!=q2)or (q2==3 and q2==q5 and q5==q1 and q3!=q2 )):
                                                if(q3==0 and q0==q4 or q3==1 and q1==q6 or q3==2 and q0==q8 or q3==3 and q5==q9 ):
                                                    if(q4==0 and q7==0 or q4==1 and q3==1 or q4==2 and q8==2 or q4==3 and q6==q4):
                                                        if(q5==0 and q1==q3 and q1==q7 or q5==1 and q7==q0 and q7==q5 or q5==2 and q7==q2 and q7==q9 or q5==3 and q7==q4 and q7==q8  ):
                                                            if(q6==0 and b[2]<=b[1] and b[2]<=b[3] and b[2]<=b[0] or q6==1 and b[1]<=b[0] and b[1]<=b[3] and b[1]<=b[2] or q6==2 and b[0]<=b[1] and b[0]<=b[3] and b[0]<=b[2] or q6==3 and b[3]<=b[1] and b[3]<=b[2] and b[3]<=b[0] ):
                                                                if(q7==0 and q6!=q0+1 and q6!=q0-1 or q7==1 and q4!=q0+1 and q4!=q0-1 or q7==2 and q1!=q0+1 and q1!=q0-1 or q7==3 and q9!=q0+1 and q9!=q0-1    ):

                                                                    if(q0==q5):
                                                                        if(q8==0 and q5!=q4 or q8==1 and q4!=q9 or q8==2 and q4!=q1 or q8==3 and q8!=q4 ):
                                                                            zz=max(b)-min(b)
                                                                            if(q9==0 and zz==3 or q9==1 and zz==2 or q9==2 and zz==4 or q9==3 and zz==1):
                                                                                say()

                                                                    else:
                                                                        if (q8 == 0 and q5 == q4 or q8 == 1 and q4 == q9 or q8 == 2 and q4 == q1 or q8 == 3 and q8 == q4):
                                                                            zz = max(b) - min(b)
                                                                            if (q9 == 0 and zz == 3 or q9 == 1 and zz == 2 or q9 == 2 and zz==4 or q9 == 3 and zz==1):
                                                                                say()



