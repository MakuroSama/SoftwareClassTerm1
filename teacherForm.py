from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
def conDb():
    global cs, con
    con = mysql.connector.connect(host="localhost",user="root",password="",database="register") 
    cs = con.cursor()
    
 
def mainTeacherForm():
    def clearForm():
        entryTeacherID.delete(0,END)
        entryTeacherName.delete(0,END)
        entryTeacherLastname.delete(0,END)
        entryTeacherMajor.delete(0,END)
        entryTeacherEmail.delete(0,END)
        entryTeacherTel.delete(0,END)
    def insertData():
        if entryTeacherID.get() == "" or entryTeacherName.get() == "" or entryTeacherLastname.get() == "" or entryTeacherMajor.get() == "" or entryTeacherEmail.get() == "" or entryTeacherTel.get() == "":
            messagebox.showwarning("warning", "please enter all info")
        else:
            conDb()
            cs = con.cursor()
            sql = "INSERT INTO tb_teacher(id_teacher,f_name,l_name,major,email,tel) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (
                str (entryTeacherID.get()),
                str(entryTeacherName.get()),
                str(entryTeacherLastname.get()),
                str(entryTeacherMajor.get()),
                str(entryTeacherEmail.get()),
                str(entryTeacherTel.get())             
            )
        cs.execute(sql,val)
        con.commit()
        con.close()
        cs.close()
        clearForm()
        messagebox.showwarning("warning", "data saved successfully")
    def selectTreeView(event):

        clearFrom()
        item = view.selection()
        for i in item:
            entryTeacherID.insert("",view.item(i, "values")[0])
            entryTeacherName.insert("",view.item(i, "values")[1])
            entryTeacherLastname.insert("",view.item(i, "values")[2])
            entryTeacherMajor.insert("",view.item(i, "values")[3])
            entryTeacherEmail.insert("",view.item(i, "values")[4])
            entryTeacherTel.insert("",view.item(i, "values")[5])
    def updateData():
        if not view.selection():
            messagebox.showinfo("warning", "คุณยังไม่ได้เลือกข้อมูล")
        else:
            conDb()
            cs.execute("UPDATE tb_teacher set id_teacher = %s, f_name = %s, l_name, major = %s, email = %s, tel = %s", (str(entryTeacherID.get()), str(entryTeacherName.get()), str(entryTeacherLastname.get()), str(entryTeacherMajor.get()), str(entryTeacherEmail.get()), str(entryTeacherTel.get())))

            msgBox = messagebox.askquestion("Information", "ต้องการเเก้ไขข้อมูลมั้ย")
            if msgBox == "yes":
                con.commit()
        con.close()
        cs.close()
        clearForm()
        insertDataTreeview()

    def deleteData():
        if not view.selection():
            messagebox.showinfo("Information", "You haven't selected the entry to delete")
        else:
            item = view.selection()
            for i in item:
                conDb()
                cs.execute("DELETE FROM tb_teacher WHERE id_teacher = %s" % view.item(i,"values")[0]) 
                messageBox = messagebox.askquestion("warning", "Do you want to delete this entry?")

                if messageBox == "yes":
                    con.commit()
            con.close()
            cs.close()
            clearForm()
            insertDataTreeview()
            messagebox.showwarning("warning", "Saved successfully")
    def insertDataTreeview():
        for c in view.get_children():   
            view.delete(c)
        conDb()
        cs.execute("SELECT * FROM tb_teacher")
        data = cs.fetchall()
        for d in data:
            view.insert("", "END", values=d)
        con.close()
        cs.close()
    root = Tk()
    root.title("TeacherRegisteration")
    root.geometry("900x620")

    lblFrame = ttk.LabelFrame(root, text="add/edit personal info", labelanchor="nw")
    lblFrame.place(height=300, width=500, x=10, y=10)

    lblTeacherID =  ttk.Label(lblFrame, text="TeacherID", font=16)
    lblTeacherID.place(height=20, width=80, x=20, y=20)
    
    lblTeacherName =  ttk.Label(lblFrame, text="Name", font=16)
    lblTeacherName.place(height=20, width=80, x=20, y=75)

    lblTeacherSurname =  ttk.Label(lblFrame, text="Surname", font=16)
    lblTeacherSurname.place(height=20, width=80, x=20, y=110)

    lblTeacherMajor =  ttk.Label(lblFrame, text="Major", font=16)
    lblTeacherMajor.place(height=20, width=80, x=20, y=150)

    lblTeacherEmail =  ttk.Label(lblFrame, text="Email", font=16)
    lblTeacherEmail.place(height=20, width=80, x=20, y=190)

    lblTeacherTel =  ttk.Label(lblFrame, text="Tel", font=16)
    lblTeacherTel.place(height=20, width=80, x=20, y=230)

    entryTeacherID = ttk.Entry(lblFrame,)
    entryTeacherID.place(height=30, width=180, x=120, y=20)
    entryTeacherName = ttk.Entry(lblFrame,)
    entryTeacherName.place(height=30, width=180, x=120, y=75)
    entryTeacherLastname = ttk.Entry(lblFrame,)
    entryTeacherLastname.place(height=30, width=180, x=120, y=110)
    entryTeacherMajor = ttk.Entry(lblFrame,)
    entryTeacherMajor.place(height=30, width=180, x=120, y=150)
    entryTeacherEmail = ttk.Entry(lblFrame,)
    entryTeacherEmail.place(height=30, width=180, x=120, y=190)
    entryTeacherTel = ttk.Entry(lblFrame,)
    entryTeacherTel.place(height=30, width=180, x=120, y=230)

    saveBtn = ttk.Button(root, text="save",command=insertData)
    saveBtn.place(height=50, width=150, x=600, y=20)
    editBtn = ttk.Button(root, text="edit", command=updateData)
    editBtn.place(height=50, width=150, x=600, y=75)
    deleteBtn = ttk.Button(root, text="delete",command=deleteData)
    deleteBtn.place(height=50, width=150, x=600, y=130)
    cancelBtn = ttk.Button(root, text="cancel")
    cancelBtn.place(height=50, width=150, x=600, y=185)
    exitBtn = ttk.Button(root, text="exit", command=exit)
    exitBtn.place(height=50, width=150, x=600, y=240)

    view = ttk.Treeview(root,columns=("ID", "Name", "Lastname", "Major", "Email", "Tel"), show="headings")
    view.place(height=250, width=820, x=20, y=350)

    scrollBar = ttk.Scrollbar(root, orient="vertical")
    scrollBar.place(height=248, x=822, y=352)

    view.config(yscrollcommand=scrollBar.set)
    view.column("#1", width="80")
    view.column("#2", width="100")
    view.column("#3", width="100")
    view.column("#4", width="120")
    view.column("#5", width="120")
    view.column("#6", width="80")

    view.heading("#1", text="ID")
    view.heading("#2", text="Name")
    view.heading("#3", text="Surname")
    view.heading("#4", text="Major")
    view.heading("#5", text="Email")
    view.heading("#6", text="Tel")
    view.bind('<ButtonRelease>', selectTreeView)
    insertDataTreeview()
    root.mainloop()
if __name__== "__main__":
        mainTeacherForm()

