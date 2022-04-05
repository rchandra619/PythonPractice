import numpy as np

a = 56
t1 = (20,30,40)
t2 = (40 ,50 ,60)

t_combine = t1 + t2
t_combine = 3*t_combine

print(3*t_combine[2])
list1 = {5,6,78,2}
list2 = {56,89,32,5}
#l3 = list2 + list1
#print(list1[0]*3)


class Demo1:
    # a =56
    b = 45

    def adding(self, x):
        return x + self.a

class NumPyExamples:

    aa = np.arange(40,70,3)
    #print(aa)
    ab = np.linspace(40,76,26)
    #print(ab)
    def ranmdom_numpy(self):
        a3 = np.random.randn(5,4,3,5)
        # 0.41375006
        print(a3)

ne = NumPyExamples()
ne.ranmdom_numpy()