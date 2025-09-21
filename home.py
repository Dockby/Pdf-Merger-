import tkinter as tk
from tkinter import PhotoImage, filedialog, messagebox
from pypdf import PdfWriter



def upload_files():

    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not files:
        return


    merger = PdfWriter()

    try:

        for pdf in files:
            merger.append(pdf)


        save_path = filedialog.asksaveasfilename(
            title="Save Merged PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if save_path:
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"PDF merged successfully!\nSaved at:\n{save_path}")
        else:
            merger.close()

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")



window = tk.Tk()
window.title("PDF MERGER")
window.geometry("500x500")
window.config(bg="white")


canvas = tk.Canvas(window, bg="white", width=200, height=100, highlightthickness=0)
img = PhotoImage(file="logo-3.png")  # your logo file
canvas.create_image(100, 60, image=img)
canvas.grid(row=0, column=0, padx=120)


drag = tk.Button(
    text="Upload Files To Merge",
    command=upload_files,
    bg="lightblue",
    fg="black",
    font=("Arial", 12, "bold")
)
drag.grid(row=7, columnspan=3, sticky="n", pady=100)

window.mainloop()

