print ("Введите x"); x=float(input())
print ("Введите y"); y=float(input())
if (x > 0 and y > 0) :
     print("Точка в 1 четверти")
elif (x < 0 and y>0) :
     print("Точка в 2 четверти")
elif (x<0 and y<0) : 
     print("Точка в 3 четверти")
elif (x>0 and y<0) :
     print("Точка в 4 четверти")
elif (x==0 and y!=0) :
     print("Точка на оси Y")
elif (x!=0 and y==0) :
     print("Точка на оси X")