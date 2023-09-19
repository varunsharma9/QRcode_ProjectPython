import qrcode
qr = qrcode.QRCode(
    version=10,  # QR code version (1 to 40, 1 being the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  # Size of each QR code box
    border=4,  # Border size
)

# Add data to the QR code
data = "https://www.linkedin.com/in/varun-sharma-210b34230"
qr.add_data(data)
# Create a QR code image
qr.make(fit=True)
qr_image = qr.make_image(fill_color="grey", back_color="black")
# Display the QR code
qr_image.show()
img.save("---png")