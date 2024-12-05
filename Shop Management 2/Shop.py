import os
import random
import pickle
import datetime

File = "Staffs.dat "
FILESTOCK = "Stock.dat"
filecash = "Cashier.dat"



def genidstaff(n=100000):
    while True:
        yield n + 1
def ct(n=10000):
    while True:
        yield n+1


class staff:
    count_staff = 0

    def __init__(self,fulln = "",  name="", sur="", staffID="", marriage="", sex="", age=0, dob=0, fatname="", tel=""
                 ,sal =0):
        self.staff_fullname = fulln
        self.staff_name = name
        self.staff_surname = sur
        self.staff_id = staffID
        self.staff_state = marriage
        self.staff_sex = sex
        self.staff_age = age
        self.staff_dob = dob
        self.staff_fther = fatname
        self.staff_tel = tel
        self.staff_sal = sal
        staff.count_staff += 0

    def idStaff(self):
        while True:
            s = "S"
            fh = open(r"Idgenstaff.txt", 'a+')
            ft = open(r"tempkeystaff.txt", 'a+')
            fl = open("staffid.log", 'a+')
            g = fh.read()
            sd = int(g)
            fh.close()
            cts = genidstaff(sd)
            a = next(cts)
            fl.write("\n" + str(a))
            ft.write(str(a))
            fl.close()
            ft.close()
            code = s + str(a)
            self.staff_id = code
            print (self.staff_id)
            os.remove("Idgenstaff.txt")
            os.rename("tempkeystaff.txt", "Idgenstaff.txt")
            break

    def stateStaff(self):
        print ("Enter marrital state\n1.Single\n2.Married")
        self.staff_state = input(":")
        if self.staff_state == "1":
            self.staff_state = "Single"
        elif self.staff_state == "2":
            self.staff_state = "Married"

    def dobStaff(self):
        self.staff_age = int(input("Enter age:"))
        a = input("Enter date of birth [must be two digits]:")
        b = input("Enter month of birth [must be two digits]:")
        c = input("Enter year:")
        self.staff_dob = a + "/" + b + "/" + c

    def sexStaff(self):
        print ("Enter sex\n1.Man\n2.Woman")
        opt = input(":")
        if opt == "1":
            self.staff_sex = "Man"
        elif opt == "2":
            self.staff_sex = "Woman"
        self.staff_fther = input("Enter father's name:")
        self.staff_tel = input("Enter telephone no:")

    def surStaff(self):
        sn = input("Enter surname of staff \n:")
        self.staff_surname = sn.capitalize()

    def nameStaff(self):
        nn = input("Enter name of staff[Only name] \n:")
        self.staff_name = nn.capitalize()
    def fullnStaff(self):
        staff.nameStaff(self)
        staff.surStaff(self)
        self.staff_fullname = self.staff_name + "/t" + self.staff_surname



    # ADDING_STAFF
    # BY USING VARIOUS OF USER DEFINED FUNCTIONb
    def addStaff(self):
        print("\t\t\tAdd Staff")
        staff.fullnStaff(self)
        staff.idStaff(self)
        staff.stateStaff(self)
        staff.dobStaff(self)
        staff.sexStaff(self)
        staff.count_staff += 1

    def showdetail(self):
        print ("\t\tDetail System")
        print (10 * "\t\t*")
        print ("\t\t\tBio-Data")
        print ("Staff_ID:", self.staff_id, "\nName:", self.staff_name, "\n", self.staff_surname)
        print ("Marriage state:", self.staff_state, "Sex:", self.staff_sex)
        print ("DOB:", self.staff_dob, "\nFather's name:", self.staff_fther, "\nTel:", self.staff_tel)

