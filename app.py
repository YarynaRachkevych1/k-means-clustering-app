import tkinter as tk
from choose_points import ChoosePoints
from clustering import clustering

POINTS_POS_PATH = 'points_positions.txt'

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("350x250")
        
        button_width = 20
        button_height = 5

        self.points_button = tk.Button(root, text="Choose points", command=self.choose_points, width=button_width, height=button_height)
        self.points_button.pack(pady=20)

        self.clustering_button = tk.Button(root, text="Do clustering", command=self.do_clustering, width=button_width, height=button_height)
        self.clustering_button.pack(pady=20)


    def choose_points(self):
        ChoosePoints(POINTS_POS_PATH)

    def do_clustering(self):
        clustering(POINTS_POS_PATH, self.clusters_num)

    def show_main_menu(self):
        self.root.deiconify() 
        
def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
