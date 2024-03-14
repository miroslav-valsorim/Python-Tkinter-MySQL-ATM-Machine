import tkinter as tk
from tkinter import ttk, CENTER
from SQL_to_python_functions.SQL_insert_to_database import insert_varibles_into_table
from SQL_to_python_functions.SQL_get_new_user_id import get_new_user_id


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#000066')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Python Bank',
                                 font=('helvetica', 20, 'bold'),
                                 foreground='#ffffff',
                                 background='#000066')
        heading_label.pack(pady=20)

        main_menu_label = tk.Label(self,
                                   text="Enter your information here",
                                   font=('helvetica', 13),
                                   fg='white',
                                   bg='#000066')
        main_menu_label.pack()

        # creating user first name entry
        first_name = tk.Label(self,
                              text='First Name',
                              font=('helvetica', 10),
                              bg='#000066',
                              fg='white')
        first_name.pack(pady=1)

        my_first_name = tk.StringVar()
        first_name_entry_box = tk.Entry(self,
                                        textvariable=my_first_name,
                                        justify=CENTER,
                                        font=('helvetica', 10),
                                        width=15)
        first_name_entry_box.focus_set()
        first_name_entry_box.pack(ipady=2)

        # creating user last name entry
        last_name = tk.Label(self,
                             text='Last Name',
                             font=('helvetica', 10),
                             bg='#000066',
                             fg='white')
        last_name.pack(pady=1)

        my_last_name = tk.StringVar()
        second_name_entry_box = tk.Entry(self,
                                         textvariable=my_last_name,
                                         justify=CENTER,
                                         font=('helvetica', 10),
                                         width=15)
        second_name_entry_box.focus_set()
        second_name_entry_box.pack(ipady=2)

        # creating user PIN entry
        user_pin = tk.Label(self,
                            text='PIN (Should contain 4 numbers)',
                            font=('helvetica', 10),
                            bg='#000066',
                            fg='white')
        user_pin.pack(pady=1)

        my_user_pin = tk.StringVar()
        user_pin_entry_box = tk.Entry(self,
                                      textvariable=my_user_pin,
                                      justify=CENTER,
                                      font=('helvetica', 10),
                                      width=15)
        user_pin_entry_box.focus_set()
        user_pin_entry_box.pack(ipady=2)

        # hiding the entered value with *
        def handle_focus_in(_):
            user_pin_entry_box.configure(fg='black', show='*')

        user_pin_entry_box.bind('<FocusIn>', handle_focus_in)

        wrong_label = tk.Label(self,
                               text='',
                               font=('helvetica', 10),
                               fg='white',
                               bg='#000066',
                               anchor='n')
        wrong_label.pack(fill='both', expand=True)

        def pop_up_msg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            popup.geometry("230x100")
            label = ttk.Label(popup, text=msg, font=('helvetica', 10))
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()

        # first and last name validators
        def check_user_entry_name(name):
            if name.isalpha():
                return True
            else:
                pop_up_msg("Name should contains only letters!")
                return False

        # PIN validator
        def check_user_pin(pin):
            if pin.isdigit() and len(pin) == 4:
                return True
            else:
                pop_up_msg("PIN doesn't meet requirements")

        # registering new user to our Bank(database)
        def register_new_user():
            check_first_name = my_first_name.get()
            check_last_name = my_last_name.get()
            check_pin = my_user_pin.get()
            currency = 0

            if check_user_entry_name(check_first_name):
                if check_user_entry_name(check_last_name):
                    if check_user_pin(check_pin):
                        result = insert_varibles_into_table(check_first_name, check_last_name, currency, check_pin)
                        if result:
                            my_first_name.set('')
                            my_last_name.set('')
                            my_user_pin.set('')
                            controller.show_frame('LoginPage')
                            new_id = get_new_user_id()
                            pop_up_msg("Your account has been created!\n"
                                       f"Your user ID is {str(new_id)}\n"
                                       f"Now you can log in with the current ID")

                        else:
                            wrong_label['text'] = 'Something went wrong, try again or contact our support'

        register_button = tk.Button(self,
                                    text='Register',
                                    command=register_new_user,
                                    relief='raised',
                                    borderwidth=3,
                                    width=10,
                                    height=1)
        register_button.pack(pady=10)
