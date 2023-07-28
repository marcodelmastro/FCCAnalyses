import numpy as np 
from matplotlib import pyplot as plt

x = [1 , 1.5, 2, 2.5] 

ycomplet = [6.613, 6.713, 6.822 , 6.924] 
ylljjvv = [16.79, 17.48, 18.49, 19.59]
yllvvjj = [8.929, 8.934, 8.951, 8.965]
yvvlljj = [8.744, 8.845, 8.920, 9.013]

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
    plt.ylabel(r'$\delta\Gamma_{H}/\Gamma_{H}$ (%)')
    plt.yscale('log')
    plt.title(r'Evolution of $\delta\Gamma_{H}/\Gamma_{H}$ while degrading neutral hadrons energy resolution', wrap = True)
    plt.grid(True, which='major', linestyle = '--')
    plt.grid(True, which='minor', linestyle = '--')
    plt.legend()
    plt.savefig("outputs/bilansmearlog.png")


else : 
    plt.plot(x,ylljjvv,'b^', label = r'lljj$\nu\nu$ channel') 
    plt.plot(x,yllvvjj,'g^', label = r'll$\nu\nu$jj channel') 
    plt.plot(x,yvvlljj,'y^', label = r'$\nu\nu$lljj channel') 
    plt.plot(x,ycomplet,'ro', label = 'Combination') 
    plt.axis([0.5, 3, 6, 20])
    plt.xlabel('Scale factor')
    plt.ylabel(r'$\delta\Gamma_{H}/\Gamma_{H}$ (%)')
    plt.title(r'Evolution of $\delta\Gamma_{H}/\Gamma_{H}$ while degrading neutral hadrons energy resolution', wrap = True)
    plt.grid(True, which='both', linestyle = '--')

    plt.legend()
    plt.savefig("outputs/bilansmearlin.png")
