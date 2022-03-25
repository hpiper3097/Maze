from matplotlib import pyplot as plt, animation

class MazeAnimator:
    def __init__(self):
        self.maze = []
        self.t = []

    def render(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Sheesh') 
        cax = ax.pcolormesh(self.maze, vmin=0, vmax=1, cmap='Pastel1')

        #animation stuff here

        plt.draw()
        plt.show()

    def set_maze(self, maze):
        self.maze = maze

    def set_t(self, t):
        self.t = np.array(t)

    def set_start(self, start):
        self.start = start

def main():
    print('Do not execute self as a script.')

if __name__ == '__main__':
    main()
        