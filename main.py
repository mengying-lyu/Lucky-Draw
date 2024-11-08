from tkinter import *
from tkinter import messagebox
from random import *
from tkinter import filedialog
import pandas as pd

def winner(master):
    global data
    global indx
    master.quit()

    master = Tk()
    master.geometry("350x250")
    master.title("Winner")

    # Randomly select a winner from the participants
    randval = randint(1, indx)

    print(indx, randval)

    detail = "Congratulations 🎉\n" + data[randval][0] + "\nStudent Number is\n" + data[randval][1]

    # Display winner information
    winnerLabel = Label(master, text=detail, font="arial 15 bold", fg="red")
    winnerLabel.place(relx=0.5, rely=0.5, anchor="center")

    # # Exit button to close the winner window
    # exitButton = Button(root, text="Exit", font="arial 10 bold", width=5, command=lambda: exitButtonAction(root))
    # exitButton.place(relx=0.5, rely=0.8, anchor="center")

    master.resizable(False, False)
    master.mainloop()

# def got_to_draw():
#     global indx
#     global data
#
#     master = Tk()
#     master.geometry("350x300")
#     master.title("Dorothy Draw🎉")
#
#     # Button to start the draw and display the winner
#     clickButton = Button(master, text="Just Click it", font="arial 10 bold", width=30, command=lambda: winner(master))
#     clickButton.place(relx=0.5, rely=0.5, anchor="center")
#
#     # # Button to exit the draw window
#     # exitButton = Button(master, text="Exit", bg="red", fg="black", width=5, command=lambda: exitButtonAction(master))
#     # exitButton.place(relx=0.8, rely=0.0)
#
#     master.resizable(False, False)
#     master.mainloop()

# def drawButtonAction():
#     global data
#     global indx
#     if len(data) >= 2:
#         got_to_draw()
#     else:
#         messagebox.showerror("Error", "Draw cannot happen due to insufficient members")

def show_the_list():
    master = Tk()
    master.title("Member List")
    master.geometry("400x400")

    scroll = Scrollbar(master)
    scroll.pack(side=RIGHT, fill=Y)

    listbox = Listbox(master, height=15, width=40, yscrollcommand=scroll.set)
    listbox.place(relx=0.5, rely=0.5, anchor="center")
    scroll.config(command=listbox.yview)

    cnt = 1
    for i in range(1, indx + 1):
        name = data[i][0]
        mobile = data[i][1]
        listbox.insert(END, f"{cnt}. {name}  ---  {mobile}")
        cnt += 1

    master.resizable(False, False)
    master.mainloop()

def change_window(master):
    master.quit()
    master.withdraw()
    aWindow = Toplevel(root)
    aWindow.destroy()
    root.iconify()
    root.deiconify()

def insertInfo(name, mobile, name_event, mobile_event, master):
    global indx
    global data

    # Clear the entry fields after inserting the information
    name_event.delete(0, END)
    mobile_event.delete(0, END)

    # Convert inputs to strings for safety
    name = str(name)
    mobile = str(mobile)

    # Increment the index and store the new entry
    indx += 1
    data[indx] = [name, mobile]

    # Show a message indicating successful insertion
    messagebox.showinfo("insertInfo", f"{indx}. Insertion Successful!!")

def insertFromExcel():
    global indx
    global data

    # Open a file dialog to select the Excel file
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    # Check if a file was selected
    if file_path:
        try:
            # Read the Excel file into a pandas DataFrame
            df = pd.read_excel(file_path)

            # Ensure the DataFrame has the expected columns: "Name" and "ID"
            if "Name" in df.columns and "ID" in df.columns:
                for _, row in df.iterrows():
                    name = str(row["Name"])
                    mobile = str(row["ID"])

                    # Increment the index for each new entry
                    indx += 1
                    data[indx] = [name, mobile]

                # Show a success message
                messagebox.showinfo("Success", f"Successfully imported {len(df)} records from {file_path}")
            else:
                messagebox.showerror("Error", "Excel file must contain 'Name' and 'ID' columns.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read Excel file: {e}")

def insertButtonAction():
    root.withdraw()
    master = Tk()
    master.title("Insert Menu")
    master.geometry("350x250+200+250")

    # Entry fields for name and mobile number
    nameLabel = Label(master, text="Enter new student Name: ", font="arial 15")
    nameLabel.place(relx=0.5, rely=0.2, anchor="center")

    nameEntry = Entry(master)
    nameEntry.place(relx=0.5, rely=0.3, anchor="center", width=150)

    mobileNumberLabel = Label(master, text="Enter new student ID: ", font="arial 15")
    mobileNumberLabel.place(relx=0.5, rely=0.5, anchor="center")

    mobileNumberEntry = Entry(master)
    mobileNumberEntry.place(relx=0.5, rely=0.6, anchor="center", width=150)

    nameEntry.delete(0, END)
    mobileNumberEntry.delete(0, END)

    # Button to insert information
    insertButton = Button(master, text="Insert", command=lambda: insertInfo(nameEntry.get(), mobileNumberEntry.get(), nameEntry, mobileNumberEntry, master))
    insertButton.config(font="arial 15", bg="red", fg="red", width=10)
    insertButton.place(relx=0.5, rely=0.75, anchor="center")

    # Button to show the list of participants
    showListButton = Button(master, text="Show List", command=show_the_list)
    showListButton.config(font="arial 15", bg="white", fg="blue", width=10)
    showListButton.place(relx=0.5, rely=0.9, anchor="center")

    # Button to go back to the main window
    backButton = Button(master, text="<<Back", fg="black", font="bold 12", width=5, command=lambda: change_window(master))
    backButton.place(relx=0.0, rely=0.0)

    master.resizable(False, False)
    master.mainloop()


# Predefined data for participants
data = {
    1: ["Alice", "ID001"],
    2: ["Bob", "ID002"],
    3: ["Charlie", "ID003"]
}
indx = len(data)  # Set initial index to 3 since we have 3 entries

root = Tk()

root.title("Dorothy Draw🎉")
root.geometry("350x300+200+250")

# Button to open data entry window
insertButton = Button(root, text="Insert New One", font="arial 15 bold", width=20, command=insertButtonAction)
insertButton.place(relx=0.5, rely=0.3, anchor="center")

insertListButton = Button(root, text="Insert Excel file", font="arial 15 bold", width=20, command=insertFromExcel)
insertListButton.place(relx=0.5, rely=0.5, anchor="center")

# Button to initiate the draw
drawButton = Button(root, text="Draw", font="arial 15 bold", width=20, command=lambda: winner(root))
drawButton.place(relx=0.5, rely=0.7, anchor="center")

# exitButton = Button(root, text="Exit", font="arial 15 bold", width=20, command = lambda : exitButtonAction(root));
# exitButton.place(relx=0.5, rely=0.8, anchor = "center");


root.resizable(False, False);
root.mainloop();