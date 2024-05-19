import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
import datetime
import pandas as pd
from tkintertable import TableCanvas, TableModel

cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost;"
            "Database=library;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
root = tk.Tk()
root.title("University Library Management")
root.geometry("840x530")
root.resizable(False, False)
root.configure(bg='#2E2E2E')

bg_color = '#2E2E2E'
fg_color = '#E0E0E0'
btn_bg_color = '#4A4A4A'
btn_fg_color = '#E0E0E0'
btn_hover_color = '#616161'

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background=btn_bg_color, foreground=btn_fg_color, borderwidth=1, focusthickness=3,
                font=('Andalus', 17), focuscolor='none')
style.map('TButton', background=[('active', btn_hover_color)])

title = tk.Label(text="University Library Management System", font=('Baskerville Old Face', 25), bg=bg_color, fg=fg_color)
title.pack(pady=30)

log_entries = []


def select(column, table, cnxn):
    query = "Select " + column + " from " + table
    df = pd.read_sql(query, cnxn)
    return df


def showbooks(criteria, value, cnxn):
    sql_query = f"SELECT * FROM BOOKS WHERE {criteria} = ?"
    df = pd.read_sql(sql_query, cnxn, params=[value])
    return df


def insertStudent(FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email, cnxn):
    sql_query = """
            INSERT INTO Students (FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email)
            VALUES (?, ?, ?, ?, ?, ?)
            """
    cursor = cnxn.cursor()
    DateOfBirth = datetime.datetime.strptime(DateOfBirth, '%Y-%m-%d').date()
    cursor.execute(sql_query, (FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email))
    cnxn.commit()
    cursor.close()


def insertAdmin(SSN, FirstName, LastName, cnxn):
    sql_query = """
            INSERT INTO Admins (SSN, FirstName, LastName)
            VALUES (?, ?, ?)
            """
    cursor = cnxn.cursor()
    cursor.execute(sql_query, (SSN, FirstName, LastName))
    cnxn.commit()
    cursor.close()


def insertBorrows(TransactionID, BorrowDate, ISBN, SID, cnxn):
    sql_query = """
            INSERT INTO Borrows (TransactionID, BorrowDate, ISBN, SID)
            VALUES (?, ?, ?, ?)
            """
    cursor = cnxn.cursor()
    BorrowDate = datetime.datetime.strptime(BorrowDate, '%Y-%m-%d').date()

    isbn_query = """
                 SELECT 1
                 FROM Books
                 WHERE ISBN = ?
                 """
    cursor.execute(isbn_query, (ISBN,))
    isbn_exists = cursor.fetchone()

    sid_query = """
                SELECT 1
                FROM Students
                WHERE SID = ?
                """
    cursor.execute(sid_query, (SID,))
    sid_exists = cursor.fetchone()

    if isbn_exists and sid_exists:
        cursor.execute(sql_query, (TransactionID, BorrowDate, ISBN, SID))
        cnxn.commit()
    else:
        messagebox.showerror("Error", "ISBN or SID does not exist.")

    cursor.close()


def delete_book(isbn, cnxn):
    referenced_tables = [
        'Borrows',
        'Manages',
        'Publishes',
        'Writes'
    ]

    for table in referenced_tables:
        delete_query = f"DELETE FROM {table} WHERE ISBN = ?"
        cursor = cnxn.cursor()
        cursor.execute(delete_query, (isbn,))
        cnxn.commit()

    delete_query = "DELETE FROM Books WHERE ISBN = ?"
    cursor = cnxn.cursor()
    cursor.execute(delete_query, (isbn,))
    cnxn.commit()
    cursor.close()
    messagebox.showinfo("Info",
                        f"The book with ISBN {isbn} has been deleted from all referencing tables and the Books table.")


def join_students_books(sid_values, cnxn):
    sid_str = ", ".join(str(sid) for sid in sid_values)

    sid_query = """
                SELECT 1
                FROM Students
                WHERE SID IN ({})
                """.format(sid_str)
    cursor = cnxn.cursor()
    cursor.execute(sid_query)
    sids_exist = cursor.fetchall()

    if not sids_exist:
        print("One or more SID values do not exist.")
        return None

    query = "SELECT Students.SID, Students.FirstName, Students.LastName, Books.* " \
            "FROM Students " \
            "JOIN Borrows " \
            "ON Students.SID = Borrows.SID " \
            "JOIN Books " \
            "ON Borrows.ISBN = Books.ISBN " \
            "WHERE Students.SID IN ({})".format(sid_str)

    df = pd.read_sql(query, cnxn)

    grouped_df = df.groupby('SID')

    concatenated_df = pd.concat([group for _, group in grouped_df], ignore_index=True)

    return concatenated_df


