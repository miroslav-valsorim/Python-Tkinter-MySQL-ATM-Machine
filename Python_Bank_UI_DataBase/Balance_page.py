import tkinter as tk


class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#000066')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Python Bank',
                                 font=('helvetica', 20, 'bold'),
                                 foreground='#ffffff',
                                 background='#000066')
        heading_label.pack(pady=20)

        current_balance = tk.Label(self,
                                   text='Your current balance is',
                                   font=('helvetica', 13),
                                   bg='#000066',
                                   fg='white')

        current_balance.pack(pady=10)

        # getting the value of 'Balance' and setting it as value
        var = controller.shared_data['Balance']

        balance_label = tk.Label(self,
                                 textvariable=var,
                                 font=('helvetica', 13),
                                 fg='white',
                                 bg='#000066',
                                 anchor='w')
        balance_label.pack()

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
