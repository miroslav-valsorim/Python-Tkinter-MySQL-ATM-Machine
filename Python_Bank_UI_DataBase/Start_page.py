import tkinter as tk


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#000066')
        self.controller = controller
        self.controller.title('Python Banking Operations')
        self.controller.geometry("550x380")

        heading_label = tk.Label(self,
                                 text='Welcome to Python Bank',
                                 font=('helvetica', 20, 'bold'),
                                 foreground='#ffffff',
                                 background='#000066')
        heading_label.pack(pady=40)

        def show_login_page():
            controller.show_frame('LoginPage')

        login_button = tk.Button(self,
                                 text='Login',
                                 command=show_login_page,
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        login_button.pack(pady=10)
        login_button.place(x=100, y=160)

        def show_registration_page():
            controller.show_frame('RegisterPage')

        register_button = tk.Button(self,
                                    text='Register',
                                    command=show_registration_page,
                                    borderwidth=3,
                                    width=20,
                                    height=3)
        register_button.pack(pady=50)
        register_button.place(x=300, y=160)
