import tkinter as tk
from Python_Bank_UI_DataBase.Start_page import StartPage
from Python_Bank_UI_DataBase.Balance_page import BalancePage
from Python_Bank_UI_DataBase.Login_page import LoginPage
from Python_Bank_UI_DataBase.Menu_page import MenuPage
from Python_Bank_UI_DataBase.Register_page import RegisterPage
from Python_Bank_UI_DataBase.Withdraw_page import WithdrawPage
from Python_Bank_UI_DataBase.Deposit_page import DepositPage


class PythonBankUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'First_name': tk.StringVar(),
                            'Last_name': tk.StringVar(),
                            'Personal_ID': tk.IntVar(),
                            'PIN': tk.IntVar(),
                            'Balance': tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoginPage, RegisterPage, MenuPage, BalancePage, WithdrawPage, DepositPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=5, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show frame for the given page
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = PythonBankUI()
    app.mainloop()
