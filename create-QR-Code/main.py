import qrcode
import qrcode.image.svg

def qrcode_png():
    qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=2)

    qr.add_data("http://google.com")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QRCode.png")

def qrcode_svg():
    factory = qrcode.image.svg.SvgPathImage
    svg_img = qrcode.make("Hello World!", image_factory=factory)
    svg_img.save("myQR.svg")

def main():
    qrcode_png()
    qrcode_svg()

if __name__=='__main__':
    main()