import numpy as np 
from matplotlib import pyplot as plt

x = [1 , 1.5, 2, 2.5] 

ycomplet = [0, 1.5, 3.2, 4.7]
ylljjvv = [0, 4.1, 10.1, 16.7]
yllvvjj = [0, 0.1, 0.2, 0.4]
yvvlljj = [0, 1.2, 2.0, 3.1]


plt.figure(figsize=(8,5))


scale = 'lin'

if scale == 'log': 

    default_x_ticks = range(len(x))
    plt.plot(default_x_ticks, ylljjvv,'b^', label = r'lljj$\nu\nu$ channel') 
    plt.plot(default_x_ticks, yllvvjj,'g^', label = r'll$\nu\nu$jj channel')
    plt.plot(default_x_ticks, yvvlljj,'y^', label = r'$\nu\nu$lljj channel') 
    plt.plot(default_x_ticks, ycomplet,'ro', label = 'Combination') 
    plt.xticks(default_x_ticks, x)

    plt.xlabel('Scale factor')
    plt.ylabel(r'Degradation of precision on $\Gamma_{H}$ (%)')
    plt.yscale('log')
    plt.title(r'Degradation of precision on $\Gamma_{H}$ (while degrading neutral hadrons energy resolution)', wrap = True)
    plt.grid(True, which='major', linestyle = '--')
    plt.grid(True, which='minor', linestyle = '--')
    plt.legend()
    plt.savefig("outputs/deltagammalog.png")


else : 
    default_x_ticks = range(len(x))
    plt.plot(default_x_ticks, ylljjvv,'b^', label = r'lljj$\nu\nu$ channel') 
    plt.plot(default_x_ticks, yllvvjj,'g^', label = r'll$\nu\nu$jj channel')
    plt.plot(default_x_ticks, yvvlljj,'y^', label = r'$\nu\nu$lljj channel') 
    plt.plot(default_x_ticks, ycomplet,'ro', label = 'Combination') 
    plt.xticks(default_x_ticks, x)
    plt.xlabel('Scale factor')
    plt.ylabel(r'Degradation of precision on $\Gamma_{H}$ (%)')
    plt.title(r'Degradation of precision on $\Gamma_{H}$ (while degrading neutral hadrons energy resolution)', wrap = True)
    plt.grid(True, which='both', linestyle = '--')

    plt.legend()
    plt.savefig("outputs/deltagammalin.png")
