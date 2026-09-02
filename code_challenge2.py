money = eval(input("Enter Money to Deposit ---->>>"))
print(type(money))
print("================================ PH BANK DENOMINATION ===========================")
print(" MONEY TO DEPOSIT --------> ", money, "php")

thousand = money // 1000
thousand_sukli = money % 1000

five_h = thousand_sukli // 500
five_h_sukli = thousand_sukli % 500

two_h = five_h_sukli // 200
two_h_sukli = five_h_sukli % 200

one_h = two_h_sukli // 100
one_h_sukli = two_h_sukli % 100

fifty = one_h_sukli // 50
fifty_sukli = one_h_sukli % 50

twenty = fifty_sukli // 20
twenty_sukli = fifty_sukli % 20

ten = twenty_sukli // 10
ten_sukli = twenty_sukli % 10

five = ten_sukli // 5
five_sukli = ten_sukli % 5

one = five_sukli // 1
one_sukli = five_sukli % 1

print()
print("\n\t1000-", thousand)
print("\t500-", five_h)
print("\t200", two_h)
print("\t100", one_h)
print("\t50-", fifty)
print("\t20", twenty)
print("\tten-", ten)
print("\t5-", five)
print("\t1-", one)
