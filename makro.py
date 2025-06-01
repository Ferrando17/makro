import pyautogui
import time
import threading
from pynput import keyboard

clicking = False 
click_mode = 'left' # 

# tıklama hızı
CLICK_INTERVAL = 0.005 # surdaki sayiyi değiştirerek hızını ayarlayabilirsin

def click_thread():
    """
    Bu fonksiyon ayrı bir iş parçacığında (thread'de) çalışacak ve tıklamaları yapacak.
    """
    global clicking, click_mode 
    while True: 
        if clicking: 
            current_x, current_y = pyautogui.position() 
            
            if click_mode == 'left':
                pyautogui.click(x=current_x, y=current_y) 
            elif click_mode == 'right':
                pyautogui.rightClick(x=current_x, y=current_y)
            
            time.sleep(CLICK_INTERVAL) 
        else: 
            time.sleep(0.01) # CPU yorulmasin

def on_press(key):
    """
    Bu fonksiyon klavye tuşuna basıldığında çağrılır.
    Auto clicker'ı başlatma/durdurma, modu değiştirme ve tamamen kapatma kontrolünü yapar.
    """
    global clicking, click_mode 
    try:
        # Programı tamamen kapatmak için 'b' tuşu
        if key.char == 'b': 
            print("Auto Clicker Kapatılıyor Kanka...")
            clicking = False     # Tıklamayı durdur
            return False         
        
        # Açma/Kapatma (toggle) için 'v' tuşu
        elif key.char == 'v': 
            if clicking: 
                print("Auto Clicker Durduruluyor Hacı (v tuşuyla)...")
                clicking = False
            else: 
                print("Auto Clicker Başlıyor Hacı (v tuşuyla)...")
                clicking = True
        
        
        elif key.char == 'x':
            if click_mode != 'left':
                click_mode = 'left'
                print("Mod: SOL TIK (X tuşuyla seçildi)")
            else:
                print("Mod zaten SOL TIK Kanka.")
        
       
        elif key.char == 'c':
            if click_mode != 'right':
                click_mode = 'right'
                print("Mod: SAĞ TIK (C tuşuyla seçildi)")
            else:
                print("Mod zaten SAĞ TIK Kanka.")

    except AttributeError:
        pass 

def on_release(key):
    """
    Bu fonksiyon klavye tuşu bırakıldığında çağrılır.
    Şimdilik boş.
    """
    pass

if __name__ == "__main__": 
    print("Auto Clicker Hazırlandı Kardeşim.")
    print("Farenizi nereye tıklayacaksanız oraya götürün.")
    print("'v' tuşuna basarak auto clicker'ı BAŞLATIN/DURDURUN (aç-kapa yapın).")
    print("'x' tuşuna basarak SOL TIK moduna geçin.")
    print("'c' tuşuna basarak SAĞ TIK moduna geçin.")
    print("'b' tuşuna basarak auto clicker'ı TAMAMEN KAPATIN.")
    print(f"Başlangıç Modu: {click_mode.upper()} TIK")
    print(f"Tıklama Hızı: Saniyede {int(1/CLICK_INTERVAL)} tıklama (20 CPS)")


    click_worker = threading.Thread(target=click_thread)
    click_worker.daemon = True 
    click_worker.start() 

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join() 

    print("Auto Clicker Tamamen Kapandı Gitti.")