def DeleteStud(SID, conn):
    crsr = conn.cursor()
    query = f"Delete from Borrows where SID = {SID}"
    crsr.execute(query)
    query = f"Delete from Students where SID = {SID}"
    crsr.execute(query)
    conn.commit()
    


def UpdateStud(SID, Col, Val, conn):
    if Col == 'SID':
        
        raise Exception('Cannot Edit Student\'s Id')
    crsr = conn.cursor()
    query = f"Update Students set {Col} = '{Val}' where SID = {SID}"
    crsr.execute(query)
    conn.commit()


def UpdateBook(ISBN, Col, Val, conn):
    if Col == 'ISBN':
        
        raise Exception('Cannot Edit Book\'s ISBN')
    crsr = conn.cursor()
    query = f"Update Books set {Col} = '{Val}' where ISBN = {ISBN}"
    crsr.execute(query)
    conn.commit()


def Number_of_Books_Borrowed_by_AllStuds(conn):
    crsr = conn.cursor()
    query = """
        Select Students.SID, CONCAT(Students.FirstName, ' ', Students.LastName) as FullName, count(*) as Number_of_Borrowed_Books
        from Students join Borrows on Students.SID = Borrows.SID
        group By Students.SID, Students.FirstName, Students.LastName
    """
    crsr.execute(query)
    data = crsr.fetchall()


    return data

def Number_of_Books_Borrowed_by_AStud(SID, conn):
    crsr = conn.cursor()
    query = f"""
        select Students.SID, Students.FirstName, Students.LastName, count(*) as BooksBorrowed
        from Borrows join Students on Students.SID = Borrows.SID
        GROUP by Students.SID, Students.FirstName, Students.LastName
        HAVING Students.SID = {SID}
    """
    crsr.execute(query)
    data = crsr.fetchall()

    return data[0] if data else None

def NumberOfBooksWrittenByAllAuthors(conn):
    crsr = conn.cursor()
    query = """
        Select Author.Name, count(*) as Number_of_Books
        from Author JOIN Books on Author.Name = Books.AuthorName
        group By Author.Name
    """
    crsr.execute(query)
    data = crsr.fetchall()

    return data

def BooksByAuthor(Name, conn):
    query = f"""
        SELECT Author.Name, Books.ISBN, Books.Name, Books.PublisherName, Books.Genre, Books.PublicationYear
        from Author join Books on Author.Name = Books.AuthorName
        where Author.Name = '{Name}'
    """
    crsr = conn.cursor()
    crsr.execute(query)
    data = crsr.fetchall()

    return data

def UpdateAdmin(SSN,Col,Val,conn):
    if Col == 'SSN':
      
      raise Exception('Cannot Edit Admin\'s SSN')
    crsr = conn.cursor()
    query = f"Update Admins set {Col} = '{Val}' where SSN = {SSN}"
    crsr.execute(query)
    conn.commit()


