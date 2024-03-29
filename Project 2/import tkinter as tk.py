import tkinter as tk
from tkinter import filedialog
import datetime

class Note:
    def __init__(self, title, text, created):
        self.title = title
        self.text = text
        self.created = created

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title('Notebook')
        self.notebook = []
        self.notes = []

        self.title_label = tk.Label(self, bg='light gray', text='Note Title:')
        self.title_label.grid(padx=10, pady=10, row=1, column=0, sticky='e')

        self.text_label = tk.Label(self, bg='light gray', text='Note Text:')
        self.text_label.grid(padx=10, pady=10, row=2, column=0, sticky='e')

        # Entry fields for title and text
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(padx=10, pady=10, row=1, column=1, sticky='w')

        self.text_entry = tk.Text(self, height=10, width=60)
        self.text_entry.grid(padx=10, pady=10, row=2, column=1)

        # Buttons
        self.submit_button = tk.Button(self, text='Submit', command=self.submit)
        self.submit_button.grid(padx=10, pady=10, row=3, column=0)

        self.save_button = tk.Button(self, text='Save Notebook', command=self.save_notebook)
        self.save_button.grid(padx=10, pady=10, row=3, column=1)

        self.load_button = tk.Button(self, text='Load Notebook', command=self.load_notebook)
        self.load_button.grid(padx=10, pady=10, row=4, column=1)

        self.open_notebook_button = tk.Button(self, text='Open Notebook', command=self.open_notebook_window)
        self.open_notebook_button.grid(padx=10, pady=10, row=4, column=0)

        self.note_frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.note_frame.grid(row=5, columnspan=2, sticky='nsew')

    def submit(self):
        title = self.title_entry.get()
        text = self.text_entry.get('1.0', 'end').strip('\n')
        created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(title, text, created)
        self.notes.append(note)
        self.display_notes()  # Update displayed notes
        return None

    def save_notebook(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, 'w') as file:
                for note in self.notes:
                    file.write(f"Title: {note.title}\n")
                    file.write(f"Text: {note.text}\n")
                    file.write(f"Created: {note.created}\n")
                    file.write("\n")
            print(f"Notebook saved to {filename}")

    def load_notebook(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            self.notes = []  # Clear existing notes
            with open(filename, 'r') as file:
                lines = file.readlines()
                note_data = {}
                for line in lines:
                    if line.startswith('Title:'):
                        note_data['title'] = line[7:].strip()
                    elif line.startswith('Text:'):
                        note_data['text'] = line[6:].strip()
                    elif line.startswith('Created:'):
                        note_data['created'] = line[9:].strip()
                    elif line == '\n':
                        note = Note(note_data['title'], note_data['text'], note_data['created'])
                        self.notes.append(note)
                        note_data = {}
            print(f"Notebook loaded from {filename}")
            self.display_notes()  # Update displayed notes

    def open_notebook_window(self):
        notebook_window = NotebookWindow(self.notes)
        notebook_window.mainloop()

    def display_notes(self):
        # Clear existing notes
        for widget in self.note_frame.winfo_children():
            widget.destroy()

        # Display notes
        for i, note in enumerate(self.notes):
            note_frame = tk.Frame(self.note_frame, bd=2, relief=tk.RAISED)
            note_frame.grid(row=i, column=0, sticky='ew')

            title_label = tk.Label(note_frame, text=f"Title: {note.title}")
            title_label.grid(row=0, column=0, sticky='w')

            text_label = tk.Label(note_frame, text=f"Text: {note.text}")
            text_label.grid(row=1, column=0, sticky='w')

            created_label = tk.Label(note_frame, text=f"Created: {note.created}")
            created_label.grid(row=2, column=0, sticky='w')

            # Create a closure to capture the current value of i
            note_frame.bind("<Button-1>", lambda event, idx=i: self.open_note_window(idx))

class NotebookWindow(tk.Toplevel):
    def __init__(self, notes):
        super().__init__()
        self.geometry("400x300")
        self.title("Notebook")
        self.notes = notes

        self.note_frame = tk.Frame(self)
        self.note_frame.pack(fill=tk.BOTH, expand=True)

        for i, note in enumerate(self.notes):
            note_frame = tk.Frame(self.note_frame, bd=2, relief=tk.RAISED)
            note_frame.grid(row=i, column=0, sticky='ew')

            title_label = tk.Label(note_frame, text=f"Title: {note.title}")
            title_label.grid(row=0, column=0, sticky='w')

            text_label = tk.Label(note_frame, text=f"Text: {note.text}")
            text_label.grid(row=1, column=0, sticky='w')

            created_label = tk.Label(note_frame, text=f"Created: {note.created}")
            created_label.grid(row=2, column=0, sticky='w')

            # Create a closure to capture the current value of i
            note_frame.bind("<Button-1>", lambda event, idx=i: self.open_note_window(idx))

    def open_note_window(self, note_index):
        note = self.notes[note_index]
        note_window = tk.Toplevel(self)
        note_window.title(note.title)
        note_label = tk.Label(note_window, text=note.text)
        note_label.pack()

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.mainloop()
