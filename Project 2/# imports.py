# imports
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import datetime # one module for working with dates and times

# The MainWindow class creates a custom GUI window based on the tkinter window (tk.Tk)
# It has an __init__() method, and three additional methods (new_note(), open_notebook(), and save_notebook())
# These methods correspond to new, open, and save buttons in the window.
# The new_note method calls the NoteForm class to create a new note form top level window.

class MainWindow(tk.Tk):
    def __init__(self):  #initialize the main window
        super().__init__() # initialize it as a tkinter window
        
        self.geometry("600x400") # set the default window size
        self.title('Notebook') #set the default window title
        self.notebook = [] # initialize an attribute named 'notebook' as an empty list
        self.notes = []
        
        #This creates a label on the screen to tell the user that the text that is put in the box is the note title
        self.title_label = tk.Label(self, text="Note Title:")
        self.title_label.grid(padx=10, pady=10, row=1, column=0, sticky='e')
        
        #This is creates a box for the user to input their code title
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(padx=10, pady=10, row=1, column=1, sticky='w')
        
        #This creates a label on the screen to tell the user that the box next to it is the note description
        self.desc_label = tk.Label(self, text="Note Description:")
        self.desc_label.grid(padx=10, pady=10, row=2, column=0, sticky='e')
        
        #This creates a box for user text input
        self.desc_text = tk.Text(self, height=15, width=50)
        self.desc_text.grid(padx=10, pady=10, row=2, column=1, sticky='e')
        
        self.new_note_button = tk.Button(self, text="Save Note", command=self.new_note)
        self.new_note_button.grid(padx=10, pady=10, row=3, column=0)
        
        #Creates and places a save button on the screen
        self.create_notebook_button = tk.Button(self, text="Save Notebook", command=self.save_notebook)
        self.create_notebook_button.grid(padx=10, pady=10, row=3, column=1)
        
        #This makes a button on the main window which if the user clicks it, it self destructs and closes the window
        self.quit_window = tk.Button(self, text="Exit", command=self.destroy)
        self.quit_window.grid(padx=10, pady=10, row=4, column=0)
        
        #Puts the load notebook file button on screen
        self.load_notebooks = tk.Button(self, text="Select Notebook", command=self.open_notebook)
        self.load_notebooks.grid(padx=10, pady=10, row=4, column=1)
        
        # add additional lines to the __init__() function
        
    def new_note(self):
        note_window = NoteForm(self, self.notebook, self.notes)
        return None

    def open_notebook(self):
        filepath = filedialog.askopenfilename(initialdir="C:\Users\loudd\OneDrive\Desktop\INST 326\Files",
                                              filetypes=[("text files", "*.txt"),
                                              ("all files", "*.*")])
        file = open(filepath, "r")
        file_list = file.read().split('\n')
        file.close()
        self.title_entry.delete(0, 'end')
        self.desc_text.delete('1.0', 'end')
        self.title_entry.insert(0, file_list[0])
        self.desc_text.insert('1.0', file_list[1])
        meta = file_list[2]
        print(meta)


    def save_notebook(self):
        file = filedialog.asksaveasfile(initialdir="C:\Users\loudd\OneDrive\Desktop\INST 326\Files",
                                          defaultextension=".txt", 
                                          filetypes=[("text file", ".txt"),
                                         ("all files", ".*")])
        filetext = self.submit()
        file.write(filetext)
        file.close()# replace with the code needed to save the notebook
        return None


# the NoteForm() class creates a Toplevel window that is a note form containing fields for
# data entry for title, text, link, and tags. It also calculates a meta field with date, time, and timezone
# the Noteform class has an __init__() method, and a submit() method that is called by a submit button
# the class may contain additional methods to perform tasks like calculating the metadata, for example
# the submit method calls the MakeNote class that transforms the the entered data into a new note object.

class NoteForm(tk.Toplevel):
    
    def __init__(self, master, notebook, notes): # initialize the new object
        super().__init__(master) # initialize it as a toplevel window
        self.geometry("200x150")
        self.title("Notes")
        self.notebook = notebook
        self.notes = notes
        
        self.title_label = tk.Label(self, text="Title of Note:")
        self.title_label.grid()
        
        # add additional lines to set the new window's attributes and default parameters

        
    def submit(self):
        # add lines to the submit method
        
        new_note = MakeNote(note_dict)
        self.notes.append(new_note)
        print(self.notes)
        return None

    
# The MakeNote class takes a dictionary containing the data entered into the form window,
# and transforms it into a new note object.
# At present the note objects have attributes but no methods.

class MakeNote():
    def __init__(self, note_dict):
        # add lines to the init method
        pass # delete this line when you have entered actual code
    


# main execution

if __name__ == '__main__':
    
    main_window = MainWindow() # this creates a notebook / main window called main_window. You may change the name if you want

    main_window.mainloop()
