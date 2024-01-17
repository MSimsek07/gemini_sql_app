import sqlite3

# Connectt to SQlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor = connection.cursor()

# create the table
# NAME - SURNAME - FACULTY - DEPARTMENT - CLASS - STUDENTID - CODE23COURSE - LECTURER - EMAIL - PHONENUMBER - MARK
table_info = """
Create table STUDENT(NAME VARCHAR(25),SURNAME VARCHAR(25), FACULTY VARCHAR(255), DEPARTMENT VARCHAR(25), CLASS VARCHAR(25), STUDENTID VARCHAR(255),
COURSE VARCHAR(255), LECTURER VARCHAR(255), EMAIL VARCHAR(255), PHONENUMBER VARCHAR(255), MARK INT);
"""

cursor.execute(table_info)

# Insert Some more records

cursor.execute('''Insert Into STUDENT values('Hasan','Yeni','Teknoloji Fakültesi', 'Yazımım Mühedisliği' , '4' , '168456132' , 'Yapay Zeka', 'Yunus Santur', 'hasanyeni@gmail.com', '05347896552', 60)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ahmet', 'Yılmaz', 'Mühendislik Fakültesi', 'Bilgisayar Mühendisliği', '2', '123456789', 'Programlamaya Giriş', 'Doç. Dr. Aydın', 'ahmet@example.com', '123-456-7890', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ayşe', 'Demir', 'Fen Fakültesi', 'Kimya', '3', '987654321', 'Organik Kimya', 'Prof. Öztürk', 'ayse@example.com', '987-654-3210', 70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mustafa', 'Kaya', 'İşletme Fakültesi', 'Finans', '1', '456789012', 'Muhasebe', 'Yrd. Doç. Dr. Şahin', 'mustafa@example.com', '456-789-0123', 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Zeynep', 'Altın', 'Sağlık Bilimleri Fakültesi', 'Hemşirelik', '4', '135792468', 'Anatomi', 'Prof. Yılmaz', 'zeynep@example.com', '321-654-9870', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Emre', 'Çelik', 'Edebiyat Fakültesi', 'Türk Dili ve Edebiyatı', '2', '246801357', 'Roman Tahlili', 'Dr. Şen', 'emre@example.com', '789-012-3456', 78)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Elif', 'Aydın', 'Mimarlık Fakültesi', 'Mimarlık', '3', '159263487', 'Mimari Tasarım', 'Doç. Dr. Gür', 'elif@example.com', '654-321-0987', 82)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mehmet', 'Güneş', 'Eğitim Fakültesi', 'Fen Bilgisi Öğretmenliği', '1', '369852147', 'Biyoloji', 'Yrd. Doç. Dr. Koç', 'mehmet@example.com', '987-654-3210', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Gamze', 'Kurt', 'İletişim Fakültesi', 'Halkla İlişkiler', '4', '852369741', 'Medya Planlama', 'Prof. Erdoğan', 'gamze@example.com', '321-987-6540', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ali', 'Aktaş', 'Fen-Edebiyat Fakültesi', 'Tarih', '2', '147258369', 'Osmanlı Tarihi', 'Doç. Dr. Güneş', 'ali@example.com', '012-345-6789', 75)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sema', 'Öztürk', 'Sağlık Bilimleri Fakültesi', 'Fizyoterapi', '3', '584619237', 'Fizyoterapi Teknikleri', 'Prof. Atalay', 'sema@example.com', '789-456-1230', 88)''')


# Disspaly ALl the records

print("The isnerted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes int he databse
connection.commit()
connection.close()
