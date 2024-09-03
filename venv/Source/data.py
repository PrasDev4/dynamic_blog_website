from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3

root = Tk()

class home:
    def __init__(self, root):
        self.root = root
        self.root.title("College Event Blog")
        self.create_home_page()
        self.conn = sqlite3.connect('mydata.db')
        self.cursor = self.conn.cursor()
        self.create_admin_table()
        self.create_posts_table()
    def create_admin_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admins (admin_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,email TEXT UNIQUE NOT NULL)''')
        self.conn.commit() 
    def create_admin_details(self, username,email):
        self.cursor.execute("INSERT INTO admins (username, email) VALUES(?, ?)",(username, email))
        self.conn.commit()

    def create_posts_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts (post_id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)''')
        self.conn.commit()
    def submit_page(self):
        username = self.name_entry.get()
        email = self.password_entry.get()
        if self.authenticate_admin(username, email):
            self.name_label.destroy()
            self.name_entry.destroy()
            self.password_label.destroy()
            self.password_entry.destroy()
            self.submit_btn.destroy()
            self.back_btn.destroy()
            self.placement_btn = Button(root, text='Placements', font=('Courier New',15,'bold'),command=self.placement_page)
            self.placement_btn.place(x=50, y=150)
        
            self.technical_btn = Button(root, text='Technical Events', font=('Courier New',15,'bold'),command=self.technical_page)
            self.technical_btn.place(x=50, y=300)
        
            self.sports_btn = Button(root, text='Sports', font=('Courier New',15,'bold'),command=self.sports_page)
            self.sports_btn.place(x=50, y=450)
        
            self.cultural_btn = Button(root, text='Cultural', font=('Courier New',15,'bold'),command=self.cultural_page)
            self.cultural_btn.place(x=50, y=600)

            self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.create_home_page)
            self.back_btn.place(x=600, y=500)
        else:
            messagebox.showerror("Login Failed", "Invalid username or email")

    def authenticate_admin(self, username, email):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM admins WHERE username=? AND email=?', (username, email))
        admin = cursor.fetchone()
        return admin is not None

    
    def create_box(self):
        def get_input():
            user_input = entry.get("1.0",tk.END)
            self.cursor.execute("INSERT INTO posts (content) VALUES (?)", (user_input,))
            self.conn.commit()
            messagebox.showinfo('Post', 'Your post/comment is successfully saved')
            box_window.destroy()

        box_window = tk.Toplevel(self.root)
        box_window.title("Text Input")


        entry = tk.Text(box_window, height=30, width=50)
        entry.pack()

        button = tk.Button(box_window, text="Submit", command=get_input)
        button.pack()

    def display_posts(self):
        self.clear_home_page()
        self.cursor.execute('SELECT content FROM posts')
        posts = self.cursor.fetchall()
        for i, post in enumerate(posts):
            post_label = Label(self.root, text=f"Post {i + 1}: {post[0]}", font=('Courier New', 15))
            post_label.pack()

        self.back_btn = Button(self.root, text='BACK', font=('Courier New',15,'bold'), bd=4, command=self.create_home_page)
        self.back_btn.pack()

    def clear_home_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_home_page(self):
        self.bg_img = Image.open('bimg - Copy.png')
        self.bg_img = self.bg_img.resize((2000,2000))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x =0 , y = 0)

        self.home_title = Label(root, text='Welcome', font = ('Courier New', 20, 'bold'))
        self.home_title.pack(fill = 'x')

        self.home_btn = Button(root, text='Home', font=('Courier New', 15, 'bold'), command=self.home_page)
        self.home_btn.place(x=10, y=200)

        self.getintouch_btn = Button(root, text='Get in Touch', font=('Courier New', 15, 'bold'),command=self.getintouch_page)
        self.getintouch_btn.place(x=100, y=200)

        self.aboutus_btn = Button(root, text='About Us', font=('Courier New', 15, 'bold'),command=self.aboutus_page)
        self.aboutus_btn.place(x=300, y=200)

        self.admin_btn = Button(root, text='Admin', font=('Courier New', 15, 'bold'), command=self.admin_page)
        self.admin_btn.place(x=450, y=200)

        '''self.posts_btn = Button(root, text='View Posts', font=('Courier New', 15, 'bold'), command=self.display_posts)
        self.posts_btn.place(x=600, y=200)'''
   
    def getintouch_page(self):
        self.home_title.destroy()
        self.home_btn.destroy()
        self.getintouch_btn.destroy()
        self.aboutus_btn.destroy()
        self.admin_btn.destroy()

        root = self.root
        self.enter_email = Label(root, text='Student Voice', font=('Courier New', 15 ,'bold'))
        self.enter_email.pack(fill='x')
    
        self.name_label = Label(root, text="enter name", font=('Courier New', 15, 'bold'))
        self.name_label.place(x=50, y=150)
        self.name_entry = Entry(root, font=('Courier New', 15,'bold'))
        self.name_entry.place(x=250 , y=150)

        self.email_label = Label(root, text="enter email", font=('Courier New',15 ,'bold'))
        self.email_label.place(x=50, y=300)
        self.email_entry = Entry(root, font=('Courier New',15 ,'bold'))
        self.email_entry.place(x=250,y=300)

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.create_home_page)
        self.back_btn.place(x=600, y=500)

        self.post_comment_btn = Button(root, text='POST/COMMENT', font=('Courier New',15,'bold'), bd=4,command=self.validate_input)
        self.post_comment_btn.place(x=50, y=450)

    def validate_input(self):
        username = self.name_entry.get()
        email = self.email_entry.get()

        if username.strip() == "":
            messagebox.showerror("Validation Error", "Username cannot be empty.")
        elif "@gmail.com" not in email:
            messagebox.showerror("Validation Error", "Email must be a valid Gmail address.")
        else:
            self.get_in_touch_up()

    
    def get_in_touch_up(self):
        self.back_btn.destroy()
        self.post_comment_btn.destroy()
        self.name_entry.destroy()
        self.name_label.destroy()
        self.email_entry.destroy()
        self.email_label.destroy()
        
        self.placement_btn = Button(root, text='Placements', font=('Courier New',15,'bold'),command=self.create_box)
        self.placement_btn.place(x=50, y=150)
        
        self.technical_btn = Button(root, text='Technical Events', font=('Courier New',15,'bold'),command=self.create_box)
        self.technical_btn.place(x=50, y=300)
        
        self.sports_btn = Button(root, text='Sports', font=('Courier New',15,'bold'),command=self.create_box)
        self.sports_btn.place(x=50, y=450)
        
        self.cultural_btn = Button(root, text='Cultural', font=('Courier New',15,'bold'),command=self.create_box)
        self.cultural_btn.place(x=50, y=600)

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.create_home_page)
        self.back_btn.place(x=600, y=500)

 
    def home_page(self):

        self.home_title.destroy()
        self.home_btn.destroy()
        self.getintouch_btn.destroy()
        self.aboutus_btn.destroy()
        self.admin_btn.destroy()

        
        self.placement_btn = Button(root, text='Placements', font=('Courier New',15,'bold'),command=self.display_posts)
        self.placement_btn.place(x=50, y=150)
        
        self.technical_btn = Button(root, text='Technical Events', font=('Courier New',15,'bold'),command=self.display_posts)
        self.technical_btn.place(x=50, y=300)
        
        self.sports_btn = Button(root, text='Sports', font=('Courier New',15,'bold'),command=self.display_posts)
        self.sports_btn.place(x=50, y=450)
        
        self.cultural_btn = Button(root, text='Cultural', font=('Courier New',15,'bold'),command=self.display_posts)
        self.cultural_btn.place(x=50, y=600)

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.create_home_page)
        self.back_btn.place(x=600, y=500)
    #home page display buttons
    def placement_homepage(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
        
    def technical_homepage(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
        
    def sports_homepage(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
       
    def cultural_homepage(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
    
    #admin page buttons
    def placement_page(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
        self.create_box()
    def technical_page(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
        self.create_box()
    def sports_page(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
        self.create_box()
    def cultural_page(self):

        self.placement_btn.destroy()
        self.technical_btn.destroy()
        self.sports_btn.destroy()
        self.cultural_btn.destroy()

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.home_page)
        self.back_btn.place(x=600, y=500)
        self.create_box()
    
    def admin_page(self):
        
        self.home_title.destroy()
        self.home_btn.destroy()
        self.getintouch_btn.destroy()
        self.aboutus_btn.destroy()
        self.admin_btn.destroy()

        root = self.root
        self.enter_name = Label(root, text='Admin Login', font=('Courier New', 15 ,'bold'))
        self.enter_name.pack(fill='x')
        
        self.name_label = Label(root, text="enter name", font=('Courier New', 15, 'bold'))
        self.name_label.place(x=50, y=150)
        self.name_entry = Entry(root, font=('Courier New', 15,'bold'))
        self.name_entry.place(x=250 , y=150)

        self.password_label = Label(root, text="enter email", font=('Courier New',15 ,'bold'))
        self.password_label.place(x=50, y=300)
        self.password_entry = Entry(root, font=('Courier New',15 ,'bold'))
        self.password_entry.place(x=250, y=300)

        self.submit_btn = Button(root, text='SUBMIT', font=('Courier New',15,'bold'), bd=4,command=self.submit_page)
        self.submit_btn.place(x=500, y=500)

        self.back_btn = Button(root, text='BACK', font=('Courier New',15,'bold'), bd=4,command=self.create_home_page)
        self.back_btn.place(x=600, y=500)


    def aboutus_page(self):      
        self.clear_home_page()

        about_text = """Welcome to our College Event Blog!

        We are dedicated to providing you with the latest updates and information about various events happening at our college. Whether it's about placements, technical events, sports, or cultural activities, you'll find it all here.

        Our platform also allows students to share their thoughts, opinions, and experiences through posts and comments.

        Stay tuned for exciting updates and get involved in the vibrant community of our college event enthusiasts!

        - The College Event Blog Team
        
        
        """

        wrap_length = min(self.root.winfo_width() - 1000, 600)

        about_label = Label(self.root, text=about_text, font=('Courier New', 15), wraplength=wrap_length, anchor="w", justify="left")
        about_label.pack()

        self.back_btn = Button(self.root, text='BACK', font=('Courier New', 15, 'bold'), bd=4, command=self.create_home_page)
        self.back_btn.pack()


    def login(self):
        messagebox.showinfo('post','login successful')

    def entry(self):
        messagebox.showinfo('post','your postcd/comment is succesfully saved')
    
    def _del_(self):
        self.conn.close()
home =home(root)
'''home.create_admin_details("maha","maha@gmail.com")'''
root.geometry('500x300+550+150')
root.mainloop()