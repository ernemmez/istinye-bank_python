# Bu Proje Eren Emmez(Student -> 222016758) Tarafından Istinye Unv. BIL101 Dersi İçin Geliştirilmiştir.
import time

# DATABASE
user1Name = "Ahmet"
user1Password = "1234"
user2Name = "Zeynep"
user2Password = "4321"


def main():  # ana kapsayıcı func.
    def loginPage(numberOfAttempts, lastUser, lastUserBalance):  # Login Sayfası.

        def checkInputs():  # Giriş İşlemi
            username = input("Your Name:")
            password = input("Your Password:")

            if username == user1Name or username == user2Name:
                if password == user1Password or password == user2Password:
                    return username
                else:
                    print("Password or Username is wrong!")
                    return False
            else:
                print("Password or Username is wrong!")

        # Login Deneme Sayısı Döngüsü
        while numberOfAttempts < 4:
            print("\n-- Istinye Bank (v0.1)--")
            print("\nPlease Login Your Account")
            currentUser = checkInputs()
            if currentUser:
                # Son giriş yapan kullanıcı adı ile şuan giriş yapan kullanıcı aynı ise mainMenu'ye son giriş yapan kullanıcının son bakiyesini gönderir.
                mainMenu(currentUser, lastUserBalance if lastUser == currentUser else None)
                break
            else:
                numberOfAttempts += 1
                if numberOfAttempts >= 3:  # 3 kez hatalı giriş yapıldıysa bir süre sonra tekrar denememizi ister
                    print("You have entered incorrectly 3 times. Please try again later!")
                    break

    def logout(activeUser, userBalance):  # Çıkış İşlemi
        startApp(activeUser, userBalance)

    def getUserBalance(sessionBalance):  # Aktif Oturum Açmış kullanıcı bakiyesini döndürür.
        if sessionBalance is not None:
            return sessionBalance
        else:
            return 0

    def accountInfo(activeUser, userBalance):  # Hesap Bilgisini verir
        print("\n-- Istinye Bank (v0.1)--")
        # Formatlanmış tarih ve saatimizi yazdırır
        print(f"— {time.strftime('%Y-%m-%d %H:%M:%S')} —\n------------------------")
        if activeUser == "Ahmet":
            print(
                f"Your Name: {user1Name} \nYour Password: {user1Password}\nYour Amount: {userBalance}₺")
            input("Press Enter to back to main menu\n")
            mainMenu(activeUser, userBalance)
        elif activeUser == "Zeynep":
            print(
                f"Your Name: {user2Name} \nYour Password: {user2Password}\nYour Amount: {userBalance}₺")
            input("Press Enter to back to main menu\n")
            mainMenu(activeUser, userBalance)

    def depositMoney(activeUser, userBalance):  # Hesaba Para yüklememizi sağlar
        amountDeposit = int(input("Please enter the amount you want to drop: "))
        if amountDeposit:
            print(f"{amountDeposit}₺ withdrawn from your account\nGoing back to main menu...\n")
            mainMenu(activeUser,
                     userBalance + amountDeposit)  # Ana sayfayı render eder ve ana sayfaya son bakiyeyi gönderir.

    def withdrawMoney(activeUser, userBalance):  # Hesaptan para çekmemizi sağlar
        amountWithdraw = int(input("Please enter the amount you want to withdraw: "))

        if amountWithdraw > userBalance:
            print(f"You don’t have {amountWithdraw}₺ in your account\nGoing back to main menu...\n")
            mainMenu(activeUser, None)
        else:
            print(f"{amountWithdraw}₺ withdrawn from your account\nGoing back to main menu...\n")
            mainMenu(activeUser, userBalance - amountWithdraw)

    def transferMoney(activeUser, userBalance): # Para transferi yapmamızı sağlar
        amountTransfer = int(input("Please enter the amount you want to transfer: "))

        if amountTransfer > userBalance:
            print("Sorry! You don’t have enough money to complete this transaction")
        else:
            result = userBalance - amountTransfer
            print(f"\nYour transfer transaction worth {amountTransfer}₺ has been completed successfully.")
            print("1. Go back to main menu \n2. Transfer again")
            choice = input("Please select choice:")

            if choice == "1":
                mainMenu(activeUser, result)
            elif choice == "2":
                transferMoney(activeUser, result)

    # Ana menüyü render eder sayfa routelarını yapar, aktif kullanıcı ve bakiyesini tutar.
    def mainMenu(activeUser, sessionBalance):
        print("\n-- Istinye Bank (v0.1)--\n")
        print(f"Welcome {activeUser}!")
        print("1. Withdraw Money \n2. Deposit Money \n3. Transfer Money \n4. My Account Information \n5. Logout ")
        choice = input("Please select choice:")
        if choice == "1":
            print("-Withdraw Money-")
            withdrawMoney(activeUser, getUserBalance(sessionBalance))
        elif choice == "2":
            print("-Deposit Money-")
            depositMoney(activeUser, getUserBalance(sessionBalance))
        elif choice == "3":
            print("Transfer Money")
            transferMoney(activeUser, getUserBalance(sessionBalance))
        elif choice == "4":
            accountInfo(activeUser, getUserBalance(sessionBalance))
        elif choice == "5":
            logout(activeUser, getUserBalance(sessionBalance))

    def startApp(lastUser, last_User_Balance):  # Banka programımızı çalıştırır.

        print("\n-- Welcome To Istinye Bank (v0.1)--\n")
        print('Please Select the Action You Want to Perform (Example: "1")')
        print("1. Login \n2. Exit App")
        choice = input("Please select choice:")

        if choice == "1":
            loginPage(0, lastUser, last_User_Balance)

    startApp(None, 0)
    # 1. parametre: Son giriş yapan kullanıcıyı temsil eder. İlk kez çalıştırıldığı durumda son giriş yapan kullanıcı olmadığı için None verildi.
    # 2. parametre = Son giriş yapan kullanıcının bakiyesini temsil eder. İlk kez çalıştırıldığı durumda son giriş yapan kullanıcı olmadığı için 0 verildi.


main()