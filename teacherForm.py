from tkinter import *
from tkinter import ttk
 
def mainTeacherForm():
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

    saveBtn = ttk.Button(root, text="save")
    saveBtn.place(height=50, width=150, x=600, y=20)
    editBtn = ttk.Button(root, text="edit")
    editBtn.place(height=50, width=150, x=600, y=75)
    deleteBtn = ttk.Button(root, text="delete")
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

    root.mainloop()
if __name__== "__main__":
    mainTeacherForm()

