# Random Colour Generator, GTT, 18/03
# v1 - Interface...
# v3 - Colour box GUI
# v4 - Canvas adjustment experiment...
# v5 - Set maximum number of bits and put in error message label (max should be 11 bits).
# v7 - makes text white for dark colours and black for light colours.

# To do...
# ? Make code efficient...


from tkinter import *
import random


class MakeChart:
    def __init__(self, parent):
        # *** GUI Frame Set Up ***
        self.generator_frame = Frame(parent)
        self.generator_frame.grid()

        # *** GUI ***

        self.heading_label = Label(self.generator_frame, text="Colour Generator", font="arial 16 bold")
        self.heading_label.grid(row=0)

        self.bits_label = Label(self.generator_frame, text="How many bits?")
        self.bits_label.grid(row=1)

        # Red / Green / Blue Choice Labels / boxes
        self.choose_frame = Frame(self.generator_frame, padx=10, pady=10)
        self.choose_frame.grid(row=2)

        self.red_bits = StringVar()
        self.red_bits.set("1")
        self.red_bits_label = Label(self.choose_frame, text="Red: ")
        self.red_bits_label.grid(row=0, column=0)
        self.red_bits_entry = Entry(self.choose_frame, width=5, textvariable=self.red_bits)
        self.red_bits_entry.grid(row=0, column=1)

        self.green_bits = StringVar()
        self.green_bits.set("1")
        self.green_bits_label = Label(self.choose_frame, text="Green: ")
        self.green_bits_label.grid(row=1, column=0)
        self.green_bits_entry = Entry(self.choose_frame, width=5, textvariable=self.green_bits)
        self.green_bits_entry.grid(row=1, column=1)

        self.blue_bits = StringVar()
        self.blue_bits.set("1")
        self.blue_bits_label = Label(self.choose_frame, text="Blue: ")
        self.blue_bits_label.grid(row=2, column=0)
        self.blue_bits_entry = Entry(self.choose_frame, width=5, textvariable=self.blue_bits)
        self.blue_bits_entry.grid(row=2, column=1)

        # Do It Button
        self.doit_button = Button(self.generator_frame, text="do it", width=10, font="arial 12 bold",
                                  bg="white", command=self.to_chart)
        self.doit_button.grid(row=3, padx=10, pady=10)

        # Help / Quit Buttons go here...
        self.button_frame = Frame(self.generator_frame)
        self.button_frame.grid(row=4, pady=10)

        self.help_btn = Button(self.button_frame, text="Help", font="Arial 12 bold",
                               padx=2, pady=2, bg="navajo white", command=self.var_help)
        self.help_btn.grid(row=0, column=1)

        self.quit_btn = Button(self.button_frame, text="Quit",
                               font="Arial 12 bold", padx=2, pady=2,
                               fg="white", bg="maroon", command=root.destroy)
        self.quit_btn.grid(row=0, column=2)

    def to_chart(self):
        self.var_red_bits = self.red_bits.get()
        self.var_green_bits = self.green_bits.get()
        self.var_blue_bits = self.blue_bits.get()

        ok = "yes"

        # Check red bits entry...
        try:
            int(self.var_red_bits)
            if int(self.var_red_bits) < 0:
                ok = "no"
                self.red_bits_entry.config(bg="pink")
                self.bits_label.config(text="Too small", fg="red", font="arial 10 bold")
            elif int(self.var_red_bits) > 8:
                ok = "no"
                self.red_bits_entry.config(bg="pink")
                self.bits_label.config(text="Too big", fg="red", font="arial 10 bold")
            else:
                self.red_bits_entry.config(bg="white")

        except ValueError:
            ok = "no"
            self.red_bits_entry.config(bg="pink")
            self.bits_label.config(text="Enter an Integer", fg="red", font="arial 10 bold")

        # Check green bit entry...
        try:
            int(self.var_green_bits)
            if int(self.var_green_bits) < 0:
                ok = "no"
                self.green_bits_entry.config(bg="pink")
                self.bits_label.config(text="Too small", fg="green", font="arial 10 bold")
            elif int(self.var_green_bits) > 8:
                ok = "no"
                self.green_bits_entry.config(bg="pink")
                self.bits_label.config(text="Too big", fg="green", font="arial 10 bold")
            else:
                self.green_bits_entry.config(bg="white")

        except ValueError:
            ok = "no"
            self.green_bits_entry.config(bg="pink")
            self.bits_label.config(text="Enter an Integer", fg="green", font="arial 10 bold")

        # Check blue bit entry...
        try:
            int(self.var_blue_bits)
            if int(self.var_blue_bits) < 0:
                ok = "no"
                self.blue_bits_entry.config(bg="pink")
                self.bits_label.config(text="Too small", fg="blue", font="arial 10 bold")
            elif int(self.var_blue_bits) > 8:
                ok = "no"
                self.blue_bits_entry.config(bg="pink")
                self.bits_label.config(text="Too big", fg="blue", font="arial 10 bold")
            else:
                self.blue_bits_entry.config(bg="white")

        except ValueError:
            ok = "no"
            self.blue_bits_entry.config(bg="pink")
            self.bits_label.config(text="Enter an Integer", fg="blue", font="arial 10 bold")

        # Check that total # of bits is less than 12
        try:
            total = int(self.var_red_bits) + int(self.var_green_bits) + int(self.var_blue_bits)
            if total > 11:
                ok = "no"
                self.bits_label.config(text="Too many bits", fg="red", font="arial 10 bold")

            if ok == "yes":
                Display(self.var_red_bits, self.var_green_bits, self.var_blue_bits)
                self.generator_frame.destroy()
        except ValueError:
            print()

    def var_help(self):
            get_help = Help()
            get_help.help_text.configure(text="Choose the number of bits and then generate a colour chart")

