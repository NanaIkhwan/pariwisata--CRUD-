from flask import Flask, render_template, request, redirect, url_for
from DB_Operations import add_booking, get_bookings, edit_booking, cancel_booking, get_booking_by_id

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', section='home')

@app.route('/content')
def content():
    bookings = get_bookings()
    return render_template('index.html', section='content', bookings=bookings)

@app.route('/about')
def about():
    return render_template('index.html', section='about')

@app.route('/book', methods=['POST'])
def book():
    # Mengambil data dari form
    name = request.form['name']
    email = request.form['email']
    destination = request.form['destination']
    booking_date = request.form['booking_date']
    
    # Menambahkan pemesanan ke database
    add_booking(name, email, destination, booking_date)
    
    return redirect(url_for('content'))

@app.route('/edit/<int:booking_id>', methods=['GET', 'POST'])
def edit(booking_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        destination = request.form['destination']
        booking_date = request.form['booking_date']
        
        # Update pemesanan di database
        edit_booking(booking_id, name, email, destination, booking_date)
        return redirect(url_for('content'))
    
    booking = get_booking_by_id(booking_id)
    
    # Debugging log
    print(f"Booking data: {booking}")
    
    return render_template('edit_booking.html', booking=booking)


@app.route('/cancel/<int:booking_id>')
def cancel(booking_id):
    # Menghapus pemesanan dari database
    cancel_booking(booking_id)
    
    return redirect(url_for('content'))


if __name__ == '__main__':
    app.run(debug=True)