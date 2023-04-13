#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

conn = mysql.connector.connect(user = 'root',
    host = 'localhost',
    database = 'test')

print(conn)

conn.close()


# In[7]:


import mysql.connector

dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE db_V3922008")


# In[8]:


import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user = "root",
  passwd ="",
  database = "db_V3922008"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE data_stok_barang (
                    Id_Barang VARCHAR(25) PRIMARY KEY,
                    Nama_Barang VARCHAR(30) NOT NULL,
                    Harga_Barang INT,
                    Stok_Awal INT,
                    Barang_Masuk INT,
                    Barang_Keluar INT,
                    Stok_Akhir INT
                    
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[3]:


import mysql.connector

#Koneksikan ke database
dataBase = mysql.connector.connect(
  host ="localhost",
  user = "root",
  passwd ="",
  database = "db_V3922008"
)

cursorObject = dataBase.cursor()

#Script untuk menambahkan data ke dalam tabel
def insert_data( Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir ):
    sql = "INSERT INTO data_stok_barang (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    cursorObject.execute(sql, val) 
    dataBase.commit()

    print(" ")
    print("Data telah berhasil ditambahkan")

#Script untuk menampilkan data dari tabel
def show_data():
    query = "SELECT * FROM data_stok_barang"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data telah berhasil ditampilkan")

#Script untuk mengubah data di dalam tabel
def update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir):
    sql = "UPDATE data_stok_barang SET Nama_Barang = %s, Harga_Barang = %s, Stok_Awal = %s, Barang_Masuk = %s, Barang_Keluar = %s, Stok_Akhir = %s WHERE Id_Barang = %s"
    val = (Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir, Id_Barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data telah berhasil diupdate")

#Script untuk menghapus data dari dalam tabel
def delete_data(Id_Barang):
    sql = "DELETE FROM data_stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data telah berhasil dihapus")

#Script untuk mencari data melalui Id_Barang
def search_data(id_barang):
    sql = "SELECT * FROM data_stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    
    myresult = cursorObject.fetchall()
    
    for x in myresult:
        print(x)
        
    print(" ")
    print("Data telah berhasil dicari")

#Script untuk pilihan menu
while True:
    print(" ")
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Cari data")
    print("6. Keluar")
    print("-------------------")
    menu = input("Pilih menu> ") #Input ini digunakan untuk mencari pilihan menu
    print(" ")

    #Pilihan 1 "Insert data"
    if menu == "1":
        Id_Barang = input("Masukkan Id Barang : ")
        Nama_Barang = input("Masukkan Nama Barang : ")
        Harga_Barang = int(input("Masukkan Harga Barang : "))
        Stok_Awal = int(input("Masukkan Stok Awal : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar : "))
        
        #Script rumus untuk mencari stok_akhir
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        
        #Script untuk mencetak Stok_Akhir dari perhitungan rumus sebelumnya
        print("Stok Akhir : ", Stok_Akhir)
        
        insert_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    #Pilihan 2 "Show data"
    elif menu == "2":
        show_data()

    #Pilihan 3 "Update data"
    elif menu == "3":
        Id_Barang = input("Masukkan Id Barang yang akan diupdate : ")
        Nama_Barang = input("Masukkan Nama Barang baru : ")
        Harga_Barang = int(input("Masukkan Harga Barang baru : "))
        Stok_Awal = int(input("Masukkan Stok Awal baru : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk baru : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar baru : "))
        
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        print("Stok Akhir setelah diupdate : ", Stok_Akhir)
        
        update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

    #Pilihan 4 "Hapus data"
    elif menu == "4":
        Id_Barang = input("Masukkan Id Barang yang akan dihapus : ")
        
        delete_data(Id_Barang)

    #Pilihan 5 "Cari data"
    elif menu == "5":
        Id_Barang = input("Masukkan Id Barang yang akan dicari : ")
        
        search_data(Id_Barang)

    #Pilihan 6 "Keluar dari program"
    elif menu == "6":
        print("Terima kasih anda sudah menggunakan program kami")
        break

    #Ketika menginputkan data tidak sesuai dengan pilihan yang tersedia
    else:
        print("Maaf pilihan anda tidak sesuai, pilih menu dengan benar")


# In[ ]:




