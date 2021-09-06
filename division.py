

import pyupbit
import schedule
import time

access = "bbZGbVfCJ4xvm3wja3NU7wPUmurynDhbLeEPlfll"
secret = "S2ksETmtVg4S5Pawqzy6WdIphBzhucVbVPHPRiYR"
upbit = pyupbit.Upbit(access, secret)

    

print()
print(" AutoTrading Start - for the Financial Independence......!!!")


def job(): 

    


    a = upbit.get_balance("KRW") -500000

    b = upbit.get_balance("KRW-BTC") * pyupbit.get_current_price("KRW-BTC")
    c = upbit.get_balance("KRW-XRP") * pyupbit.get_current_price("KRW-XRP")
    d = upbit.get_balance("KRW-ADA") * pyupbit.get_current_price("KRW-ADA")
    f = upbit.get_balance("KRW-ETH") * pyupbit.get_current_price("KRW-ETH")
    h = upbit.get_balance("KRW-DOGE") * pyupbit.get_current_price("KRW-DOGE")

    e = a + b + c+ d + f + h


    
   
    time.sleep(0.5)     


    if c/e <= 0.145 :                                     
        upbit.buy_market_order("KRW-XRP", 0.15*e-c)       

        if b/e <= 0.495 :                                 
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    
            
        if b/e >= 0.505 :                                 
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  


    if c/e >= 0.155 :                                     
        upbit.sell_market_order("KRW-XRP", (c-0.15*e) / pyupbit.get_current_price("KRW-XRP"))    

        if b/e <= 0.495 :                                 
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    
            
        if b/e >= 0.505 :                                  
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC")) 


    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "   ADA 보유액 : ", f"{float(d):.1f}", "   ADA 비율 :", f"{float(d/e):.3f}", "(적정 : 0.15)")
    time.sleep(0.5)     


    if d/e <= 0.145 :                                     
        upbit.buy_market_order("KRW-ADA", 0.15*e-d)                        

        if b/e <= 0.495 :                                
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)   
            
        if b/e >= 0.505 :                                 
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  


    if d/e >= 0.155 :                                     
        upbit.sell_market_order("KRW-ADA", (d-0.15*e) / pyupbit.get_current_price("KRW-ADA"))     

        if b/e <= 0.495 :                                
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    
            
        if b/e >= 0.505 :                                 
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  


    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "   ETH 보유액 : ", f"{float(f):.1f}", "   ETH 비율 :", f"{float(f/e):.3f}", "(적정 : 0.15)")
    time.sleep(0.5)     


    if f/e <= 0.145 :                                     
        upbit.buy_market_order("KRW-ETH", 0.15*e-f)      

        if b/e <= 0.495 :                                
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    
            
        if b/e >= 0.505 :                                 
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  


    if f/e >= 0.155 :                                     
        upbit.sell_market_order("KRW-ETH", (f-0.15*e) / pyupbit.get_current_price("KRW-ETH"))    

        if b/e <= 0.495 :                                
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    
            
        if b/e >= 0.505 :                                
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  


    print(" ---> BTC 보유액 :", f"{float(b):.1f}", "  DOGE 보유액 : ", f"{float(h):.1f}", "  DOGE 비율 :", f"{float(h/e):.3f}", "(적정 : 0.05)")
    time.sleep(0.5)     
    print( )
    


    if h/e <= 0.045 :                                     
        upbit.buy_market_order("KRW-DOGE", 0.05*e-h)      

        if b/e <= 0.495 :                                 
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)   
            
        if b/e >= 0.505 :                                 
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))  


    if h/e >= 0.055 :                                     
        upbit.sell_market_order("KRW-DOGE", (h-0.05*e) / pyupbit.get_current_price("KRW-DOGE"))   

        if b/e <= 0.495 :                                 
            upbit.buy_market_order("KRW-BTC", 0.5*e-b)    
            
        if b/e >= 0.505 :                                   
            upbit.sell_market_order("KRW-BTC", (b-0.5*e) / pyupbit.get_current_price("KRW-BTC"))    
    time.sleep(0.5)     

schedule.every().minute.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
