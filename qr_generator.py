#-----------linux------------------------

import qrcode
import os

def generate_qr(link, output_file="qrcode.png"):
    # Create QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save image
    img.save(output_file)

    print(f"✅ QR Code generated successfully: {output_file}")


if __name__ == "__main__":
    link = "https://play.google.com/store/apps/details?id=in.itfixer199.app"

    # ✅ IMPORTANT: use .png or .jpg
    output_path = "/home/anandth07/Desktop/qr.png"

    generate_qr(link, output_path)

