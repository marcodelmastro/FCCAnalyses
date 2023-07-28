import numpy as np 
from matplotlib import pyplot as plt

x = [1 , 1.5, 2, 2.5] 

ycomplet = [6.613, 6.713, 6.822 , 6.924] 
ylljjvv = [16.79, 17.48, 18.49, 19.59]
yllvvjj = [8.929, 8.934, 8.951, 8.965]
yvvlljj = [8.744, 8.845, 8.920, 9.013]


plt.figure(figsize=(8,8))

plt.subplot(221)
plt.plot(x,ylljjvv,'bo') 
plt.xlabel('Value of the scale factor')
plt.ylabel('$\delta\Gamma_{H}/\Gamma_{H}$ (%)')
plt.axis([0.5, 3, 16.7, 20.0])
plt.grid(True)
plt.text(0.6, 19.7, 'Channel lljjvv', color = 'b')

#plt.title('Channel lljjvv')

plt.subplot(222)
plt.plot(x,yllvvjj,'go') 
plt.xlabel('Value of the scale factor')
plt.ylabel('$\delta\Gamma_{H}/\Gamma_{H}$ (%)')
plt.axis([0.5, 3, 8.920, 8.970])
plt.grid(True)
plt.text(0.6, 8.966, 'Channel llvvjj', color = 'g')
#plt.title('Channel llvvjj')

plt.subplot(223)
plt.plot(x,yvvlljj,'yo') 
plt.xlabel('Value of the scale factor')
plt.ylabel('$\delta\Gamma_{H}/\Gamma_{H}$ (%)')
plt.axis([0.5, 3, 8.70, 9.10])
plt.grid(True)
plt.text(0.6, 9.07, 'Channel vvlljj', color = 'y')
#plt.title('Channel vvlljj')

plt.subplot(224)
plt.plot(x,ycomplet,'ro') 
plt.xlabel('Value of the scale factor')
plt.ylabel('$\delta\Gamma_{H}/\Gamma_{H}$ (%)')
plt.axis([0.5, 3, 6.6, 7.0])
plt.grid(True)
plt.text(0.6, 6.97, 'Three channels', color = 'r')
#plt.title('Channel lljjvv')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
plt.suptitle('Evolution of $\delta\Gamma_{H}/\Gamma_{H}$ while degrading perfomances on neutral hadrons energy', wrap = True)

#plt.plot(x,ycomplet,'bo') 
#plt.xlabel('Value of the scale factor')
#plt.ylabel('Uncertainty on the Higgs width (%)')
#plt.axis([0.5, 3, 6.6, 7.0])
#plt.text(1, 6.75, r'$30\% / \sqrt{E}$')
#plt.title('Evolution of $\delta\Gamma_{H}$ while degrading performances on neutral hadrons energy',wrap=True)
#plt.grid(True)
plt.savefig("outputs/bilansmear4plots.png")
