# 전달값과 반환값

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
def withdraw_night(balance, money): # 저녁 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 튜플 형식 리턴

balance = 0 # 잔액
balance = deposit(balance, 1000) # 입금이 완료되었습니다. 잔액은 1000 원입니다.
# print(balance) # 1000
# balance = withdraw(balance, 2000) # 출금이 완료되지 않았습니다. 잔액은 1000 원입니다.
# balance = withdraw(balance, 500) # 출금이 완료되었습니다. 잔액은 500 원입니다.

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
# 수수료 100 원이며, 잔액은 400 원입니다.