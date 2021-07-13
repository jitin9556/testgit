def cube_root(x):


    for num1 in range(1,100):
        for num2 in range(1,100):
            for num3 in range(1,100):
                

                if num1 == num2 and num2 == num3:
                    if num1*num2*num3 == x:

                        print('这个数的3次开方是：%d'%(num1)) 
                    else:
                        
                        break
                       

             
                    
cube_root(x=int(input("输入数字：")))





    

    
    





