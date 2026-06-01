# QR Code Generator

A minimal command-line tool to convert any URL into a QR code image using Python.

## Features

- Convert any URL to a QR code instantly
- Saves output as a `.png` image
- Auto-appends `.png` extension if not provided

## Requirements

- Python 3.x
- `qrcode`
- `Pillow` (required by qrcode for image saving)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/qr-generator.git
   cd qr-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

You'll be prompted to:
1. Enter the URL you want to convert
2. Enter the filename to save the QR code (`.png` is added automatically)

## Example

```
Enter url want to convert : https://github.com
Enter file name want to save qr : github_qr
```

This saves the QR code as `github_qr.png` in the current directory.

## Output

![QR Code Example](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/220px-QR_code_for_mobile_English_Wikipedia.svg.png)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
