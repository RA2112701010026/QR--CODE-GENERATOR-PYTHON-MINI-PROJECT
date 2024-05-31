import qrcode
#take upi id as a input 
upi_id=input("enter your UPI ID : " )
#upi id formate =  upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MASSAGE

phonepay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

phonepay_qr=qrcode.make(phonepay_url)
googlepay_qr=qrcode.make(googlepay_url)
paytmpay_qr=qrcode.make(paytm_url)

#saving qr code
phonepay_qr.save("phonepay_qr.png")
googlepay_qr.save("googlepay_qr.png")
paytmpay_qr.save("paytmpay_qr.png")

#displaying qr code 
phonepay_qr.show()
googlepay_qr.show()
paytmpay_qr.show()