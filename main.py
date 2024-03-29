from tkinter import *
from PIL import Image, ImageTk
from tkinter import font

# ========================================
# figure out how to remove default text when you click into the text box
# change mouse pointer to hand when hovering button
# create csv file to save list on close
# add item to list when Enter is hit
# ========================================

TITLE_FONT = ('Segoe Script', 25, "bold")
BODY_FONT = ("Courier", 13, "bold")
LIGHT_PINK = "#FEECE9"
DARK_PINK = "#FE7E6D"
LIGHT_BLUE = "#CCD1E4"
DARK_BLUE = "#2F3A8F"

num_of_items = 1
all_buttons = []
placement = 0
list_items = []


def add_item():
    """add item to the to do list, replace finished item, or send warning if too many items"""
    global num_of_items
    global all_buttons
    global placement
    global list_items

    # keep adding new tasks if there are less than 8
    if num_of_items < 8:
        add_to_list = new_item.get()
        # add new list item to list of tasks
        list_items.append(Label(text=add_to_list, font=BODY_FONT, bg=LIGHT_PINK, fg=DARK_PINK))
        list_items[-1].config(pady=10)
        list_items[-1].grid(column=1, row=num_of_items)
        # add new button to list of buttons
        all_buttons.append(Button(image=final_incomplete, borderwidth=0, bg=LIGHT_PINK, command=lambda var=placement: complete_task(var)))
        all_buttons[-1].grid(column=0, row=num_of_items)
        # increment placement to track where button is in buttons list
        placement += 1
        # increment num_of_items to keep track of which row each item should be placed on
        num_of_items += 1
    else:
        i = 0
        space = False
        keep_checking = True

        # check to find first completed task and replace with new task
        for button in all_buttons:
            if button['image'] == 'pyimage2' and keep_checking:
                button['image'] = final_incomplete
                list_items[i]['text'] = new_item.get()
                space = True
                keep_checking = False
            i += 1

        # if there is no space left after replacing a completed item, send warning message
        if not space:
            warning = Toplevel()
            warning.title("Finish tasks")
            warning.config(bg=LIGHT_PINK, pady=20)
            label = Label(warning, text="Please complete a task before adding more.\n\nYou can do this!", font=BODY_FONT, fg=DARK_BLUE, bg=LIGHT_PINK)
            label.grid(column=0, row=0, padx=20, pady=10)
            okay = Button(warning, text="Back to ToDo List", bg=LIGHT_BLUE, fg=DARK_BLUE, command=warning.destroy)
            okay.grid(column=0, row=1, padx=20, pady=10)

    # reset default text in input box
    new_item.delete(0, 'end')
    new_item.insert(0, "Add new item...")


def complete_task(index):
    """loop through all_buttons and replace incomplete pic with complete pic"""
    global all_buttons
    for i in range(len(all_buttons)):
        if i == index:
            all_buttons[i]['image'] = final_check


window = Tk()
window.title("ToDo")
window.config(bg=LIGHT_PINK)
window.config(pady=20, padx=20)

title_label = Label(text="ToDo :", font=TITLE_FONT, bg=LIGHT_PINK, fg=DARK_BLUE)
title_label.grid(column=0, row=0)

# Prepare incomplete, complete, and pencil pictures
incomplete_button = Image.open('Hands - Denied.png')
incomplete = incomplete_button.resize((40, 40), Image.ANTIALIAS)
final_incomplete = ImageTk.PhotoImage(incomplete)

check_button = Image.open('Hands - Checkmark.png')
check = check_button.resize((40, 40), Image.ANTIALIAS)
final_check = ImageTk.PhotoImage(check)

add_button = Image.open('Hands - Pencil 1.png')
add = add_button.resize((90, 50), Image.ANTIALIAS)
final_add = ImageTk.PhotoImage(add)

######### image of woman reading, might add back in later
# canvas = Canvas(width=175, height=113, bg=LIGHT_PINK, highlightthickness=0)
# reading_pic = Image.open('ReadingSideDoodle.png')
# new_reading_pic = reading_pic.resize((175, 113), Image.ANTIALIAS)
# final_reading_pic = ImageTk.PhotoImage(new_reading_pic)
# canvas.create_image(88, 57, image=final_reading_pic)
# canvas.grid(column=1, row=7)

new_item = Entry(width=30, fg=DARK_BLUE, bg=LIGHT_BLUE)
new_item.insert(0, "Add new item...")
new_item.grid(column=1, row=8)

add_button = Button(image=final_add, bg=LIGHT_PINK, fg=LIGHT_PINK, borderwidth=0, command=add_item)
add_button.grid(column=2, row=8)

# print tuple of all font families
# print(font.families())

window.mainloop()
