import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from PIL import Image, UnidentifiedImageError
import tempfile

WATERMARK_PATH = 'C:/Users/lazar/Downloads/DANIEL/Linkedin Photo.jpg'


def watermark_image():
    # Load image to watermark
    try:
        image_to_watermark = Image.open(image_path.get()).convert("RGBA")
    except (AttributeError, UnidentifiedImageError):
        messagebox.showerror(title="Watermark App", message='Invalid image')
    else:
        # Load watermark Image
        watermark = Image.open(WATERMARK_PATH).convert("RGBA")

        # Make Watermark Transparent
        mask = watermark.convert('L').point(lambda x: min(x, 35))
        watermark.putalpha(mask)

        # Get watermark width and height
        watermark_width, watermark_height = watermark.size

        # Calculate watermark ratio
        watermark_aspect_ratio = watermark_width / watermark_height

        # Get image to watermark width and height
        image_width, image_height = image_to_watermark.size

        # Resize watermark to fit in image to watermark
        new_watermark_width = image_width * 0.25
        watermark.thumbnail((new_watermark_width, new_watermark_width / watermark_aspect_ratio), Image.ANTIALIAS)

        # Copy image to watermark
        image_with_watermark = image_to_watermark.copy()

        # Add watermark
        for i in range(0, image_with_watermark.size[0], watermark.size[0]):
            for j in range(0, image_with_watermark.size[1], watermark.size[1]):
                image_with_watermark.paste(watermark, (i, j), watermark)

        # Generate random name for file
        temporary_path = tempfile.NamedTemporaryFile()
        temporary_name = temporary_path.name.split("\\")[-1]

        # Save image file with watermark
        try:
            image_with_watermark.save(folder_path.get() + f'/{temporary_name}.png', quality=100)
        except PermissionError:
            messagebox.showerror(title="Watermark App", message='Invalid destination folder (Permission Denied)')
        else:
            messagebox.showinfo(title="Watermark App", message="Imaged Saved successfully")


def browse_image():
    filename = askopenfilename(filetypes=(("JPG", "*.jpg"), ("All files", "*.*")))
    image_path.insert(tkinter.END, filename)


def select_folder():
    folder = askdirectory()
    folder_path.insert(tkinter.END, folder)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Watermark App")
window.config(padx=25, pady=25)

image_label = tkinter.Label(text='Please browse the image to be watermarked')
image_label.grid(row=0, column=1, sticky="W")

browse_button = tkinter.Button(window, text="Browse Image", command=browse_image)
browse_button.grid(row=1, column=2)

image_path = tkinter.Entry(width=50)
image_path.grid(row=1, column=1)

image_label = tkinter.Label(text='Select destination folder')
image_label.grid(row=2, column=1, sticky="W")

folder_button = tkinter.Button(window, text="Select folder", command=select_folder)
folder_button.grid(row=3, column=2)

folder_path = tkinter.Entry(width=50)
folder_path.grid(row=3, column=1)

convert_button = tkinter.Button(text="Watermark", command=watermark_image)
convert_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
