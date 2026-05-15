from dotenv import load_dotenv, find_dotenv, dotenv_values
from rich.console import Console
import argparse

SENSITIVE_KEYS = ["PASSWORD","API","PASS","PASSWD","PWD","SECRET","SECRET_KEY","API_KEY","ACCESS_KEY","PRIVATE_KEY","TOKEN","AUTH_TOKEN","JWT_SECRET","DB_PASSWORD","DATABASE_PASSWORD","MYSQL_PASSWORD","POSTGRES_PASSWORD","REDIS_PASSWORD","MONGO_PASSWORD","EMAIL_PASSWORD","SMTP_PASSWORD","AWS_SECRET_ACCESS_KEY","CLIENT_SECRET","ENCRYPTION_KEY","SESSION_SECRET"]
EMAIL_KEYS = ["EMAIL","EMAIL_ADDRESS","MAIL","MAIL_ADDRESS","ADMIN_EMAIL","SUPPORT_EMAIL","CONTACT_EMAIL","USER_EMAIL","SMTP_EMAIL","SMTP_USER","SMTP_USERNAME","MAIL_USERNAME","MAIL_USER","EMAIL_USER","EMAIL_USERNAME","FROM_EMAIL","NOREPLY_EMAIL","NOREPLY_ADDRESS","ACCOUNT_EMAIL","LOGIN_EMAIL","AUTH_EMAIL"]
symbols = ['&', '/', '\\', '!', '-', '_', '#', '@', '$', '%']


def main():
    console = Console()
    CounterSame = 0
    ValueEx = 0
    CounterSame2 = 0

    parser = argparse.ArgumentParser(description="A simple tool check for .env file and example.env file, takes 2 parameters first one for example file name the second one for the main env file that contains data")
    parser.add_argument("--example", nargs='?', default="example.env")
    parser.add_argument("--env", nargs='?', default=".env")
    args = parser.parse_args()

    console.print("---------check for keys---------", style="bold")
    ExampleData = dotenv_values(find_dotenv(args.example, raise_error_if_not_found=True))
    CurrentData = dotenv_values(find_dotenv(args.env, raise_error_if_not_found=True))

    for k, v in CurrentData.items():
        if v == None or v == "":
            console.print(f"Missing key value for {k}", style="bold red")
        else:
            ValueEx += 1
    if ValueEx == len(CurrentData):
        console.print("Every key has a value", style="bold green")

    console.print("---------if files matches---------", style="bold")
    for ExD in ExampleData.keys():
        if ExD not in CurrentData.keys():
            console.print(f"The Key {ExD} Missing in your .env file ", style="bold underline red")
            CounterSame += 1

    for Crd in CurrentData.keys():
        if Crd not in ExampleData.keys():
            console.print(f"The Key {Crd} not required in the example file", style="bold underline red")
            CounterSame2 += 1

    if CounterSame == 0 and CounterSame2 == 0:
        console.print("The .env file matches the example file", style="bold green")

    console.print("---------Password security report---------", style="bold")

    for CrD, v in CurrentData.items():
        CheckSymbol = 0
        LowerCount = 0
        UpperCount = 0
        PasswordWeakCount = 0
        words = CrD.upper().split("_")
        if CrD.upper() in SENSITIVE_KEYS or any(word in SENSITIVE_KEYS for word in words):
            for l in v:
                if l in symbols:
                    CheckSymbol += 1
                if l.islower():
                    LowerCount += 1
                if l.isupper():
                    UpperCount += 1
            if LowerCount == 0 and UpperCount == 0:
                console.print(f"You should use chars in {CrD}", style="bold underline red")
                PasswordWeakCount += 1
            if LowerCount == 0:
                console.print(f"use a lowercase char in {CrD}", style="bold yellow")
                PasswordWeakCount += 1
            if UpperCount == 0:
                console.print(f"use an uppercase char in {CrD}", style="bold yellow")
                PasswordWeakCount += 1
            if CheckSymbol == 0:
                console.print(f"Add a unique symbol in {CrD}", style="bold underline red")
                PasswordWeakCount += 1
            if len(v) < 8:
                console.print(f"Password too short in {CrD}", style="bold underline red")
                PasswordWeakCount += 1
            if PasswordWeakCount > 0:
                console.print(f"{PasswordWeakCount} security issues detected in {CrD}", style="bold red")
                print("")
            else:
                console.print(f"No security issues detected in {CrD}", style="bold green")
                print("")

    console.print("---------Email validation report---------", style="bold")
    for CrD, v in CurrentData.items():
        words = CrD.upper().split("_")
        if CrD.upper() in EMAIL_KEYS or any(word in EMAIL_KEYS for word in words):
            if "@" not in v:
                console.print(f"Enter a valid Email in {CrD}", style="bold underline red")
            else:
                console.print(f"The Email {CrD} is valid", style="bold green")


if __name__ == "__main__":
    main()