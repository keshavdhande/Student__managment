from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
 # pip install pillow for show images
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os

class Student:
    def __init__(self, root):
        self.root = root
        # this are geometry screen size points
        self.root.geometry('1530x790+0+0')
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.wm_iconbitmap("icon.ico")
        # variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # code for show first image
        img = Image.open("college_images/11th.jpg")  # for store image
        img = img.resize((540, 160), Image.ANTIALIAS)  # adjust size of images
        self.photoimg = ImageTk.PhotoImage(img)
        self.btn_1 = Button(self.root, command=self.open_img,
                            image=self.photoimg, cursor="hand2")
        # this show image to window
        self.btn_1.place(x=0, y=0, width=540, height=160)
        # code for show second image

        img_2 = Image.open("college_images/pic5.jpg")  # for store image
        # adjust size of images
        img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_2)
        self.btn_2 = Button(self.root, command=self.open_img_2,
                            image=self.photoimg_1, cursor="hand2")
        # this show image to window
        self.btn_2.place(x=540, y=0, width=540, height=160)
        # code for show third image

        img_3 = Image.open("college_images/3rd.jpg")  # for store image
        # adjust size of images
        img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        self.btn_3 = Button(self.root, command=self.open_img_3,
                            image=self.photoimg_3, cursor="hand2")
        # this show image to window
        self.btn_3.place(x=1000, y=0, width=540, height=160)

       # code for show background image
        img_4 = Image.open("college_images/university.jpg")  # for store image
        # adjust size of images
        img_4 = img_4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2,
                       relief=RIDGE)  # bd stands for border
        # it will show background image
        bg_lbl.place(x=0, y=160, width=1530, height=710)
        #this is title

        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "Sans Serif", 34), fg="blue", bg="white")
        lbl_title.place(x=0, y=0, width=1530, height=45)
        exit_button = Button(text="Exit", command=root.quit, height=2, width=12, fg="red", font=(
            "", 9, 'bold'), bg='white', bd=1, relief=SOLID,)
        exit_button.place(y=164, x=1230)
        # its like an frame above background imag e
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white",)
        Manage_frame.place(x=15, y=55, height=580, width=1329)

        # left frame
        # fg means font color  #you used manage here because we want to show our left frame onto the out manage frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=(
            "times new roman", 12, "bold"), fg="red", bg="white")
        DataLeftFrame.place(x=15, y=10, width=620, height=540)

        # current course labelframe
        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=1, relief=SOLID, padx=2, text="Current Course Information", font=(
            "times new roman", 12, "bold"), fg="green", bg="white")  # fg means font color  #you used manage here because we want to show our left frame onto the out manage frame
        std_lbl_info_frame.place(x=0, y=11, width=600, height=115)

        # Department
        lbl_dep = Label(std_lbl_info_frame, text="Department:", font=(
            "arial", 12, "bold"), bg="white")  # this is a label for department
        # sticky west for put it on west site
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=(
            "arial", 12, "bold"), width=17, state="readonly")
        combo_dep["value"] = ("Select Department", "Computer", "IT", "Civil")
        # this will show by default value at 0 index i.e select department
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10,
                       sticky=W)  # padx stands for padding
        # course
        course_std = Label(std_lbl_info_frame, text="Courses:", font=(
            "arial", 12, "bold"), bg="white")  # this is a label for department
        # sticky west for put it on west site
        course_std.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course, font=(
            "arial", 12, "bold"), width=17, state="readonly")
        com_txtcourse_std["value"] = (
            "Select Course", "BCS", "BCA", "MCA", "MCS")
        # this will show by default value at 0 index i.e select department
        com_txtcourse_std.current(0)
        # padx stands for padding
        com_txtcourse_std.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year

        currunt_year = Label(std_lbl_info_frame, font=(
            "arial", 12, "bold"), text="Year:", bg="white")
        currunt_year.grid(row=1, column=0, sticky=W, padx=2, pady=10)
        cpm_txt_current_year = ttk.Combobox(
            std_lbl_info_frame, state="readonly", textvariable=self.var_year, font=("arial", 12, "bold"), width=17)
        cpm_txt_current_year['value'] = (
            "Select year", "2020-2021", "2021-2022", "2022-2023")
        cpm_txt_current_year.current(0)
        cpm_txt_current_year.grid(row=1, column=1, sticky=W, padx=2)

        # semester
        label_Semester = Label(std_lbl_info_frame, font=(
            "arial", 12, "bold"), text="Semester:", bg="white")
        label_Semester.grid(row=1, column=2, sticky=W, padx=2, pady=10)
        com_semester = ttk.Combobox(std_lbl_info_frame, state="readonly",
                                    textvariable=self.var_semester, font=("arial", 12, "bold"), width=17)

        com_semester['value'] = (
            "Select Semester", "sem1", "sem2", "sem3", "sem4", 'sem5', "sem6")
        com_semester.current(0)
        com_semester.grid(row=1, column=3, sticky=W, padx=2, pady=10)

        # student class frame
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=0.5, relief=SOLID, padx=5, text="Student Class  Information", font=(
            "times new roman", 12, "bold"), fg="green", bg="white")  # fg means font color  #you used manage here because we want to show our left frame onto the out manage frame
        std_lbl_class_frame.place(x=0, y=150, width=600, height=230)
        # id
        label_id = Label(std_lbl_class_frame, font=(
            "arial", 12, "bold"), text="Student Id:", bg="white")
        label_id.grid(row=0, column=0, sticky=W, padx=2, pady=7)
        id_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_id, font=(
            "arial", 12, "bold"), width=20)
        id_entry.grid(row=0, column=1, sticky=W, padx=2, pady=7)
        # name
        lbl_name = Label(std_lbl_class_frame, font=(
            "arial", 12, "bold"), text="Full Name:", bg="white")
        lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=7)
        txt_name = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_name, font=(
            "arial", 11, "bold"), width=20)
        txt_name.grid(row=0, column=3, sticky=W, padx=2, pady=7)
        # division
        lbl_div = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Class Division:", bg="white")
        lbl_div.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        com_txt_div = ttk.Combobox(std_lbl_class_frame, state="readonly",
                                   textvariable=self.var_div, font=("arial", 12, "bold"), width=18)
        com_txt_div['value'] = ("Select Division", "A", "B", "C", "D")
        com_txt_div.current(0)
        com_txt_div.grid(row=1, column=1, sticky=W, padx=2, pady=7)
        # Roll
        lbl_roll = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Roll No:", bg="white")
        lbl_roll.grid(row=1, column=2, sticky=W, padx=2, pady=7)
        txt_roll = ttk.Entry(std_lbl_class_frame, textvariable=self.var_roll, font=(
            "arial", 11, "bold"), width=20)
        txt_roll.grid(row=1, column=3, sticky=W, padx=2, pady=7)
        # gender
        lbl_gender = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Gender:", bg="white")
        lbl_gender.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        com_txt_gender = ttk.Combobox(std_lbl_class_frame, state="readonly",
                                      textvariable=self.var_gender, font=("arial", 12, "bold"), width=18)
        com_txt_gender['value'] = ("Select", "Male", "Female", "other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # dob
        lbl_dob = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="DOB:", bg="white")
        lbl_dob.grid(row=2, column=2, sticky=W, padx=2, pady=7)
        txt_dob = ttk.Entry(std_lbl_class_frame, width=20,
                            textvariable=self.var_dob, font=("arial", 11, "bold"))
        txt_dob.grid(row=2, column=3, padx=2, pady=7)

        # Email
        lbl_email = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Email:", bg="white")
        lbl_email.grid(row=3, column=0, sticky=W, padx=2, pady=7)
        txt_email = ttk.Entry(
            std_lbl_class_frame, textvariable=self.var_email, width=22, font=("arial", 11, "bold"))
        txt_email.grid(row=3, column=1, padx=2, pady=7)

        # phone
        lbl_phone = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Phone no:", bg="white")
        lbl_phone.grid(row=3, column=2, sticky=W, padx=2, pady=7)
        txt_phone = ttk.Entry(std_lbl_class_frame, width=20,
                              textvariable=self.var_phone, font=("arial", 11, "bold"))
        txt_phone.grid(row=3, column=3, padx=2, pady=7)

        # address
        lbl_address = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        txt_address = ttk.Entry(
            std_lbl_class_frame, textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=4, column=1, padx=2, pady=7)

        # teacher
        lbl_teacher = Label(std_lbl_class_frame, font=(
            "arial", 11, "bold"), text="Teacher:", bg="white")
        lbl_teacher.grid(row=4, column=2, sticky=W, padx=2, pady=7)
        txt_teacher = ttk.Entry(std_lbl_class_frame, width=20,
                                textvariable=self.var_teacher, font=("arial", 11, "bold"))
        txt_teacher.grid(row=4, column=3, padx=2, pady=7)

  # frames for button
        btn_frame = Frame(DataLeftFrame, bd=1, relief=SOLID, bg="white")
        btn_frame.place(x=0, y=400, height=38, width=650)

        btn_Add = Button(btn_frame, text="save", command=self.add_data, font=(
            "arial", 11, "bold"), width=16, bg="blue", fg="white")
        btn_Add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", command=self.update_data, font=(
            "arial", 11, "bold"), width=16, bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", command=self.delete_data, font=(
            "arial", 11, "bold"), width=16, bg="blue", fg="white")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset_data, font=(
            "arial", 11, "bold"), width=16, bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=1)

        # Right  frame
        # fg means font color  #you used manage here because we want to show our left frame onto the out manage frame
        DatarightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Details", font=(
            "times new roman", 12, "bold"), fg="red", bg="white")
        DatarightFrame.place(x=640, y=10, width=670, height=540)

        # fg means font color  #you used manage here because we want to show our left frame onto the out manage frame
        search_Frame = LabelFrame(DatarightFrame, bd=4, relief=RIDGE, padx=2, text="View Student & Search System", font=(
            "times", 12, "bold"), fg="black", bg="white")
        search_Frame.place(x=0, y=10, width=655, height=65)

        searcg_by = Label(search_Frame, font=("arial", 11, "bold"),
                          text="Search By:", bg="wheat", fg="red")
        searcg_by.grid(row=0, column=0, sticky=W, padx=5, pady=7)

        # search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(
            search_Frame, state="readonly", textvariable=self.var_com_search, font=("arial", 12, "bold"), width=13)
        com_txt_search['value'] = (
            "Select Option", "Roll", "Phone", "stundnt_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=3, pady=7)

        self.var_search = StringVar()

        txt_search = ttk.Entry(
            search_Frame, width=22, textvariable=self.var_search, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_Frame, text="Search", command=self.search_data, font=(
            "arial", 11, "bold"), width=10, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=3)

        btn_showAll = Button(search_Frame, text="Show All", command=self.fetch_data, font=(
            "arial", 11, "bold"), width=10, bg="blue", fg="white")
        btn_showAll.grid(row=0, column=4, padx=3)

        # student table and scroll bar
        # table frame
        tabel_frame = Frame(DatarightFrame, bd=4, relief=RIDGE)
        tabel_frame.place(x=0, y=90, width=655, height=350)

        # score bar
        scroll_x = ttk.Scrollbar(tabel_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame, orient=VERTICAL)

        # for heading
        self.student_table = ttk.Treeview(tabel_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll",
                                          "gender", "dob", "email", "phone", "address", "teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading('course', text="Course")
        self.student_table.heading('year', text="Year")
        self.student_table.heading('sem', text="Semester")
        self.student_table.heading('id', text="Student Id")
        self.student_table.heading('name', text="Student Name")
        self.student_table.heading('div', text="Class div")
        self.student_table.heading('roll', text="Roll no")
        self.student_table.heading('gender', text="Gender")
        self.student_table.heading('dob', text="DOB")
        self.student_table.heading('email', text="Email")
        self.student_table.heading('phone', text="Phone No")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('teacher', text="Teacher Name")

        self.student_table["show"] = "headings"

        self.student_table.column('dep', width=170)
        self.student_table.column('course', width=170)
        self.student_table.column('year', width=170)
        self.student_table.column('sem', width=170)
        self.student_table.column('id', width=170)
        self.student_table.column('name', width=170)
        self.student_table.column('div', width=170)
        self.student_table.column('roll', width=170)
        self.student_table.column('gender', width=170)
        self.student_table.column('dob', width=170)
        self.student_table.column('email', width=170)
        self.student_table.column('phone', width=170)
        self.student_table.column('address', width=170)
        self.student_table.column('teacher', width=170)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All Field Are required")
        else:
            try:
                # this is for connectio of mysql database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="studentdata")
                my_cursur = conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_std_id.get(),
                                   self.var_std_name.get(),
                                   self.var_div.get(),
                                   self.var_roll.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Sucess", "Student has been Added ! ", parent=self.root)

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Due to {str(es)}", parent=self.root)


# fetch function


    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="studentdata")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from student")
        data = my_cursur.fetchall()
        if(len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

    # functin for update data

    def update_data(self):
        if (self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == ""):

            messagebox.showerror("Error", "All Field Are required")
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Are you sure update this student data", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="root", database="studentdata")
                    my_cursur = conn.cursor()
                    my_cursur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s  where stundnt_id=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not update:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Sucess", "Student Successfully updated", parent=self.root)

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Due to {str(es)}", parent=self.root)

    # delete data
    def delete_data(self):
        if (self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror(
                "Error", "All Field Are required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    'Delete', "Are you sure to delete this Student")
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="root", database="studentdata")
                    my_cursur = conn.cursor()
                    sql = "delete from student where stundnt_id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursur.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Your Student has been Deleted", parent=self.root)

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Due to {str(es)}", parent=self.root)
    # reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

# for search data
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "please select option")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="studentdata")
                my_cursur = conn.cursor()
                my_cursur.execute("select * from student where " + str(
                    self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = my_cursur.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "Error", f"Due to {str(es)}", parent=self.root)
# open img

    def open_img(self):
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="open Images", filetypes=(
            ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")))
        img = Image.open(fln)
        # adjust size of images
        img_browse = img.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_br = ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_br)

    def open_img_2(self):
        fln3 = filedialog.askopenfilename(initialdir=os.getcwd(), title="open Images", filetypes=(
            ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")))
        img3 = Image.open(fln3)
        # adjust size of images
        img_browse = img3.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_br3 = ImageTk.PhotoImage(img_browse)
        self.btn_2.config(image=self.photoimg_br3)

    def open_img_3(self):
        fln2 = filedialog.askopenfilename(initialdir=os.getcwd(), title="open Images", filetypes=(
            ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")))
        img_2 = Image.open(fln2)
        img_browse_2 = img_2.resize(
            (540, 160), Image.ANTIALIAS)  # adjust size of images
        self.photoimg_br2 = ImageTk.PhotoImage(img_browse_2)
        self.btn_3.config(image=self.photoimg_br2)


class Login(Student):
    def __init__(self, root):
        self.root = root
        # this are geometry screen size points
        self.root.geometry('1530x790+0+0')
        self.root.title("login")
        self.root.wm_iconbitmap("icon.ico")


        img = Image.open("college_images/pic1.jpg")  # for store image
        img = img.resize((510, 160), Image.ANTIALIAS)  # adjust size of images
        self.photoimg = ImageTk.PhotoImage(img)
        self.btn_1 = Button(self.root, command=self.open_img,
                            image=self.photoimg, cursor="hand2")
        # this show image to window
        self.btn_1.place(x=0, y=0, width=540, height=160)
        # code for show second image

        img_2 = Image.open("college_images/pic9.jpg")  # for store image
        # adjust size of images
        img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_2)
        self.btn_2 = Button(self.root, command=self.open_img_2,
                            image=self.photoimg_1, cursor="hand2")
        # this show image to window
        self.btn_2.place(x=540, y=0, width=540, height=160)
        # code for show third image

        img_3 = Image.open("college_images/pic3.jpg")  # for store image
        # adjust size of images
        img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        self.btn_3 = Button(self.root, command=self.open_img_3,
                            image=self.photoimg_3, cursor="hand2")
        # this show image to window
        self.btn_3.place(x=1000, y=0, width=540, height=160)

       # code for show background image
        img_4 = Image.open("college_images/uni2.jpg")  # for store image
        # adjust size of images
        img_4 = img_4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2,
                       relief=RIDGE)  # bd stands for border
        # it will show background image
        bg_lbl.place(x=0, y=160, width=1530, height=710)
        #this is title

        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "Sans Serif", 34), fg="blue", bg="white")
        lbl_title.place(x=0, y=0, width=1530, height=45)
        exit_button = Button(text="Exit", command=root.quit, height=2, width=12, fg="red", font=(
            "", 9, 'bold'), bg='white', bd=1, relief=SOLID,)
        exit_button.place(y=164, x=1230)

        self.var_std_id= StringVar()
        label_id = Label(bg_lbl, font=(
            "arial", 12, "bold"), text="User Name:", bg="white")

        label_id.place(x=400,y=80)
        id_entry = ttk.Entry(bg_lbl, textvariable=self.var_std_id, font=(
            "arial", 12, "bold"), width=20)
        id_entry.place(x=500,y=80)
        # password
        self.var_std_name=StringVar()

        lbl_name = Label(bg_lbl, font=(
            "arial", 12, "bold"), text="Password:", bg="white")
        lbl_name.place(x=700,y=80)
        txt_name = ttk.Entry(bg_lbl, textvariable=self.var_std_name, font=(
            "arial", 11, "bold"), width=20)
        txt_name.place(x=800,y=80)

        btn_showAll = Button(bg_lbl, text="Login", comman=self.checkpass, font=(
            "arial", 11, "bold"),bd=2, width=20, bg="#a436bf", fg="#f7fdff")
        btn_showAll.place(x=600,y=130)







        

 


 
    def checkpass(self):
        while(self.var_std_id.get()!="admin" or self.var_std_name.get()!="admin"):
            messagebox.showinfo("Error","Invalid Password /Password")
            Login.__init__(self)
        else:
            messagebox.showinfo("Success","Login Successful")
            self.root.destroy()

          



if __name__ == "__main__":
    login=Tk()
    obj=Login(login)
    login.mainloop()
    root = Tk()  # its a toolkit
    obj = Student(root)  # its are onject create from class Student

    root.mainloop()  # for hold screen as getch in c and c++        *******
    exit(0)
