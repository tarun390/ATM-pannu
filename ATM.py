class ATM(object):
    def __init__(self, users, atmCardNumber,phoneNumber ,pinNumber):
        self.users = users
        self.atmCardNumber = atmCardNumber
        self.phoneNumber = phoneNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self):
        print('₹1000.00')

    def balanceEnquiry(self):
        print('₹37643.52')

    def cashLIMIT(self):
        print("₹_10,000.00 only")

ATMinBank = ATM("unknown","7644_1346_234","996568536",600654)

ATMinBank.balanceEnquiry()