﻿CREATE TABLE  Admins   (
   SSN  int NOT NULL,
   FirstName  varchar(255) NULL,
   LastName  varchar(255) NULL,
  PRIMARY KEY ( SSN )
);

CREATE TABLE  Author   (
   Name  varchar(255) NOT NULL,
  PRIMARY KEY ( Name )
);

CREATE TABLE  Books   (
   ISBN  int NOT NULL,
   Name  varchar(255) NOT NULL,
   AuthorName  varchar(255) NULL,
   PublisherName  varchar(255) NULL,
   BorrowingPeriod  varchar(255) NULL,
   Genre  varchar(255) NULL,
   PublicationYear  varchar(255) NULL,
  PRIMARY KEY ( ISBN )
);

CREATE TABLE  Borrows   (
   TransactionID  int NOT NULL,
   BorrowDate  date NULL,
   ISBN  int NOT NULL,
   SID  int NOT NULL,
  PRIMARY KEY ( TransactionID )
);

CREATE TABLE  Manages   (
   ISBN  int NOT NULL,
   SSN  int NOT NULL
);

CREATE TABLE  Publisher   (
   Name  varchar(255) NOT NULL,
  PRIMARY KEY ( Name )
);

CREATE TABLE  Publishes   (
   ISBN  int NULL,
   PublisherName  varchar(255) NULL
);

CREATE TABLE  Students   (
   FirstName  varchar(255) NOT NULL,
   PhoneNumber  varchar(25) NULL,
   DateOfBirth  date NOT NULL,
   LastName  varchar(255) NOT NULL,
   SID  int NOT NULL,
   Email  varchar(255) NULL,
  PRIMARY KEY ( SID )
);

CREATE TABLE  Writes   (
   AuthorName  varchar(255) NOT NULL,
   ISBN  int NOT NULL
);

