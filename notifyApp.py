import subprocess
import time
if __name__ == "__main__":
    try:
        subprocess.call(['pip', 'install','win10toast','-q'])
        from win10toast import ToastNotifier
        print("EyePro".center(100, '-'))
        while True:
            toaster = ToastNotifier()
            toaster.show_toast(title="EyePro 👀",msg="Timer Started!")
            print("[INFO] Timer started !")
            time.sleep(1200)
            toaster = ToastNotifier()
            toaster.show_toast(title="EyePro 👀",msg="Hey its 20 minutes Get your eyes off the monitor and focus 20 feet away.")
            print("[INFO] Notified...Timer restart in 20 seconds.")
            time.sleep(20)
    except:
        toaster = ToastNotifier()
        toaster.show_toast(title="EyePro 👀",msg="Exiting EyePro")
        print("Exiting EyePro".center(100, '-'))
        time.sleep(2)
        exit(0)