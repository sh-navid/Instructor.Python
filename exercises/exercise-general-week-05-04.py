## python -m pip install pygame
import pygame

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# با دستور بالا ابتدا پای-گیم را نصب کنید

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# پای-گیم یک موتور بازی است. از آن استفاده کرده ایم تا
# با رسم توپها یک گرید ۵ در ۵ بسازیم
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک کلاس برای توپ ساخته ایم تا اطلاعات توپ از جمله جای آن در صفحه
# سایز و رنگ آن را نگه داری کند
class Ball:
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size

        if x == y:
            self.color = "red"

    x = 250
    y = 250
    size = 10
    color = "blue"


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۱
# منطق این برنامه از این قسمت شروع میشود، بررسی کنید که
# اگر هر کدام از سه متغیر زیر را تغییر دهید، چه تغییری در خروجی
# برنامه حاصل میشود؟
# NUM, DISTANCE, OFFSET
NUM = 5
OFFSET = 150
DISTANCE = 50
ball_list = []
for row in range(0, NUM):
    for col in range(0, NUM):
        ball_size = (row + col) + 1
        ball_x = OFFSET + row * DISTANCE
        ball_y = OFFSET + col * DISTANCE
        ball_list.append(Ball(ball_x, ball_y, ball_size))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۲
# در قطعه کد بالا چرا از دو حلقه تو در تو استفاده شده است؟
# ----
# row و col
# به چه معنا هشتند و به چه دلیل تعریف شده اند؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۳
# در قطعه کد بالا اگر
# ball_size = (row + col) + 1
# را بصورت زیر تغییر دهیم چه اتفاقی می افتد؟
# ball_size = (row + col) * NUM

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۴
# رنگ توپهای آبی را به زرد و رنگ توپهای قرمز را به سفید تغییر دهید

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۵
# به همه ی توپها یک سایز ثابت دهید تا همه به یک اندازه رسم شوند

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک حلقه بینهایت داریم که پشت سر هم، رویدادهای بازی، منطق بازی و
# رسم صفحه بازی را کنترل میکند - تا زمانی این حلقه ادامه پیدا میکند
# که با شرطی از آن خارج شویم
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for ball in ball_list:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.size)
    pygame.display.update()