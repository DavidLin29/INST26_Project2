import tkinter as tk
from tkinter import messagebox, filedialog
import json
from datetime import datetime

class Note:
    def __init__(self, title, text, links, tags):
        self.title = title
        self.text = text
        self.links = links
        self.tags = tags
        self.metadata = self.create_metadata()

    def create_metadata(self):
        return {"timestamp": datetime.now().isoformat()}

    def to_dict(self):
        return {
            'title': self.title,
            'text': self.text,
            'links': self.links,
            'tags': self.tags,
            'metadata': self.metadata
        }

class TopWindow(tk.Toplevel):
    def __init__(self, master, note=None):
        super().__init__(master)
        self.title("New Note" if note is None else "Edit Note")
        self.note = note
        self.title_entry = tk.Entry(self, width=50)
        self.text_entry = tk.Text(self, width=50, height=10)
        self.links_entry = tk.Entry(self, width=50)
        self.tags_entry = tk.Entry(self, width=50)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_note)
        self.title_entry.pack(pady=5)
        self.text_entry.pack(pady=5)
        self.links_entry.pack(pady=5)
        self.tags_entry.pack(pady=5)
        self.submit_button.pack(pady=10)
        if note:
            self.title_entry.insert(0, note.title)
            self.text_entry.insert("1.0", note.text)
            self.links_entry.insert(0, note.links)
            self.tags_entry.insert(0, note.tags)

    def submit_note(self):
        title = self.title_entry.get()
        text = self.text_entry.get("1.0", tk.END)
        links = self.links_entry.get()
        tags = self.tags_entry.get()
        if self.note:
            self.note.title = title
            self.note.text = text
            self.note.links = links
            self.note.tags = tags
            messagebox.showinfo("Success", "Note updated successfully.")
        else:
            note = Note(title, text, links, tags)
            self.master.notes.append(note)
            messagebox.showinfo("Success", "Note added successfully.")
        self.master.update_notes_list()
        self.destroy()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notebook")
        self.geometry("800x400")
        self.notes = []
        self.create_widgets()

    def create_widgets(self):
        self.new_note_button = tk.Button(self, text="New Note", command=self.create_note)
        self.new_note_button.pack(pady=10)

        self.load_button = tk.Button(self, text="Load Notes", command=self.load_notes)
        self.load_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Save Notes", command=self.save_notes)
        self.save_button.pack(pady=10)

        self.note_listbox = tk.Listbox(self, width=100)
        self.note_listbox.pack(pady=10)

        self.note_listbox.bind("<Double-1>", self.load_selected_note)

    def create_note(self, note=None):
        TopWindow(self, note)

    def save_notes(self):
        note_data = [note.to_dict() for note in self.notes]
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        if filename:
            with open(filename, 'w') as file:
                json.dump(note_data, file, indent=4)
            messagebox.showinfo("Success", "Notes saved successfully.")

    def load_notes(self):
        filename = filedialog.askopenfilename(title="Select file", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        if filename:
            try:
                with open(filename, 'r') as file:
                    note_data = json.load(file)
                    self.notes = [Note(note['title'], note['text'], note['links'], note['tags']) for note in note_data]
                    self.update_notes_list()
                    messagebox.showinfo("Success", "Notes loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load notes: {e}")

    def load_selected_note(self, event):
        selection = self.note_listbox.curselection()
        if selection:
            index = selection[0]
            note = self.notes[index]
            self.create_note(note)

    def update_notes_list(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, note.title)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()