from MergeSort import *
from BinarySearch import *
from Btree import *
from tkinter import *

B = BTree(4)
mergearr = []
rankCol = "#F8F1F1"

window = Tk()
window.title("B-Tree, Merge Sort and Binary Search")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg="#EFF8FF")
# window.grid_columnconfigure(4, minsize=100)


#############################################################################################################################################
# Create Frame 01 for the b Tree.
frame01 = LabelFrame(window, text="B-Tree", font=("bold",
                                                  15), bg="#EFF8FF", padx=5, pady=5)
frame01.grid(row=0, column=0, padx=5, pady=5)
frame01.grid_rowconfigure(10, minsize=100)
frame01.grid_rowconfigure(4, minsize=100)

# Create Frame 02 for the Merge Sort and binary search.
frame02 = LabelFrame(window, text="Merge Sort and Binary Search", font=(
    "bold", 15), bg="#EFF8FF", padx=5, pady=5)
frame02.grid(row=0, column=1, padx=5, pady=5)
frame02.grid_rowconfigure(10, minsize=100)
frame02.grid_rowconfigure(4, minsize=100)
global frame03
frame03 = Frame(frame01, bg="#EFF8FF", padx=5, pady=5)
frame03.grid(row=9, column=0, padx=5, pady=5)

frame04 = Frame(frame02, bg="#EFF8FF", padx=5, pady=5)
frame04.grid(row=9, column=0)

# B Tree Frame.
#############################################################################################################################################

# insert Button function.


def buttonclick():
    B.insert((int(marks.get()), name.get()))
    arr = []
    B.traverse(B.root, arr)
    marks.delete(0, 'end')
    name.delete(0, 'end')
    x = 1
    for i in range(-1, -len(arr)-1, -1):
        myLabel1 = Label(frame03, text=f"{x}. {arr[i][1]} : {arr[i][0]}",
                         anchor='w', relief=GROOVE, width=25, font=("bold", 15), bg=rankCol)
        myLabel1.grid(row=x, column=0)
        x = x + 1


# Rank Label
Label(frame01, text="Rank", anchor='w', relief=GROOVE, width=25,
      font=("bold", 15), bg=rankCol, pady=2).grid(row=8, column=0)


# search Button function.
def searchClick():
    global myLabelS
    tup = B.search_key(int(markForSearch.get()))
    myLabelS = Label(frame01, text=f"{tup[1]} : {tup[0]}", anchor='w',
                     relief=GROOVE, width=15, font=("bold", 15), bg=rankCol)
    myLabelS.grid(row=6, column=1)
    markForSearch.delete(0, 'end')


# Insert Button
insertButton = Button(frame01, text="Insert", command=buttonclick,
                      bg="#A6A9B6", font=("bold", 15), width=15)
insertButton.grid(row=3, column=1, padx=10, pady=10)

# Label(frame01,text="B-Tree",font=("bold",15),bg="#EFF8FF").grid(row=0,column=0)

# Name label and text box
name = Entry(frame01, font=(14),   width=15)
name.grid(row=1, column=1)
l_name = Label(frame01, text="Name", font=("bold", 15), bg="#EFF8FF")
l_name.grid(row=1, column=0)

# Marks Lable And Text box
marks = Entry(frame01, font=(14), width=15)
marks.grid(row=2, column=1)
l_marks = Label(frame01, text="Marks", font=("bold", 15), bg="#EFF8FF")
l_marks.grid(row=2, column=0)

# search marks Lable and Text Box.
Label(frame01, text="Search Marks", font=(
    "bold", 15), bg="#EFF8FF").grid(row=4, column=0)
markForSearch = Entry(frame01, font=(14), width=15)
markForSearch.grid(row=4, column=1)

# search marks Button.
search_by_marks = Button(frame01, text="Search", command=searchClick,
                         bg="#A6A9B6", font=("bold", 15), width=15)
search_by_marks.grid(row=5, column=1)

# Reset button


def reset1():
    global frame03
    frame03.destroy()
    try:
        myLabelS.destroy()
    except Exception:
        pass
    frame03 = Frame(frame01, bg="#EFF8FF", padx=5, pady=5)
    frame03.grid(row=9, column=0)
    global B
    B = BTree(4)


# destroy
myLabelDes = Button(frame01, text="Reset", command=reset1,
                    bg="#A6A9B6", font=("bold", 15), width=15)
myLabelDes.grid(row=10, column=0)

###########################################################################################
# delete Button.


def deleteMarks():
    global B
    global frame03
    frame03.destroy()
    frame03 = Frame(frame01, bg="#EFF8FF", padx=5, pady=5)
    frame03.grid(row=9, column=0)
    B.delete(B.root, B.search_key(int(markForDelete.get())))
    x = 1
    arr = []
    B.traverse(B.root, arr)
    for i in range(-1, -len(arr)-1, -1):
        myLabel1 = Label(frame03, text=f"{x}. {arr[i][1]} : {arr[i][0]}",
                         anchor='w', relief=GROOVE, width=25, font=("bold", 15), bg=rankCol)
        myLabel1.grid(row=x, column=0)
        x = x + 1
    markForDelete.delete(0, 'end')


