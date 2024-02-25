import os
os.system('cls')

def read_text_file(file_path):
    try:
        # باز کردن فایل متنی
        with open(file_path,'r') as file:
            # خواندن محتوای فایل
            content = file.read()
            # چاپ محتوای فایل
            print("File content")
            print(content)
    except FileNotFoundError:
        # چاپ پیغام خطا اگر فایل مورد نظر پیدا نشد
        print("Error: The desired file was not found!")
    except  Exception  as e:
        # چاپ پیغام خطا اگر مشکلی در خواندن فایل به وجود آمده است
        print("Error: There was a problem reading the file", e)
        

#مسیر فایل متنی را وارد کنید
file_path=input("Please enter the path to the text file:")
# فراخوانی تابع با مسیر فایل متنی به عنوان ورودی
read_text_file(file_path)
