import csv
import os
import time
from subprocess import Popen
import pgrep as pgrep
import customtkinter
import tkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("500x350")


# File to save the log
log_file = "./top_process.csv"

# Maintenance file path
maintenance_file = "/tmp/maintenance.txt"


# Loop for 5 minutes with 5 seconds interval
end_time = time.time() + 15
while time.time() < end_time:
    date_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Check if the top process is running
    top_running = pgrep.pgrep("top")
    if len(top_running) >= 1:
        log_entry = [date_time, "Top is running"]
    else:
        # Check if maintenance file exists
        if os.path.exists(maintenance_file):
            log_entry = [date_time, "We are under maintenance mode!"]
        else:
            # Start the top process
            Popen("top")
            log_entry = [date_time, "Top was started"]

        # Write log entry to file
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(log_entry)

    maintenance_entries = []
    with open(log_file) as f:
        reader = csv.reader(f)
        header = next(reader)  # skip the header
        for row in reader:
            if row[1] == "We are under maintenance mode!":
                maintenance_entries.append(row)
    print(f"Number of maintenance entries: {len(maintenance_entries)}")

    time.sleep(5)

entries = []
lines = []

with open(log_file) as f:
    reader = csv.reader(f)
    header = next(reader)  # skip the header
    for row in reader:
        if row[1] == "Top was started":
            entries.append(row)

var = tkinter.Variable(value=entries)

listbox = tkinter.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tkinter.EXTENDED
)



def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()

    #get selected items
    selected_lines = lines.append([listbox.get(i) for i in selected_indices])
    print(lines)


# Show the entries in a GUI
def show_entries():
    listbox.pack(expand=True, fill=tkinter.BOTH)


def save_entries():
    file_path = filedialog.asksaveasfilename()
    with open(file_path, 'w') as f:
        f.writelines(lines)


listbox.bind('<<ListboxSelect>>', items_selected)

show_button = tkinter.Button(master=root, text="Show entries", command=show_entries)
show_button.pack(pady=12, padx=10)

save_button = tkinter.Button(master=root, text="Save entries", command=save_entries)
save_button.pack(pady=12, padx=10)


root.mainloop()
