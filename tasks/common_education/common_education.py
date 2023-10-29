from functools import reduce
import  math as m
x = [1.11, 1.13, 1.09, 1.05, 1.06]
x_med = 1.088
y = [1.07, 1.06,1.03,1.09,1.12]
y_med  = 1.074
z = [1.05, 1.08, 1.04, 1.11, 1.06]
z_med = 1.068

def comp_cov(x,x_m, y, y_m):
    sum = 0
    for i in range(5):
        sum+=  (x[i]-x_m)*(y[i]-y_m)

    return  sum/4
def comp_d (x,x_m):
    sum = 0
    for i in range(5):
        sum+= (x[i]-x_m)**2
    return  sum/4
def comp_dov_interval(x_m,x_d):
    return x_m- m.sqrt(x_d)/m.sqrt(5) * 2.776 , x_m+ m.sqrt(x_d)/m.sqrt(5) * 2.776


def comp_cov_matrix():
    pass
print(comp_d(z,z_med))
print(reduce(lambda x,y:x+y,z)/5)
print(reduce(lambda x,y: (x-x_med)**2, z)/4)
print(comp_cov(y,y_med,z,z_med)/(m.sqrt(0.0011)*m.sqrt(0.0007)))
print(comp_dov_interval(z_med, 0.0007
                        ))