# Delete marks Lable and Text Box.
Label(frame01, text="Delete Marks", font=(
    "bold", 15), bg="#EFF8FF").grid(row=12, column=0)
markForDelete = Entry(frame01, font=(14), width=15)
markForDelete.grid(row=12, column=1)

# delete marks Button.
delete_by_marks = Button(frame01, text="Delete", command=deleteMarks,
                         bg="#A6A9B6", font=("bold", 15), width=15)
delete_by_marks.grid(row=13, column=1)
################################################################################################

# Merege Sort and Binary search frame 02
##################################################################################################################################################

# button click function for insert


def buttonclick2():
    global mergearr
    mergearr.append((int(marks2.get()), name2.get()))
    mergearr = mergeSort(mergearr)
    marks2.delete(0, 'end')
    name2.delete(0, 'end')
    x = 1
    for i in mergearr:
        myLabel = Label(frame04, text=f"{x}. {i[1]} : {i[0]}", anchor='w',
                        relief=GROOVE, width=25, font=("bold", 15), bg=rankCol)
        myLabel.grid(row=x+8, column=0)
        x = x + 1


# rank lable
Label(frame02, text="Rank", anchor='w', relief=GROOVE, width=25,
      font=("bold", 15), bg=rankCol, pady=2).grid(row=8, column=0)

# button click function for search.


def searchClick2():
    global mergearr
    temp = []
    global myLabelS2
    for i in range(-1, -len(mergearr)-1, -1):
        temp.append(mergearr[i])
    tup = binarySearch(temp, 0, len(temp)-1, int(markForSearch2.get()))
    k = 0
    for i in tup:
        myLabelS2 = Label(frame02, text=f"{i[1]} : {i[0]}", anchor='w',
                          relief=GROOVE, width=15, font=("bold", 15), bg=rankCol)
        myLabelS2.grid(row=6+k, column=1)
        k += 1
    markForSearch2.delete(0, 'end')


# inset button.
insertButton2 = Button(frame02, text="Insert", command=buttonclick2,
                       bg="#A6A9B6", font=("bold", 15), width=15)
insertButton2.grid(row=3, column=1, padx=10, pady=10)

# Label(frame02,text="Merge Sort and Binary Search",font=("bold",15),bg="#EFF8FF").grid(row=0,column=0)
# Text box and the label for name
name2 = Entry(frame02, font=(14), width=15)
name2.grid(row=1, column=1)
l_name2 = Label(frame02, text="Name", font=("bold", 15), bg="#EFF8FF")
l_name2.grid(row=1, column=0)

# lable and text box for marks
marks2 = Entry(frame02, font=(14), width=15)
marks2.grid(row=2, column=1)
l_marks2 = Label(frame02, text="Marks", font=("bold", 15), bg="#EFF8FF")
l_marks2.grid(row=2, column=0)

# label and text box for search
Label(frame02, text="Search Marks", font=(
    "bold", 15), bg="#EFF8FF").grid(row=4, column=0)
markForSearch2 = Entry(frame02, font=(14), width=15)
markForSearch2.grid(row=4, column=1)

# search button.
search_by_marks2 = Button(frame02, text="Search", command=searchClick2,
                          bg="#A6A9B6", font=("bold", 15), width=15)
search_by_marks2.grid(row=5, column=1)

# Reset button


def reset2():
    global frame04
    frame04.destroy()
    try:
        myLabelS2.destroy()
    except Exception:
        pass
    frame04 = Frame(frame02, bg="#EFF8FF", padx=5, pady=5)
    frame04.grid(row=9, column=0)
    global mergearr
    mergearr = []


# destroy
myLabelDes2 = Button(frame02, text="Reset", command=reset2,
                     bg="#A6A9B6", font=("bold", 15), width=15)
myLabelDes2.grid(row=10, column=0)

###########################################################################################
# delete Button.


def deleteMarks2():
    global mergearr
    global frame04
    temp = []
    frame04.destroy()
    frame04 = Frame(frame02, bg="#EFF8FF", padx=5, pady=5)
    frame04.grid(row=9, column=0)
    for i in range(-1, -len(mergearr)-1, -1):
        temp.append(mergearr[i])
    tup = binarySearch(temp, 0, len(temp)-1, int(markForDelete2.get()))
    # print(tup[0])
    mergearr.remove(tup[0])
    x = 1
    for i in mergearr:
        myLabel2 = Label(frame04, text=f"{x}. {i[1]} : {i[0]}", anchor='w',
                         relief=GROOVE, width=25, font=("bold", 15), bg=rankCol)
        myLabel2.grid(row=x+8, column=0)
        x = x + 1
    markForDelete2.delete(0, 'end')


# Delete marks Lable and Text Box.
Label(frame02, text="Delete Marks", font=(
    "bold", 15), bg="#EFF8FF").grid(row=12, column=0)
markForDelete2 = Entry(frame02, font=(14), width=15)
markForDelete2.grid(row=12, column=1)

# delete marks Button.
delete_by_marks2 = Button(frame02, text="Delete", command=deleteMarks2,
                          bg="#A6A9B6", font=("bold", 15), width=15)
delete_by_marks2.grid(row=13, column=1)

################################################################################################


window.mainloop()
