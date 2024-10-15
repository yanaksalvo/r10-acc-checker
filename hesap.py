import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

try:
    driver = webdriver.Firefox()
    driver.get("https://www.r10.net/kontrol-paneli/")
    username_field = driver.find_element(By.ID, "vb_login_username")
    password_field = driver.find_element(By.ID, "vb_login_password")
    username_field.send_keys("USERNAME") # :
    password_field.send_keys("PASSWORD") # :
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    print(f"{GREEN}Hesaba giriş yapıldı, bol kazançlar.{RESET}")

    while True:
        if driver.current_url != "https://www.r10.net/kontrol-paneli/":
            driver.get("https://www.r10.net/kontrol-paneli/")
            print(f"{BLUE}Yanlış sayfada bulunuluyordu, https://www.r10.net/kontrol-paneli/ sayfasına geri dönüldü.{RESET}")
        else:
            print(f"{BLUE}Doğru sayfadasınız: https://www.r10.net/kontrol-paneli/{RESET}")

        try:
            countdown_selector = "li.deleted:nth-child(6) > ol:nth-child(1) > li:nth-child(4) > span:nth-child(1)"
            countdown_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, countdown_selector))
            )
            if countdown_element and "0 gün, 0 saat, 0 dakika, 1 saniye" in countdown_element.text:
                print(f"{RED}'0 gün, 0 saat, 0 dakika, 1 saniye' metni bulundu, sayfa yenileniyor.{RESET}")
                driver.refresh()
                time.sleep(5)
                continue
        except Exception as e:
            print(f"{RED}Geri sayım metni bulunamadı veya hata oluştu: {e}{RESET}")

        for i in range(1, 6):
            button_selector = f"li.deleted:nth-child({i}) > ol:nth-child(1) > li:nth-child(4) > span:nth-child(1) > a:nth-child(1)"
            try:
                button = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, button_selector))
                )
                button.click()
                print(f"{GREEN}Buton {i} tıklandı.{RESET}")
            except Exception as e:
                print(f"{RED}{i}. buton bulunamadı veya görünmüyor: {e}{RESET}")
                continue

            time.sleep(10)

except Exception as e:
    print(f"{RED}Giriş sırasında hata oluştu: {e}{RESET}")

finally:
    input("Hata kontrolü için herhangi bir tuşa basın...")
    driver.quit()