class Display:
    def __init__(self, red_bits, green_bits, blue_bits):

        # converts integers to hex values
        def makehex(value):
            value = hex(int(value))
            # print(value)
            str(value)
            if len(value) == 3:
                value = value.replace("0x", "0")
            else:
                value = value.replace("0x0", "0")
                value = value.replace("0x1", "1")
                value = value.replace("0x2", "2")
                value = value.replace("0x3", "3")
                value = value.replace("0x4", "4")
                value = value.replace("0x5", "5")
                value = value.replace("0x6", "6")
                value = value.replace("0x7", "7")
                value = value.replace("0x8", "8")
                value = value.replace("0x9", "9")
                value = value.replace("0xa", "a")
                value = value.replace("0xb", "b")
                value = value.replace("0xc", "c")
                value = value.replace("0xd", "d")
                value = value.replace("0xe", "e")
                value = value.replace("0xf", "f")

            return value

        red = int(red_bits)
        green = int(green_bits)
        blue = int(blue_bits)

        # makes colours...
        if red > 0:
            red_colors = 2 ** red
            red_factor = 255 // (red_colors - 1)

        if green > 0:
            green_colors = 2 ** green
            green_factor = 255 // (green_colors - 1)

        if blue > 0:
            blue_colors = 2 ** blue
            blue_factor = 255 // (blue_colors - 1)

        red_parts = [0]
        green_parts = [0]
        blue_parts = [0]

        # gets possible rgb values for amount of bits
        if red > 0:
            for item in range(1, red_colors):
                value = item * red_factor
                red_parts.append(value)

        if green > 0:
            for item in range(1, green_colors):
                value = item * green_factor
                green_parts.append(value)

        if blue > 0:
            for item in range(1, blue_colors):
                value = item * blue_factor
                blue_parts.append(value)

        # Generates hex colour codes
        code_list = []
        dark_value = []
        color_code = ""
        for red_item in range(0, len(red_parts)):
            red_value_int = red_parts[red_item]
            red_value = makehex(red_value_int)

            for green_item in range(0, len(green_parts)):
                green_value_int = green_parts[green_item]
                green_value = makehex(green_value_int)

                for blue_item in range (0, len(blue_parts)):
                    blue_value_int = blue_parts[blue_item]
                    blue_value = makehex(blue_value_int)

                    colour_code = "#"+red_value + green_value + blue_value
                    code_list.append(colour_code)

                    dark_bright = red_value_int + green_value_int + blue_value_int
                    dark_value.append(dark_bright)


        ### GUI Set Up...

        self.color_box = Toplevel()

        self.outer_frame = Frame(self.color_box)
        self.outer_frame.grid()

        self.frame = Frame(self.outer_frame)
        self.frame.grid(row = 0)

        canvas_height=len(code_list) * 5
        self.canvas=Canvas(self.frame, bg='#FFFFFF', width=960,
                           height=500, scrollregion=(0, 0, 2500, canvas_height))

        vbar=Scrollbar(self.frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)

        self.canvas.config(yscrollcommand=vbar.set)

        self.colour_blocks = Frame(self.canvas)

        # The window below is in the canvas and is needed for scrolling.
        self.canvas.create_window((0,0), window=self.colour_blocks, anchor="nw")
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)

        # set up colour lables...
        NUM_COL = 8

        for i in range(len(code_list)):

            dark_int = dark_value[i]
            if dark_int < 254:
                text_color = "#ffffff"
            else:
                text_color = "#000000"

            lbl = Label(self.colour_blocks, bg=code_list[i], text=code_list[i], fg=text_color, padx=10,
                        pady=10, width=12)
            lbl.grid(row=i // NUM_COL, column=i % NUM_COL)

        self.back_button = Button(self.outer_frame, text="back", font="arial 16 bold", bg="white",
                                  command=self.back)
        self.back_button.grid(row=3)

        self.length_label = Label(self.outer_frame, text="Colours Generated: {}".format(len(code_list)),
                                  font="arial 12 bold")
        self.length_label.grid(row=4)

    def back(self):
        MakeChart(root)
        self.color_box.destroy()


class Help:
    def __init__(self):

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        how_heading = Label(self.help_frame, text="Help / Instructions", font="arial 10 bold")
        how_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, wrap=250)
        self.help_text.grid(column=0, row=1)

        dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange", font="arial 10 bold",
                             command=self.close_help)
        dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Chart Generator")
    Generate = MakeChart(root)
    root.mainloop()
