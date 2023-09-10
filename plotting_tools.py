import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import numpy as np

def bode(exp,freq:np.ndarray) -> Figure:

    fig:Figure
    mag:plt.Axes
    pha:plt.Axes
    fig, [mag,pha] = plt.subplots(nrows=2,ncols=1)
    pha.sharex(mag)

    output = exp(freq)
    magnitude = np.sqrt(np.real(output) +np.imag(output))
    phase = np.arctan(np.imag(output)/np.real(output))
    
    mag.plot(freq,magnitude)
    pha.plot(freq,phase)

    return fig

    


    



class TooManyDependantsError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def main():
    f = lambda a: a+1
    freq = np.logspace(1,2,100,base=10)
    bode(f,freq)

if __name__ == "__main__":
    main()