def sign_up():
    def admin_signup():
        top = tk.Toplevel(root)
        top.title("Admin Sign Up")
        top.geometry("400x300")
        top.configure(bg=bg_color)

        tk.Label(top, font=("Andalus", 16), text="SSN:", bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.1)
        ssn_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        ssn_entry.place(relx=0.5, rely=0.1)

        tk.Label(top, text="First Name: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
        first_name_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        first_name_entry.place(relx=0.5, rely=0.2)

        tk.Label(top, text="Last Name: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.3)
        last_name_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        last_name_entry.place(relx=0.5, rely=0.3)

        def addadmin():
            SSN = ssn_entry.get()
            FirstName = first_name_entry.get()
            LastName = last_name_entry.get()
            insertAdmin(SSN, FirstName, LastName, cnxn)
            log_entries.append("Admin signed up")
            messagebox.showinfo("Info", "Admin signed up!")

        tk.Button(top, text="Sign Up", font=('Andalus', 15),
                  command=addadmin, bg=btn_bg_color, width=15,
                  fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.8, anchor='center')

    def student_signup():
        top = tk.Toplevel(root)
        top.title("Student Sign Up")
        top.geometry("400x400")
        top.configure(bg=bg_color)
        tk.Label(top, text="First Name: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.1)
        first_name_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        first_name_entry.place(relx=0.5, rely=0.13)

        tk.Label(top, text="Last Name: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.2)
        last_name_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        last_name_entry.place(relx=0.5, rely=0.23)

        tk.Label(top, text="Phone Number: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.3)
        phone_number_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        phone_number_entry.place(relx=0.5, rely=0.33)

        tk.Label(top, text="Date of Birth: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.4)
        dob_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        dob_entry.place(relx=0.5, rely=0.43)

        tk.Label(top, text="Email: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.5)
        email_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        email_entry.place(relx=0.5, rely=0.53)

        tk.Label(top, text="SID: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.6)
        sid_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
        sid_entry.place(relx=0.5, rely=0.63)

        def addstudent():
            FirstName = first_name_entry.get()
            LastName = last_name_entry.get()
            PhoneNumber = phone_number_entry.get()
            DateOfBirth = dob_entry.get()
            Email = email_entry.get()
            SID = sid_entry.get()
            insertStudent(FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email, cnxn)
            log_entries.append("Student signed up")
            messagebox.showinfo("Info", "Student signed up!")

        tk.Button(top, text="Sign Up", font=('Andalus', 15),
                  command=addstudent, bg=btn_bg_color, width=15,
                  fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.9, anchor='center')

    top = tk.Toplevel(root)
    top.title("Sign Up")
    top.geometry("400x200")
    top.configure(bg=bg_color)

    tk.Button(top, text="Admin", font=('Andalus', 15),
              command=admin_signup, bg=btn_bg_color,
              fg=btn_fg_color, width=30, activebackground=btn_hover_color).place(relx=0.5, rely=0.3, anchor='center')

    tk.Button(top, text="Student", font=('Andalus', 15),
              command=student_signup, bg=btn_bg_color,
              fg=btn_fg_color, width=30, activebackground=btn_hover_color).place(relx=0.5, rely=0.6, anchor='center')


def update_user():
    def update_action():
        sid = sid_entry.get()
        column = column_entry.get()
        value = value_entry.get()
        UpdateStud(sid, column, value, cnxn)
        log_entries.append("Student updated")
        messagebox.showinfo("Info", "Student updated!")

    top = tk.Toplevel(root)
    top.title("Update Student")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="SID: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    sid_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    sid_entry.place(relx=0.5, rely=0.23)

    tk.Label(top, text="Column: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.4)
    column_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    column_entry.place(relx=0.5, rely=0.43)

    tk.Label(top, text="Value: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.6)
    value_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    value_entry.place(relx=0.5, rely=0.63)

    tk.Button(top, text="Update", font=('Andalus', 15),
              command=update_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.9, anchor='center')


def add_book():
    def add_action():
        isbn = isbn_entry.get()
        title = title_entry.get()
        author = author_entry.get()
        publisher = publisher_entry.get()
        borrowing_period = borrowing_period_entry.get()
        genre = genre_entry.get()
        year = year_entry.get()

        sql_query = """
            INSERT INTO Books (ISBN, Name, AuthorName, PublisherName, BorrowingPeriod, Genre, PublicationYear)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        cursor = cnxn.cursor()
        cursor.execute(sql_query, (isbn, title, author, publisher, borrowing_period, genre, year))
        cnxn.commit()
        cursor.close()

        log_entries.append("Book added")
        messagebox.showinfo("Info", "Book added!")

    top = tk.Toplevel(root)
    top.title("Add Book")
    top.geometry("500x500")
    top.configure(bg=bg_color)

    tk.Label(top, font=("Andalus", 16), text="ISBN:", bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.1)
    isbn_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    isbn_entry.place(relx=0.5, rely=0.1)

    tk.Label(top, text="Book Title: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    title_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    title_entry.place(relx=0.5, rely=0.2)

    tk.Label(top, text="Author: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.3)
    author_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    author_entry.place(relx=0.5, rely=0.3)

    tk.Label(top, text="Publisher: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.4)
    publisher_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    publisher_entry.place(relx=0.5, rely=0.4)

    tk.Label(top, text="Borrowing Period: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.5)
    borrowing_period_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    borrowing_period_entry.place(relx=0.5, rely=0.5)

    tk.Label(top, text="Genre: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.6)
    genre_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    genre_entry.place(relx=0.5, rely=0.6)

    tk.Label(top, text="Year: ", bg=bg_color, font=("Andalus", 16), fg=fg_color).place(relx=0.1, rely=0.7)
    year_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    year_entry.place(relx=0.5, rely=0.7)

    tk.Button(top, text="Add", font=('Andalus', 12), command=add_action,
              bg=btn_bg_color, width=6,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.9, anchor='center')


def update_book():
    def update_action():
        isbn = isbn_entry.get()
        column = column_entry.get()
        value = value_entry.get()
        UpdateBook(isbn, column, value, cnxn)
        log_entries.append("Book updated")
        messagebox.showinfo("Info", "Book updated!")

    top = tk.Toplevel(root)
    top.title("Update Book")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="ISBN: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    isbn_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    isbn_entry.place(relx=0.5, rely=0.23)

    tk.Label(top, text="Column: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.4)
    column_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    column_entry.place(relx=0.5, rely=0.43)

    tk.Label(top, text="Value: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.6)
    value_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    value_entry.place(relx=0.5, rely=0.63)

    tk.Button(top, text="Update", font=('Andalus', 15),
              command=update_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.9, anchor='center')


def show_books():
    top = tk.Toplevel(root)
    top.title("Show Books")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="Search Criteria:", font=("Andalus", 15), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    search_criteria_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    search_criteria_entry.place(relx=0.5, rely=0.21)
    tk.Label(top, text="Value:", font=("Andalus", 15), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.3)
    Value_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    Value_entry.place(relx=0.5, rely=0.31)

    def show_action():
        search_criteria = search_criteria_entry.get()
        value_entry = Value_entry.get()
        books = showbooks(search_criteria, value_entry, cnxn)

        if not books.empty:
            top = tk.Toplevel(root)
            top.title("Search")
            frame = tk.Frame(top)
            frame.pack(expand=True, fill='both')
            tk.Label(top, text="Books", font=('Andalus', 20), bg=bg_color, fg=fg_color).pack(pady=10)
            table_model = TableModel()
            table = TableCanvas(frame, model=table_model, editable=False)
            table_model.importDict(books.to_dict('index'))
            table.show()
        else:
            messagebox.showinfo("No Results", "No books found matching the search criteria.")

        log_entries.append("Searched books")

    tk.Button(top, text="Search", font=('Andalus', 15), command=show_action,
              bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.6, anchor='center')


def browse_books():
    def browse_action():
        books = select('*', 'Books', cnxn)
        top = tk.Toplevel(root)
        top.title("Browse Books")
        top.configure(bg=bg_color)

        tk.Label(top, text="Books", font=('Andalus', 20), bg=bg_color, fg=fg_color).pack(pady=10)

        frame = tk.Frame(top)
        frame.pack(expand=True, fill='both')

        table_model = TableModel()
        table = TableCanvas(frame, model=table_model, editable=False)
        table_model.importDict(books.to_dict('index'))
        table.show()

        log_entries.append("Browsing books")

    top = tk.Toplevel(root)
    top.title("Browse Books")
    top.geometry("600x400")
    top.configure(bg=bg_color)

    tk.Label(top, font=("Andalus", 16), text="Browse through the library", bg=bg_color, fg=fg_color).place(relx=0.5,
                                                                                                           rely=0.2,
                                                                                                           anchor='center')
    tk.Button(top, text="Browse", font=('Andalus', 15),
              command=browse_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.4, anchor='center')


def show_log():
    top = tk.Toplevel(root)
    top.title("Action Log")
    top.geometry("500x500")
    top.configure(bg=bg_color)

    tk.Label(top, text="LOG", bg=bg_color, fg=fg_color, font=('Andalus', 24)).pack(pady=10)

    log_text = tk.Text(top, font=('Helvetica', 12), bg=btn_bg_color, fg=fg_color, wrap='word', state='normal')
    log_text.pack(expand=True, fill='both')

    for entry in log_entries:
        log_text.insert('end', "\n    " + entry + "\n")

    log_text.config(state='disabled')


def deleteBook():
    def delete_action():
        isbn = isbn_entry.get()
        delete_book(isbn, cnxn)
        log_entries.append("Book deleted")
        messagebox.showinfo("Info", "Book deleted!")

    top = tk.Toplevel(root)
    top.title("Delete Book")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="ISBN: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    isbn_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    isbn_entry.place(relx=0.5, rely=0.23)

    tk.Button(top, text="Delete", font=('Andalus', 15),
              command=delete_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.8, anchor='center')


def borrow():
    def borrow_action():
        transaction_id = transaction_id_entry.get()
        borrow_date = borrow_date_entry.get()
        isbn = isbn_entry.get()
        sid = sid_entry.get()
        insertBorrows(transaction_id, borrow_date, isbn, sid, cnxn)
        log_entries.append("Book borrowed")
        messagebox.showinfo("Info", "Book borrowed!")

    top = tk.Toplevel(root)
    top.title("Borrow")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="Transaction ID: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    transaction_id_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    transaction_id_entry.place(relx=0.5, rely=0.23)

    tk.Label(top, text="Borrow Date: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.3)
    borrow_date_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    borrow_date_entry.place(relx=0.5, rely=0.33)

    tk.Label(top, text="ISBN: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.4)
    isbn_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    isbn_entry.place(relx=0.5, rely=0.43)

    tk.Label(top, text="SID: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.5)
    sid_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    sid_entry.place(relx=0.5, rely=0.53)

    tk.Button(top, text="Borrow", font=('Andalus', 15),
              command=borrow_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.8, anchor='center')


def borrowedBooks():
    def browse_action():
        sids = sid_entry.get()
        sid_list = [sid.strip() for sid in sids.split(',')]
        books = join_students_books(sid_list, cnxn)

        if books is not None:
            top = tk.Toplevel(root)
            top.title("Borrowed Books")
            frame = tk.Frame(top)
            frame.pack(expand=True, fill='both')
            tk.Label(top, text="Borrowed Books", font=('Andalus', 20), bg=bg_color, fg=fg_color).pack(pady=10)
            table_model = TableModel()
            table = TableCanvas(frame, model=table_model, editable=False)
            table_model.importDict(books.to_dict('index'))
            table.show()
        else:
            messagebox.showinfo("No Results", "No books found for the given SID values")

        log_entries.append("Browsing borrowed books")

    top = tk.Toplevel(root)
    top.title("Borrowed Books")
    top.geometry("600x400")
    top.configure(bg=bg_color)

    tk.Label(top, font=("Andalus", 16), text="Enter SID values separated by commas", bg=bg_color, fg=fg_color).place(
        relx=0.5, rely=0.2, anchor='center')
    sid_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 14), fg=fg_color)
    sid_entry.place(relx=0.5, rely=0.3, anchor='center')

    tk.Button(top, text="Browse", font=('Andalus', 15),
              command=browse_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.5, anchor='center')


def deleteStud():
    def delete_action():
        sid = sid_entry.get()
        DeleteStud(sid, cnxn)
        log_entries.append("Student deleted")
        messagebox.showinfo("Info", "Student deleted!")

    top = tk.Toplevel(root)
    top.title("Delete Student")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="SID: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    sid_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    sid_entry.place(relx=0.5, rely=0.23)

    tk.Button(top, text="Delete", font=('Andalus', 15),
              command=delete_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.8, anchor='center')



def report():
    def number_of_books_borrowed_by_all_students():

        data = Number_of_Books_Borrowed_by_AllStuds(cnxn)
        top = tk.Toplevel(root)
        top.title("Report")
        top.geometry("1000x600")
        top.configure(bg=bg_color)

        tk.Label(top, text="SID", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.1)
        tk.Label(top, text="Full Name", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.5, rely=0.1)
        tk.Label(top, text="Number of Borrowed Books", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.8, rely=0.1)

        for i, row in enumerate(data):
            tk.Label(top, text=row[0], font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2 + i * 0.1)
            tk.Label(top, text=row[1], font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.5, rely=0.2 + i * 0.1)
            tk.Label(top, text=row[2], font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.8, rely=0.2 + i * 0.1)










    def number_of_books_written_by_all_authors():
        data = NumberOfBooksWrittenByAllAuthors(cnxn)
        top = tk.Toplevel(root)
        top.title("Report")
        top.geometry("1500x600")
        top.configure(bg=bg_color)

        tk.Label(top, text="Author", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.1)
        tk.Label(top, text="Number of Books", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.8, rely=0.1)

        for i, row in enumerate(data):
            tk.Label(top, text=row[0], font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2 + i * 0.1)
            tk.Label(top, text=row[1], font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.8, rely=0.2 + i * 0.1)





    top = tk.Toplevel(root)
    top.title("Report")
    top.geometry("450x400")
    top.configure(bg=bg_color)
    tk.Button(top, text="Number of Books Borrowed by All Students", font=('Andalus', 15),
                command=number_of_books_borrowed_by_all_students, bg=btn_bg_color, width=35,
                fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.3, anchor='center')

    tk.Button(top, text="Number of Books Written by All Authors", font=('Andalus', 15),
                command=number_of_books_written_by_all_authors, bg=btn_bg_color, width=35,
                fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.5, anchor='center')


















def update_admin():
    def update_action():
        ssn = ssn_entry.get()
        column = column_entry.get()
        value = value_entry.get()
        UpdateAdmin(ssn, column, value, cnxn)
        log_entries.append("Admin updated")
        messagebox.showinfo("Info", "Admin updated!")

    top = tk.Toplevel(root)
    top.title("Update Admin")
    top.geometry("400x300")
    top.configure(bg=bg_color)

    tk.Label(top, text="SSN: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.2)
    ssn_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    ssn_entry.place(relx=0.5, rely=0.23)

    tk.Label(top, text="Column: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.4)
    column_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    column_entry.place(relx=0.5, rely=0.43)

    tk.Label(top, text="Value: ", font=("Andalus", 16), bg=bg_color, fg=fg_color).place(relx=0.1, rely=0.6)
    value_entry = tk.Entry(top, bg=btn_bg_color, font=('Helvetica', 12), fg=fg_color)
    value_entry.place(relx=0.5, rely=0.63)

    tk.Button(top, text="Update", font=('Andalus', 15),
              command=update_action, bg=btn_bg_color, width=15,
              fg=btn_fg_color, activebackground=btn_hover_color).place(relx=0.5, rely=0.9, anchor='center')


btn_sign_up = ttk.Button(root, text="Sign Up", command=sign_up)
btn_update_user = ttk.Button(root, text="Update User", command=update_user)
btn_add_book = ttk.Button(root, text="Add Book", command=add_book)
btn_update_book = ttk.Button(root, text="Update Book", command=update_book)
btn_show_books = ttk.Button(root, text="Show Books", command=show_books)
btn_browse_books = ttk.Button(root, text="Browse Books", command=browse_books)
btn_show_log = ttk.Button(root, text="Log", command=show_log)
btn_delete_book = ttk.Button(root, text="Delete Book", command=deleteBook)
btn_borrow_book = ttk.Button(root, text="Borrow Book", command=borrow)
btn_borrowed_books = ttk.Button(root, text="Borrowed Books", command=borrowedBooks)
btn_delete_student = ttk.Button(root, text="Delete Student", command=deleteStud)

btn_report = ttk.Button(root, text="Report", command=report)
btn_update_admin = ttk.Button(root, text="Update Admin", command=update_admin)


button_width = 250
button_height = 50
spacing_x = 20
spacing_y = 40

# First row
btn_sign_up.place(x=20, y=105, width=button_width, height=button_height)
btn_update_user.place(x=20 + button_width + spacing_x, y=105, width=button_width, height=button_height)
btn_add_book.place(x=20 + 2 * (button_width + spacing_x), y=105, width=button_width, height=button_height)

# Second row
btn_update_book.place(x=20, y=105 + button_height + spacing_y, width=button_width, height=button_height)
btn_show_books.place(x=20 + button_width + spacing_x, y=105 + button_height + spacing_y, width=button_width,
                     height=button_height)
btn_browse_books.place(x=20 + 2 * (button_width + spacing_x), y=105 + button_height + spacing_y, width=button_width,
                       height=button_height)

# Third row
btn_borrow_book.place(x=20, y=105 + 2 * (button_height + spacing_y), width=button_width, height=button_height)
btn_borrowed_books.place(x=20 + button_width + spacing_x, y=105 + 2 * (button_height + spacing_y), width=button_width,
                         height=button_height)
btn_delete_book.place(x=20 + 2 * (button_width + spacing_x), y=105 + 2 * (button_height + spacing_y),
                        width=button_width, height=button_height)


# Fourth row
btn_delete_student.place(x=20, y=105 + 3 * (button_height + spacing_y), width=button_width, height=button_height)
btn_report.place(x=20 + button_width + spacing_x, y=105 + 3 * (button_height + spacing_y), width=button_width,
                 height=button_height)
btn_show_log.place(x=20 + 2 * (button_width + spacing_x), y=105 + 3 * (button_height + spacing_y), width=button_width,
                     height=button_height)

# Fifth row
btn_update_admin.place(x=20, y=105 + 4 * (button_height + spacing_y), width=button_width, height=button_height)


root.mainloop()
