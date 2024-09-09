"""Author: Rhea Lal, Date: 3/6/24 - 9/9/24, Purpose: A GUI program that tests 
and teaches users (aged 18-30) on over-consumption.
"""
# Importing all the modules for the program
"""Provides functions for creating and removing a directory / folder."""
import os
"""Allows intergers / values to be manipulated randomly."""
import random
"""For using regular expressions."""
import re
"""The ability to open websites on web browser."""
import webbrowser
"""Allows the current date and time to be imported."""
from datetime import datetime

"""Imports tkinter library."""
import tkinter as tk
"""Allows access to the Tk themed widget set."""
from tkinter import ttk
"""Holds integer data where we can set integer data and can retrieve it"""
from tkinter import IntVar
"""Importing the tkinter text style."""
from tkinter import Text
"""Allowing the text to be inserted in a canvas."""
from tkinter import INSERT
"""Import the specific font style from the tkinter library."""
from tkinter import font
"""Allows the tkinter style of message box that pops up."""
from tkinter import messagebox as mb
"""Imports the tkinter style of image that are saved to display and modify."""
from PIL import Image
"""Imports the tkinter style of image that are saved to display and modify.."""
from PIL import ImageTk


# Data of questions and answers and options
data={
    "question": [
        "What does over-consumption mean?",
        "Who do you think is the biggest consumer group for material goods?",
        "How many kgs of waste ends up in our landfill every year?",
        "How many kgs does each household contribute?",
        "What percent of the waste ends up getting recycled?",
        "If all 8 billion of us consumed at the level of the average citizen "
        "of the United States of America, we would need about ___ earths.",
        "What are some ways to consume sustainability?",
        "By 2100, if we do nothing, the temperature of the Earth's surface is"
        " projected to increase by how many degrees celcius?",
        "How many kilograms of e-waste is generated globally each year?",
        "Which material is the most commonly overconsumed and leads to "
        "significant environmental pollution?",
        "How does overconsumption contribute to climate change?",
        "What percentage of global food production is wasted annually?",
        "What is the main driver of overconsumption in developed countries?",
        "What is the average carbon footprint of an individual in a high-"
        "consumption country per year?",
        "What is the estimated amount of plastic waste produced globally "
        "each year?"
    ],
    "answer": [
        2,  # question 1 answer, and continued for the rest of questions below.
        2,  
        1,
        3,
        3,
        3,
        4, 
        2, 
        3,
        4, 
        1,
        3, 
        2,  
        4, 
        1  
    ],
    "options": [
        ["The decrease of the use of cars",
         "The excessive consumption or use of something",
         "The decrease consumption of something",
         "The excessive use of energy"
        ],
        ["Millennials (1981 - 1996)",
         "Gen Z (1997 - 2012)",
         "Gen X (1965 - 1980)",
         "Baby Boomers (1946 - 1964)"
        ],
        ["17,000,000 tonnes",
         "25,000,000 tonnes",
         "14,000,000 tonnes",
         "1,000,000 tonnes"
        ],
        ["510 kgs",
         "626 kgs",
         "784 kgs",
         "976 kgs"
        ],
        ["12%",
         "28%",
         "37%",
         "72%"
        ],
        ["At least 3",
         "At least 4",
         "At least 5",
         "At least 6"
        ],
        ["Reduce, Reuse, Recycle",
         "Support Local and Organic",
         "Advocate for Change",
         "All of the above"
        ],
        ["2°C",
         "4°C",
         "6°C",
         "8°C"
        ],
        ["10 million tonnes",
         "20 million tonnes",
         "50 million tonnes",
         "100 million tonnes"
        ],
        ["Glass",
         "Wood",
         "Metal",
         "Plastic"
        ],
        ["It increases greenhouse gas emissions.",
         "It reduces greenhouse gas emissions.",
         "It has no impact on climate change.",
         "It stabilizes the climate."
        ],
        ["10%",
         "20%",
         "30%",
         "40%"
        ],
        ["Lack of awareness",
         "Cultural values and consumerism",
         "Government policies",
         "Environmental regulations"
        ],
        ["2 tonnes CO2",
         "5 tonnes CO2",
         "10 tonnes CO2",
         "20 tonnes CO2"
        ],
        ["300 million tonnes",
         "500 million tonnes",
         "700 million tonnes",
         "1 billion tonnes"
        ]
    ]
}


# The Main Window (the first one users will see)
class MainWindow:
    """Main window code."""
    def __init__(self, master):
        """Basic code for the display of the window."""
        self.master=master
        self.master.title("EcoSmart")
        self.master.configure(bg="oldlace")
        self.master.resizable(False, False)

        # Calculate center position
        w_w=1200
        w_h=750
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()

        x_position=(screen_width-w_w)//2
        y_position=(screen_height-w_h)//4

        # Set window geometry
        self.master.geometry(f"{w_w}x{w_h}+{x_position}+{y_position}")

        self.firstwindow=tk.Frame(self.master, bg="oldlace")
        self.firstwindow.pack(fill="both", expand=True)

        # Title and headings of the window
        label=tk.Label(self.firstwindow, 
                       text="EcoSmart\nOverconsumption Quiz", 
                       font=("Helvetica", 28, "bold"), 
                       fg="green", bg="oldlace")
        label.pack(pady=40)

        description=tk.Label(self.firstwindow, text="Welcome!\nThis "+
                             "program is to teach and test you on "+
                             "your knowledge about \nover-consumption. "+
                             "If you are new here, please sign up, "+
                             "otherwise login.",font=("Helvetica", 15), 
                             fg="green", bg="oldlace")
        description.place(x=290, y=140)

        # Buttons on the window, that do different things
        signup_button=tk.Button(self.firstwindow, text="SIGN UP", width=10, 
                                height=2, fg="green", bg="white",
                                font=("Helvetica", 10, "bold"),
                                command=self.signup)
        signup_button.place(x=1090, y=50)

        login_button=tk.Button(self.firstwindow, text="LOGIN", width=10, 
                               height=2, fg="green", bg="white",
                               font=("Helvetica", 10, "bold"),
                               command=self.login)
        login_button.place(x=985, y=50)

        exit_button=tk.Button(self.firstwindow, text='EXIT', width=10, 
                              height=2, fg="black", bg="white", 
                              font=("Helvetica", 10, "bold"),
                              command=self.check_exit)
        exit_button.place(x=1090, y=685)

        # Code to add a picture to the window
        # Read the Image
        image=Image.open("picture1.png")

        # Resize the image using resize() method
        resize_image=image.resize((650, 500))

        img=ImageTk.PhotoImage(resize_image)

        # Create a label and add resize image
        label1=tk.Label(image=img)
        label1.image=img
        label1.place(x=280, y=220)

        self.pending_user_info={}
        self.create_sidebar()

    # The other buttons on the window (sidebar) and will always be there
    def create_sidebar(self):
        """The buttons on the side of the window (will always be there)."""
        buttons=[
            ("HOME", self.open_popup),
            ("USER\nMANUAL", self.open_popup),
            ("QUIZ", self.open_popup),
            ("LEARN", self.open_popup),
            ("ALTERNATIVE\nPRODUCTS", self.open_popup),
            ("ABOUT", self.open_popup),
            ("HELP", self.open_popup)
        ]

        for i, (text, command) in enumerate(buttons):
            btn=tk.Button(self.master, text=text, width=11, height=2,
                            font=("Helvetica", 10, "bold"), fg="green", 
                            bg="white", command=command)
            btn.place(x=50, y=50+i*100)

    def check_exit(self):
        """Ask if they want to exit (verify)."""
        result=mb.askquestion("Exit", "Are you sure you want to exit"+
                              " the program now?")
        if result=="yes":
            self.master.destroy()

    def open_popup(self):
        """Tell user to sign in / login first if side bar buttons are 
        clicked.
        """
        mb.showwarning("Warning", "Please login or sign up first please.")

    # Open the different windows when the specific button is clicked
    def signup(self):
        """Open sign up window."""
        self.signup_window=SignUpWindow(self)
    
    def login(self):
        """Open login window."""
        self.login_window=LoginWindow(self)

    # This function stores all the users info. Will be called everywhere
    def store_pending_user_info(self, first_name, username, password, 
                                date_of_birth):
        """Storing users details."""
        self.pending_user_info={
            "username":username,
            "password":password,
            "first_name":first_name,
            "date_of_birth":date_of_birth
        }
        self.user_info=self.pending_user_info