ALTER TABLE  Borrows  ADD CONSTRAINT  StudentBorrows  FOREIGN KEY ( SID ) REFERENCES  Students  ( SID );
ALTER TABLE  Borrows  ADD CONSTRAINT  BorrowedBook  FOREIGN KEY ( ISBN ) REFERENCES  Books  ( ISBN );
ALTER TABLE  Manages  ADD CONSTRAINT  AdminManages  FOREIGN KEY ( SSN ) REFERENCES  Admins  ( SSN );
ALTER TABLE  Manages  ADD CONSTRAINT  ManagedBook  FOREIGN KEY ( ISBN ) REFERENCES  Books  ( ISBN );
ALTER TABLE  Publishes  ADD CONSTRAINT  BookPublished  FOREIGN KEY ( ISBN ) REFERENCES  Books  ( ISBN );
ALTER TABLE  Publishes  ADD CONSTRAINT  PublishingPublisher  FOREIGN KEY ( PublisherName ) REFERENCES  Publisher  ( Name );
ALTER TABLE  Writes  ADD CONSTRAINT  AuthorWrites  FOREIGN KEY ( AuthorName ) REFERENCES  Author  ( Name );
ALTER TABLE  Writes  ADD CONSTRAINT  WrittenBook  FOREIGN KEY ( ISBN ) REFERENCES  Books  ( ISBN );
/*for admins*/
INSERT INTO Admins (FirstName, LastName, SSN) VALUES
	('Athena', 'Holder', '2263303432'),
	('Naomi', 'Mack', '9799715148'),
	('Millicent', 'Bard', '9379642068'),
	('Marcella', 'Schneider', '0416576575'),
	('Edythe', 'Nicholas', '9482999290'),
	('Valene', 'Canales-Stauffer', '5058913202'),
	('Chas', 'Banda', '8296318004'),
	('Lorrie', 'East', '5004928717'),
	('Helene', 'Montoya', '8076179536'),
	('Tresa', 'Stewart', '4716234200'),
	('Joselyn', 'Singleton', '2388340011'),
	('Cheryll', 'Sheehan', '9650491747'),
	('Bernita', 'Sanchez', '0585606613'),
	('Wilbur', 'Roger', '2260993118'),
	('Donnell', 'Parrish', '0814974041'),
	('Charlene', 'Smith', '7163377515'),
	('Adella', 'Cramer', '5396322547'),
	('Demetrice', 'Pringle', '6425428318'),
	('Rhett', 'Crowley', '8219846996'),
	('Cleora', 'Rubio', '4352585605'),
	('Rupert', 'Langlois', '9622327855'),
	('Latrice', 'Breeden', '5854979244'),
	('Annemarie', 'Robledo', '2787804663'),
	('Corene', 'Larry', '0478523148'),
	('Wade', 'Bartholomew', '5687582595'),
	('Tamisha', 'Ames', '4960153405'),
	('Cecilia', 'Grimes-Graham', '2724637845'),
	('Jeane', 'Matias', '6096677478'),
	('Bertram', 'Stock', '2021491444'),
	('Arie', 'Willoughby', '7935733769'),
	('Marisha', 'Baxley', '1306924736'),
	('Chin', 'Mayo', '5204083609'),
	('Mathilde', 'Boland', '3610090230'),
	('Beatriz', 'Saddler', '2564342411'),
	('Cecelia', 'Broadnax', '7657215691'),
	('Cortez', 'Holloway', '4926140033'),
	('Cynthia', 'Isaacson', '7008193915'),
	('Brett', 'Andre-Geiger', '0677170003'),
	('Cristin', 'Beverly', '1899766512'),
	('Ella', 'Hale', '6118185841'),
	('Cheree', 'Alicea', '6636508001'),
	('Gina', 'Chisolm', '0680653518'),
	('Modesta', 'Maki', '2076394244'),
	('Nicolasa', 'Bloom', '4003345073'),
	('Rosetta', 'Brittain', '6537944870'),
	('Juliane', 'Medeiros', '3437228926'),
	('Juliane', 'Hadden', '0967379467'),
	('Theodore', 'Hulsey', '7100560496'),
	('Carroll', 'Zeigler', '3878346312'),
	('Jonathan', 'Lafferty', '7513645153'),
	('Mckinley', 'Passmore', '7658880012'),
	('Nubia', 'Fain', '4564796770'),
	('Fernando', 'Mickens', '7776167914'),
	('Jackelyn', 'Osgood', '6749401963'),
	('Davida', 'Tennant', '0944021668'),
	('Lanora', 'Hoyt', '5804125761'),
	('Dee', 'Gerber-Knapp', '3154907001'),
	('Claudette', 'Appleton', '7890141708'),
	('Gigi', 'Morrill', '0321898456'),
	('Ileen', 'Carver', '9309593472'),
	('Ronald', 'Behrens', '2070153130'),
	('Marianela', 'Osburn', '2898381253'),
	('Lynda', 'Chaffin', '2325489282'),
	('Geoffrey', 'Downs', '6870074265'),
	('Rolande', 'Delgado', '4856365560'),
	('Maddie', 'Gilmore', '9624122032'),
	('Ta', 'Whelan', '5191140160'),
	('Alise', 'Robinette', '4702185305'),
	('Danyell', 'Healey', '7351167634'),
	('Jose', 'Downs', '6633800279'),
	('Abram', 'Cardoza', '5135944083'),
	('Garret', 'Keating', '0095100909'),
	('Alicia', 'Leavitt', '1268928948'),
	('Jamika', 'Moten', '6690109133'),
	('Lawanna', 'Atwell', '0775005050'),
	('Jadwiga', 'Roush', '4213975237'),
	('Dina', 'Borges', '7636674351'),
	('Dotty', 'Manns', '5011714010'),
	('Marlin', 'Major', '6099222283'),
	('Neely', 'Jamieson', '9697186208'),
	('Cristobal', 'Soliz', '3342006255'),
	('Norah', 'Hardin', '3592509440'),
	('Alta', 'Holbrook', '1810475537'),
	('Janeen', 'Williamson', '2568560048'),
	('Salina', 'Tuggle', '1982501674'),
	('Liane', 'Cowan', '8690092808'),
	('Marcene', 'Heinrich', '8755106230'),
	('Cameron', 'Liddell', '2141615145'),
	('Milda', 'Mcclanahan', '9543765319'),
	('Felica', 'Bolt', '6854372417'),
	('Zenobia', 'Stamps', '7830117122'),
	('Margarette', 'Thornton', '5993474475'),
	('David', 'Broussard', '8298066907'),
	('Valerie', 'Jacks', '7477352386'),
	('Maia', 'Upshaw', '8624430662'),
	('Holli', 'Ricks', '0582172812'),
	('Carroll', 'Fernandez', '3645045095'),
	('Reed', 'Law', '9741597249'),
	('Sunni', 'Plunkett', '8409857924');
