document.getElementById('booking-form').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('popup').style.display = 'flex';
    document.getElementById('confirmation').style.display = 'block';
});

document.getElementById('booking-form').addEventListener('submit', function(event) {
    console.log("Formulir dikirimkan.");
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const destination = document.getElementById('destination').value;

    if (!name || !email || !destination) {
        console.log("Formulir belum lengkap.");
        event.preventDefault(); // Mencegah pengiriman jika ada yang kosong
    } else {
        console.log(`Nama: ${name}, Email: ${email}, Tujuan: ${destination}`);
    }
});