import os
from dotenv import load_dotenv , find_dotenv , dotenv_values


SENSITIVE_KEYS = ["PASSWORD","API","PASS","PASSWD","PWD","SECRET","SECRET_KEY","API_KEY","ACCESS_KEY","PRIVATE_KEY","TOKEN","AUTH_TOKEN","JWT_SECRET","DB_PASSWORD","DATABASE_PASSWORD","MYSQL_PASSWORD","POSTGRES_PASSWORD","REDIS_PASSWORD","MONGO_PASSWORD","EMAIL_PASSWORD","SMTP_PASSWORD","AWS_SECRET_ACCESS_KEY","CLIENT_SECRET","ENCRYPTION_KEY","SESSION_SECRET"]
EMAIL_KEYS = ["EMAIL","EMAIL_ADDRESS","MAIL","MAIL_ADDRESS","ADMIN_EMAIL","SUPPORT_EMAIL","CONTACT_EMAIL","USER_EMAIL","SMTP_EMAIL","SMTP_USER","SMTP_USERNAME","MAIL_USERNAME","MAIL_USER","EMAIL_USER","EMAIL_USERNAME","FROM_EMAIL","NOREPLY_EMAIL","NOREPLY_ADDRESS","ACCOUNT_EMAIL","LOGIN_EMAIL","AUTH_EMAIL"]
symbols=['&','/','\\','!','-','_','#','@','$','%']

#عرفت ازاي اجيب الداتا من الملف الحمدلله
print("------------Example------------")
ExampleData=dotenv_values(find_dotenv("example.env",raise_error_if_not_found=True))
for k,v in ExampleData.items():
    #print(f"{k}=>{v}")
    #بتاكد ان كل كيي معاه فاليو 
    if v == None:
        raise Exception (f"Missing key value for {k}")
    
print("")

print("------------Data------------")

CurrentData=dotenv_values(find_dotenv(raise_error_if_not_found=True))
for k,v in CurrentData.items():
    #print(f"{k}=>{v}")#بتاكد ان كل كيي معاه فاليو 
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
    words=CrD.upper().split("_")
    if CrD.upper() in SENSITIVE_KEYS or any(word in SENSITIVE_KEYS for word in words)    :
        for l in v:
            if l in symbols:
                CheckSymbol+=1
            if l.islower():
                LowerCount+=1
            if l.isupper():
                UpperCount+=1
        if LowerCount == 0 and UpperCount == 0 :
            raise Exception (f"You should use chars in {CrD}")
        if LowerCount == 0:
            print(f"use a lower case char (preferred) in {CrD}")
        if UpperCount == 0 :
            print(f"use an upper case char (preferred) in {CrD}")
        if CheckSymbol == 0:
            raise Exception(f"Add a unique symbol in {CrD}")
        if len(v) < 8:
            raise Exception(f"Password too short in {CrD}")
    if CrD.upper() in  EMAIL_KEYS:
        if "@" not in v:
            raise Exception(f"Enter a valid Email in {CrD}")