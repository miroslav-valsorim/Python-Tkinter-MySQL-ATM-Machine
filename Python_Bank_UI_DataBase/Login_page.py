import tkinter as tk
from tkinter import ttk, CENTER

from SQL_to_python_functions.SQL_view_account_balance import view_account_balance
from SQL_to_python_functions.SQL_check_if_exists import check_if_client_already_exist


class LoginPage(tk.Frame):

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

        # creating user id entry
        user_id = tk.Label(self,
                           text='User ID',
                           font=('helvetica', 10),
                           bg='#000066',
                           fg='white')
        user_id.pack(pady=1)

        my_user_id = tk.StringVar()
        user_id_entry_box = tk.Entry(self,
                                     textvariable=my_user_id,
                                     justify=CENTER,
                                     font=('helvetica', 10),
                                     width=15)
        user_id_entry_box.focus_set()
        user_id_entry_box.pack(ipady=2)

        # hides the value entered with *
        def handle_focus_in(_):
            user_id_entry_box.configure(fg='black', show='*')

        user_id_entry_box.bind('<FocusIn>', handle_focus_in)

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
        second_name = tk.Label(self,
                               text='Last Name',
                               font=('helvetica', 10),
                               bg='#000066',
                               fg='white')
        second_name.pack(pady=1)

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
                            text='PIN',
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

        # hides the value entered with *
        def handle_focus_in(_):
            user_pin_entry_box.configure(fg='black', show='*')

        user_pin_entry_box.bind('<FocusIn>', handle_focus_in)

        def pop_up_msg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            popup.geometry("200x100")
            label = ttk.Label(popup, text=msg, font=('helvetica', 10))
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()

        def check_user():
            check_id = my_user_id.get()
            check_first_name = my_first_name.get()
            check_last_name = my_last_name.get()
            check_pin = my_user_pin.get()

            result = check_if_client_already_exist(check_id, check_first_name, check_last_name, check_pin)

            if result:
                my_user_id.set('')
                my_first_name.set('')
                my_last_name.set('')
                my_user_pin.set('')

                # IMPORTANT !
                # setting the entered data from user as shared_data through all the frames
                # so all frames can work with it

                currency = view_account_balance(check_id)

                controller.shared_data['First_name'].set(check_first_name)
                controller.shared_data['Last_name'].set(check_last_name)
                controller.shared_data['Personal_ID'].set(check_id)
                controller.shared_data['PIN'].set(check_pin)
                controller.shared_data['Balance'].set(currency)

                controller.show_frame('MenuPage')
            else:
                pop_up_msg("Some of the information you\n"
                           "have entered is not valid !\n"
                           "Try again!")

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_user,
                                 relief='raised',
                                 borderwidth=3,
                                 width=10,
                                 height=1)
        enter_button.pack(pady=10)
