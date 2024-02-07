from tkinter import *
from ventana import *
from ventana import Ventana

def main():
    root = Tk()
    root.wm_title("Crud Python MySql")
    app = Ventana(root)
    app.mainloop()

if __name__ == "__main__":
    main() 