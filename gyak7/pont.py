import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

class Pont:
    def __init__(self, x=0, y=0):
        """
            Létrehoz egy új (x,y) pontot,
            ha nem adjuk meg az értéküket,
            akkor a pontot az origóba teszi.
        """
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Pont({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def origotol_mert_tavolsag(self):
        """
            A pont origótól mért távolsága.
        """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def tavolsag_masik_ponttol(self, other):
        """
            Euklideszi távolság az other ponttól.
        """
        return (((self.x-other.x) ** 2) + ((self.y -other.y) ** 2)) ** 0.5
    
    def plot_pont(self):
        plt.scatter([self.x],[self.y])
        plt.scatter([0],[0], marker='x')
        max_coord=max(self.x,self.y)
        plt.ylim((-2*max_coord,2*max_coord))
        plt.xlim((-2*max_coord,2*max_coord))
        
    