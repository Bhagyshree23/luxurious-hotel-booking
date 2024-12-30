import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class LuxuryHotelBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Luxury Hotel Booking System")
        self.root.geometry("800x600")

        # Initialize variables
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.check_in_var = tk.StringVar()
        self.check_out_var = tk.StringVar()
        self.room_type_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Luxury Hotel Booking", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        # Create form
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        # Name
        tk.Label(form_frame, text="Full Name:").grid(row=0, column=0, pady=5, padx=5)
        tk.Entry(form_frame, textvariable=self.name_var).grid(row=0, column=1, pady=5, padx=5)

        # Email
        tk.Label(form_frame, text="Email:").grid(row=1, column=0, pady=5, padx=5)
        tk.Entry(form_frame, textvariable=self.email_var).grid(row=1, column=1, pady=5, padx=5)

        # Check-in date
        tk.Label(form_frame, text="Check-in Date (DD/MM/YYYY):").grid(row=2, column=0, pady=5, padx=5)
        tk.Entry(form_frame, textvariable=self.check_in_var).grid(row=2, column=1, pady=5, padx=5)

        # Check-out date
        tk.Label(form_frame, text="Check-out Date (DD/MM/YYYY):").grid(row=3, column=0, pady=5, padx=5)
        tk.Entry(form_frame, textvariable=self.check_out_var).grid(row=3, column=1, pady=5, padx=5)

        # Room type
        tk.Label(form_frame, text="Room Type:").grid(row=4, column=0, pady=5, padx=5)
        room_types = ["Deluxe Suite", "Presidential Suite", "Royal Suite", "Executive Suite"]
        room_dropdown = tk.OptionMenu(form_frame, self.room_type_var, *room_types)
        self.room_type_var.set(room_types[0])
        room_dropdown.grid(row=4, column=1, pady=5, padx=5)

        # Submit button
        submit_btn = tk.Button(self.root, text="Book Now", command=self.submit_booking)
        submit_btn.pack(pady=20)

    def validate_dates(self, check_in, check_out):
        try:
            check_in_date = datetime.strptime(check_in, "%d/%m/%Y")
            check_out_date = datetime.strptime(check_out, "%d/%m/%Y")
            
            if check_out_date <= check_in_date:
                return False
            return True
        except ValueError:
            return False

    def submit_booking(self):
        name = self.name_var.get()
        email = self.email_var.get()
        check_in = self.check_in_var.get()
        check_out = self.check_out_var.get()
        room_type = self.room_type_var.get()

        # Basic validation
        if not all([name, email, check_in, check_out, room_type]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if not self.validate_dates(check_in, check_out):
            messagebox.showerror("Error", "Invalid dates! Please use DD/MM/YYYY format and ensure check-out is after check-in.")
            return

        # Success message
        booking_details = f"""
        Booking Confirmed!
        
        Name: {name}
        Email: {email}
        Check-in: {check_in}
        Check-out: {check_out}
        Room Type: {room_type}
        
        Thank you for choosing our Luxury Hotel!
        """
        messagebox.showinfo("Booking Successful", booking_details)
        
        # Clear form
        self.name_var.set("")
        self.email_var.set("")
        self.check_in_var.set("")
        self.check_out_var.set("")
        self.room_type_var.set("Deluxe Suite")

if __name__ == "__main__":
    root = tk.Tk()
    app = LuxuryHotelBooking(root)
    root.mainloop()
