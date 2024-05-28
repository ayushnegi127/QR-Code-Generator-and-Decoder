# QR Code Generator and Decoder

This Python script allows you to generate QR codes from data and decode existing QR code images.

## Prerequisites

- Python 3.x
- Required Python packages: `qrcode`, `PIL`, `pyzbar`

You can install the required packages using pip:

```
pip install qrcode pillow pyzbar
```

## Usage

1. **Generate QR Code:**
    - Run the script and choose the option to generate a QR code.
    - Enter the data you want to encode in the QR code.
    - Provide the file path where you want to save the QR code image.

2. **Decode QR Code:**
    - Run the script and choose the option to decode a QR code.
    - Enter the file path of the QR code image you want to decode.

## Example

### Generating a QR Code

```bash
$ python qr_code.py
Do you want to generate or decode a QR code? (enter 'generate' or 'decode'): generate
Enter the data to encode in the QR code: Hello, world!
Enter the file path to save the QR code image: hello_world_qr.png
QR code saved as hello_world_qr.png
```

### Decoding a QR Code

```bash
$ python qr_code.py
Do you want to generate or decode a QR code? (enter 'generate' or 'decode'): decode
Enter the file path of the QR code image to decode: hello_world_qr.png
Decoded data: Hello, world!
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