class Stock:
    """Class Stock is for Stock Management in 
    The project Super groceries Shop of Sireethon and Tanuj
    This is for study purpose only
    """
    def __init__(self, iname= "",ids ="",quantity=0,brand = "",maincat ="",categories ="",man="",exp="",weight=0,date="",priceT =0,priceNT =0 ):
        self.item_name = iname
        self.item_category = categories
        self.item_maincategory = maincat
        self.item_id = ids
        self.item_expdate = exp
        self.item_qty = quantity
        self.item_brand = brand
        self.item_weight = weight
        self.item_datetime = date
        self.item_manudate = man
        self.weight = weight #in gram , in Kg ,in litre(cold drink)
        self.item_priceT = priceT
        self.item_priceNT = priceNT

    def category(self):
        print ("\t\t\t\tCategories\n***Press any of the following number to action***")
        print ("1.Food&Beverage\n2.Furnitures and Wares\n3.Electronic\n4.Health and Medicine")
        n = int(input("Enter choice[1-5]"))
        if n == 1:#For food type
            print ("Press '1' for Food\nPress '2' for Beverage")
            n = int(input())
            if n == 1:#REal food
                self.item_maincategory = "Food"
                print ("\t\t----------Type of Food----------")
                print ("1.Fruits\n2.Vegetables\n3.Grain\n4.Dairy ")
                print ("Enter ")
                n = int(input("Enter Type of Food from the above[1-4]:"))
                if n == 1:
                    self.item_category = "Fruit"
                elif n == 2:
                    self.item_category = "Vegetable"
                elif n == 3:
                    self.item_category = "Grain"
                elif n == 4:
                    self.item_category = "Dairy Product"

            elif n == 2:#Beverage Type
                self.item_maincategory = "Beverage"
                print ("\t\t----------Type pf Beverage----------")
                print ("1.Liquor\n2.Cold drink\n3.Juice")
                n = int(input("Enter Type of Beverage[1-3]:"))
                if n == 1:
                    self.item_category = "Liquor"
                if n == 2:
                    self.item_category = "Cold drink"
                if n == 3:
                    self.item_category = "Juice"




        elif n== 2:#Furniture and Wares Type
            self.item_maincategory = "Furniture and Wares"
            print ("\t\t----------Type of Furniture and Wares----------")
            print ("1.Kitchen\n2.Bedroom\n3.Bathroom\n4.Living room\n5.Outside")
            print ("Enter type of furniture[1-5]:")

            n = int(input())
            if n == 1:
                self.item_category = "Kitchen"
            elif n == 2:
                self.item_category = "Bedroom"
            elif n == 3:
                self.item_category = "Bathroom"
            elif n == 4:
                self.item_category = "Living room"
            elif n == 5:
                self.item_category = "Outside"
            else:
                print ("Wrong choice")
                print ("Try again")

        # Choice 3
        # Electrocic
        # Sireethon

        elif n == 3:
            self.item_maincategory = "Electronic"
            print ("\t\t----------Type of Electronic----------")
            print ("1.Kitchen\n2.Bedroom\n3.Bathroom\n4.Living room\n5.Outside\n6.Others")
            print ("Enter type of Electronics[1-6]:")
            n = int(input())
            if n == 1:
                self.item_category = "Kitchen"
            elif n == 2:
                self.item_category = "Bedroom"
            elif n == 3:
                self.item_category = "Bathroom"
            elif n == 4:
                self.item_category = "Living room"
            elif n == 5:
                self.item_category = "Outside"
            elif n == 6:
                self.item_category = "Others"
            else:
                print ("Wrong choice")
                print ("Try again")

        # Health and Medicine
        # In type of cosmetic things

        elif n == 4:
            self.item_maincategory = "H&M"
            print ("\t\t----------Type of Health and Medicines----------")
            print ("1.Cosmetic\n2.Skin threatment\n3.Medicine\n4.Hair threat")
            print ("Enter type of health and medicine[1-4]")
            n = int(input())
            if n == 1:
                self.item_category = "Cosmetic"
            elif n == 2:
                self.item_category = "Skin"
            elif n == 3:
                self.item_category = "Med"
            elif n == 4:
                self.item_category = "Hair"
            else:
                print ("Wrong choice\nPlease try again")

    def stock_idgen(self):
        frt = ""   # AKA Front Code
        bck = ""   # AKA Back Code
        while True:
            Stock.category(self)
            if self.item_maincategory == "Food":
                frt = "F"

                if self.item_category == "Fruit":
                    bck = "FR"                    #Fruits

                elif self.item_category == "Vegetable":
                    bck = "VG"                    #VEGETABLEs

                elif self.item_category == "Grain":
                    bck = "GR"                    #Grains

                elif self.item_category == "Dairy Product":
                    bck = "DP"

            #Beverage Type
            #START

            elif self.item_maincategory == "Beverage":
                frt = "B"
                if self.item_category == "Liquor":
                    bck = "LQ"

                elif self.item_category == "Cold drink":
                    bck = "CD"

                elif self.item_category == "Juice":
                    bck = "JC"
            # Furniture
            # START
            elif self.item_maincategory == "Furniture and Wares":
                frt = "F"
                if self.item_category == "Kitchen":
                    bck = "K"

                elif self.item_category == "Bedroom":
                    bck = "BD"

                elif self.item_category == "Bathroom":
                    bck = "BH"

                elif self.item_category == "Living room":
                    bck = "LV"

                elif self.item_category == "Outside":
                    bck = "OS"
            elif self.item_maincategory == "Electronic":
                frt = "E"
                if self.item_category == "Kitchen":
                    bck = "K"

                elif self.item_category == "Bedroom":
                    bck = "BD"

                elif self.item_category == "Bathroom":
                    bck = "BH"

                elif self.item_category == "Living room":
                    bck = "LV"

                elif self.item_category == "Outside":
                    bck = "OS"
            elif self.item_maincategory == "H&M":
                frt = "HM"
                if self.item_category == "Cosmetic":
                    bck = "CS"

                elif self.item_category == "Skin":
                    bck = "SK"

                elif self.item_category == "Med":
                    bck = "MD"

                elif self.item_category == "Hair":
                    bck = "HR"
            fh = open(r" Idgengens.txt ", 'a+')
            ft = open(r" tempkey.txt ", 'a+')
            g = fh.read()

            sd = int(g)
            fh.close()
            cts = ct(sd)
            a = next(cts)
            ft.write(str(a))
            ft.close()
            code = frt + str(a) + bck
            self.item_id = code
            print (self.item_id)
            os.remove("Idgengens.txt")
            os.rename("tempkey.txt","Idgengens.txt")
            break


    def stock_price(self):
        tax = 0.18
        profit = 0.5 #percent
        while True:
            try:
                ipp = int(input("Insert principal price:"))

                price = ipp + ( ipp // profit )
                p = price + ( price * tax )
                self.item_priceT = p
                self.item_priceNT = price
                break
            except TypeError:
                print ("Type error\nPlease Enter No. Type!!")
                continue
    def stock_expdnf(self):
        while True:
            try:
                print ("Enter Manufacturer date by the format dd/mm/yyyy")
                datef = input("Enter date:")
                monthf = input("Enter month")
                yearf = input("Enter year:")
                self.item_manudate = datef + "/" + monthf + "/" + yearf
                print ("Enter Expire date by the format dd/mm/yyyy")
                datee = input("Enter expire date:")
                monthe = input("Enter month:")
                yeare = input("Enter year")
                self.item_expdate = datee + "/" + monthe + "/" + yeare
                break
            except TypeError:
                print ("Type error")

    def stock_additem(self):
        itt = input("Enter item's name:")
        self.item_name = itt.capitalize()
        itb = input("Enter item's brand")
        self.item_brand = itb.upper()
        Stock.stock_idgen(self)
        Stock.stock_price(self)
        self.item_qty = int(input("Enter quantity to be added:"))
        weight = int(input("Enter weight in gram"))
        self.item_weight = str(weight) + "\tgram"
        now = datetime.datetime.now()
        self.item_datetime = now.strftime("%d-%m-%Y  Time:%H:%M  Day:%A")

    def stock_showitem(self):
        print (20 * "-" + "STOCK_MANAGEMENT_SYSTEM" + 20 * "-")
        print (20 * "*" + "Detail of Item" + 20 * "*")
        print ("Item name:", self.item_name)
        print ("ID NO:", self.item_id)
        print ("Brand:", self.item_brand)
        print ("Category:", self.item_maincategory,"-",self.item_category)
        print ("Weight:", self.item_weight)
        print ("Quantity left:", self.item_qty)
        print ("Last Modification on:", self.item_datetime)



class Cashier(staff,Stock):
    cus_counter = 0

    def __init__(self, cashname="", cashstate="", cashier="", block="", cashprofit=0
                 , cashtotal=0, cashtax=0, timelogin="", timelogout="", timeitem="",staffID="",name="",sur="",fulln=""
                 ,iname = "",quantity = 0,sold = 0,itemsold = ""):
        staff.__init__(self ,name,sur,fulln,staffID)
        Stock.__init__(self,iname,quantity)
        self.cash_name = cashname
        self.cash_cashier = cashier
        self.cash_state = cashstate
        self.cash_block = block
        self.cash_profit = cashprofit
        self.cash_total = cashtotal
        self.cash_tax = cashtax
        self.cash_login = timelogin
        self.cash_logout = timelogout
        self.cash_timeitem = timeitem
        self.cash_sold = sold
        self.cash_fulln = fulln
        self.cash_itemsold = itemsold
        Cashier.cus_counter += 0

    def cashier_block(self):
        while True:
            print ("Cashire block from [A-E]")
            print ("Enter 1-5 to operate")
            print ("1.A\n2.B\n3.C\n4.D\n5.E")
            alpha = []
            for blocks in range(65,70):
                alpha.append(chr(blocks))
            ipb = int(input())
            if ipb == 1:
                self.cash_block = alpha[0]
            elif ipb == 2:
                self.cash_block = alpha[1]
            elif ipb == 3:
                self.cash_block = alpha[2]
            elif ipb == 4:
                self.cash_block = alpha[3]
            elif ipb == 5:
                self.cash_block = alpha[4]
            else:
                print ("Wrong choice")
            break



    
def cashier_state(self):
        print ("Cashier State")
        print ("Select state of cashier")
        print ("1.Online\n2.Offline")
        while True:
            try:
                n = int(input("Enter [1-2]:"))
                if n == 1:
                    self.cash_state = "Online"

                elif n == 2:
                    self.cash_state = "Offline"
                break
            except TypeError:
                print ("Type error please enter only No.")
                continue
        def cashier_assign(self):
            print ("Assign worker for block -->",self.cash_block)
            self.fullnStaff()

        def cashier_profit(self):
            self.cash_profit = 0
        def cashier_total(self):
            self.cash_total = 0
            self.cash_sold = 0
        def cashier_itemsold(self):
            self.cash_itemsold = ""



        def cashier_add(self):
            Cashier.cashier_block(self)
            Cashier.cashier_assign(self)
            Cashier.cashier_state(self)
            Cashier.cashier_profit(self)
            Cashier.cashier_total(self)
            Cashier.cashier_total(self)
            Cashier.cashier_itemsold(self)

        def cashier_sold(self):
            fc = open(filecash, "ab+")
            fo = open('FILESTOCK.dat', 'ab+')
            ft = open('temptempsold.dat', 'ab+')
            fl = open('cashier log.dat', 'ab+')
            isold = input("Enter item name:")
            ib = pickle.load(fo)
            if isold == ib.item_name:
                print ("Price:",ib.item_priceT)

        def cashier_login(self):
            print ("Successfully log in")
            print ("At",datetime.datetime.now())

        def cashier_logout(self):
            print ("Successfully log out")
            print ("Time:",datetime.datetime.now())

        def cashier_show(self):
            print ("Block:",self.cash_block)
            print ("Name of Cashier:",self.cash_fulln)
            print ("Item sold:",self.cash_sold)
            print ("Total sold:",self.cash_total)
            print ("Total tax:",self.cash_tax)
            print ("Total profit:",self.cash_profit)

#Cashier----------------------------------------------------------------------------------------------------------------
def cashier_sold(bk):
    if not os.path.isfile('FILESTOCK'):
        print ("File is not exist")
    else:
        fc = open(filecash,"ab+")
        fct = open("tempcash.dat","ab+")
        fo = open('FILESTOCK.dat','ab+')
        ft = open('temptempsold.dat','ab+')
        fl = open('cashier log.dat','ab+')
        isold = input("Enter Item's name to be sold")
        fg = 0
        try:
            it = Stock()
            it = pickle.load(fo)
            ic = Cashier()
            ch = "Y"
            while bk == ic.cash_block:
                while ch == "Y":
                    if it.item_name == isold:
                        q = int(input("quantity to be sold:"))
                        qq = it.item_qty
                        remain = qq - q
                        it.item_qty = remain
                        pickle.dump(it,ft)
                        d = datetime.datetime.now()
                        log = isold,"is sold item remained >>",remain,"\nat",d
                        pickle.dump(log,fl)
                        #For dump to cashier file
                        ic.cash_itemsold = isold
                        ic.cash_total += it.item_priceT
                        ic.cash_tax += ic.cash_total * 0.18
                        pickle.dump(ic,fct)

                        ch = input("Do u want to sell more item[Y/N]:")
                        ch.upper()
                        if ch =="Y":
                            continue
                        else:
                            break

                    else:
                        print (isold,"is not exist")
        except EOFError:
            pass
        fo.close()
        ft.close()
        fl.close()
        fct.close()
        fc.close()
        os.remove(filecash)
        os.rename("tempcash.dat",filecash)
        os.remove('FILESTOCK.dat')
        os.rename('temptempsold.dat','FILESTOCK.dat')

def check_autho(b):
    fo = open(filecash, 'ab+')
    fl = open("cashlog.dat", "ab+")
    print ("Welcome to Cashier")
    print ("Please Enter name and Password")
    pickle.load(fo)
    name = input("Enter name:")
    sur = input("Enter surname:")
    full = name + "\t" + sur
    pwd = "Enter password to proceed:"
    ic = Cashier()
    if full == ic.cash_fulln:
        if pwd == "admin":
            print ("Welcome",full,"\nBlock",b)
            ic.cashier_login()
            pickle.dump(ic,fl)

        else:
            print ("Invalid password please try again")


    else:
        "Invalid Username"
    fo.close()
    fl.close()


def cashier_remove(n=""):

    sobj = open(filecash, 'ab+')
    tempoj = open("tempobj.dat", 'ab+')
    nsc = input("Enter cashier[A-E]:")
    nsc.upper()
    fg = 0
    try:
        while True:
            it = Cashier()
            it = pickle.load(sobj)
            if it.cash_block != nsc:
                pickle.dump(it, sobj)
                fg = 1
                print ("Cashier block",n,"is deleted")
            elif fg == 0:
                print ("Block is not found")
    except EOFError:
        pass
    sobj.close()
    tempoj.close()
    os.remove(filecash)
    os.rename("tempobj.dat", filecash)


def cashier_start():
    if not os.path.isfile(filecash):
        print ("File is not exist")
    else:
        fo = open(filecash,'ab+')
        ft = open("temptemp.dat","a+")
        fl = open("cashlog.dat","ab+")
        chc = int(input("Enter choice to proceed:"))
        itemm = 0
        print ("1.Cashier adding\n2.Selling system\n3.State of cashier")
        try:
            ic = Cashier()
            if chc == 1:
                ic.cashier_add()
                pickle.dump(ic,fo)

                print ("Added Cashier")
            elif chc == 2:
                print (20 * "-" + "Selling System" + 20 * "-")
                print (45 * "-")
                pickle.load(fo)
                bk = input("Enter block[A-E]:")
                bk.upper()
                if bk == ic.cash_block:
                    if check_autho(bk):
                        cashier_sold()
                else:

                    print ("Invalid Block")

            elif chc == 3:
                print ("Cashier Status")
                ch = input("Enter Cashiere[A-E]")
                ch.capitalize()
                if ch == ic.cash_block :
                    pickle.load(fo)
                    ic.cashier_show()
                else:
                    print ("No block")
        except EOFError:
            pass


        fo.close()
        ft.close()
        fl.close()
#-----------------------------------------------------------------------------------------------------------------
#Staff------------------------------------------------------------------------------------------------------------
def check_file():
    if not os.path.isfile(File):
        print (File, "Does not exist")

def staff_add(n):
    if not (os.path.isfile(File)):
        print (File, "Does not exist")

    else:
        a = input("Continue to Staff adding?:")
        sobk = open(File, "ab+")
        while True:
            if a == "Y":
               try:

                    it = staff()
                    it.addStaff()
                    pickle.dump(it,sobk)
                    k = input("Do u want to show the data of employee[y/n]:")
                    k = k.upper()
                    sobk.close()
                    if k == "Y":
                        sobk = open(File, "rb+")
                        pickle.load(sobk)
                        it.showdetail()
                        a = input("Do u want to add more staff[y/n]:")
                        a = a.upper()
                        if a == "Y":
                            continue
                        else:
                            break
                    else:
                        break

               except EOFError:

                  pass

            sobk.close()



def staff_search():
    if not (os.path.isfile(File)):
        print (File, "Does not exist")

    else:
        sobk = open(File, "rb")
        staff_name = input("Enter staff name to be searchrd")
        try:
            fg = 0

            while True:
                it = pickle.load(sobk)
                staffN = it.name
                if staffN == staff_name:
                    print ("Staff is found")
                    it.showdetail()
                    fg = 1
                    break
                elif fg == 0:
                    print (staff_name, "Not found")
        except EOFError:
            pass

        sobk.close()


# item update
def staff_update():
    if check_file():
        print ("Try again")
    else:
        sobj = open(File, "rb")
        tempobj = open("tempstaffs.dat", "wb")
        nama = input("Enter staff name to be update")
        fg = 0
        try:
            it = staff()
            it = pickle.load(sobj)
            if it.name == nama:
                print ("\t\t\t\tStaff Detail")
                it.showdetail()
                it.addStaff()
                pickle.dump(it, tempobj)
                fg = 1
            else:
                pickle.dump(it, tempobj)
        except EOFError:
            pass
        if fg == 0:
            print ("Staff is not found"), nama
        tempobj.close()
        sobj.close()
        os.remove("Staffs.dat")
        os.rename("tempstaffs.dat", "Staffs.dat")


def staff_delete():
    if check_file():
        print ("Try again")
    else:
        sobj = open(File, 'rb')
        tempoj = open("tempobj.dat", 'ab+')
        nsc = input("Enter name/ID of the employee")
        s = nsc
        fg = 0
        try:
            while True:
                it = staff()
                it = pickle.load(sobj)
                if it.staff_id != s:
                    pickle.dump(it, sobj)
                    fg = 1
                    print ("Staff os deleted")
                elif fg == 0:
                    print ("ID is not found")
        except EOFError:
            pass
        sobj.close()
        tempoj.close()
        os.remove(File)
        os.rename("tempobj.dat", File)

#-----------------------------------------------------------------------------------------------------------------------

#Main
def cash_addrev():
    print (10 * "_" + "Cashier Management System" + "_" * 10)
    print (40 * "*")
    print (20 * "-" + "Add or Remove Cashier" + "-" *20)
def cash_ass():
    print (10 * "_" + "Cashier Management System" + "_" * 10)
    print (40 * "*")
    print ("Cashier Assign")


def cash_state():
    print (10* "_" + "Cashier Management System" + "_" * 10)
    print (40 * "*")
    print (20 * "-" + "Cashier Status" + "-" * 20)
def cashier():
    print (10* "_" + "Cashier Management System" + "_" * 10)
    print (40 * "*")
    print ("1).Cashier's Status\n2).Assign Cashierer\n3.Add/remove cashier\n4).Back to Main Menu)")

# State---------------------------------------------------------------------------------------------
def summary():
    print("SUMMARY")
    print(20 * "*")

def State_Moutcome():
    print("Monthly Outcome")
    print(20 * "*")
    print(20 * "_" + "STATEMENT" + 20 * "_")
    print(20 * "*")
    print(20 * "-" + "OVERALL PROFIT" + 20 * "-")



def State():  # In-Main Menu 3rd choice
    print(10 * "_" + 10 * "[" + "STATEMENT" + 10 * "]" + 10 * "_")
    print(20 * "*")
    print("1).Overall Profit\n2).Monthly outcome\n3).Summary\nB).Back to Main Menu")



# State----------------------------------------------------------------------------------------------
# Store----------------------------------------------------------------------------------------------
def Stock():
    print("Stock Checking")
    print(20 * "*")
    print("1).State of Stock\n2).Lastest sold\n3).Lastest stored items\nA).Back to Store Management\nB).Back to Main Menu")


def detail_item():
    print("Enter the item's name to see detail")
    print(20 * "*")


def detail_storemag():
    print("\t\t\tDetail_sub_Menu")
    print(20 * "*")
    print("1).Select item(s)\nA).Back to Store Management\nB).Back to Main Menu")
    print(20 * "*")


def storemag():  # In-Main Menu 2nd choice
    print("\t\t\tSTORE MANAGEMENT")
    print(20 * "*")
    print("1).Add/Remove items\n2).Detail of Items\n3).Stock\nB).Back to Main Menu")
    print(20 * "*")


# Store------------------------------------------------------------------------------------------------
# Staff------------------------------------------------------------------------------------------------
def sub2_staffmag():
    print(20 * "-" + "Staff Management" + 20 * "-")
    print(20 * "-" + "OTHERS" + "-" * 20)
    print("1).Search staff\n2).Update staff data\nA).Back to Staff Management\nB).Back to Main Menu")
    n = input("Enter choice:")
    if n == "1":
        print("Search staff")
        staff_search(n)
    elif n == "2":
        print("Update Staff")
        staff_update()
    elif n == "A" or "a":
        staffmag()
    elif n == "B" or "b":
        Mainmenu()
    else:
        print("Wrong choice")
        

def sub1_staffmag():
    print("1).Add staff\n2).Remove staff\n3.Back to Staff Management\n4).Others\nB).Back to Main Menu")
    n = input("Enter choice:")
    while True:
        if n == "1":
            staff_add()
        elif n == "2":
            print("Delete Staff")
            staff_delete()
        elif n == "3":
            staffmag()
        elif n == "4":
            sub2_staffmag()
        elif n == "b" or n == "B":
            Mainmenu()





def staffmag():  # In-Main Menu 1st choice
    print(20 * "-" + "Staff Management" + 20 * "-")
    print("1).Add/Remove Staff\n2).Staff detail\n3).Back to Main Menu")
    print("Enter choice[1-3]")
    n = int(input(":"))
    if n == 1:
        sub1_staffmag()
    elif n == 2:
        sub2_staffmag()
    elif n == 3:
        print("Back To main menu")
        Mainmenu()

# Staff--------------------------------------------------------------------------------------------------

def Mainmenu():
    print(20 * "*")
    print("\t\t\tWELCOME TO HY Shop")
    print(20 * "*")
    print("\t\t\tWELCOME MANAGER")  # for manager_MODE
    print("1.Staff Management\n2.Store Management\n3.State\n4.Cashier\n5.Log out")
    n = int(input(":"))
    if n == 1:
        staffmag()
    elif n == 2:
        storemag()
    elif n == 3:
        State()
    elif n == 4:
        cashier()
    elif n == 5:
        print("Logout")

Mainmenu()