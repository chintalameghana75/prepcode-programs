
data= input()
data=data.split()
salary=int(data[0])
hir=int(data[1]*salary/100)
da=int(data[3]*salary/100)
pf=int(data[3]*salary/100)
allowence=(data[4])
if allowence=='a':
    print(salary+hir+da+pf+1500)
elif allowence=='b':
    print(salary+hir+da+-pf+1700)
else:
    print(salary+hir+da+-pf+200)