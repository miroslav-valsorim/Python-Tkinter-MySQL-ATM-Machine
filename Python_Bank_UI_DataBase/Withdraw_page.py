import tkinter as tk
from tkinter import ttk, CENTER

from SQL_to_python_functions.SQL_remove_curent_amount_from_balance import remove_currency_from_user


class WithdrawPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#000066')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Python Bank',
                                 font=('helvetica', 20, 'bold'),
                                 foreground='#ffffff',
                                 background='#000066')
        heading_label.pack(pady=20)

        choose_amount_label = tk.Label(self,
                                       text='Choose the amount you want to withdraw',
                                       font=('helvetica', 10),
                                       fg='white',
                                       bg='#000066')
        choose_amount_label.pack()

        def pop_up_msg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            popup.geometry("250x100")
            label = ttk.Label(popup, text=msg, font=('helvetica', 10))
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()

        def withdraw(amount):
            var = controller.shared_data['Balance']
            user = controller.shared_data['Personal_ID']

            def check_balance():
                if amount > int(var.get()):
                    return False
                else:
                    return True

            if check_balance():
                controller.shared_data['Balance'].set(int(var.get()) - amount)
                remove_currency_from_user(user.get(), amount)
                controller.show_frame('MenuPage')
                cash.set('')
                pop_up_msg(f"{amount}$ were removed from your balance!")

            else:
                controller.show_frame('BalancePage')
                cash.set('')
                pop_up_msg("Not enough money in you account")

        twenty_button = tk.Button(self,
                                  text='20',
                                  command=lambda: withdraw(20),
                                  relief='raised',
                                  borderwidth=3,
                                  width=10,
                                  height=1)
        twenty_button.pack(pady=5)

        sixty_button = tk.Button(self,
                                 text='60',
                                 command=lambda: withdraw(60),
                                 relief='raised',
                                 borderwidth=3,
                                 width=10,
                                 height=1)
        sixty_button.pack(pady=5)

        eighty_button = tk.Button(self,
                                  text='80',
                                  command=lambda: withdraw(80),
                                  relief='raised',
                                  borderwidth=3,
                                  width=10,
                                  height=1)
        eighty_button.pack(pady=5)

        one_hundred_button = tk.Button(self,
                                       text='100',
                                       command=lambda: withdraw(100),
                                       relief='raised',
                                       borderwidth=3,
                                       width=10,
                                       height=1)
        one_hundred_button.pack(pady=5)

        choose_other_amount_label = tk.Label(self,
                                             text='Enter other amount you want to withdraw\n'
                                                  'If it is different than the ones above',
                                             font=('helvetica', 10),
                                             fg='white',
                                             bg='#000066')
        choose_other_amount_label.pack()

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(self,
                                      textvariable=cash,
                                      justify=CENTER,
                                      font=('helvetica', 10),
                                      width=12)
        other_amount_entry.pack(ipady=7)

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=lambda: withdraw(int(cash.get())),
                                 relief='raised',
                                 borderwidth=3,
                                 width=12,
                                 height=2)
        enter_button.pack(pady=10)
