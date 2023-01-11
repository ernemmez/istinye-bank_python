import time
import enum


class activicionKind(enum.Enum):
    deposite = 2
    withdrawals = 3
    transfersEtc = 4


class processMember(enum.Enum):
    time = 1
    total = 2
    to = 3


class activicion:
    def __init__(self, username, password, activicionKind, Info):
        self.userN = username
        self.passW = password
        self.kind = activicionKind
        self.Info = Info


musteriBir = ["Ahmet", 1234, 90]

musteriIki = ["Zeynep", 4321, 15]

musteriUc = ["Antonio", 4422, 80]

setMoney = 0
select = 0
onlineCustomer = ''
activicionList = []

userName = ''
password = 0


def GetTime():
    return f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}  {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}'


def Logging(_activicion):
    activicionList.append(_activicion)
    # and if you want write some io library code


# def GetLogsTwo(actKind, actList, user, passW):
#     for act in list(actList):
#         if act.kind == actKind and act.userN == user and act.passW == passW:
#             match act.kind.name:
#                 case activicionKind.transfersEtc.name:
#                     print(f'Time Person Amount:\n   {list(act.Info.values())[0]} Transferred to {list(act.Info.values())[2]} {list(act.Info.values())[1]} TL')
#                     break
#                 case activicionKind.withdrawals.name:
#                     print(f'{list(act.Info.values())[0]} {list(act.Info.values())[1]} TL')
#                     break
#                 case activicionKind.deposite.name:
#                     print(f'{list(act.Info.values())[0]} {list(act.Info.values())[1]} TL')
#                     break
#     for act in list(actList):
#         if act.kind == actKind and list(act.Info.values())[2] == user and act.passW == passW:
#             print(f'Time Person Amount:\n   {list(act.Info.values())[0]} Transferred to from me {act.userN} {list(act.Info.values())[1]} TL')

def GetTransferLogs(eachLog, toWho):
    if toWho == 'sender':
        print(f'{list(eachLog.Info.values())[0]} transferred to {list(eachLog.Info.values())[2]} {list(eachLog.Info.values())[1]}')
    elif toWho == 'receiver':
        print(f'{list(eachLog.Info.values())[0]} transferred to me from {eachLog.userN} {list(eachLog.Info.values())[1]}')
    else:
        print('Log source is exists')

def GetWithdrawalOrDepositeLogs(eachLog):
    print(f'{list(eachLog.Info.values())[0]}  {list(eachLog.Info.values())[1]}')


#
def GetLogs(actKind, actList, user, passW):

    if actKind == activicionKind.transfersEtc.name:
        for act in list(actList):
            if act.kind.name == activicionKind.transfersEtc.name and act.userN == user and act.passW == passW:
                GetTransferLogs(act, 'sender')
        for act in list(actList):
            if act.kind.name == activicionKind.transfersEtc.name and list(act.Info.values())[2] == user:
                GetTransferLogs(act, 'receiver')

    elif actKind == activicionKind.withdrawals.name:
        for act in list(actList):
            if act.kind.name == activicionKind.withdrawals.name and act.userN == user and act.passW == passW:
                GetWithdrawalOrDepositeLogs(act)

    elif actKind == activicionKind.deposite.name:
        for act in list(actList):
            if act.kind.name == activicionKind.deposite.name and act.userN == user and act.passW == passW:
                GetWithdrawalOrDepositeLogs(act)
    else:
        print('Log source is exists')


#def GetLogs(actList, user, passW):
#    for act in list(actList):
#        if act.userN == user and act.passW == passW:
#            print('User Activities Report:\n')
#            if act.kind.name == activicionKind.withdrawals.name or act.kind.name == activicionKind.deposite:
#                if act.kind.name == activicionKind.withdrawals.name:
#                    print(f'Your Withdrawals:\n{list(act.Info.values())[0]} {list(act.Info.values())[1]} TL')
#                else:
#                    print(f'Your Deposits:\n{list(act.Info.values())[0]} {list(act.Info.values())[1]} TL')
#            elif act.kind.name == activicionKind.transfersEtc.name:
#                print(f'Your Transfers:\n   Time Person Amount:\n   {list(act.Info.values())[0]} Transferred to {list(act.Info.values())[2]} {list(act.Info.values())[1]} TL')
#        elif list(act.Info.values())[2] == user and act.passW == passW:
#            print('User Activities Report:\n')
#            if act.kind.name == activicionKind.transfersEtc.name:
#                print(f'Your Transfers:\n   Time Person Amount:\n   {list(act.Info.values())[0]} Transferred to me from {list(act.userN)} {list(act.Info.values())[1]} TL')




def Process(_activicion):

    Logging(_activicion)
    sender = getOnlineCustomer(_activicion.userN)
    if len(list(_activicion.Info.values())) == 3:
        receiver = getOnlineCustomer(list(_activicion.Info.values())[2])
    amount = list(_activicion.Info.values())[1]


    if _activicion.kind.name == activicionKind.withdrawals.name:
        sender[2] -= amount
    elif _activicion.kind.name == activicionKind.deposite.name:
        sender[2] += amount
    elif _activicion.kind.name == activicionKind.transfersEtc.name:
        sender[2] -= amount
        receiver[2] += amount
    else:
        print('An error occurred while logging')





def getOnlineCustomer(cus):
    if musteriBir[0] == cus:
        return musteriBir
    elif musteriIki[0] == cus:
        return musteriIki
    elif musteriUc[0] == cus:
        return musteriUc


