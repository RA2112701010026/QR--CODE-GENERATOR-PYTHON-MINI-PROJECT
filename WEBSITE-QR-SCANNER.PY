import qrcode

website_address=input("enter your website address : ")

user_website_address=f"{website_address}"

user_website_qr=qrcode.make(user_website_address)

user_website_qr.save("user_website_qr.png")
user_website_qr.show()