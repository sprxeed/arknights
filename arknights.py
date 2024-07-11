import pytesseract
from airtest.core.api import *
from airtest.aircv import *
from PIL import Image

__author__ = "freedom"
auto_setup(__file__, devices=["android://127.0.0.1:5037/emulator-5554"])
# 进入副本
# start = Template(r"images/tpl1718872352636.png", record_pos=(0.105, -0.092), resolution=(1872, 1170))
# fight = Template(r"images/tpl1718873064425.png", record_pos=(0.06, 0.275), resolution=(1872, 1170))

# 第1次对手机截屏
screen1 = G.DEVICE.snapshot()
# 根据坐标进行局部截图，即图标左上角和右下角的坐标(坐标可以在AirtestIDE里获取)
screen1 = aircv.crop_image(screen1, (599, 156, 744, 302))
# 保存局部截图(清晰度99最高)，保存成功后会返回文件名和截图大小
r1 = try_log_screen(screen1, quality=99)
# 打印返回，形如：{'screen': '1642500247024.jpg', 'resolution': (145, 146)}
print(f'r1:{r1}')


test = Image.open(r"images/tpl1718872352636.png")
print(pytesseract.image_to_string(test))

# 选择关卡
def select():
    touch(start)

    touch(fight)
    if exists():
        return



