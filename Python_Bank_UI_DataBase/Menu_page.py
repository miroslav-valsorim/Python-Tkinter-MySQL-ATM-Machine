import tkinter as tk


class MenuPage(tk.Frame):

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
                                   text='Main Menu',
                                   font=('helvetica', 15),
                                   fg='white',
                                   bg='#000066')
        main_menu_label.pack()

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button = tk.Button(self,
                                    text='Withdraw',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=12,
                                    height=2)
        withdraw_button.pack(pady=10)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button = tk.Button(self,
                                   text='Deposit',
                                   command=deposit,
                                   relief='raised',
                                   borderwidth=3,
                                   width=12,
                                   height=2)
        deposit_button.pack(pady=10)

        def balance():
            controller.show_frame('BalancePage')

        balance_button = tk.Button(self,
                                   text='Balance',
                                   command=balance,
                                   relief='raised',
                                   borderwidth=3,
                                   width=12,
                                   height=2)
        balance_button.pack(pady=10)

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
