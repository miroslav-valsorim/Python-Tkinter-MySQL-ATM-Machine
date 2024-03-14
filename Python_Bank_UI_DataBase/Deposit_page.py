import tkinter as tk
from tkinter import ttk, CENTER

from SQL_to_python_functions.SQL_add_to_balance import add_currency_to_user


class DepositPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#000066')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Python Bank',
                                 font=('helvetica', 20, 'bold'),
                                 foreground='#ffffff',
                                 background='#000066')
        heading_label.pack(pady=20)

        enter_amount_label = tk.Label(self,
                                      text='Enter amount',
                                      font=('helvetica', 13),
                                      bg='#000066',
                                      fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 justify=CENTER,
                                 font=('helvetica', 10),
                                 width=12)
        deposit_entry.pack(ipady=7)

        # depositing cash to balance
        # converting both vas and user to int/string/float
        # because they are both objects
        def deposit_cash():
            var = controller.shared_data['Balance']
            user = controller.shared_data['Personal_ID']

            controller.shared_data['Balance'].set(int(var.get()) + int(cash.get()))

            add_currency_to_user(user.get(), cash.get())

            controller.show_frame('MenuPage')
            result = cash.get()

            cash.set('')
            pop_up_msg(f"You have deposited {result}$")

        def pop_up_msg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            popup.geometry("200x100")
            label = ttk.Label(popup, text=msg, font=('helvetica', 10))
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=deposit_cash,
                                 relief='raised',
                                 borderwidth=3,
                                 width=12,
                                 height=2)
        enter_button.pack(pady=10)

        # creating two buttons for Menu and Exit to start page
        def menu():
            controller.show_frame('MenuPage')

        menu_button = tk.Button(self,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=12,
                                height=2)
        menu_button.pack(pady=10)

        def exit_page():
            controller.show_frame('StartPage')

        exit_button = tk.Button(self,
                                text='Exit',
                                command=exit_page,
                                relief='raised',
                                borderwidth=3,
                                width=12,
                                height=2)
        exit_button.pack(pady=10)
