import os
from dotenv import load_dotenv , find_dotenv , dotenv_values


secret = ['password','token','key','pwd','secret','key','private','api']
symbols=['&','/','\\','!','-','_','#','@','$','%']

#عرفت ازاي اجيب الداتا من الملف الحمدلله
print("------------Example------------")
ExampleData=dotenv_values(find_dotenv("example.env",raise_error_if_not_found=True))
for k,v in ExampleData.items():
    print(f"{k}=>{v}")
    #بتاكد ان كل كيي معاه فاليو 
    if v == None:
        raise Exception (f"Missing key value for {k}")
    
print("")

print("------------Data------------")

CurrentData=dotenv_values(find_dotenv(raise_error_if_not_found=True))
for k,v in CurrentData.items():
    print(f"{k}=>{v}")#بتاكد ان كل كيي معاه فاليو 
    if v == None:
        raise Exception (f"Missing key value{k}")
    
    
    
for ExD in ExampleData.keys():#بتاكد ان كل كيي مطلوب موجود في فايل ال env
    if ExD not in CurrentData.keys():
        raise Exception (f"The Key {ExD} Missing in your .env file ") 
    
for CrD in CurrentData.keys():#بتاكد ان مفيش كيي زياده مكتوب
    if CrD not in ExampleData.keys():
        raise Exception (f"the key {CrD} is not required")
for CrD,v in CurrentData.items():
    CheckSymbol = 0
    LowerCount = 0
    UpperCount = 0 
    if CrD.lower() in secret:
        for l in v:
            if l in symbols:
                CheckSymbol+=1
            if l.islower():
                LowerCount+=1
            if l.isupper():
                UpperCount=+1
        if LowerCount == 0 & UpperCount == 0 :
            raise Exception (f"You should use chars in {CrD}")
        if LowerCount == 0:
            print(f"use a lower case char (preferred) in {CrD}")
        if UpperCount == 0 :
            print(f"use an upper case char (preferred) in {CrD}")
        if CheckSymbol == 0:
            print(f"Add a unique symbol (preferred) in {CrD}")
        if len(v) < 8:
            raise Exception(f"Password too short in {CrD}")
        