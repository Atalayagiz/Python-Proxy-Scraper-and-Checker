import os
import requests
from datetime import datetime

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def create_directory_tree(script_directory):
    checked_proxies_folder = os.path.join(script_directory, "checked_proxies")

    if not os.path.exists(checked_proxies_folder):
        os.makedirs(checked_proxies_folder)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
    timestamp_folder = os.path.join(checked_proxies_folder, timestamp)
    os.makedirs(timestamp_folder)

    proxy_types = ["http_https", "socks4", "socks5"]
    for proxy_type in proxy_types:
        proxy_type_folder = os.path.join(timestamp_folder, proxy_type)
        os.makedirs(proxy_type_folder)

    return timestamp_folder

def check_proxy(proxy_type, proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }

    try:
        response = requests.get("https://www.example.com", proxies=proxies, timeout=1)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass

    return False

def load_proxies_from_file(file_path):
    proxies = []
    with open(file_path, "r") as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

def combine_proxy_lists(*lists):
    combined_list = []
    for proxy_list in lists:
        combined_list.extend(proxy_list.split('\n'))
    return combined_list

def scrape_proxies_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Hata oluştu: {e}')
        return ''

def main_menu():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    timestamp_folder = create_directory_tree(script_directory)

    while True:
        clear_screen()
        print("Ana Menü:")
        print("1. Proxy Scraper")
        print("2. Proxy Checker")
        print("3. Çıkış")
        
        choice = input("Seçiminizi girin (1/2/3): ")
        
        if choice == '1':
            proxy_scraper()
        elif choice == '2':
            proxy_checker(timestamp_folder)
        elif choice == '3':
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

def proxy_scraper():
    while True:
        clear_screen()
        print("Scraper Menüsü:")
        print("1. HTTP/HTTPS")
        print("2. SOCKS4")
        print("3. SOCKS5")
        print("4. Ana Menüye Dön")
        
        choice = input("Seçiminizi girin (1/2/3/4): ")
        
        if choice == '1':
            scrape_proxies("http_https")
        elif choice == '2':
            scrape_proxies("socks4")
        elif choice == '3':
            scrape_proxies("socks5")
        elif choice == '4':
            return
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

def scrape_proxies(proxy_type):
    clear_screen()

    # Hangi türde proxy'i çekeceğinize göre URL'yi ayarlayın
    if proxy_type == "http_https":

        url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://www.proxy-list.download/api/v1/get?type=http'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://api.openproxylist.xyz/http.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)

            print ('ctrl+a, ctrl+v to copy all proxy.')
            input()

        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)


    elif proxy_type == "socks4":
        url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://www.proxy-list.download/api/v1/get?type=socks4'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://api.openproxylist.xyz/socks4.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)

            print ('ctrl+a, ctrl+v to copy all proxy.')
            input()

        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

    elif proxy_type == "socks5":

        url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://www.proxy-list.download/api/v1/get?type=socks5'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://api.openproxylist.xyz/socks5.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)
        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)

        url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
        # İstek gönderin ve web sayfasını alın
        response = requests.get(url)

        # Yanıt durumunu kontrol edin
        if response.status_code == 200:
            # Sayfa içeriğini raw metin olarak alın
            raw_text = response.text

            # Raw metni yazdırın veya işleyin
            print(raw_text)

            print ('ctrl+a, ctrl+v to copy all proxy.')
            input()

        else:
            print('Sayfa alınamadı. Hata kodu:', response.status_code)
    else:
        print("Geçersiz proxy türü. Tekrar deneyin.")
        return

def proxy_checker(timestamp_folder):
    while True:
        clear_screen()
        print("Checker Menüsü:")
        print("1. HTTP/HTTPS")
        print("2. SOCKS4")
        print("3. SOCKS5")
        print("4. Ana Menüye Dön")
        
        choice = input("Seçiminizi girin (1/2/3/4): ")
        
        if choice == '1':
            proxy_type = "http_https"
            break
        elif choice == '2':
            proxy_type = "socks4"
            break
        elif choice == '3':
            proxy_type = "socks5"
            break
        elif choice == '4':
            return
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

    file_path = input("Proxy listesi dosyasının yolunu girin: ")
    proxy_list = load_proxies_from_file(file_path)
    check_proxies(proxy_list, proxy_type, timestamp_folder)

def check_proxies(proxy_list, proxy_type, timestamp_folder):
    clear_screen()

    working_proxies = []
    not_working_proxies = []

    for proxy in proxy_list:
        if check_proxy(proxy_type, proxy):
            print(f"[+] Working proxy: {proxy}")
            working_proxies.append(proxy)
        else:
            print(f"[-] Not working proxy: {proxy}")
            not_working_proxies.append(proxy)

    save_path = os.path.join(timestamp_folder, proxy_type)
    create_directory(save_path)

    with open(os.path.join(save_path, "working.txt"), "w") as working_file:
        working_file.write("\n".join(working_proxies))

    with open(os.path.join(save_path, "not_working.txt"), "w") as not_working_file:
        not_working_file.write("\n".join(not_working_proxies))

if __name__ == "__main__":
    main_menu()
