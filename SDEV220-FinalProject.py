import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar


appointments_file = "appointments.json"
try:
    with open(appointments_file, "r") as file:
        appointments = json.load(file)
except FileNotFoundError:
    appointments = {"appointments":[]}
    with open(appointments_file, "w") as file:
        json.dump(appointments, file)

# Function to save appointments
def save_appointments():
    with open(appointments_file, "w") as file:
        json.dump(appointments, file)


def book_appointment_window():
    def submit_appointment():
        global appointments
        selected_date = calendar.get_date()
        selected_time = time_dropdown.get()
        selected_service = service_dropdown.get()
        comments = comment_entry.get()

        print(f"Date: {selected_date}, Time: {selected_time}, Service: {selected_service}, Comments: {comments}")

        # Check if the selected date and time are already booked
        for appt in appointments:
            if "date" in appt and "time" in appt:  # Safeguard against missing keys
                if appt["date"] == selected_date and appt["time"] == selected_time:
                    messagebox.showerror("Error", "This time slot is already booked.")
                    return

        # Create a new appointment
        new_appointment = {
            "customer_name": "Alex",  # Temporary placeholder
            "date": selected_date,
            "time": selected_time,
            "service": selected_service,
            "comments": comments
        }
        appointments["appointments"].append(new_appointment)
        save_appointments()  # Save to JSON
        messagebox.showinfo("Success", "Appointment successfully booked!")
        booking_window.destroy()


    # Create the booking window
    booking_window = tk.Toplevel(root)
    booking_window.title("Book Appointment")
    booking_window.geometry("400x400")

    # Calendar for selecting a date
    tk.Label(booking_window, text="Select a Date:").pack(pady=5)
    calendar = Calendar(booking_window, date_pattern="yyyy-mm-dd")
    calendar.pack(pady=10)

    # Dropdown for selecting a time
    tk.Label(booking_window, text="Select a Time:").pack(pady=5)
    time_var = tk.StringVar()
    time_dropdown = ttk.Combobox(
        booking_window, textvariable=time_var, state="readonly",
        values=["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM"]
    )
    time_dropdown.pack(pady=10)

    # Dropdown for selecting a service
    tk.Label(booking_window, text="Select a Service:").pack(pady=5)
    service_var = tk.StringVar()
    service_dropdown = ttk.Combobox(
        booking_window, textvariable=service_var, state="readonly",
        values=["Grooming", "Vaccination", "Check-up", "Training"]
    )
    service_dropdown.pack(pady=10)

    # Add comments
    comment_label = tk.Label(booking_window, text="Comments:")
    comment_label.pack(pady=5)

    comment_entry = tk.Entry(booking_window, width=50)
    comment_entry.pack(pady=5)

    # Submit button
    submit_button = tk.Button(booking_window, text="Submit Appointment", command=submit_appointment)
    submit_button.pack(pady=20)



def staff_login():
    # For now, just show a simple message when staff click the button
    messagebox.showinfo("Staff Login", "Staff login functionality will be implemented here.")


# Main GUI setup 
root = tk.Tk()
root.title("Pet Parlor Appointment Scheduler")
root.geometry("400x300")

# Create and pack the Book Appointment button for customers
button_customer = tk.Button(root, text="Book Appointment", width=20, command=book_appointment_window)
button_customer.pack(pady=20)

# Create and pack the Staff Login button
button_staff = tk.Button(root, text="Staff Login", width=20, command=staff_login)
button_staff.pack(pady=20)

# Run the main event loop to display the window
root.mainloop()