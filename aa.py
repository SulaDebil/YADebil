class train:
    def __init__(self, tra, punkt, nomer, time, obzh, kupe, plaz):
        self.tra=tra
        self.punkt = punkt
        self.nomer = nomer
        self.time = time
        self.obzh = obzh
        self.kupe = kupe
        self.plaz = plaz

        def tramp(self, punkt):
            if punkt == "Moscow":
                print(self.tra)

        def yaer(self, punkt, time):
            if punkt == "Moscow" and time > 15:
                print(self.tra)

        def last(self, punkt, obzh):
            if punkt == "Moscow" and obzh > 0:
                print(self.tra)
q=train(1,"Moscow",1,12,1,5,9)
w=train(2,"Astana",2,13,2,5,9)
e=train(3,"Moscow",3,15,10,5,9)
r=train(4,"Astana",4,14,9,5,9)
t=train(5,"Moscow",5,13,0,5,9)
y=train(6,"Moscow",6,17,0,5,99)
u=train(7,"Moscow",7,18,0,5,9)
i=train(8,"Astana",8,19,7,5,9)
o=train(9,"Moscow",9,20,3,5,9)
c=[q,w,e,r,t,y,u,i,o] 
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
            