# All the code for the sign up window
class SignUpWindow:
    """Code for sign up window."""
    def __init__(self, parent):
        """Basic code for the display of the sign up window."""
        self.parent=parent
        self.signup_window=tk.Toplevel()
        self.signup_window.title("Signup Window")
        self.signup_window.configure(bg="oldlace")
        self.signup_window.resizable(False, False)

        # Calculate center position
        w_w=600  # Window width
        w_h=550  # Window height
        screen_width=self.signup_window.winfo_screenwidth()
        screen_height=self.signup_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.signup_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        # Headings for the different entries
        title=tk.Label(self.signup_window, text="Sign Up", 
                       font=("Helvetica", 20, "bold"), 
                       fg="black", bg="oldlace")
        title.pack(pady=20)

        title1=tk.Label(self.signup_window, text="First Name", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title1.pack(pady=2)

        self.first_name=self.create_entry("First Name")

        title2=tk.Label(self.signup_window, text="Username", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title2.pack(pady=2)

        self.username=self.create_entry("Username")

        title3=tk.Label(self.signup_window, text="Password", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title3.pack(pady=2)

        self.password=self.create_entry("Password", show="*")

        title4=tk.Label(self.signup_window, text="Confirm Password", 
                        font=("Helvetica", 13, "bold"), fg="black", 
                        bg="oldlace")
        title4.pack(pady=2)

        self.confirm_password=self.create_entry("Password", show="*")

        title5=tk.Label(self.signup_window, 
                        text="Date of Birth (DD/MM/YYYY)", 
                        font=("Helvetica", 13, "bold"), fg="black", 
                        bg="oldlace")
        title5.pack(pady=2)

        self.date_of_birth=self.create_entry("(DD/MM/YYYY)")

        next_button=tk.Button(self.signup_window, text="NEXT", width=7,
                              font=("Helvetica", 15, "bold"), 
                              height=1, fg="green", bg="white", 
                              command=self.signup)
        next_button.pack(pady=20)

        # Button that changes between the sign up and login windows
        def change2():
            """Changing between the sign up and login window."""
            LoginWindow(parent)
            self.signup_window.destroy()

        login_change_button=tk.Button(self.signup_window, text="LOGIN", 
                                      font=("Helvetica", 15, "bold"),
                                      width=7, height=1, fg="green", 
                                      bg="white", command=change2)
        login_change_button.place(x=480, y=20)

        back_button=tk.Button(self.signup_window, text="EXIT", width=7,
                              font=("Helvetica", 15, "bold"),
                              height=1, fg="black", bg="white", 
                              command=self.signup_window.destroy)
        back_button.place(x=480, y=485)

    def create_entry(self, placeholder, show=None):
        """Display what the entry is for."""
        entry=tk.Entry(self.signup_window, show=show, 
                       font=("Helvetica", 12))
        entry.pack(pady=10)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, e=entry, 
                   p=placeholder:self.on_entry_click(event, e, p))
        entry.bind("<FocusOut>", lambda event, e=entry, 
                   p=placeholder:self.on_focusout(event, e, p))
        entry.config(fg="grey")
        return entry

    def on_entry_click(self, event, entry, placeholder):
        """Show the text they input."""
        if entry.get()==placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focusout(self, event, entry, placeholder):
        """The colour of what the entry line is for."""
        if entry.get()=="":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def validate_date_of_birth(self, date_of_birth):
        """Validate the birthdate with the current time and date."""
        try:
            birthdate=datetime.strptime(date_of_birth, "%d/%m/%Y")
            return birthdate
        except ValueError:
            return None

    # Validating all the entry fields (data collected from user)
    def validate_fields(self):
        """Validating all the users details they input."""
        first_name=self.first_name.get().strip()
        username=self.username.get().strip()
        password=self.password.get().strip()
        confirm_password=self.confirm_password.get().strip()
        date_of_birth=self.date_of_birth.get().strip()

        if (first_name=="First Name" or username=="Username" or 
            password=="Password" or confirm_password=="Confirm Password" or 
            date_of_birth=="Date of Birth (DD/MM/YYYY)"):
            mb.showwarning("Incomplete Fields", "Please fill out all "+
                           "the fields.", parent=self.signup_window)
            return False
        
        if len(first_name)>10 or len(username)>10 or len(password)>10:
            mb.showwarning("Invalid Input", "First name, username, and"+
                           " password must be 10 characters or less.", 
                           parent=self.signup_window)
            return False

        if not first_name.isalpha():
            mb.showwarning("Invalid First Name", "First name can only "+
                           "contain letters.", 
                           parent=self.signup_window)
            return False

        if not re.match("^[A-Za-z0-9]+$", username):
            mb.showwarning("Invalid Username", "Username can only "+
                           "contain letters and numbers without "+
                           "spaces.", parent=self.signup_window)
            return False

        if password!=confirm_password:
            mb.showerror("Error", "Passwords do not match.", 
                         parent=self.signup_window)
            return False

        birthdate=self.validate_date_of_birth(date_of_birth)
        if not birthdate:
            mb.showerror("Invalid Date Of Birth", "Please enter a valid "+
                         "date of birth. Remember to include the ' / '.", 
                         parent=self.signup_window)
            return False

        age=(datetime.today()-birthdate).days//365
        if age<0 or age>90:
            mb.showerror("Invalid Date Of Birth", "Invalid date of birth. "+
                         "Remember to include the ' / '.", 
                         parent=self.signup_window)
            return False
        elif age<18 or age>30:
            if age<10:
                age_maybe=mb.askquestion("Age Notice", "Are you sure"+
                                         "that is the correct age?", 
                                         parent=self.signup_window)
                if age_maybe=="no":
                    return False
            else:
                mb.showwarning("Age Notice", "This program is "+
                               "designed for ages 18-30. You are still"+
                               " able to use the program.", 
                               parent=self.signup_window)
        else:
            mb.showwarning("Age Notice", "This program is designed for"+
                           " ages 18-30.", parent=self.signup_window)
                
        return True
    
    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)
    
    # Saving the data if all the entries is correctly inputted
    def signup(self):
        """Saving the data and telling the user that."""
        if not self.validate_fields():
            return

        first_name=self.first_name.get().strip()
        username=self.username.get().strip()
        password=self.password.get().strip()
        date_of_birth=self.date_of_birth.get().strip()
        birthdate=self.validate_date_of_birth(date_of_birth)

        if os.path.exists(f"{username}.txt"):
            mb.showwarning("Warning", "Your username already exists. "+
                           "Please choose another one or if you have "+
                           "already signed up before, please login "+
                           "(click the button on the top right)", 
                           parent=self.signup_window)
            return

        with open(f"{username}.txt", "w") as file:
            file.write(f"First Name: {first_name}\n")
            file.write(f"Birthdate: {birthdate.strftime('%d/%m/%Y')}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")

        self.parent.store_pending_user_info(first_name, username, 
                                            password, date_of_birth)
        
        mb.showinfo("Success", "Your data has been saved. Please login"+
                    " next time with your exact details. Thank you :)", 
                    parent=self.signup_window)
        self.signup_window.destroy()
        self.open_dashboard()


# All the code for the sign up window
class LoginWindow:
    """The code for the login window."""
    def __init__(self, parent):
        """The basic code for the main display of the login window."""
        self.parent=parent
        self.login_window=tk.Toplevel()
        self.login_window.title("Login Window")
        self.login_window.configure(bg="oldlace")
        self.login_window.resizable(False, False)

        # Calculate center position
        w_w=600  # Window width
        w_h=320  # window height
        screen_width=self.login_window.winfo_screenwidth()
        screen_height=self.login_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.login_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        # Headings for the different entries
        title=tk.Label(self.login_window, text="Login", 
                       font=("Helvetica", 20, "bold"), 
                       fg="black", bg="oldlace")
        title.pack(pady=20)

        title1=tk.Label(self.login_window, text="Username", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title1.pack(pady=2)

        self.username=self.create_entry("Username")

        title2=tk.Label(self.login_window, text="Password", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title2.pack(pady=2)
        
        self.password=self.create_entry("Password", show="*")

        next_button=tk.Button(self.login_window, text="NEXT", width=7, 
                              height=1, fg="green", bg="white", 
                              font=("Helvetica", 15, "bold"),
                              command=self.login)
        next_button.pack(pady=20)

        # Button that changes between the sign up and login windows
        def change():
            """Change between the sign up and login windows, when button 
            clicked.
            """
            SignUpWindow(parent)
            self.login_window.destroy()

        signup_change_button=tk.Button(self.login_window, text="SIGN UP", 
                                       font=("Helvetica", 15, "bold"), 
                                       width=7, height=1, fg="green", 
                                       bg="white", command=change)
        signup_change_button.place(x=480, y=20)

        back_button=tk.Button(self.login_window, text="EXIT", 
                              font=("Helvetica", 15, "bold"), width=7, 
                              height=1, fg="black", bg="white", 
                              command=self.login_window.destroy)
        back_button.place(x=480, y=260)

    def create_entry(self, placeholder, show=None):
        """Display what the entry is for."""
        entry=tk.Entry(self.login_window, show=show, 
                         font=("Helvetica", 12))
        entry.pack(pady=10)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, e=entry, 
                   p=placeholder:self.on_entry_click(event, e, p))
        entry.bind("<FocusOut>", lambda event, e=entry, 
                   p=placeholder:self.on_focusout(event, e, p))
        entry.config(fg="grey")
        return entry

    def on_entry_click(self, event, entry, placeholder):
        """Show the text they input."""
        if entry.get()==placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focusout(self, event, entry, placeholder):
        """The colour of what the entry line is for."""
        if entry.get()=="":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)

    # Validating all the entry fields (data collected from user)
    def validate_login(self, username, password):
        """Validating all the users details they input."""
        if os.path.exists(f"{username}.txt"):
            with open(f"{username}.txt", "r") as file:
                lines=file.readlines()
                stored_username=lines[2].split(": ")[1].strip()
                stored_password=lines[3].split(": ")[1].strip()
                if username==stored_username and password==stored_password:
                    self.parent.store_pending_user_info(
                        first_name=lines[0].split(": ")[1].strip(),
                        username=stored_username,
                        password=stored_password,
                        date_of_birth=lines[1].split(": ")[1].strip()
                    )
                    return True
        return False

    # Saving the data if all the entries is correctly inputted
    def login(self):
        """Saving the data and telling the user that."""
        username=self.username.get()
        password=self.password.get()

        if self.validate_login(username, password):
            self.login_window.destroy()
            self.open_dashboard()
        else:
            mb.showwarning("Error", "Please fill out all the fields", 
                           parent=self.login_window)


# Randomised quiz code
class RandomQuiz:
    """Code for the randomised (shuffled) quiz."""
    def __init__(self, root, user_info):
        """The basic code for the display of the quiz window."""
        self.root=root
        self.root.configure(bg="oldlace")
        self.q_no=0
        self.correct=0
        self.user_info=user_info
        self.display_title()

        # Prepare and shuffle the questions
        self.prepare_questions()

        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_question()
        self.display_options()
        self.buttons()
        self.data_size=len(self.questions)

        # Progress bar
        style=ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='green')
        self.progress_var=tk.DoubleVar()
        self.progress_bar=ttk.Progressbar(self.root, maximum=100, 
                                          length=300, 
                                          variable=self.progress_var, 
                                          style="green.Horizontal."+    
                                          "TProgressbar")
        self.progress_bar.place(x=50, y=95)
        self.update_progress_bar()

    # Getting the questions randomised - shuffled
    def prepare_questions(self):
        """Shuffling the questions - from the list in the dictionary."""
        combined=list(zip(data['question'], data['answer'], 
                            data['options']))
        random.shuffle(combined)
        self.questions, self.answers, self.options=zip(*combined)

    def next_btn(self):
        """Tell the user that they need to click an option (answer)."""
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option before"+
                           " proceeding.", parent=self.root)
            return
        
        if self.check_ans(self.q_no):
            self.correct += 1
        
        self.q_no += 1

        if self.q_no == self.data_size:
            self.update_progress_bar(final=True)  # Progress bar to 100%
            self.root.after(100, self.display_result) 
        else:
            self.update_progress_bar()
            self.display_question()
            self.display_options()

    # Displaying the users quiz result after completed
    def display_result(self):
        """Displaying the correct, wrong, and overall score of the quiz.
        And saving it to their user profile file. 
        """
        wrong_count=self.data_size-self.correct
        correct=f"Correct: {self.correct}"
        wrong=f"Wrong: {wrong_count}"
        score=int(self.correct/self.data_size*100)
        result=f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}", 
                    parent=self.root)
        
        date=datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # Save results to user's file with their info
        username=self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data: 
            data.write("\nQuiz scores: \n")
            data.write(f"Date: {date}\n")
            data.write(f"Correct: {self.correct}\n")
            data.write(f"Wrong: {wrong_count}\n")
            data.write(f"Score: {score}%\n")
        
        # Add the popup messagebox
        mb.showinfo("Learn More", "To do better next time, go to the 'LEARN'"+
                    " tab to learn more about over-consumption.", 
                    parent=self.root)
        
        self.root.destroy()

    def check_ans(self, q_no):
        """Checking the answers of the options the user clicked."""
        return self.opt_selected.get()==self.answers[q_no]

    def buttons(self):
        """Important buttons for the quiz."""
        next_button=tk.Button(self.root, text="NEXT", command=self.next_btn,
                              bg="white", fg="black", width=7, height=1, 
                              font=("Helvetica", 16, "bold"))
        next_button.place(x=470, y=550)
        quit_button=tk.Button(self.root, text="EXIT", 
                              bg="white", width=7, height=1,
                              fg="black", command=self.check_exit,
                              font=("Helvetica", 16, "bold"))
        quit_button.place(x=920, y=95)

    def check_exit(self):
        """Verify if the user wants to exit, because progress will 
        not be saved.
        """
        result=mb.askquestion("Exit", "Are you sure you want to exit the "+
                              "quiz now? Your progress won't be saved.", 
                              parent=self.root)
        if result=="yes":
            self.root.destroy()

    def display_options(self):
        """Displaying the options for the different questions."""
        val=0
        self.opt_selected.set(0)  # Reset the selected option
        for option in self.options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    # Displaying the questions of the quiz (shuffled from before)
    def display_question(self):
        """Displaying the questions for the quiz."""
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label=tk.Label(self.root, text=self.questions[self.q_no], 
                              width=100, font=('Helvetica', 20, 'bold'), 
                              anchor='w', wraplength=900, justify='left', 
                              bg="oldlace", fg="black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        """Title of the quiz."""
        title=tk.Label(self.root, text="OVERCONSUMPTION QUIZ",
                       width=50, height=2, bg="green", fg="white", 
                       font=("Helvetica", 26, "bold"))
        title.place(x=0, y=0)

    def radio_buttons(self):
        """How the option are shown and clicked my the user (radio buttons)."""
        q_list=[]
        y_pos=250
        while len(q_list)<4:
            radio_btn=tk.Radiobutton(self.root, text=" ", 
                                     variable=self.opt_selected,
                                     value=len(q_list)+1, 
                                     font=("Helvetica", 18), fg="black", 
                                     bg="oldlace")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos+=60
        return q_list

    def update_progress_bar(self, final=False):
        """Updating the progress bar when moving onto the next question."""
        if final or self.q_no >= self.data_size:
            self.progress_var.set(100)
        else:
            self.progress_var.set((self.q_no/self.data_size) * 100)


# Code for the normal ordered quiz
class Quiz:
    """Code for the normal ordered quiz."""
    def __init__(self, root, user_info):
        """The basic code for the display of the quiz window."""
        self.root=root
        self.root.configure(bg="oldlace")
        self.q_no=0
        self.correct=0
        self.user_info=user_info
        self.display_title()
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(data['question'])
        
        # Progress bar
        style=ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='green')
        self.progress_var=tk.DoubleVar()
        self.progress_bar=ttk.Progressbar(self.root, maximum=100, length=300, 
                                          variable=self.progress_var, 
                                          style="green.Horizontal."+
                                          "TProgressbar")
        self.progress_bar.place(x=50, y=95)
        self.update_progress_bar()

    def next_btn(self):
        """Tell the user that they need to click an option (answer)."""
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option "+
                           "before proceeding.", parent=self.root)
            return
        
        if self.check_ans(self.q_no):
            self.correct += 1
        
        self.q_no += 1

        if self.q_no == self.data_size:
            self.update_progress_bar(final=True)  # Progress bar to 100%
            self.root.after(100, self.display_result)  
        else:
            self.update_progress_bar()
            self.display_question()
            self.display_options()
    
    # Display the results of the quiz to the user
    def display_result(self):
        """Displaying the correct, wrong, and overall score of the quiz.
        And saving it to their user profile file. 
        """
        wrong_count=self.data_size-self.correct
        correct=f"Correct: {self.correct}"
        wrong=f"Wrong: {wrong_count}"
        score=int(self.correct/self.data_size*100)
        result=f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}", 
                    parent=self.root)
        
        date=datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # Save results to user's file with their info
        username=self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data: 
            data.write("\nQuiz scores: \n")
            data.write(f"Date: {date}\n")
            data.write(f"Correct: {self.correct}\n")
            data.write(f"Wrong: {wrong_count}\n")
            data.write(f"Score: {score}%\n")

        # Add the popup messagebox
        mb.showinfo("Learn More", "To do better next time, go to the 'LEARN'"+
                    " tab to learn more about over-consumption.", 
                    parent=self.root)
        self.root.destroy()

    def check_ans(self, q_no):
        """Checking the answers of the options the user clicked."""
        return self.opt_selected.get()==data['answer'][q_no]

    def buttons(self):
        """Important buttons for the quiz."""
        next_button=tk.Button(self.root, text="NEXT", command=self.next_btn,
                              bg="white", fg="black", width=7, height=1, 
                              font=("Helvetica", 16, "bold"))
        next_button.place(x=470, y=550)
        quit_button=tk.Button(self.root, text="EXIT", 
                              bg="white", width=7, height=1,
                              fg="black", command=self.check_exit,
                              font=("Helvetica", 16, "bold"))
        quit_button.place(x=920, y=95)

    def check_exit(self):
        """Verify if the user wants to exit, because progress will 
        not be saved.
        """
        result=mb.askquestion("Exit", "Are you sure you want to exit the"+
                              " quiz now?", parent=self.root)
        if result=="yes":
            self.root.destroy()

    def display_options(self):
        """Displaying the options for the different questions."""
        val=0
        self.opt_selected.set(0)
        for option in data['options'][self.q_no]:
            self.opts[val]['text']=option
            val+=1
    
    # Displaying the question of the quiz (in the normal order)
    def display_question(self):
        """Displaying the questions for the quiz."""
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label=tk.Label(self.root, text=data['question'][self.q_no], 
                                width=100, font=('Helvetica', 20, 'bold'), 
                                anchor='w', wraplength=900, justify='left',
                                bg="oldlace", fg="black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        """Title of the quiz."""
        title=tk.Label(self.root, text="OVERCONSUMPTION QUIZ",
                         width=50, bg="green", fg="white", height=2,
                         font=("Helvetica", 26, "bold"))
        title.place(x=0, y=0)

    def radio_buttons(self):
        """How the option are shown and clicked my the user (radio buttons)."""
        q_list=[]
        y_pos=250
        while len(q_list)<4:
            radio_btn=tk.Radiobutton(self.root, text=" ", 
                                     variable=self.opt_selected,
                                     value=len(q_list)+1, 
                                     font=("Helvetica", 18),
                                    fg="black", 
                                     bg="oldlace")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos+=60
        return q_list

    def update_progress_bar(self, final=False):
        """Updating the progress bar when moving onto the next question."""
        if final or self.q_no >= self.data_size:
            self.progress_var.set(100)
        else:
            self.progress_var.set((self.q_no/self.data_size) * 100)


# Code for the main dashboard window (after the user has logged in)
class DashboardWindow:
    """Code for the window after user had logged in."""
    def __init__(self, master, user_info):
        """Basic functionality and display for the window."""
        self.master=master
        self.user_info=user_info
        self.dashboard_window=tk.Toplevel(master)
        self.dashboard_window.title("Dashboard")
        self.dashboard_window.configure(bg="oldlace")
        self.dashboard_window.resizable(False, False)

        # Calculate center position
        w_w=1200  # Window width
        w_h=750  # window height
        screen_width=self.dashboard_window.winfo_screenwidth()
        screen_height=self.dashboard_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.dashboard_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        title=tk.Label(self.dashboard_window, text="EcoSmart", 
                       font=("Helvetica", 20, "bold"), fg="green", 
                       bg="oldlace")
        title.pack(pady=20)

        # Sidebar and main area
        self.create_sidebar()
        self.create_main_area()

        exit_button=tk.Button(self.dashboard_window, text='EXIT', 
                              font=("Helvetica", 10, "bold"), width=10, 
                              height=2, fg="black", bg="white", 
                              command=self.check_exit)
        exit_button.place(x=1090, y=685)

        signout_button=tk.Button(self.dashboard_window, text='SIGN OUT', 
                                 font=("Helvetica", 10, "bold"), width=10, 
                                 height=2, fg="black", bg="white", 
                                 command=self.signout)
        signout_button.place(x=1090, y=620)

        profile_button=tk.Button(self.dashboard_window, text='PROFILE', 
                                 font=("Helvetica", 10, "bold"), width=10, 
                                 height=2, fg="green", bg="white", 
                                 command=self.display_profile)
        profile_button.place(x=1090, y=50)

        self.display_home()

    def check_exit(self):
        """Verify if the user wants to exit."""
        result=mb.askquestion("Exit", "Are you sure you want to exit the "+
                              "program now?", parent=self.dashboard_window)
        if result=="yes":
            self.master.destroy()

    def signout(self):
        """Verify if the user wants to sign out."""
        result=mb.askquestion("Sign Out", "Are you sure you want to sign "+
                              "out of the program now?", 
                              parent=self.dashboard_window)
        if result=="yes":
            self.dashboard_window.destroy()

    # The buttons on the side - tabs - because they are all in the same
    # window.
    def create_sidebar(self):
        """The side bar buttons on the window."""
        buttons=[
            ("HOME", self.display_home),
            ("USER\nMANUAL", self.display_manual),
            ("QUIZ", self.display_quiz),
            ("LEARN", self.display_success_stories),
            ("ALTERNATIVE\nPRODUCTS", self.display_alternative_products),
            ("ABOUT", self.display_about),
            ("HELP", self.display_help)
        ]

        for i, (text, command) in enumerate(buttons):
            btn=tk.Button(self.dashboard_window, text=text, width=11, 
                          height=2, font=("Helvetica", 10, "bold"), 
                          fg="green", bg="white", command=command)
            btn.place(x=50, y=50+i*100)

    # The area that will be cleared to create the tab look. Where it 
    # will be on the same window but the display will change in the 
    # specified area.
    def create_main_area(self):
        """Specified area of the window that soon will be cleared 
        everytime another tab is pressed (sidebar buttons - tabs).
        """
        self.main_frame=tk.Frame(self.dashboard_window, bg="oldlace")
        self.main_frame.place(x=250, y=50, width=900, height=700)

    def clear_main_area(self):
        """Clearing the specified area for the tabs."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # The Home page of the Dashboard Window
    def display_home(self):
        """The home page of the window. The display of titles etc."""
        self.clear_main_area() # Specified part cleared for the new display                                        

        # Title label
        title_label=tk.Label(self.main_frame, text="Home Page", 
                             font=("Helvetica", 30), fg="black", 
                             bg="oldlace")
        title_label.place(x=240, y=5)

        label=tk.Label(self.main_frame, 
                       text="Welcome to the Home Page\nThis program is to "+
                       "teach and test you on your knowledge about \nover"+
                       "-consumption. Click the buttons on the side "+
                       "to navigate through the program.", 
                       font=("Helvetica", 14),
                       fg="green", bg="oldlace")
        label.place(x=10, y=60)

        # Load and display image
        home_image_path="picture1.png"
        home_image=Image.open(home_image_path)
        resize_image=home_image.resize((700, 530))
        self.home_img=ImageTk.PhotoImage(resize_image)

        home_image_label=tk.Label(self.main_frame, image=self.home_img)
        home_image_label.image=self.home_img  
        home_image_label.place(y=130, x=0)

    # The window that shows the user manual 
    def display_manual(self):
        """The display of the user manual for the user - as a picture."""
        self.clear_main_area() # Specified part cleared for the new display 

        title2=tk.Label(self.main_frame, text="User Manual", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

        # Load and display image - of the user manual
        manual_image_path="manual.png"
        manual_image=Image.open(manual_image_path)
        resize_image=manual_image.resize((730, 600))
        self.manual_img=ImageTk.PhotoImage(resize_image)

        manual_image_label=tk.Label(self.main_frame, image=self.manual_img, 
                                      borderwidth=0, highlightthickness=0)
        manual_image_label.image=self.manual_img  
        manual_image_label.place(y=80, x=5)

    # The quiz page of the dashboard window. Where the user can click 
    # what kind of quiz they want to do (random or normal).
    def display_quiz(self):
        """Displaying the quiz page where the user can choose between the 
        normal or shuffled quiz order. 
        """
        self.clear_main_area() # Specified part cleared for the new display 

        # Title label
        title_label=tk.Label(self.main_frame, text="Quiz Page", 
                             font=("Helvetica", 30), fg="black", 
                             bg="oldlace")
        title_label.place(x=249, y=5)

        label=tk.Label(self.main_frame, text="Welcome to the Quiz Page\nTo"+
                       " take the quiz, press the quiz button below.\n"+
                       "And decide if you want to have it randomised or not"+
                       ".\nThen go onto the Learn tab to teach yourself "+
                       "more, to do better in the quiz, next time.",
                       font=("Helvetica", 15), fg="green", bg="oldlace")
        label.place(x=0, y=80)

        # Load and display image
        image_path="overconsumption.jpg"
        image=Image.open(image_path)
        resize_image=image.resize((750, 350))
        img=ImageTk.PhotoImage(resize_image)

        image_label=tk.Label(self.main_frame, image=img)
        image_label.image=img  
        image_label.place(y=200, x=0)

        # Quiz button
        quiz_button=tk.Button(self.main_frame, text='QUIZ', width=10, 
                              height=2, font=("Helvetica", 10, "bold"), 
                              fg="green", bg="white", 
                              command=self.step1_open_quiz_window)
        quiz_button.place(x=300, y=635)

    # The learning page of the Dashboard Window. There is also a button
    # that will show some interesting and educational video / pictures 
    # about the topic
    def display_success_stories(self):
        """Where the user can read more educational stories about the topic,
        and click the more info button to get educational pictures / videos.
        """
        self.clear_main_area()

        # Title
        title_label=tk.Label(self.main_frame, 
                             text="Learn About Over-Consumption", 
                             font=("Helvetica", 30), fg="black", 
                             bg="oldlace")
        title_label.place(x=70, y=5)

        # Create a Canvas widget
        canvas=tk.Canvas(self.main_frame, bg="oldlace", width=750, 
                         height=530)
        canvas.place(x=-20, y=70)

        # Add a scrollbar to the canvas
        scrollbar=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                command=canvas.yview)
        scrollbar.place(x=733, y=70, height=536)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        frame=tk.Frame(canvas, bg="oldlace")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Function to update the scrollregion of the canvas
        def update_scrollregion(event):
            """Updating the scroll feature of the information."""
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", update_scrollregion)

        # Information content - educational for the user to read
        content="""
What is Over-Consumption?
Over-consumption refers to the excessive use of resources beyond what is sustainable. This habit leads to
significant environmental degradation, including deforestation, loss of biodiversity, pollution, and 
climate change. The constant demand for new products fuels over-consumption, driven by the desire for 
the latest technology, fashion trends, and other consumer goods.

Historical Context of Over-Consumption

The Industrial Revolution
The roots of over-consumption trace back to the Industrial Revolution, which began in the late 18th 
century. This period marked a significant shift from manual labor to industrialized production, 
leading to mass production and mass consumption. Industries heavily relied on non-renewable 
resources such as coal and oil, driving economic growth but also causing severe environmental 
degradation and resource depletion.

Environmental Impact
The rapid industrialization resulted in increased pollution, deforestation, and the extraction of 
natural resources at unprecedented rates. The focus on economic expansion often overlooked environmental
sustainability, setting a precedent for future consumption patterns.

The Current State of Over-Consumption

Affluent Lifestyles and Global Disparities
Today, over-consumption is a global challenge, predominantly driven by affluent lifestyles in developed 
countries. The consumption of natural resources varies widely across the globe, with wealthier nations 
consuming far more resources than developing countries. For instance, the average North American 
consumes 90 kilograms of resources each day, significantly higher than the global average.

Environmental Consequences
Modern consumption patterns contribute to increased carbon emissions, pollution, and biodiversity loss. 
The demand for new products and technological advancements exacerbates these issues. Despite efforts to 
improve efficiency through technology, the continuous rise in consumption levels offsets any gains 
towards sustainability.

Impact of Over-Consumption
Environmental Pollution: Over-consumption leads to increased waste production, much of which ends up in 
landfills or oceans. For example, plastic pollution has become a critical issue, contributing to the 
destruction of marine life and ecosystems.

Resource Depletion: 
The extraction and use of natural resources at unsustainable rates result in the depletion of vital 
resources such as water, minerals, and fossil fuels. This creates a strain on the environment and 
future generations.

Climate Change: 
The production and disposal of consumer goods are significant contributors to greenhouse gas 
emissions, driving climate change. The carbon footprint of high-consumption lifestyles, particularly
in wealthier countries, exacerbates global warming.

Sustainable Practices
Addressing over-consumption requires individual lifestyle changes and broader economic reforms. 
Sustainable practices such as using renewable resources, reducing waste, and promoting circular 
economies are essential for mitigating the impacts of over-consumption.

Addressing Over-Consumption

Innovative Solutions
Looking ahead, addressing over-consumption demands a fundamental shift in how economies operate 
and how individuals perceive wealth and consumption. Relying solely on technological solutions 
is insufficient; systemic changes are necessary.

Economic and Policy Reforms
Future strategies include implementing policies that promote sustainable consumption, encouraging the 
development of green technologies, and fostering a culture of conservation and mindfulness.

Success Stories in Combating Over-Consumption

Tamil Nadu, India:
Tamil Nadu has shown that increasing literacy and workforce participation can correlate with 
reduced carbon emissions. By focusing on education and sustainable economic practices, the state has
made strides in mitigating the impact of urbanization on the environment.

Malaysia and the Philippines: 
These countries have implemented “ship-back” initiatives to return waste to the 
originating countries in the Global North. This move has forced international measures for better 
waste management and reinforced the importance of global environmental justice.

UNICEF’s Efforts: 
UNICEF has been actively working to improve children’s environments worldwide. Their reports 
highlight the need for better environmental policies that are child-sensitive, reducing pollutants, 
and ensuring high-quality housing and neighborhoods. This effort also focuses on protecting the most
vulnerable children from environmental harms.

Conclusion
Understanding the historical context, current state, and future strategies for addressing 
over-consumption helps us appreciate the urgency of adopting sustainable practices. By learning 
from past mistakes and current successes, we can work towards a more sustainable and equitable future.



.

"""

        # Add the information content to the frame
        text_widget=tk.Text(frame, wrap=tk.WORD, font=("Helvetica", 12), 
                            bg="oldlace", bd=0, fg="black", width=100, 
                            height=33)
        
        # Split content into paragraphs and add to text_widget with formatting
        paragraphs=content.strip().split('\n\n')
        for paragraph in paragraphs:
            lines=paragraph.strip().split('\n')
            if lines:
                first_line=lines[0]
                remaining_lines='\n'.join(lines[1:])
                text_widget.insert(tk.END, first_line+'\n', 'first_line')
                if remaining_lines:
                    text_widget.insert(tk.END, remaining_lines+'\n\n')
        
        text_widget.tag_configure('first_line', font=("Helvetica", 16, "bold"))
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # The scrollbar
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        self.main_frame.pack_propagate(False)
        self.main_frame.config(padx=20, pady=10)

        # Add the Photos / Videos button
        photos_button=tk.Button(self.main_frame, text="MORE INFORMATION", 
                                bg="white", font=("Helvetica", 13, "bold"), 
                                command=self.open_photos_window)
        photos_button.place(x=240, y=625)

    # The code for the photos/vidoes page
    def open_photos_window(self):
        """Window where there are videos and pictures that are eductational
        for the topic. 
        """
        self.photos_window=tk.Toplevel(self.master)
        self.photos_window.title("Photo / Videos")
        self.photos_window.configure(bg="oldlace")
        self.photos_window.resizable(False, False)

        # Calculate center position
        w_w=1000  # Window width
        w_h=600  # window height
        screen_width=self.photos_window.winfo_screenwidth()
        screen_height=self.photos_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.photos_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        title=tk.Label(self.photos_window, text="EcoSmart", 
                         font=("Helvetica", 20, "bold"), fg="green", 
                         bg="oldlace")
        title.pack(pady=20)

        # Video links and buttons
        def open_video1():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=KLiXmteCvUI"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text="Video About Our "+
                                 "Obsession With Economic Growth:", 
                                 font=("Helvetica", 11, 'bold'), fg="black", 
                                 bg="oldlace")
        video_url_label.pack(pady=10)
        
        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 1", fg = "green",
                      font=("Helvetica", 12, 'bold'), command=open_video1)
        btn.pack(pady=7)

        # Video links and buttons
        def open_video2():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=MilcnqXKjR4&t=177s"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text="Video About How "+
                                 "Consumerism Ruins Our Planet\nAnd Finances:", 
                                 font=("Helvetica", 11, 'bold'), fg="black", 
                                 bg="oldlace")
        video_url_label.pack(pady=10)

        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 2", fg = "green",
                      font=("Helvetica", 12, 'bold'), command=open_video2)
        btn.pack(pady=7)

        # Video links and buttons
        def open_video3():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=8eoeB_Dxba8"
            webbrowser.open(video_url)

        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text="Video About How "+
                                 "Overconsumption\nThreatens Our Planet:", 
                                 font=("Helvetica", 11, 'bold'), fg="black", 
                                 bg="oldlace")
        video_url_label.pack(pady=10)
        
        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 3", fg = "green",
                      font=("Helvetica", 12, 'bold'), command=open_video3)
        btn.pack(pady=7)

        # Video links and buttons
        def open_video4():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=gDc6PB5iGjI"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text=" Video About "+
                                  "Global Environmental\nImpacts Of "+
                                  "Consumption:", 
                                  font=("Helvetica", 11, 'bold'), fg="black", 
                                  bg="oldlace")
        video_url_label.pack(pady=10)
        
        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 4", fg = "green",
                      font=("Helvetica", 12, 'bold'), command=open_video4)
        btn.pack(pady=7)

        back=tk.Button(self.photos_window, text="EXIT",  
                       font=("Helvetica", 13, 'bold'), 
                       command=self.photos_window.destroy)
        back.pack(pady=30)

        # Load and display image 1
        image_path1="picture4.webp"
        image1=Image.open(image_path1)
        resize_image1=image1.resize((250, 250))
        img1=ImageTk.PhotoImage(resize_image1)

        image_label1=tk.Label(self.photos_window, image=img1)
        image_label1.image=img1  
        image_label1.place(y=20, x=19)

        # Load and display image 2
        image_path2="picture3.jpg"
        image2=Image.open(image_path2)
        resize_image2=image2.resize((250, 250))
        img2=ImageTk.PhotoImage(resize_image2)

        image_label2=tk.Label(self.photos_window, image=img2)
        image_label2.image=img2  
        image_label2.place(y=20, x=730)

        # Load and display image 3
        image_path3="picture2.jpg"
        image3=Image.open(image_path3)
        resize_image3=image3.resize((350, 250))
        img3=ImageTk.PhotoImage(resize_image3)

        image_label3=tk.Label(self.photos_window, image=img3)
        image_label3.image=img3  
        image_label3.place(y=330, x=630)

        # Load and display image 4
        image_path4="picture5.png"
        image4=Image.open(image_path4)
        resize_image4=image4.resize((350, 250))
        img4=ImageTk.PhotoImage(resize_image4)

        image_label4=tk.Label(self.photos_window, image=img4)
        image_label4.image=img4  
        image_label4.place(y=330, x=19)
    
    # The page where it shows users common unsustainable products and 
    # in a table format of budget friendly sustainable alternatives    
    def display_alternative_products(self):
        """Displaying the alternative products, as a table format."""
        self.clear_main_area()

        title_label=tk.Label(self.main_frame, text="Budget-Friendly "+
                             "Alternative Products Page", 
                             font=("Helvetica", 30), fg="black", bg="oldlace")
        title_label.place(x=0, y=5)

        info_label=tk.Label(self.main_frame, text="Some alternatives to "+
                            "common unsustainable products.", 
                            font=("Helvetica", 15), fg="green", bg="oldlace")
        info_label.place(x=105, y=60)

        columns=('PRODUCTS', 'ALTERNATIVES')
        tree=ttk.Treeview(self.main_frame, columns=columns, show='headings')
        tree.heading('PRODUCTS', text='PRODUCTS')
        tree.heading('ALTERNATIVES', text='ALTERNATIVES')

        products_alternatives=[ # The different products 
            ('Glad Wrap', 'Beeswax wraps'),
            ('Plastic Bags', 'Reusable cloth bags'),
            ('Plastic Containers', 'Glass or stainless steel containers'),
            ('Plastic Straws', 'Metal, bamboo, or glass straws'),
            ('Disposable Coffee Cups', 'Reusable coffee cups'),
            ('Plastic Cutlery', 'Bamboo or metal cutlery'),
            ('Paper Towels', 'Reusable cloth towels'),
            ('Single-use Water Bottles', 'Reusable water bottles'),
            ('Disposable Razors', 'Safety razors'),
            ('Plastic Toothbrushes', 'Bamboo toothbrushes'),
            ('Conventional Cotton Pads', 'Reusable makeup remover pads'),
            ('Plastic Wrap', 'Silicone food covers'),
            ('Disposable Period Products', 'Period cup or reusable cloth pads')
        ]

        for product, alternative in products_alternatives:
            tree.insert('', tk.END, values=(product, alternative))

        tree.place(x=0, y=100, width=770, height=530)

        # Aesthetics of how to display it
        style=ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16, "bold"), 
                        foreground="green")
        style.configure("Treeview", font=("Helvetica", 14), rowheight=38)

    # The about page on the dashbaord window.
    def display_about(self):
        """Displaying the about info of the entire program and picture."""
        self.clear_main_area()

        label=tk.Label(self.main_frame, text="Welcome to the About Page", 
                       font=("Helvetica", 16), fg="oldlace", bg="oldlace")
        label.pack(pady=20)

        # Title label
        title_label=tk.Label(self.main_frame, text="About Page", 
                             font=("Helvetica", 30), fg="black", 
                             bg="oldlace")
        title_label.place(x=235, y=5)

        # Create a Text widget to display file contents
        self.configfile=Text(self.main_frame, wrap="word", bd=0, 
                             bg="oldlace", font=("Helvetica", 13))
        self.configfile.config(state='normal') 
        self.configfile.place(x=0, y=100, width=775, height=250)

        # Add a scrollbar to the canvas
        scrollbar=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                command=self.configfile.yview)
        scrollbar.place(x=762, y=100, height=250)
        self.configfile.configure(yscrollcommand=scrollbar.set)

        # Define tags for the font color and bold text
        self.configfile.tag_configure("custom_color", foreground="black")
        self.configfile.tag_configure("bold", font=("Helvetica", 13, "bold"))

        # Open and read the file
        filename="aboutpagetext"
        try:
            with open(filename, 'r') as f:
                content=f.read()
                self.configfile.insert(INSERT, content)
                
                # Example of making specific text bold
                self.configfile.tag_add("bold", "1.0", "1.end")
                self.configfile.tag_add("bold", "5.0", "5.end")
                self.configfile.tag_add("bold", "6.0", "6.end")
                self.configfile.tag_add("bold", "10.0", "10.end")
                self.configfile.tag_add("bold", "13.0", "13.end")
                self.configfile.tag_add("bold", "14.0", "14.end")
                self.configfile.tag_add("bold", "17.0", "17.end")
                
                # Apply custom color to the entire content
                self.configfile.tag_add("custom_color", "1.0", "end")
        except FileNotFoundError:
            self.configfile.insert(INSERT, f"Error: File '{filename}' "+
                                   "not found.")
        
        self.configfile.config(state='disabled')  # Text widget read-only

        # Load and display image
        image_path="aboutus.png"
        image=Image.open(image_path)
        resize_image=image.resize((700, 300))
        img=ImageTk.PhotoImage(resize_image)

        image_label=tk.Label(self.main_frame, image=img)
        image_label.image=img  
        image_label.place(x=30, y=370)

    # The help page on the dashboard window
    def display_help(self):
        """Displaying the help questions and answer of the program and 
        picture.
        """
        self.clear_main_area()

        # Title label
        title_label=tk.Label(self.main_frame, text="Help Page", 
                             font=("Helvetica", 30), fg="black", 
                             bg="oldlace")
        title_label.place(x=255, y=5)

        # Create a Text widget to display file contents
        self.configfile=Text(self.main_frame, wrap="word", bd=0, 
                             bg="oldlace", font=("Helvetica", 13))
        self.configfile.config(state='normal')  
        self.configfile.place(x=0, y=100, width=775, height=250)

        # Add a scrollbar to the canvas
        scrollbar=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                command=self.configfile.yview)
        scrollbar.place(x=762, y=100, height=250)
        self.configfile.configure(yscrollcommand=scrollbar.set)

        # Define tags for the font color and bold text
        self.configfile.tag_configure("custom_color", foreground="black")
        self.configfile.tag_configure("bold", font=("Helvetica", 13, "bold"))

        # Open and read the file
        filename="helppagetext"
        try:
            with open(filename, 'r') as f:
                content=f.read()
                self.configfile.insert(INSERT, content)
                
                # Making specific text bold
                self.configfile.tag_add("bold", "1.0", "1.end")
                self.configfile.tag_add("bold", "2.0", "2.9")
                self.configfile.tag_add("bold", "3.0", "3.7")
                self.configfile.tag_add("bold", "5.0", "5.9")
                self.configfile.tag_add("bold", "6.0", "6.7")
                self.configfile.tag_add("bold", "8.0", "8.9")
                self.configfile.tag_add("bold", "9.0", "9.9")
                self.configfile.tag_add("bold", "10.0", "10.7")
                self.configfile.tag_add("bold", "11.0", "11.9")
                self.configfile.tag_add("bold", "12.0", "12.9")
                self.configfile.tag_add("bold", "13.0", "13.7")
                self.configfile.tag_add("bold", "15.0", "15.end")
                self.configfile.tag_add("bold", "16.0", "16.end")
                self.configfile.tag_add("bold", "17.0", "17.9")
                self.configfile.tag_add("bold", "18.0", "18.7")
                self.configfile.tag_add("bold", "21.0", "21.9")
                self.configfile.tag_add("bold", "22.0", "22.7")
                self.configfile.tag_add("bold", "24.0", "24.9")
                self.configfile.tag_add("bold", "25.0", "25.7")
                self.configfile.tag_add("bold", "27.0", "27.9")
                self.configfile.tag_add("bold", "28.0", "28.7")
                self.configfile.tag_add("bold", "30.0", "30.9")
                self.configfile.tag_add("bold", "31.0", "31.9")
                self.configfile.tag_add("bold", "32.0", "32.7")
                self.configfile.tag_add("bold", "35.0", "35.9")
                self.configfile.tag_add("bold", "36.0", "36.7")

                # Apply custom color to the entire content
                self.configfile.tag_add("custom_color", "1.0", "end")
        except FileNotFoundError:
            self.configfile.insert(INSERT, f"Error: File '{filename}' "+
                                   "not found.")
        
        self.configfile.config(state='disabled')  # text widget read-only

        # Load and display image
        image_path="helppagepic.jpg"
        image=Image.open(image_path)
        resize_image=image.resize((700, 300))
        img=ImageTk.PhotoImage(resize_image)

        image_label=tk.Label(self.main_frame, image=img)
        image_label.image=img 
        image_label.place(x=30, y=370)

    # Displaying the user profile 
    def display_profile(self):
        """Showing the user profile and quiz results. Everything in the 
        user file. Different for every user for privacy reasons. 
        """
        self.clear_main_area()
        if 'first_name' in self.user_info:
            profile_frame=tk.Frame(self.main_frame, bg="oldlace")
            profile_frame.place(x=240, y=45)  

            title_label=tk.Label(profile_frame, text="Profile Information", 
                                 font=("Helvetica", 20, "bold"), 
                                 bg="oldlace", fg="black")
            title_label.grid(row=0, column=0, columnspan=2, pady=(5, 20))

            info_label=tk.Label(self.main_frame, text="Your profile details"+
                                " and all your quiz results.", 
                                font=("Helvetica", 15), fg="green", 
                                bg="oldlace")
            info_label.place(x=155, y=10)

            labels=["First Name:", "Username:", 
                      "Date of Birth:", "Password:"]
            values=[self.user_info['first_name'], self.user_info['username'], 
                    self.user_info['date_of_birth'], 
                    self.user_info['password']]

            for i, (label_text, value_text) in enumerate(zip(labels, values)):
                label=tk.Label(profile_frame, text=label_text, 
                               font=("Helvetica", 15, "bold"), bg="oldlace", 
                               fg="black", anchor="w")
                label.grid(row=i+1, column=0, sticky="w", padx=(0, 20), pady=5)
                value=tk.Label(profile_frame, text=value_text, 
                               font=("Helvetica", 15), bg="oldlace", 
                               fg="black", anchor="w")
                value.grid(row=i+1, column=1, sticky="w", pady=5)
        else:
            label=tk.Label(self.main_frame, text="Profile information not"+
                           " available", font=("Helvetica", 16), fg="black", 
                           bg="oldlace")
            label.place(x=250, y=60)  

        # Label saying 'quiz results:'
        quiz_label=tk.Label(self.main_frame, text="Quiz Results:", 
                            font=("Helvetica", 18, "bold"), fg="black", 
                            bg="oldlace")
        quiz_label.place(x=275, y=280)

        # Create a Text widget to display file contents
        text_widget=tk.Text(self.main_frame, wrap="word", 
                            font=("Helvetica", 13, "bold"), bg="oldlace", 
                            bd=0, fg="black", width=60, height=17)
        text_widget.place(x=140, y=320, width=485, height=280)

        # Add the code to show the file content below the profile information
        file_path=f"{self.user_info['username']}.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines=file.readlines()
                if len(lines)>5:
                    content=''.join(lines[5:])  # Skip the first 5 lines
                    text_widget.insert(tk.END, content)
                    text_widget.tag_configure('bold', 
                                              font=("Helvetica", 13, "bold"))

                    # Apply the bold tag to "Quiz scores:"
                    start_idx=1.0
                    while True:
                        start_idx=text_widget.search("Quiz scores:", 
                                                       start_idx, tk.END)
                        if not start_idx:
                            break
                        end_idx=f"{start_idx}+{len('Quiz scores:')}c"
                        text_widget.tag_add('bold', start_idx, end_idx)
                        start_idx=end_idx
                else:
                    text_widget.insert(tk.END, "You have not completed any"+
                                       " quizzes.")
        else:
            no_file_label=tk.Label(self.main_frame, text="File not found", 
                                   font=("Helvetica", 16), fg="black", 
                                   bg="oldlace")
            no_file_label.place(x=250, y=250)  

        text_widget.config(state=tk.DISABLED)

        # Add scrollbar
        scrollbar1=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                 command=text_widget.yview)
        scrollbar1.place(x=615, y=320, height=280)
        text_widget.configure(yscrollcommand=scrollbar1.set)

    # Code to open the quiz (the user chooses shuffled or normal order)
    def step1_open_quiz_window(self):
        """Asks the user which kind of quiz they want, random or normal and
        will open whichever one they choose (the different classes).
        """
        popup_q1=tk.Toplevel()
        popup_q1.title("QUIZ")
        popup_q1.resizable(False, False)

        # Calculate center position
        window_w=1050  # Window width  
        window_h=650   # Window height
        screen_width=popup_q1.winfo_screenwidth()
        screen_height=popup_q1.winfo_screenheight()

        x_position=(screen_width-window_w)//2
        y_position=(screen_height-window_h)//4

        # Set window geometry
        popup_q1.geometry(f"{window_w}x{window_h}+{x_position}+{y_position}")

        result=mb.askquestion("Option", "Do you want a randomised "+
                              "order of the questions, or the "+
                              "original order?\n(Yes for "+
                              "randomised, No for original)", 
                              parent=self.dashboard_window)

        # Opens based on user repsonse from the question messagebox 
        if result=='yes':
            popup_q1.attributes('-topmost', True)  # keep window on top
            RandomQuiz(popup_q1, self.user_info)
        else:
            popup_q1.attributes('-topmost', True)  # keep window on top
            Quiz(popup_q1, self.user_info)

# To run the entire program (from beginning)
root=tk.Tk()
app=MainWindow(root)
root.mainloop()