/*for books*/
INSERT INTO Books (ISBN, Name, AuthorName, PublisherName, BorrowingPeriod, Genre, PublicationYear) VALUES
	('439023483', '  The Hunger Games (The Hunger Games, #1)  ', 'Suzanne Collins', 'Scholastic Corporation', '5', 'Dystopian', '2008'),
	('439554934', '  Harry Potter and the Sorcerer  s Stone (Harry Potter, #1)  ', '  J.K. Rowling, Mary GrandPré  ', 'Bloomsbury (UK) / Scholastic (US)', '3', 'Fantasy', '1997'),
	('316015849', '  Twilight (Twilight, #1)  ', 'Stephenie Meyer', '  Little, Brown and Company  ', '3', 'Fantasy/Romance', '2005'),
	('61120081', 'To Kill a Mockingbird', 'Harper Lee', 'Harper & Brothers', '4', 'Classics', '1960'),
	('743273567', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Charles Scribner  s Sons', '5', 'Classics', '1925'),
	('525478817', 'The Fault in Our Stars', 'John Green', 'Dutton Books', '6', 'Young Adult/Romance', '2012'),
	('618260307', 'The Hobbit', 'J.R.R. Tolkien', 'George Allen & Unwin', '2', 'Fantasy', '1937'),
	('316769177', 'The Catcher in the Rye', 'J.D. Salinger', '  Little, Brown and Company  ', '7', 'Classics', '1951'),
	('1416524797', '  Angels & Demons  (Robert Langdon, #1)  ', 'Dan Brown', 'Pocket Books', '9', 'Thriller/Mystery', '2000'),
	('679783261', 'Pride and Prejudice', 'Jane Austen', '  T. Egerton, Whitehall  ', '4', 'Classics/Romance', '1813'),
	('1594480001', 'The Kite Runner', 'Khaled Hosseini', 'Riverhead Books', '7', 'Contemporary Fiction', '2003'),
	('62024035', '  Divergent (Divergent, #1)  ', 'Veronica Roth', 'Katherine Tegen Books', '2', 'Dystopian', '2011'),
	('451524934', '1984', '  George Orwell, Erich Fromm, Celâl Üster  ', 'Secker & Warburg', '3', 'Dystopian', '1949'),
	('452284244', 'Animal Farm', 'George Orwell', 'Secker & Warburg', '3', 'Classics', '1945'),
	('553296981', 'The Diary of a Young Girl', '  Anne Frank, Eleanor Roosevelt, B.M. Mooyaart-Doubleday  ', 'Uitgeverij Contact', '6', 'Non-Fiction/Memoir', '1947'),
	('307269752', '  The Girl with the Dragon Tattoo (Millennium, #1)  ', '  Stieg Larsson, Reg Keeland  ', 'Norstedts F�rlag', '1', 'Mystery/Thriller', '2005'),
	('439023491', '  Catching Fire (The Hunger Games, #2)  ', 'Suzanne Collins', 'Scholastic Corporation', '1', 'Dystopian', '2009'),
	('43965548', '  Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)  ', '  J.K. Rowling, Mary GrandPré, Rufus Beck  ', 'Bloomsbury (UK) / Scholastic (US)', '9', 'Fantasy', '1999'),
	('618346252', '  The Fellowship of the Ring (The Lord of the Rings, #1)  ', 'J.R.R. Tolkien', 'George Allen & Unwin', '9', 'Fantasy', '1954'),
	('439023513', '  Mockingjay (The Hunger Games, #3)  ', 'Suzanne Collins', 'Scholastic Corporation', '3', 'Dystopian', '2010'),
	('439358078', '  Harry Potter and the Order of the Phoenix (Harry Potter, #5)  ', '  J.K. Rowling, Mary GrandPré  ', 'Bloomsbury (UK) / Scholastic (US)', '9', 'Fantasy', '2003'),
	('316166685', 'The Lovely Bones', 'Alice Sebold', '  Little, Brown and Company  ', '7', 'Contemporary Fiction', '2002'),
	('439064864', '  Harry Potter and the Chamber of Secrets (Harry Potter, #2)  ', '  J.K. Rowling, Mary GrandPré  ', 'Bloomsbury (UK) / Scholastic (US)', '8', 'Fantasy', '1998'),
	('439139600', '  Harry Potter and the Goblet of Fire (Harry Potter, #4)  ', '  J.K. Rowling, Mary GrandPré  ', 'Bloomsbury (UK) / Scholastic (US)', '4', 'Fantasy', '2000'),
	('545010225', '  Harry Potter and the Deathly Hallows (Harry Potter, #7)  ', '  J.K. Rowling, Mary GrandPré  ', 'Bloomsbury (UK) / Scholastic (US)', '8', 'Fantasy', '2007'),
	('307277674', '  The Da Vinci Code (Robert Langdon, #2)  ', 'Dan Brown', 'Doubleday', '9', 'Thriller/Mystery', '2003'),
	('439785960', '  Harry Potter and the Half-Blood Prince (Harry Potter, #6)  ', '  J.K. Rowling, Mary GrandPré  ', 'Bloomsbury (UK) / Scholastic (US)', '4', 'Fantasy', '2005'),
	('140283331', 'Lord of the Flies', 'William Golding', 'Faber and Faber', '3', 'Classics', '1954'),
	('743477111', 'Romeo and Juliet', '  William Shakespeare, Robert           Jackson  ', 'Thomas Creede', '1', 'Classics', '1595'),
	('297859382', 'Gone Girl', 'Gillian Flynn', 'Crown Publishing Group', '4', 'Thriller/Mystery', '2012'),
	('399155341', 'The Help', 'Kathryn Stockett', 'Amy Einhorn Books', '1', 'Contemporary Fiction', '2009'),
	('142000671', 'Of Mice and Men', 'John Steinbeck', 'Viking Press', '7', 'Classics', '1937'),
	('739326228', 'Memoirs of a Geisha', 'Arthur Golden', 'Alfred A. Knopf', '1', 'Historical Fiction', '1997'),
	('1612130291', '  Fifty Shades of Grey (Fifty Shades, #1)  ', 'E.L. James', 'Vintage Books', '9', 'Romance/Erotica', '2011'),
	('61122416', 'The Alchemist', '  Paulo Coelho, Alan R. Clarke  ', 'Rocco', '9', 'Fiction', '1988'),
	('385732554', '  The Giver (The Giver, #1)  ', 'Lois Lowry', 'Houghton Mifflin', '9', 'Dystopian', '1993'),
	('60764899', '  The Lion, the Witch, and the Wardrobe (Chronicles of Narnia, #1)  ', 'C.S. Lewis', 'Geoffrey Bles', '9', 'Fantasy', '1950'),
	('965818675', 'The Time Traveler  s Wife', 'Audrey Niffenegger', 'MacAdam/Cage', '3', 'Romance/Sci-Fi', '2003'),
	('553588486', '  A Game of Thrones (A Song of Ice and Fire, #1)  ', 'George R.R. Martin', 'Bantam Spectra', '8', 'Fantasy', '1996'),
	('143038419', '  Eat, Pray, Love  ', 'Elizabeth Gilbert', 'Penguin Books', '5', 'Non-Fiction/Memoir', '2006'),
	('786838655', '  The Lightning Thief (Percy Jackson and the Olympians, #1)  ', 'Rick Riordan', 'Miramax Books / Disney Hyperion', '7', 'Fantasy', '2005'),
	('451529308', '  Little Women (Little Women, #1)  ', 'Louisa May Alcott', 'Robert Brothers', '3', 'Classics', '1868'),
	('142437204', 'Jane Eyre', '  Charlotte Brontë, Michael Mason  ', '  Smith, Elder & Co.  ', '3', 'Classics', '1847'),
	('553816713', '  The Notebook (The Notebook, #1)  ', 'Nicholas Sparks', 'Warner Books', '8', 'Romance', '1996'),
	('770430074', 'Life of Pi', 'Yann Martel', 'Alfred A. Knopf', '8', 'Adventure/Fantasy', '2001'),
	('1565125606', 'Water for Elephants', 'Sara Gruen', 'Algonquin Books', '8', 'Historical Fiction/Romance', '2006'),
	('375831002', 'The Book Thief', 'Markus Zusak', 'Knopf', '4', 'Historical Fiction', '2005'),
	('307347974', 'Fahrenheit 451', 'Ray Bradbury', 'Ballantine Books', '2', 'Dystopian', '1953'),
	('316160199', '  New Moon (Twilight, #2)  ', 'Stephenie Meyer', '  Little, Brown and Company  ', '5', 'Fantasy/Romance', '2006'),
	('60513039', 'Where the Sidewalk Ends', 'Shel Silverstein', 'Harper & Row', '4', 'Poetry', '1974'),
	('1416914285', '  City of Bones (The Mortal Instruments, #1)  ', 'Cassandra Clare', 'Simon & Schuster', '7', 'Fantasy', '2007'),
	('316160202', '  Eclipse (Twilight, #3)  ', 'Stephenie Meyer', '  Little, Brown and Company  ', '1', 'Fantasy/Romance', '2007'),
	('375826696', '  Eragon (The Inheritance Cycle, #1)  ', 'Christopher Paolini', 'Knopf', '7', 'Fantasy', '2002'),
	('345391802', '  The Hitchhiker  s Guide to the Galaxy (Hitchhiker  s Guide to the Galaxy, #1)  ', 'Douglas Adams', 'Pan Books', '9', 'Sci-Fi/Comedy', '1979'),
	('60929871', 'Brave New World', 'Aldous Huxley', 'Chatto & Windus', '7', 'Dystopian', '1932'),
	('316067920', '  Breaking Dawn (Twilight, #4)  ', 'Stephenie Meyer', '  Little, Brown and Company  ', '7', 'Fantasy/Romance', '2008'),
	('142001740', 'The Secret Life of Bees', 'Sue Monk Kidd', 'Viking Press', '7', 'Contemporary Fiction', '2001'),
	('142437174', 'The Adventures of Huckleberry Finn', '  Mark Twain, John Seelye, Guy Cardwell  ', 'Scholastic Point', '7', 'Classics', '1884'),
	('64410935', 'Charlotte  s Web', '  E.B. White, Garth Williams, Rosemary Wells  ', 'Thomas Cautley Newby', '7', 'Children  s/Fantasy', '1952'),
	('1400032717', 'The Curious Incident of the Dog in the Night-Time', 'Mark Haddon', 'Atria Books', '8', 'Contemporary Fiction/Mystery', '2003'),
	('1594633665', 'The Girl on the Train', 'Paula Hawkins', 'Delacorte Press/Seymour Lawrence', '2', 'Thriller/Mystery', '2015'),
	('679879242', '  The Golden Compass (His Dark Materials, #1)  ', 'Philip Pullman', 'Macmillan Publishers', '2', 'Fantasy', '1995'),
	('393978893', 'Wuthering Heights', '  Emily Brontë, Richard J. Dunn  ', 'Riverhead Books', '5', 'Classics/Romance', '1847'),
	('743454537', 'My Sister  s Keeper', 'Jodi Picoult', 'Pocket Books', '2', 'Contemporary Fiction', '2004'),
	('385333846', 'Slaughterhouse-Five', 'Kurt Vonnegut Jr.', 'Katherine Tegen Books', '1', 'Classics/Science Fiction', '1969'),
	('446675539', 'Gone with the Wind', 'Margaret Mitchell', 'Tor Books', '9', 'Horror', '1936'),
	('1594489505', 'A Thousand Splendid Suns', 'Khaled Hosseini', '  Lackington, Hughes, Harding, Mavor & Jones  ', '1', 'Sci-Fi/Romance', '2007'),
	('671027344', 'The Perks of Being a Wallflower', 'Stephen Chbosky', 'Doubleday', '6', 'Young Adult/Contemporary Fiction', '1999'),
	('7442912', '  Insurgent (Divergent, #2)  ', 'Veronica Roth', '  Little, Brown and Company  ', '4', 'Classics/Romance', '2012'),
	('812550706', '  Ender  s Game (Ender  s Saga, #1)  ', 'Orson Scott Card', 'Dutton Books', '4', 'Young Adult/Mystery', '1985'),
	('141439475', 'Frankenstein', '  Mary Wollstonecraft Shelley, Percy Bysshe Shelley, Maurice Hindle  ', '  Thomas Egerton, Military Library  ', '4', 'Contemporary Fiction', '1818'),
	('450040186', 'The Shining (The Shining #1)', 'Stephen King', '  Farrar, Straus and Giroux  ', '7', 'Classics', '1977'),
	('316068047', '  The Host (The Host, #1)  ', 'Stephenie Meyer', 'Broadway Books', '9', 'Children  s/Fantasy', '2008'),
	('142402516', 'Looking for Alaska', 'John Green', 'Unknown', '9', 'Non-Fiction/Memoir', '2005'),
	('140280090', '  Bridget Jones  s Diary (Bridget Jones, #1)  ', 'Helen Fielding', '�ditions Gallimard', '6', 'Non-Fiction/Adventure', '1996'),
	('141439661', 'Sense and Sensibility', '  Jane Austen, Tony Tanner, Ros Ballaster  ', 'Scribner', '9', 'Classics/Historical Fiction', '1811'),
	('439244196', '  Holes (Holes, #1)  ', '  Louis Sachar, Louis Sachar  ', 'Villard', '3', 'Science Fiction', '1998'),
	('307275558', '  The Devil Wears Prada (The Devil Wears Prada, #1)  ', 'Lauren Weisberger', 'Chapman & Hall', '1', 'Children  s/Fantasy', '2003'),
	('143039954', 'The Odyssey', '  Homer, Robert Fagles, E.V. Rieu, Frédéric Mugler, Bernard Knox  ', 'Alfred A. Knopf', '1', 'Thriller', '-720'),
	('156012197', 'The Little Prince', '  Antoine de Saint-Exupéry, Richard Howard, Dom Marcos Barbosa, Melina Karakosta  ', 'Harper & Row', '9', 'Historical Fiction/Memoir', '1946'),
	('743247540', 'The Glass Castle', 'Jeannette Walls', 'Wynwood Press', '5', 'Young Adult/Contemporary Fiction', '2005'),
	('385486804', 'Into the Wild', 'Jon Krakauer', 'Hill & Wang', '4', 'Fantasy/Romance', '1996'),
	('141439602', 'A Tale of Two Cities', '  Charles Dickens, Richard Maxwell, Hablot Knight Browne  ', 'Dutton Books', '4', 'Young Adult/Contemporary Fiction', '1859'),
	('307348130', '  Jurassic Park (Jurassic Park, #1)  ', 'Michael Crichton', 'Harcourt Brace Jovanovich', '9', 'Young Adult/Science Fiction', '1990'),
	('60256656', 'The Giving Tree', 'Shel Silverstein', 'Viking Press', '5', 'Non-Fiction/Economics', '1964'),
	('385338600', 'A Time to Kill', 'John Grisham', 'Delacorte Press', '8', 'Children  s/Fantasy', '1989'),
	('374500010', 'Night (The Night Trilogy #1)', '  Elie Wiesel, Marion Wiesel  ', 'William Morrow and Company', '6', 'Magical Realism', '1958'),
	('142414930', 'Paper Towns', 'John Green', 'Frederick Warne & Co', '7', 'Classics/Horror', '2008'),
	('345418263', 'The Princess Bride', 'William Goldman', 'Literatura Contempor�nea', '1', 'Romance/Erotica', '1973'),
	('140385720', 'The Outsiders', 'S.E. Hinton', '  Ward, Lock & Co.  ', '2', 'Horror', '1967'),
	('385737947', '  The Maze Runner (Maze Runner, #1)  ', 'James Dashner', 'Vintage Books', '2', 'Mystery/Thriller', '2009'),
	('61234001', '  Freakonomics: A Rogue Economist Explores the Hidden Side of Everything (Freakonomics, #1)  ', '  Steven D. Levitt, Stephen J. Dubner  ', 'Archibald Constable and Company', '4', 'Romance/Erotica', '2005')

/*for students*/
INSERT INTO Students (FirstName, LastName,PhoneNumber, DateOfBirth, Email, SID) VALUES
	('Verda', 'Reece', '+212-3003-547-383', '1994-04-16', 'henrietta-singletary0@dictionary.com', '85298'),
	('Madlyn', 'Hinkle', '+689-7509-455-743', '1972-01-12', 'priscilladaily@hotmail.com', '60473'),
	('Anthony', 'Gulley', '+592-7516-788-020', '1994-09-11', 'ashlea00@observation.com', '87909'),
	('Ignacio', 'Sharpe', '+33-4762-258-462', '1982-07-22', 'lorretta.thompson@scoop.com', '10142'),
	('Maricruz', 'Calvert', '+218-9603-707-346', '2004-12-13', 'efren0418@funding.com', '80162'),
	('Vallie', 'Dykes', '+965-6942-639-991', '2014-11-24', 'catalina_chapman63@yahoo.com', '40537'),
	('Joycelyn', 'Hadley', '+60-0387-810-676', '2023-01-04', 'milagro.pinkerton@pro.com', '90907'),
	('Helga', 'Tomlinson', '+33-9125-092-468', '1995-05-17', 'felica8@memphis.com', '92106'),
	('Annett', 'Townes', '+53-3971-839-437', '1978-06-03', 'june6643@cambridge.com', '69951'),
	('Tequila', 'Hendrix', '+263-0360-459-562', '2008-08-10', 'pete-allred980@essex.com', '31470'),
	('Kerri', 'Faber', '+508-2430-892-730', '1973-11-12', 'emely-jacobsen87@vacation.com', '23482'),
	('Inell', 'Grenier', '+679-0028-761-962', '2000-10-16', 'daniele-cahill6@gmail.com', '66516'),
	('Billie', 'Wyant', '+254-8816-132-156', '1983-09-27', 'bobbie50@yahoo.com', '30118'),
	('Lavenia', 'Mccallum-Back', '+599-9829-348-901', '2007-04-13', 'deedee82@chosen.mex.com', '57050'),
	('Laurence', 'Miranda', '+353-5089-906-558', '2023-05-21', 'janeyroldan960@gmail.com', '83541'),
	('Mayme', 'Adame', '+49-3351-058-093', '2018-08-14', 'julio_franks@checks.com', '63112'),
	('Jen', 'Trammell', '+38-7998-514-529', '2002-12-05', 'ayana46269@gmail.com', '61217'),
	('Herminia', 'Clarkson', '+509-9502-374-239', '1976-02-03', 'earnest02340@nintendo.com', '88444'),
	('Evangelina', 'Hostetler', '+221-5634-939-367', '2008-10-17', 'beula3552@reward.com', '97421'),
	('Krystin', 'Schreiber', '+90-9842-633-649', '2000-03-01', 'petra4@generators.minano.saitama.jp', '91761'),
	('Ronna', 'Hudspeth', '+966-7729-815-426', '2007-04-05', 'audra_cano2354@prize.com', '97888'),
	('Burt', 'Pogue', '+260-2892-936-005', '1999-09-29', 'hosea98@glory.com', '06462'),
	('Hassie', 'Gay', '+967-6306-949-621', '2008-02-22', 'enolamessenger@streams.com', '86177'),
	('Jaleesa', 'Ackerman', '+33-0592-780-031', '2007-09-24', 'felice8007@richardson.com', '47549'),
	('Vernon', 'Barden', '+237-4739-709-294', '2020-11-30', 'shante_mahaffey4830@yahoo.com', '49574'),
	('Zenaida', 'Parham', '+357-4611-580-662', '1984-05-31', 'lavera1@india.com', '93085'),
	('Felicia', 'Seifert', '+48-9835-335-544', '2018-02-28', 'sherri1614@vitamin.com', '39148'),
	('Nigel', 'Rodriguez', '+966-6529-583-188', '1980-10-24', 'miltongaddis-burdette@geological.date.hokkaido.jp', '22235'),
	('Jannet', 'Howerton', '+886-6727-748-844', '1997-03-26', 'sebastian-souza4@northeast.com', '66732'),
	('Phebe', 'Tanner', '+31-4090-374-619', '1970-02-14', 'rosaria-neill379@timothy.com', '32353'),
	('Sebastian', 'Cannon', '+593-2965-689-613', '1997-04-21', 'deadra57191@hotmail.com', '22514'),
	('Farrah', 'Rodrigue', '+254-7391-040-713', '1984-05-21', 'tona0@gmail.com', '99100'),
	('Polly', 'Wilhelm', '+58-4144-973-388', '1975-12-03', 'lucie_sellars-clemens@yahoo.com', '51796'),
	('Melani', 'Vincent', '+66-2030-399-411', '2019-05-23', 'mora-cheatham44226@gmail.com', '51850'),
	('Nila', 'Linn', '+33-7590-724-683', '1973-10-17', 'quincy88778@gmail.com', '38700'),
	('Marisa', 'Vo', '+46-9381-989-023', '2007-05-30', 'tresadanner@salvation.com', '66734'),
	('Wanita', 'Mabe', '+598-3884-880-554', '2002-05-06', 'divina.lindquist59@yahoo.com', '47019'),
	('Patria', 'Lemke', '+501-9186-874-932', '2017-06-15', 'lashawnda98068@hotmail.com', '50823'),
	('Tynisha', 'Barrios', '+502-9685-255-099', '1986-09-11', 'natalie_rhea@fingers.com', '83568'),
	('Gerald', 'Amos', '+234-8273-806-163', '2017-04-15', 'ewa.benner0@gmail.com', '19905'),
	('Louise', 'Slone', '+598-0030-762-301', '2002-02-06', 'ashleigh14167@adjust.suzaka.nagano.jp', '60732'),
	('Tamisha', 'Lees', '+254-5775-086-768', '1981-09-30', 'hilton.freitas@yahoo.com', '19101'),
	('Sherika', 'Grace', '+592-0498-621-136', '2007-11-05', 'eviespillman361@gmail.com', '69293'),
	('Ami', 'Mcleod', '+56-4414-722-494', '1997-12-13', 'madelainegalindo3657@dominant.com', '79770'),
	('Damien', 'Dunlap', '+886-5985-071-197', '1987-02-03', 'joaquin4@exhibits.com', '17807'),
	('Simon', 'Thames', '+94-5788-013-892', '2002-06-22', 'modesto3@gmail.com', '04391'),
	('Jessika', 'Ricks', '+506-8928-033-361', '2008-06-02', 'devona677@yahoo.com', '98930'),
	('Moises', 'Brewer', '+39-3605-006-305', '2000-07-27', 'bee5@laboratory.com', '35451'),
	('Constance', 'Petit', '+684-7797-925-831', '1990-02-21', 'shawn7@continuity.com', '92691'),
	('Kerry', 'Bankston', '+48-8610-791-857', '2012-03-14', 'jessi2065@yahoo.com', '60441'),
	('Philomena', 'Tejada', '+251-0317-739-847', '2021-08-05', 'greg-faber@gmail.com', '84459'),
	('Latina', 'Nolan', '+54-2982-756-444', '1992-05-28', 'lillianahollenbeck6@mobiles.com', '95686'),
	('Tamiko', 'Whiteman', '+65-9563-581-072', '2011-08-27', 'marylin_shively@collected.com', '86234'),
	('Shelba', 'Peeples-Storey', '+62-1346-853-944', '1993-06-22', 'sandramoran-higgins@fed.com', '05081'),
	('Michele', 'Hoff', '+98-9478-921-811', '2019-10-13', 'cesar_wilkinson@giant.com', '62925'),
	('Lane', 'Trapp', '+260-7475-480-875', '2004-11-16', 'kimberley297@gmail.com', '75068'),
	('Buford', 'Kimbrough', '+254-4445-811-546', '2020-08-05', 'morris6@manor.com', '85854'),
	('Miyoko', 'Fife', '+44-1924-638-314', '1980-04-30', 'simona6@yahoo.com', '67339'),
	('Tomasa', 'Amundson', '+679-3760-440-677', '2018-01-03', 'tawanda9@transition.com', '19071'),
	('Dewey', 'Felton-Michaels', '+501-6209-722-704', '1988-10-27', 'lauralee_kline@gmail.com', '07450'),
	('Shizuko', 'Barlow', '+60-4346-893-693', '1986-02-01', 'tiesha.whitcomb@fg.com', '20022'),
	('Daren', 'Latham', '+64-5127-777-728', '1978-01-09', 'dorcas_deal6@isp.com', '07825'),
	('Rena', 'Hildebrand', '+972-3160-938-853', '1981-01-16', 'clifton-mckeon83@dl.com', '73428'),
	('Colleen', 'Mercier', '+266-2508-396-883', '2012-09-06', 'luann_tilton59678@hotmail.com', '16753'),
	('Danyell', 'Mattson', '+221-6964-364-986', '1988-12-03', 'willette7@gmail.com', '33429'),
	('Claude', 'Sellers', '+33-6885-566-108', '1991-12-09', 'nga_delaney-roach57465@hotmail.com', '74905'),
	('Lucius', 'Haley', '+63-5087-773-486', '2021-03-22', 'consuela4@gmail.com', '99868'),
	('Cherlyn', 'Sipes', '+263-6858-299-902', '2003-05-04', 'catrina_thorton46@developers.com', '16160'),
	('Reuben', 'Humphrey', '+598-0858-340-840', '1974-08-13', 'sabrina8371@describes.com', '89439'),
	('Latoria', 'Kirkland', '+20-8261-072-322', '1975-12-03', 'qianaguidry73795@gmail.com', '08117'),
	('Herb', 'Steffen', '+47-1900-143-924', '1996-01-23', 'yevette.sonnier@gmail.com', '10570'),
	('Nobuko', 'Nevarez', '+32-9426-272-897', '1988-06-11', 'jamison-noll@restaurant.adachi.tokyo.jp', '87734'),
	('Carolyn', 'Fernandez', '+886-6071-384-543', '2015-02-10', 'camelliaoliver9113@participants.com', '19952'),
	('Nick', 'Place', '+39-8591-455-067', '1974-09-19', 'brant_fleming73536@mailman.com', '29271'),
	('Elda', 'Lemmon', '+81-2330-245-151', '2004-07-25', 'karren_warden@yahoo.com', '86325'),
	('Bradly', 'Mcnamee', '+43-6886-807-176', '1992-04-12', 'brigida7@hotmail.com', '01694'),
	('Albertha', 'Julian', '+231-5421-163-025', '1995-04-16', 'willis.mendez05@gmail.com', '43401'),
	('Eunice', 'Ferguson', '+254-2803-527-586', '1980-11-30', 'annice-simon@gmail.com', '49548'),
	('Margret', 'Mitchell', '+358-2182-541-630', '1980-09-10', 'le.gale@hotmail.com', '64056'),
	('Soledad', 'Homer-Lind', '+234-6304-909-431', '1994-03-11', 'shelly.montague@enormous.br.com', '20068'),
	('Misty', 'Bobbitt', '+237-0575-133-231', '1990-11-17', 'contessa.keister09471@yahoo.com', '15940'),
	('Charlyn', 'Irish', '+968-2121-709-147', '1984-11-15', 'annis.kang0428@style.com', '51570'),
	('Inga', 'Belton', '+598-7643-466-449', '2008-05-06', 'rick.jeter@foundation.com', '10542'),
	('Evalyn', 'Perdue', '+265-8865-056-413', '1980-03-22', 'rebeckadanielson0986@sorts.com', '36161'),
	('Maude', 'Haller', '+358-3235-229-198', '2006-06-21', 'ward657@finest.solund.no', '19483'),
	('Silva', 'Castillo', '+234-3475-475-108', '2002-12-10', 'kenya-kasper19@hotmail.com', '57222'),
	('Humberto', 'Peak', '+39-5700-230-413', '1997-08-24', 'su-carrion@gmail.com', '34112'),
	('Madlyn', 'Munson', '+30-5814-668-382', '2014-01-19', 'eneida-luke@gmail.com', '25257'),
	('Ayanna', 'Dunning', '+503-9628-627-427', '2002-11-20', 'yuri-berryman4@tribal.com', '39208'),
	('Porsche', 'Pacheco', '+47-7399-688-982', '1989-09-09', 'melina63899@episode.com', '93976'),
	('Karyn', 'Duong', '+886-6745-991-039', '1996-05-22', 'dickadame@expedia.hockey', '17029'),
	('Rosario', 'Cecil', '+592-5905-983-860', '2013-07-22', 'lylaward27@gmail.com', '07743'),
	('Laverne', 'Lessard', '+966-0817-021-959', '2007-02-16', 'lilliam301@steam.leangaviika.no', '34478'),
	('Natacha', 'Mcfadden', '+39-7560-122-872', '1986-08-12', 'arron.hollis@hotmail.com', '91651'),
	('Ezekiel', 'Snodgrass', '+266-4651-466-611', '1982-07-14', 'zackary48699@local.com', '16233'),
	('Hortense', 'Proctor', '+263-9136-618-361', '1973-09-11', 'kandice1@ctrl.com', '83929'),
	('Era', 'Mccormack', '+66-9457-023-013', '1997-09-10', 'danyellekimble69@households.com', '79804'),
	('Judith', 'Gore', '+94-2999-940-684', '2009-02-20', 'trudy.rust6895@gmail.com', '52067'),
	('Ian', 'Borrego', '+263-0117-837-797', '2003-04-01', 'winterredding8318@difficulties.com', '19981');