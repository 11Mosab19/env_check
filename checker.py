import os
from dotenv import load_dotenv , find_dotenv , dotenv_values




#عرفت ازاي اجيب الداتا من الملف الحمدلله
print("------------Example------------")
ExampleData=dotenv_values(find_dotenv("example.env",raise_error_if_not_found=True))
for k,v in ExampleData.items():#بتاكد ان كل كيي معاه فاليو 
    if v == None:
        raise Exception (f"Missing key value for {k}")
    
print("")

print("------------Data------------")

CurrentData=dotenv_values(find_dotenv(raise_error_if_not_found=True))
for k,v in CurrentData.items():#بتاكد ان كل كيي معاه فاليو 
    if v == None:
        raise Exception (f"Missing key value{k}")
    
    
    
for ExD in ExampleData.keys():#بتاكد ان كل كيي مطلوب موجود في فايل ال env
    if ExD not in CurrentData.keys():
        raise Exception (f"The Key {ExD} Missing in your .env file ") 
    
for CrD in CurrentData.keys():#بتاكد ان مفيش كيي زياده مكتوب
    if CrD not in ExampleData.keys():
        raise Exception (f"the key {CrD} is not required")
    
