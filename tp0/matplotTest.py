import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0 , 2* np . pi , 30)

y1 = np.cos( x )
y2 = np.sin( x )

plt.plot (x , y1 , "r--" , label=" cos( x )" )
plt.plot (x , y2 , "b:o" , label=" sin( x )" )

plt.axis("equal")
plt.legend()
plt.title("TITRE")

plt.show()