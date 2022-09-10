tasks = []

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# میخواهیم لیستی از کار هایی که در یک روز باید انجام دهیم را تحت
# عنوان یک لیست نگه داری کنیم و نمایش دهیم
class Task:
    title = None
    description = None
    is_done = False

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    def done(self):
        self.is_done = True

    def __str__(self) -> str:
        done = "x" if self.is_done else "-"
        return f"[{done}] {self.title.ljust(10)} '{self.description}'"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# لیستی از تسکها میسازیم
tasks.append(Task("Buy", "Buy soda for dinner"))
tasks.append(Task("Gym", "Go to gym"))
tasks.append(Task("Mail", "Send mail to Office"))
tasks.append(Task("Wash your Car", ""))
tasks.append(Task("Buy", "Buy a pen"))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۱
# آیا میتوانید دو تسک دیگر نیز به این لیست اضافه کنید؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۲
# آیا میتوانید به کلاس تسک یک ویژگی دیگر اضافه کنید؟ اولویت و اهمیت
# هر تسک چقدر است؟ کم، متوسط، زیاد

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# دو تا از تسکهایی که ساخته ایم را در حالت انجام شده قرار میدهیم
tasks[1].done()
tasks[2].done()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تسکهایی که ساخته ایم را نمایش میدهیم
for task in tasks:
    print(task)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۳
# آیا میتوانید لیست تسکها را با حلقه
# while
# نمایش دهید؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۴
# آیا میتوانید لیست تسکها را در یک فایل ذخیره کنید؟