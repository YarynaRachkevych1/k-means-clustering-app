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

        self.points_button = tk.Button(root, text="1. Choose points", command=self.choose_points, width=button_width, height=button_height)
        self.points_button.pack(pady=20)

        self.clustering_button = tk.Button(root, text="2. Do clustering", command=self.do_clustering, width=button_width, height=button_height)
        self.clustering_button.pack(pady=20)

        self.clusters_num = None

    def choose_points(self):
        ChoosePoints(POINTS_POS_PATH)
        self.ask_for_clusters()

    def ask_for_clusters(self):
        self.input_window = tk.Toplevel(self.root)
        self.input_window.title("Enter number of clusters")
        self.input_window.geometry("300x150")

        label = tk.Label(self.input_window, text="Enter number of clusters you want to have:")
        label.pack(pady=10)

        # Entry field for input
        self.cluster_input = tk.Entry(self.input_window)
        self.cluster_input.pack(pady=10)

        # Submit button
        submit_button = tk.Button(self.input_window, text="Submit", command=self.save_cluster_num)
        submit_button.pack(pady=10)

    def save_cluster_num(self):
        try:
            self.clusters_num = int(self.cluster_input.get())
            print(f"Number of clusters set to: {self.clusters_num}")
            self.input_window.destroy() 
        except ValueError:
            print("Please enter a valid integer.")

    def do_clustering(self):
        if self.clusters_num is not None:
            clustering(POINTS_POS_PATH, self.clusters_num)
        else:
            print("Please choose points and enter the number of clusters first.")

    def show_main_menu(self):
        self.root.deiconify()

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
