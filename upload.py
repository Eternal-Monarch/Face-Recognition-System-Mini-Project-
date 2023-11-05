import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading
from tkinter import filedialog

# Placeholder for loading the model
loaded_model = None

class_labels = ['Sayantan', 'Subhasish']
webcam_active = False
cap = None
webcam_frame = None

def start_camera():
    global webcam_active
    if not webcam_active:
        start_webcam()  # Start the laptop webcam

def start_webcam_thread():
    global webcam_active, cap, webcam_frame
    cap = cv2.VideoCapture(0)
    webcam_active = True
    while webcam_active:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (340, 330))  # Resize the frame
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            if webcam_frame is None:
                webcam_frame = tk.Label(root, image=photo)
                webcam_frame.image = photo
                webcam_frame.pack(fill='both', expand=1)
            else:
                webcam_frame.configure(image=photo)
                webcam_frame.image = photo
            root.update_idletasks()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    if webcam_frame:
        webcam_frame.destroy()
        webcam_frame = None

def start_webcam():
    threading.Thread(target=start_webcam_thread).start()

def browse_image():
    file_path = filedialog.askopenfilename()
    # Implement logic to handle the selected image

def quit_app():
    global webcam_active, cap
    webcam_active = False
    if cap is not None:
        cap.release()
    root.destroy()

root = tk.Tk()
root.title("Face Recognition")
root.configure(bg="white")

# Add titles with improved styling
nit_meghalaya_label = tk.Label(root, text="National Institute of Technology, Meghalaya", bg="skyblue", fg="white", font=('Helvetica', 43, 'bold'))
nit_meghalaya_label.pack(fill='both', expand=1)

# Adding an optional custom logo in the middle of the "National Institute of Technology, Meghalaya" label
logo_image = Image.open("nit logo.jpeg")  # Replace with your image file
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="white")
logo_label.pack(fill='both', expand=1)

face_recognition_label = tk.Label(root, text="Face Recognition System", bg="green", fg="white", font=('Helvetica', 40, 'bold'))
face_recognition_label.pack(fill='both', expand=1)

subhasish_sayantan_label = tk.Label(root, text="This project is made by Subhasish Dutta and Sayantan Bose", bg="white", fg="black", font=('Helvetica', 20))
subhasish_sayantan_label.pack(fill='both', expand=1)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(fill='both', expand=1)

browse_image_button = tk.Button(button_frame, text="Browse Image", command=browse_image, fg="white", bg="blue", height=3, activebackground="navy", font=('Helvetica', 16, 'bold'))
browse_image_button.pack(side='top', padx=10, pady=10, anchor='center')

quitWindow = tk.Button(button_frame, text="Quit", command=quit_app, fg="white", bg="red", height=1, activebackground="darkred", font=('Helvetica', 20, 'bold'))
quitWindow.pack(side='top', padx=10, pady=10, anchor='center')

root.mainloop()
