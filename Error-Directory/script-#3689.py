# bug reproduction script for bug #3886 of AmazeFileManager
import sys
import time

import uiautomator2 as u2

# avd_serial: emulator-5554

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)



    d.app_start("com.amaze.filemanager.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.amaze.filemanager.debug":
            break
        time.sleep(2)
    wait()

    # 点击"..."展开设置
    out = d(resourceId="com.amaze.filemanager.debug:id/properties").click()
    if not out:
        print("Success: 点击‘...’展开设置")
    wait()

    # 点击Encrypt
    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击Encrypt")
    wait()

    #点击键盘设置密码123456
    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/til_encrypt_password"]/android.widget.FrameLayout[1]').send_keys("123456")
    if not out:
        print("Success: 设置密码")
    wait()

    # 点击键盘确认密码123456
    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/til_encrypt_password_confirm"]/android.widget.FrameLayout[1]').send_keys("123456")
    if not out:
        print("Success: 确认密码")
    wait()

    # 点击勾选框
    out = d(resourceId="com.amaze.filemanager.debug:id/checkbox_use_aze").click()
    if not out:
        print("Success: 点击勾选框")
    wait()

    # 点击GOT IT!
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击GOT IT!")
    wait()

    # 点击OK
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击OK")
    wait()

    # 点击9.zip.aze
    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[2]').click()
    if not out:
        print("Success: 点击9.zip.aze")
    wait()


    # 输入密码
    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/singleedittext_warnabletextinputlayout"]/android.widget.FrameLayout[1]').send_keys("123456")
    if not out:
        print("Success: 输入密码")
    wait()


    # 点击OK
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击OK")
    wait()

    # 点击EXTRACT
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击EXTRACT")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)