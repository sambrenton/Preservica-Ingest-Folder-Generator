import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox

# Global variable for path
DIR = ''

# Global variables for GUI style elements
FONT = 'Verdana'

# Function to save the selected output directory to global variable DIR
def find_path():
    print('test')
    global DIR
    DIR = askdirectory()
    print(DIR)
    dir_label = tk.Label(frame2, text=f'Output folder: {DIR}', font=FONT)
    dir_label.grid(row=4 ,column=3)

# Function to retrieve folder prefix from user input field
def get_prefix():
    pre = i.get()
    return pre.strip()

# Function to retrieve folder quantity from user input field
def get_quantity():
    quantity = q.get()
    try:
        return int(quantity) + 1
    except ValueError:
        messagebox.showerror(title='Value Error', message='Please enter numeric value in quantity field')
        raise SystemExit

#Function to exit program via pop up window after completion
def popup():
    ok = messagebox.showinfo(title='Folders Generated', message='Folders Generated')
    if ok == 'ok':
        raise SystemExit

# Main function to create the folders
def make_path():
    folder = get_prefix()
    for x in range (1, get_quantity()):
        os.chdir(DIR)
        os.mkdir(f'{folder}-{x}')
        if prsv1.get():
            os.chdir(f'{DIR}\\{folder}-{x}')
            os.mkdir('Preservica_preservation1_lnk')
        if prsv2.get():
            os.chdir(f'{DIR}\\{folder}-{x}')
            os.mkdir('Preservica_preservation2_lnk')
        if prsn2.get():
            os.chdir(f'{DIR}\\{folder}-{x}')
            os.mkdir('Preservica_presentation2_lnk')
        if prsn3.get():
            os.chdir(f'{DIR}\\{folder}-{x}')
            os.mkdir('Preservica_presentation3_lnk')
    popup()
                    
# Set up GUI
root = tk.Tk()
root.title('Preservica Ingest Folder Generator')

# Frame for sub-folder cehckboxes
frame1 = tk.LabelFrame(root, text='Sub-folder options', font=FONT, padx=10, pady=10)
frame1.grid(row=5, column=0, padx=25)

# Frame for output directory button and text
frame2 = tk.LabelFrame(root)
frame2.grid(row=0, column=0, pady=25, padx=25)

# Frame for prefix text field
frame3 = tk.LabelFrame(root, text="Enter folder prefix eg. 'BTC123' ", font=FONT)
frame3.grid(pady=25, padx=25, row=1)

# Frame for quantity text field
frame4 = tk.LabelFrame(root, text='Enter quantity of required folders', font=FONT)
frame4.grid(pady=25, padx=25, row=2)

# Select Output Folder Button
output = tk.StringVar()
button = tk.Button(frame2, textvariable=output, command=lambda:find_path(), font=FONT, height=1, width=20)
output.set('Select Output Folder')
button.grid(column=0, row=4, padx=5, pady=5)

# Generate Folder Button
gen = tk.StringVar()
gen_button = tk.Button(root, textvariable=gen, command=lambda:make_path(), font=FONT, height=1, width=20)
gen.set('Generate Folders')
gen_button.grid(column=0, row=6, padx=25, pady=25)

# sub folder checkboxes
prsv1 = tk.BooleanVar()
sub_folders = tk.Checkbutton(frame1, text='Preservica_preservation1_lnk', variable=prsv1, font=FONT, onvalue=True, offvalue=False, pady=10)
sub_folders.grid(row=1, column=0)

prsv2 = tk.BooleanVar()
sub_folders = tk.Checkbutton(frame1, text='Preservica_preservation2_lnk', variable=prsv2, font=FONT, onvalue=True, offvalue=False, pady=10)
sub_folders.grid(row=2, column=0)

prsn2 = tk.BooleanVar()
sub_folders = tk.Checkbutton(frame1, text='Preservica_presentation2_lnk', variable=prsn2, font=FONT, onvalue=True, offvalue=False, pady=10)
sub_folders.grid(row=3, column=0)

prsn3 = tk.BooleanVar()
sub_folders = tk.Checkbutton(frame1, text='Preservica_presentation3_lnk', variable=prsn3, font=FONT, onvalue=True, offvalue=False, pady=10)
sub_folders.grid(row=4, column=0)

# Text field for folder prefix
i = tk.Entry(frame3, width=50)
i.grid(column=0, row=0)
input_text = i.get()

# Text field for quantity
q = tk.Entry(frame4, width=10)
q.grid(column=0, row=0)
input_quan = q.get()

root.mainloop()