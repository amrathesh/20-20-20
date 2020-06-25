import subprocess
import time
if __name__ == "__main__":
    try:
        subprocess.call(['pip', 'install','win10toast','-q'])
        from win10toast import ToastNotifier
        print("EyePro".center(100, '-'))
        print("You will be notified every 20 minutes...")
        print("Do you want 10 minutes break after each hour ?")
        choice = input("Y or N :").upper()
        count = 0 
        toaster = ToastNotifier()
        while True:
            toaster.show_toast(title="EyePro 👀",msg="Timer started... ⏱")
            print("[INFO] Timer started !")
            time.sleep(1200)
            count += 1
            if(choice == 'Y' and count == 3):
                toaster.show_toast(title="EyePro 👀",msg="Its been an hour working take a 10 minutes break😄")
                count = 0
                print("[INFO] Break...Timer restart in 10 minutes.")
                time.sleep(600)
                continue
            toaster.show_toast(title="EyePro 👀",msg="Hey its 20 minutes Get your eyes off the monitor and focus 20 feet away 🍀.")
            print("[INFO] Notified...Timer restart in 20 seconds.")
            time.sleep(20)
    except:
        toaster.show_toast(title="EyePro 👀",msg="Exiting EyePro 👋🏻")
        print("Exiting EyePro".center(100, '-'))
        time.sleep(2)
        exit(0)