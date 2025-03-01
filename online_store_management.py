import mysql.connector
from tabulate import tabulate 
con = mysql.connector.connect(host = "localhost",user = "root", password = "karthik", database = "sm")
sm = con.cursor()


                                #-----------------customer details---------------------

def customer_signin():               
    cus_name = input("Enter the customer name")
    cus_city = input("Enter the city name")
    cus_state = input("Enter the state name")
    qry = "insert into customer(name,city,state) values (%s,%s,%s)"
    value1 = (cus_name,cus_city,cus_state)
    sm.execute(qry,value1)
    con.commit()
    print("Customer data successfully inserted")
    customer_signin()
    def show_cus():
    qry = "select * from customer"
    sm.execute(qry)
    data = sm.fetchall()
    print(tabulate(data,headers= ["cus_name","cus_city","cus_state"]))


show_cus()

                              #-------------product details------------------

def stock_entry():                 
    product_name  = input("Enter the product name")
    qty = int(input("Enter the quantity"))
    price_per_qty = int(input("Enter the ppq"))
    qry = "insert into stock(product_name,qty,price_per_qty) values (%s,%s,%s)"
    value2 = (product_name,qty,price_per_qty)
    sm.execute(qry,value2)
    con.commit()
    print("stock entry successfully inserted")
    stock_entry()
    def show_stock():
    qry = "select * from stock"
    sm.execute(qry)
    data2 = sm.fetchall()
    print(tabulate(data2,headers = ["product_name","qty","price_per_qty"]))


show_stock()

                                        # --------------stock update----------------

def stock_update():                        
    product_id = int(input("Enter the product id to change quantity"))
    qty = int(input("Enter the quantity number"))
    qry = "update stock set qty = %s where product_id = %s"
    value3 = (qty,product_id)
    sm.execute(qry,value3)
    con.commit()
    print("Stock quantity updated")
    stock_update()
    def get_customer():
    c_id = []
    qry = "select * from customer"
    sm.execute(qry)
    data = sm.fetchall()
    for i in data:
        c_id.append(i[0])
    return c_id

get_customer()

                                      #-------------Get Product------------------
def get_product():
    p_id = []
    qry = "select * from stock"
    sm.execute(qry)
    data = sm.fetchall()
    for i in data:
        p_id.append(i[0])
    return p_id

get_product()


                                #---------------Quantity check--------------------

def check_quantity():                  
    p_id = int(input("Enter the product id:"))
    qry = "select qty from stock where product_id = %s"
    value3 = (p_id,)
    sm.execute(qry,value3)
    data = sm.fetchall()
    return data[0][0]
    check_quantity()

                                #-----------------Product Name Checking-----------------
    def check_product_name():
    p_id = int(input("Enter the product id to check name:"))
    qry = "select product_name from stock where product_id = %s"
    value4 = (p_id,)
    sm.execute(qry,value4)
    data = sm.fetchall()
    return data[0][0]

    check_product_name()

                                 #-----------------new order-------------------

    def new_order():                       
    cu_id = int(input("Enter the customer id:"))
    p_id = int(input("Enter the product id:"))
    pr_name = check_product_name() 
    qty = int(input("Enter the quantity:"))
    ppq = int(input("Price per quantity"))
    total = qty*ppq
    qry = "insert into orders(cus_id,product_id,product_name,qty,price_per_qty,total) values(%s,%s,%s,%s,%s,%s)"
    value5 = (cu_id,p_id,pr_name,qty,ppq,total)
    sm.execute(qry,value5)
    con.commit()
    print("Order placed")

    new_order()

                                #-----------------show order-------------------

    def show_order():                           
    qry = "select * from orders"
    sm.execute(qry)
    data = sm.fetchall()
    print(tabulate(data,headers = ["cus_id","product_id","product_name","qty","price_per_qty","total price"]))

show_order()

                                        #---------Get price------------------

def get_price():
    p_id = int(input("Enter the product id:"))
    qry = "select price_per_qty from orders where cus_id = %s"
    val5 = (p_id,)
    sm.execute(qry,val5)
    data = sm.fetchall()
    print(tabulate(data,headers = ["price_per_qty"]))

    get_price()

                              #----------------Get order--------------------
    def get_order():
    o_id=[]
    qry="select order_id from orders"
    sm.execute(qry)
    data=sm.fetchall()
    for i in data:
        o_id.append(i[0])
    return o_id

    get_order()

                              #-----------------Cancel order----------------------
    def cancel_order():
    od_id = int(input("Enter the order id to cancel the order:"))
    qry = "delete from orders where order_id = %s"
    val = (od_id,)
    sm.execute(qry,val)
    sm.fetchall()
    print("Order succesfully cancelled")

    cancel_order()
    
                                #-----------ECOMMERCE--------------------

    def e_com():
    customer_id = int(input("Enter the customer id:"))
    c_id = get_customer()
    if customer_id in c_id:
        ch = int(input("1.display 2.new order 3.cancel 4.customer details update"))
        if ch == 1:
            show_stock()
        elif ch == 2:
            show_stock()
            product_id = int(input("kindly enter the product id:"))
            quantity = int(input("Enter the quantity:"))
            print("check_quantity")
            current_qty = check_quantity()
            print("Total available quantity is:",current_qty)
            if current_qty == 0:
                print("Stock is not available")
            elif current_qty >= quantity:
                new_order()
                new_qty = current_qty - quantity
                print("now total quantity is:",new_qty)
                print("Right now update this below")
                stock_update()
            else:
                print("These are available stock ",check_quantity())
                ch = input("Type yes to continue no to exit").lower()
                if ch == "yes":
                    price = get_price()
                    new_order()
                    new_qty = current_qty - quantity
                    stock_update()
                else:
                    print("Thank you....")
        elif ch == 3:
            show_order()
            order_id = int(input("Enter the order id:"))
            or_id = get_order()
            if order_id in or_id:
                p_id = int(input("Enter the product id:"))
                current_qty = check_quantity()
                cancel_qty = get_order()
                cancel_qty = sum(cancel_qty)
                new_qty = current_qty + cancel_qty
                cancel_order()
                stock_update()
                print("cancel is finished")
        elif ch == 4:
            cus_id = int(input("Enter the customer id"))
            qry = "select * from customer where cus_id = %s"
            val = (cus_id,)
            sm.execute(qry,val)
            data = sm.fetchall()
            print(tabulate(data,headers = ["cus_id","name","city","state"]))
            ch = int(input("1.name 2.city 3.state"))
            if ch == 1:
                new_name = input("Enter the new name")
                qry = "update customer set name  = %s where cus_id = %s"
                values = (new_name,cus_id)
                sm.execute(qry,values)
                con.commit()
                print("Name updated succesfully")
            elif ch == 2:
                new_city = input("Enter the city name ")
                qry = "update customer set city  = %s where cus_id = %s"
                values = (new_city,cus_id)
                sm.execute(qry,values)
                con.commit()
                print("City updated succesfully")
            elif ch == 3:
                new_state = input("Enter the state name ")
                qry = "update customer set state  = %s where cus_id = %s"
                values = (new_state,cus_id)
                sm.execute(qry,values)
                con.commit()
                print("State updated succesfully")
    else:
        print("kindly check your customer id..There is no customer available in this id")

        e_com()

        show_cus()
        show_order()
        show_stock()

                                  #--------------Select orders--------------------------
    def select_orders():
    qry="select*from orders"
    sm.execute(qry)
    dta=sm.fetchall()
    print(tabulate(dta,headers=["order_id","customer_id","product_id","product_name","quantity","price_per_quantity"]))
    select_orders()