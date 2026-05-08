import os
from dotenv import load_dotenv , find_dotenv , dotenv_values
#عرفت ازاي اجيب الداتا من الملف الحمدلله
print("------------Example------------")
ExampleData=dotenv_values(find_dotenv("example.env"))
for k,v in ExampleData.items():
    print(f"{k} => {v}")
print("#"*20)
print("------------Data------------")
CurrentData=dotenv_values(find_dotenv(".env"))
for k,v in CurrentData.items():
    print(f"{k} => {v}")