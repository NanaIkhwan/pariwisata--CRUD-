import pymysql

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='tourism_db'
    )
    return connection

# Fungsi untuk menambah pemesanan
def add_booking(name, email, destination, booking_date):
    connection = get_db_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO bookings (name, email, destination, booking_date, status)
                    VALUES (%s, %s, %s, %s, 'Pending')
                """, (name, email, destination, booking_date))
                connection.commit()
        except Exception as e:
            print(f"Error saat menambah pemesanan: {e}")
        finally:
            connection.close()
    else:
        print("Koneksi database gagal.")

# Fungsi untuk mendapatkan semua pemesanan
def get_bookings():
    connection = get_db_connection()
    if connection:
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM bookings")
                bookings = cursor.fetchall()
                return bookings
        except Exception as e:
            print(f"Error saat mengambil data: {e}")
        finally:
            connection.close()
    else:
        print("Koneksi database gagal.")
        return []

# Fungsi untuk mendapatkan pemesanan berdasarkan ID
def get_booking_by_id(booking_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM bookings WHERE id=%s", (booking_id,))
            booking = cursor.fetchone()
    finally:
        connection.close()
    return booking

# Fungsi untuk mengedit pemesanan
def edit_booking(booking_id, name, email, destination, booking_date):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE bookings 
                SET name=%s, email=%s, destination=%s, booking_date=%s 
                WHERE id=%s
            """, (name, email, destination, booking_date, booking_id))
            connection.commit()
    finally:
        connection.close()

# Fungsi untuk membatalkan pemesanan
def cancel_booking(booking_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM bookings WHERE id=%s
            """, (booking_id,))
            connection.commit()
    finally:
        connection.close()