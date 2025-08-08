import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello World")

    # Create a label with the text "Hello, world!"
    label = tk.Label(root, text="Hello, world!", padx=20, pady=20)
    label.pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