def getOnlineCustomerMoney(cus):
    if musteriBir[0] == cus:
        return int(musteriBir[2])
    elif musteriIki[0] == cus:
        return int(musteriIki[2])
    elif musteriUc[0] == cus:
        return int(musteriUc[2])


def Draw(cus):
    drawMoney = int(input('Please enter the amount you want to withdraw:'))
    if drawMoney <= getOnlineCustomerMoney(userName):
        activicionDraw = activicion(cus, getOnlineCustomer(cus)[1], activicionKind.withdrawals, {processMember.time: GetTime(), processMember.total: drawMoney})
        Process(activicionDraw)
        setMoney = 0
        print(f'{drawMoney} TL withdrawn from your account\nGoing back to main menu...')
        return True
    else:
        print(f'You don’t have {drawMoney} TL in your account\nGoing back to main menu...')
        return False


def DepositeMoney(cus):
    amountMoney = int(input('Please enter the amount you want to drop:'))

    activicionAmount = activicion(cus, getOnlineCustomer(cus)[1], activicionKind.deposite, {processMember.time: GetTime(), processMember.total: amountMoney})
    Process(activicionAmount)
    setMoney = 0
    print(f'{amountMoney} TL added to your account\nGoing back to main menu...')


def TransferEtc(cus):
    FromCus = getOnlineCustomer(cus)[0]
    ToCus = input('Warning: If you want to abort the transfer please enter abort\nPlease enter the name of the user you want transfer money to: ')

    if ToCus != 'abort':
        if FromCus != ToCus and (ToCus == musteriBir[0] or ToCus == musteriIki[0] or ToCus == musteriUc[0]):
            transferMoney = int(input('Please enter the amount you want to transfer:'))
            if transferMoney < getOnlineCustomerMoney(FromCus):
                activicionTranferEtc = activicion(FromCus, getOnlineCustomer(FromCus)[1], activicionKind.transfersEtc, {processMember.time: GetTime(), processMember.total: transferMoney, processMember.to: ToCus})
                Process(activicionTranferEtc)
                print('Money transferred successfully\nGoing back to main menu')
                return True
            else:
                print('Sorry! You don’t have enough money to complete this transaction. \n \n \n \n 1. Go back to main menu \n 2. Transfer again')
                return False
        else:
            print('User does not exist!')
            if TransferEtc(cus):
                return True
            else:
                return False
    else:
        print('Going back to main menu...')
        return True


def GetLocalTimeAndBankName():
    return print(f'   ----WELKOME TO ISTINYE BANK----\n        ------------------\n      /      ISTANBUL      \ \n     |  {GetTime()}  | \n      \                    /\n        ------------------')




def main():
    try:
        dongu = 1
        while dongu > 0:
            GetLocalTimeAndBankName()
            print('1.Login\n2.Exit')
            select = int(input())
            if select == 1:
                dongu += 1
                while dongu > 1:
                    print('What do you want login as:\n1.Admin\n2.User\n3.Go back')
                    select = int(input())
                    if select == 1:
                        print('yazılacak')
                    elif select == 2:
                        dongu += 1
                        while dongu > 2:
                            userName = input('User Name')
                            password = int(input('Password'))
                            if (userName == musteriBir[0] and password == musteriBir[1]) or (userName == musteriIki[0] and password == musteriIki[1]) or (userName == musteriUc[0] and password == musteriUc[1]):
                                dongu += 1
                                while dongu > 3:
                                    print(f'\nWelcome {userName}!\nPlease enter the number of the service:\n1.Withdraw Money\n2.Deposit Money\n3.Transfer Money\n4.My Account Information\n5.Logout')
                                    select = int(input())
                                    match select:
                                        case 1:
                                            dongu += 1
                                            while dongu > 4:
                                                Draw(userName)
                                                dongu -= 1
                                        case 2:
                                            dongu += 1
                                            while dongu > 4:
                                                DepositeMoney(userName)
                                                dongu -= 1
                                        case 3:
                                            dongu += 1
                                            while dongu > 4:
                                                transferResult = TransferEtc(userName)
                                                if transferResult:
                                                    dongu -= 1
                                                else:
                                                    select = int(input())
                                                    if select == 1:
                                                        print('Going back to main menu...')
                                                        dongu -= 1
                                                    elif select == 2:
                                                        pass
                                                    else:
                                                        print('please choose one of the options')
                                        case 4:
                                            GetLocalTimeAndBankName()
                                            print(
                                                f'Your Name: {userName}\nYour Password: {password}\nYour Amount(TL): {getOnlineCustomerMoney(userName)}')
                                            print('User Activities Report:\nYour Withdrawals:\n')
                                            GetLogs(activicionKind.withdrawals.name, activicionList, userName, password)
                                            print('Your Deposites:\n')
                                            GetLogs(activicionKind.deposite.name, activicionList, userName, password)
                                            print('Your TransferEtc:\nTime Person Amount\n')
                                            GetLogs(activicionKind.transfersEtc.name, activicionList, userName, password)
                                        case 5:
                                            dongu -= 2
                                        case _:
                                            print('please choose one of the options')
                                else:
                                    print('please choose one of the options')
                            else:
                                print('username or password is incorrect')
                    elif select == 3:
                        dongu -= 1
                    else:
                        print('please choose one of the options')
            elif select == 2:
                print('By By')
                dongu = 0

            else:
                print('please choose one of the options')
    except:
        print('Something went wrong, please try again')
        main()


main()
