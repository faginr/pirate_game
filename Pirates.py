from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Pirate Game")
title = Label(root, text='Pirate Game', width=20, borderwidth=5)
title.grid(row=0, column=0, columnspan=5)

pirate = ImageTk.PhotoImage(Image.open("/home/rex/Desktop/Code/Python/pirate_game/crate.png"))

# game board

# row 1
space_1_0 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_1_1 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_1_2 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_1_3 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_1_4 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")

# row 2
space_2_0 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_2_1 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_2_2 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_2_3 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_2_4 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")

# row 3
space_3_0 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_3_1 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_3_2 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_3_3 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_3_4 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")

# row 4
space_4_0 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_4_1 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_4_2 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_4_3 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_4_4 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")


# row 5
space_5_0 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_5_1 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_5_2 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_5_3 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")
space_5_4 = Button(root, image = pirate, text = '3', padx=0, pady=0, compound="top")



# draw row 1
space_1_0.grid(row=1,column=0)
space_1_1.grid(row=1,column=1)
space_1_2.grid(row=1,column=2)
space_1_3.grid(row=1,column=3)
space_1_4.grid(row=1,column=4)

# draw row 1
space_2_0.grid(row=2,column=0)
space_2_1.grid(row=2,column=1)
space_2_2.grid(row=2,column=2)
space_2_3.grid(row=2,column=3)
space_2_4.grid(row=2,column=4)

# draw row 3
space_3_0.grid(row=3,column=0)
space_3_1.grid(row=3,column=1)
space_3_2.grid(row=3,column=2)
space_3_3.grid(row=3,column=3)
space_3_4.grid(row=3,column=4)

# draw row 4
space_4_0.grid(row=4,column=0)
space_4_1.grid(row=4,column=1)
space_4_2.grid(row=4,column=2)
space_4_3.grid(row=4,column=3)
space_4_4.grid(row=4,column=4)

# draw row 5
space_5_0.grid(row=5,column=0)
space_5_1.grid(row=5,column=1)
space_5_2.grid(row=5,column=2)
space_5_3.grid(row=5,column=3)
space_5_4.grid(row=5,column=4)

output_message = Label(root, text='Player 1 place first pirate.', width=20, borderwidth=5)
output_message.grid(row=6, column=0, columnspan=5)

quit_button = Button(root, text="Exit", command=root.quit)
quit_button.grid(row=7, column=0, columnspan=5)

root.mainloop()
