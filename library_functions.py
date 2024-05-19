import pyodbc
import pandas as pd
import datetime

cnxn_str = (
    "DRIVER={SQL Server Native Client 11.0};"  # Replace with actual driver name
    "SERVER=localhost;"
    "DATABASE=library;"
    "Trusted_Connection=yes;"
)

# Connect to database
cnxn = pyodbc.connect(cnxn_str)
def select(column, table, cnxn):
    query = "Select " + column +" from " + table
    df = pd.read_sql(query, cnxn)
    return df
def insertStudent(FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email, cnxn):
    sql_query = """
            INSERT INTO Students (FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email)
            VALUES (?, ?, ?, ?, ?, ?)
            """
    cursor = cnxn.cursor()
    DateOfBirth = datetime.datetime.strptime(DateOfBirth, '%Y-%m-%d').date()
    cursor.execute(sql_query, (FirstName, PhoneNumber, DateOfBirth, LastName, SID, Email))
    cnxn.commit()  # Commit the transaction

    # Close the cursor
    cursor.close()
def insertAdmin(SSN, FirstName, LastName, conn):
    sql_query = """
            INSERT INTO Admins (SSN, FirstName, LastName)
            VALUES (?, ?, ?)
            """
    cursor = cnxn.cursor()
    cursor.execute(sql_query, (SSN, FirstName, LastName))
    cnxn.commit()  # Commit the transaction

    # Close the cursor
    cursor.close()
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
        print("ISBN or SID does not exist.")

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
        cursor.execute(delete_query, isbn)
        cnxn.commit()

    delete_query = "DELETE FROM Books WHERE ISBN = ?"
    cursor = cnxn.cursor()
    cursor.execute(delete_query, isbn)
    cnxn.commit()
    print(f"The book with ISBN {isbn} has been deleted from all referencing tables and the Books table.")
    return True

def showbooks(criteria, value, cnxn):
    sql_query = f"SELECT * FROM BOOKS WHERE {criteria} = ?"
    df = pd.read_sql(sql_query, cnxn, params=[value])
    return df
def DeleteStud(SID,conn):
    crsr = conn.cursor()
    query = f"Delete from Borrows where SID = {SID}"
    crsr.execute(query)
    query = f"Delete from Students where SID = {SID}"
    crsr.execute(query)
    conn.commit()
    conn.close()
def UpdateStud(SID,Col,Val,conn):
    if Col == 'SID':
      conn.close()
      raise Exception('Cannot Edit Student\'s Id')
    crsr = conn.cursor()
    query = f"Update Students set {Col} = '{Val}' where SID = {SID}"
    crsr.execute(query)
    conn.commit()
    conn.close()

def UpdateAdmin(SNN, Col, Val, conn):
    if Col == 'SSN':
        conn.close()
        raise Exception('Cannot Edit Admin\'s SSN')
    crsr = conn.cursor()
    query = f"Update Admins set {Col} = '{Val}' where SSN = {SSN}"
    crsr.execute(query)
    conn.commit()
    conn.close()
def UpdateBook(ISBN,Col,Val,conn):
    if Col == 'ISBN':
      conn.close()
      raise Exception('Cannot Edit Book\'s ISBN')
    crsr = conn.cursor()
    query = f"Update Books set {Col} = '{Val}' where ISBN = {ISBN}"
    crsr.execute(query)
    conn.commit()
    conn.close()
def Number_of_Books_Borrowed_by_AllStuds(conn):
    crsr = conn.cursor()
    query = f"""Select Students.SID,CONCAT(Students.FirstName,' ',Students.LastName) as FullName, count(*) as Number_of_Borrowed_Books
                from Students join Borrows on Students.SID = Borrows.SID
                group By Students.SID,Students.FirstName,Students.LastName"""
    crsr.execute(query)
    data = crsr.fetchall()
    #print("SID" + "  Full Name    " + "Borrowed Books")
    for tuples in data:
        for attr in tuples:
            print(attr, end=" ")
        print()
    #conn.commit()
    conn.close()
    # return data
    """
        returns a list of tuples
        if you want to handle the data yourself or pass it somewhere else
    """
def Number_of_Books_Borrowed_by_AStud(SID, conn):
    crsr = conn.cursor()
    query = f"""select Students.SID,Students.FirstName,Students.LastName,count(*) as BooksBorrowed from Borrows join Students on Students.SID = Borrows.SID
                GROUP by Students.SID,Students.FirstName,Students.LastName
                HAVING Students.SID = {SID}"""
    crsr.execute(query)
    data = crsr.fetchall()
    #print("SID" + "       Name    " + "   Borrowed Books")
    for tuples in data:
        for attr in tuples:
            print(attr, end=" ")
        print()
    #conn.commit()
    conn.close()
    #return data[0]
    """
        will return tuple containing three values; Sid,First Name, Last Name, Number of borrowed Books
    """
def NumberOfBooksWrittenByAllAuthors(conn):
    crsr = conn.cursor()
    query = """
            Select Author.Name, count(*) as Number_of_Books
            from Author JOIN Books on Author.Name = Books.AuthorName
            group By Author.Name
            """
    crsr.execute(query)
    data = crsr.fetchall()
    #print("Author" + " Books")
    for tuples in data:
        for attr in tuples:
            print(attr, end=" ")
        print()
    conn.close()
    #return data
    """
        returns list of tuples where eacht tuple is a row in the table of the schema
    """
def NumberOfBooksWrittenByAnAuthor(Name,conn):
    crsr = conn.cursor()
    query = f"""
            Select Author.Name, count(*) as Number_of_Books
            from Author JOIN Books on Author.Name = Books.AuthorName
            group By Author.Name
            Having Author.Name = '{Name}'
            """
    crsr.execute(query)
    data = crsr.fetchall()
    #print("Author" + " Books")
    for tuples in data:
        for attr in tuples:
            print(attr, end=" ")
        print()
    conn.close()
    #return data[0]
    """
        returns list of tuples where eacht tuple is a row in the table of the schema
    """
def BooksByAuthor(Name,conn):
    query = f"""SELECT Author.Name,Books.ISBN, Books.Name,Books.PublisherName,Books.Genre,Books.PublicationYear
                from Author join Books on Author.Name = Books.AuthorName
                where Author.Name = '{Name}'
            """
    crsr = conn.cursor()
    crsr.execute(query)
    data = crsr.fetchall()
    conn.close()
    for tuples in data:
        for attr in tuples:
            print(attr, end=" ")
        print()
    #return data
    """
    again if you would like to get a grip of the data itself
    """