import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# Function to generate QR code
def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"QR code saved as {file_path}")

# Function to decode QR code
def decode_qr_code(file_path):
    img = Image.open(file_path)
    decoded_objects = decode(img)
    if decoded_objects:
        decoded_data = decoded_objects[0].data.decode('utf-8')
        print(f"Decoded data: {decoded_data}")
        return decoded_data
    else:
        print("No QR code found.")
        return None

if __name__ == "__main__":
    choice = input("Do you want to generate or decode a QR code? (enter 'generate' or 'decode'): ").strip().lower()
    
    if choice == 'generate':
        data = input("Enter the data to encode in the QR code: ")
        file_path = input("Enter the file path to save the QR code image: ")
        generate_qr_code(data, file_path)
    elif choice == 'decode':
        file_path = input("Enter the file path of the QR code image to decode: ")
        decode_qr_code(file_path)
    else:
        print("Invalid choice. Please enter 'generate' or 'decode'.")
