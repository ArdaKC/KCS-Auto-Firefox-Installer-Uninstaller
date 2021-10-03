import os
import requests
import tarfile
import shutil
import base64
import os.path
language = "1"

if language == "1":
    print("---------------------------------------------------")
    print("KCS Auto Firefox Installer & Uninstaller 2021.2.0-^")
    print("---------------------------------------------------")
    print("Işlemi yaptırmak için işlemin sonunda yazan harfi büyük harf ile birlikte yazıp enter tuşuna basın.")
    print("---------------------------------------------------")
    print("Firefox'u Indir & Kur (Manuel URL)           : M")
    print("Firefox'u Manuel URL Girmeden Indir & Kur    : W")
    print("---------------------------------------------------")
    print("Gerekli Paketleri Kur                        : 1")
    print("Indirilmiş Firefox Dosyalarını Sil           : 2")
    print("---------------------------------------------------")
    print("Firefox ESR'yi kaldır                        : E")
    print("Firefox'u kaldır.                            : R")
    print("nano ile desktop dosyasını düzenle           : N")
    print("Çıkış yap                                    : X")
    print("---------------------------------------------------")
    tar = './firefox.tar.bz2'
    if os.path.isfile(tar) and os.access(tar, os.R_OK):
       print("Firefox Indirildi. Kurulum Için Hazır.")
    else:
       print("Firefox Indirilmedi.")
    print("---------------------------------------------------")     
    secenek = input("")
    print("---------------------------------------------------")
    if secenek == "W":
       print("Bu seçenek'de kurulacak olan firefox sürümü en son sürüm olmayabilir bu yüzden ESR sürümü olan firefox 91.1.0esr sürümü kurulacak. Yinede Devam Etmek Istiyor Musunuz? evet/hayır")
       inputal = input("")
       if inputal == "evet":
           URL = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/91.1.0esr/linux-x86_64/tr/firefox-91.1.0esr.tar.bz2"
           tar = './firefox.tar.bz2'
           if os.path.isfile(tar) and os.access(tar, os.R_OK):
               
            print("Firefox Zaten İndirildi. Kurulum Başlatılıyor...")
           
            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")

            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = os.path.isdir('/usr/lib/firefox')
                if firefoxkonum == True:
                    shutil.rmtree('/usr/lib/firefox')

                print("Kurulum yapılıyor...")

                tf = tarfile.open("firefox.tar.bz2")
                tf.extractall()

                klasör1 = "firefox"

                klasör2 = "/usr/lib/"

                shutil.move(klasör1, klasör2)
                firefoxdesktop = "/usr/share/applications/firefox-esr.desktop"
                if os.path.isfile(firefoxdesktop) and os.access(firefoxdesktop, os.R_OK):
                    os.remove("/usr/share/applications/firefox-esr.desktop")
                base64_bac = "W0Rlc2t0b3AgRW50cnldCk5hbWU9RmlyZWZveApOYW1lW2JnXT1GaXJlZm94Ck5hbWVbY2FdPUZpcmVmb3gKTmFtZVtjc109RmlyZWZveApOYW1lW2VsXT1GaXJlZm94Ck5hbWVbZXNdPUZpcmVmb3gKTmFtZVtmYV09RmlyZWZveApOYW1lW2ZpXT1GaXJlZm94Ck5hbWVbZnJdPUZpcmVmb3gKTmFtZVtodV09RmlyZWZveApOYW1lW2l0XT1GaXJlZm94Ck5hbWVbamFdPUZpcmVmb3gKTmFtZVtrb109RmlyZWZveApOYW1lW25iXT1GaXJlZm94Ck5hbWVbbmxdPUZpcmVmb3gKTmFtZVtubl09RmlyZWZveApOYW1lW25vXT1GaXJlZm94Ck5hbWVbcGxdPUZpcmVmb3gKTmFtZVtwdF09RmlyZWZveApOYW1lW3B0X0JSXT1GaXJlZm94Ck5hbWVbcnVdPUZpcmVmb3gKTmFtZVtza109RmlyZWZveApOYW1lW3N2XT1GaXJlZm94CkNvbW1lbnQ9QnJvd3NlIHRoZSBXb3JsZCBXaWRlIFdlYgpDb21tZW50W2JnXT3QodGK0YDRhNC40YDQsNC90LUg0LIg0JzRgNC10LbQsNGC0LAKQ29tbWVudFtjYV09TmF2ZWd1ZXUgcGVyIGVsIHdlYgpDb21tZW50W2NzXT1Qcm9obMOtxb5lbsOtIHN0csOhbmVrIFdvcmxkIFdpZGUgV2VidQpDb21tZW50W2RlXT1JbSBJbnRlcm5ldCBzdXJmZW4KQ29tbWVudFtlbF09zqDOtc+BzrnOt86zzrfOuM61zq/PhM61IM+Dz4TOv869IM+AzrHOs866z4zPg868zrnOvyDOuc+Dz4TPjApDb21tZW50W2VzXT1OYXZlZ3VlIHBvciBsYSB3ZWIKQ29tbWVudFtmYV092LXZgdit2KfYqiDYtNio2qnZhyDYrNmH2KfZhtuMINin24zZhtiq2LHZhtiqINix2Kcg2YXYsdmI2LEg2YbZhdin24zbjNivCkNvbW1lbnRbZmldPVNlbGFhIEludGVybmV0aW4gV1dXLXNpdnVqYQpDb21tZW50W2ZyXT1OYXZpZ3VlIHN1ciBJbnRlcm5ldApDb21tZW50W2h1XT1BIHZpbMOhZ2jDoWzDsyBiw7ZuZ8Opc3rDqXNlCkNvbW1lbnRbaXRdPUVzcGxvcmEgaWwgd2ViCkNvbW1lbnRbamFdPeOCpuOCp+ODluOCkumWsuimp+OBl+OBvuOBmQpDb21tZW50W2tvXT3sm7nsnYQg64+M7JWEIOuLpOuLmeuLiOuLpApDb21tZW50W25iXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtubF09VmVya2VuIGhldCBpbnRlcm5ldApDb21tZW50W25uXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtub109U3VyZiBww6UgbmV0dGV0CkNvbW1lbnRbcGxdPVByemVnbMSFZGFuaWUgc3Ryb24gV1dXIApDb21tZW50W3B0XT1OYXZlZ3VlIG5hIEludGVybmV0CkNvbW1lbnRbcHRfQlJdPU5hdmVndWUgbmEgSW50ZXJuZXQKQ29tbWVudFtydV090J7QsdC+0LfRgNC10LLQsNGC0LXQu9GMINCS0YHQtdC80LjRgNC90L7QuSDQn9Cw0YPRgtC40L3RiwpDb21tZW50W3NrXT1QcmVobGlhZGFuaWUgaW50ZXJuZXR1CkNvbW1lbnRbc3ZdPVN1cmZhIHDDpSB3ZWJiZW4KR2VuZXJpY05hbWU9V2ViIEJyb3dzZXIKR2VuZXJpY05hbWVbYmddPdCY0L3RgtC10YDQvdC10YIg0LHRgNCw0YPQt9GK0YAKR2VuZXJpY05hbWVbY2FdPU5hdmVnYWRvciB3ZWIKR2VuZXJpY05hbWVbY3NdPVdlYm92w70gcHJvaGzDrcW+ZcSNCkdlbmVyaWNOYW1lW2RlXT1XZWJicm93c2VyCkdlbmVyaWNOYW1lW2VsXT3OoM61z4HOuc63zrPOt8+Ezq7PgiDOuc+Dz4TOv8+NCkdlbmVyaWNOYW1lW2VzXT1OYXZlZ2Fkb3Igd2ViCkdlbmVyaWNOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjApHZW5lcmljTmFtZVtmaV09V1dXLXNlbGFpbgpHZW5lcmljTmFtZVtmcl09TmF2aWdhdGV1ciBXZWIKR2VuZXJpY05hbWVbaHVdPVdlYmLDtm5nw6lzesWRCkdlbmVyaWNOYW1lW2l0XT1Ccm93c2VyIFdlYgpHZW5lcmljTmFtZVtqYV0944Km44Kn44OW44O744OW44Op44Km44K2CkdlbmVyaWNOYW1lW2tvXT3sm7kg67iM65287Jqw7KCACkdlbmVyaWNOYW1lW25iXT1OZXR0bGVzZXIKR2VuZXJpY05hbWVbbmxdPVdlYmJyb3dzZXIKR2VuZXJpY05hbWVbbm5dPU5ldHRsZXNhcgpHZW5lcmljTmFtZVtub109TmV0dGxlc2VyCkdlbmVyaWNOYW1lW3BsXT1QcnplZ2zEhWRhcmthIFdXVwpHZW5lcmljTmFtZVtwdF09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtydV090JjQvdGC0LXRgNC90LXRgi3QsdGA0LDRg9C30LXRgApHZW5lcmljTmFtZVtza109SW50ZXJuZXRvdsO9IHByZWhsaWFkYcSNCkdlbmVyaWNOYW1lW3N2XT1XZWJibMOkc2FyZQpYLUdOT01FLUZ1bGxOYW1lPUZpcmVmb3ggV2ViIEJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtiZ1090JjQvdGC0LXRgNC90LXRgiDQsdGA0LDRg9C30YrRgCAoRmlyZWZveCkKWC1HTk9NRS1GdWxsTmFtZVtjYV09TmF2ZWdhZG9yIHdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbY3NdPUZpcmVmb3ggV2Vib3bDvSBwcm9obMOtxb5lxI0KWC1HTk9NRS1GdWxsTmFtZVtlbF09zqDOtc+BzrnOt86zzq7PhM63z4IgzpnPg8+Ezr/PjSBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZXNdPU5hdmVnYWRvciB3ZWIgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjCBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZmldPUZpcmVmb3gtc2VsYWluClgtR05PTUUtRnVsbE5hbWVbZnJdPU5hdmlnYXRldXIgV2ViIEZpcmVmb3gKWC1HTk9NRS1GdWxsTmFtZVtodV09RmlyZWZveCB3ZWJiw7ZuZ8Opc3rFkQpYLUdOT01FLUZ1bGxOYW1lW2l0XT1GaXJlZm94IEJyb3dzZXIgV2ViClgtR05PTUUtRnVsbE5hbWVbamFdPUZpcmVmb3gg44Km44Kn44OW44O744OW44Op44Km44K2ClgtR05PTUUtRnVsbE5hbWVba29dPUZpcmVmb3gg7Ju5IOu4jOudvOyasOyggApYLUdOT01FLUZ1bGxOYW1lW25iXT1GaXJlZm94IE5ldHRsZXNlcgpYLUdOT01FLUZ1bGxOYW1lW25sXT1GaXJlZm94IHdlYmJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtubl09RmlyZWZveCBOZXR0bGVzYXIKWC1HTk9NRS1GdWxsTmFtZVtub109RmlyZWZveCBOZXR0bGVzZXIKWC1HTk9NRS1GdWxsTmFtZVtwbF09UHJ6ZWdsxIVkYXJrYSBXV1cgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3B0XT1GaXJlZm94IE5hdmVnYWRvciBXZWIKWC1HTk9NRS1GdWxsTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbcnVdPdCY0L3RgtC10YDQvdC10YIt0LHRgNCw0YPQt9C10YAgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3NrXT1JbnRlcm5ldG92w70gcHJlaGxpYWRhxI0gRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3N2XT1XZWJibMOkc2FyZW4gRmlyZWZveApFeGVjPS91c3IvbGliL2ZpcmVmb3gvZmlyZWZveCAldQpUZXJtaW5hbD1mYWxzZQpYLU11bHRpcGxlQXJncz1mYWxzZQpUeXBlPUFwcGxpY2F0aW9uCkljb249L3Vzci9saWIvZmlyZWZveC9icm93c2VyL2Nocm9tZS9pY29ucy9kZWZhdWx0L2RlZmF1bHQxMjgucG5nCkNhdGVnb3JpZXM9TmV0d29yaztXZWJCcm93c2VyOwpNaW1lVHlwZT10ZXh0L2h0bWw7dGV4dC94bWw7YXBwbGljYXRpb24veGh0bWwreG1sO2FwcGxpY2F0aW9uL3htbDthcHBsaWNhdGlvbi92bmQubW96aWxsYS54dWwreG1sO2FwcGxpY2F0aW9uL3Jzcyt4bWw7YXBwbGljYXRpb24vcmRmK3htbDtpbWFnZS9naWY7aW1hZ2UvanBlZztpbWFnZS9wbmc7eC1zY2hlbWUtaGFuZGxlci9odHRwO3gtc2NoZW1lLWhhbmRsZXIvaHR0cHM7ClN0YXJ0dXBXTUNsYXNzPUZpcmVmb3gKU3RhcnR1cE5vdGlmeT10cnVlCg=="
                decoded = base64.b64decode(base64_bac)
                utf8decoded = decoded.decode("utf-8")
                f = open("/usr/share/applications/firefox-esr.desktop", "w")
                f.write(utf8decoded)
                f.close()
                print("işlem tamamlandı.")



            else:
                print("İşlemler iptal edildi.")
           else:

          
            print("Firefox İndiriliyor Lütfen Bekleyin...")

            r = requests.get(URL, allow_redirects=True)

            open('firefox.tar.bz2', "wb").write(r.content)

            print("Firefox Başarıyla İndirildi. Kurulum Başlatılıyor...")


            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")
            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = os.path.isdir('/usr/lib/firefox')
                if firefoxkonum == True:
                    shutil.rmtree('/usr/lib/firefox')
                ayarlar = ""
                print("Kurulum yapılıyor...")

                tf = tarfile.open("firefox.tar.bz2")
                tf.extractall()

                klasör1 = "firefox"

                klasör2 = "/usr/lib/"

                shutil.move(klasör1, klasör2)
                firefoxdesktop = "/usr/share/applications/firefox-esr.desktop"
                if os.path.isfile(firefoxdesktop) and os.access(firefoxdesktop, os.R_OK):
                    os.remove("/usr/share/applications/firefox-esr.desktop")

                base64_bac = "W0Rlc2t0b3AgRW50cnldCk5hbWU9RmlyZWZveApOYW1lW2JnXT1GaXJlZm94Ck5hbWVbY2FdPUZpcmVmb3gKTmFtZVtjc109RmlyZWZveApOYW1lW2VsXT1GaXJlZm94Ck5hbWVbZXNdPUZpcmVmb3gKTmFtZVtmYV09RmlyZWZveApOYW1lW2ZpXT1GaXJlZm94Ck5hbWVbZnJdPUZpcmVmb3gKTmFtZVtodV09RmlyZWZveApOYW1lW2l0XT1GaXJlZm94Ck5hbWVbamFdPUZpcmVmb3gKTmFtZVtrb109RmlyZWZveApOYW1lW25iXT1GaXJlZm94Ck5hbWVbbmxdPUZpcmVmb3gKTmFtZVtubl09RmlyZWZveApOYW1lW25vXT1GaXJlZm94Ck5hbWVbcGxdPUZpcmVmb3gKTmFtZVtwdF09RmlyZWZveApOYW1lW3B0X0JSXT1GaXJlZm94Ck5hbWVbcnVdPUZpcmVmb3gKTmFtZVtza109RmlyZWZveApOYW1lW3N2XT1GaXJlZm94CkNvbW1lbnQ9QnJvd3NlIHRoZSBXb3JsZCBXaWRlIFdlYgpDb21tZW50W2JnXT3QodGK0YDRhNC40YDQsNC90LUg0LIg0JzRgNC10LbQsNGC0LAKQ29tbWVudFtjYV09TmF2ZWd1ZXUgcGVyIGVsIHdlYgpDb21tZW50W2NzXT1Qcm9obMOtxb5lbsOtIHN0csOhbmVrIFdvcmxkIFdpZGUgV2VidQpDb21tZW50W2RlXT1JbSBJbnRlcm5ldCBzdXJmZW4KQ29tbWVudFtlbF09zqDOtc+BzrnOt86zzrfOuM61zq/PhM61IM+Dz4TOv869IM+AzrHOs866z4zPg868zrnOvyDOuc+Dz4TPjApDb21tZW50W2VzXT1OYXZlZ3VlIHBvciBsYSB3ZWIKQ29tbWVudFtmYV092LXZgdit2KfYqiDYtNio2qnZhyDYrNmH2KfZhtuMINin24zZhtiq2LHZhtiqINix2Kcg2YXYsdmI2LEg2YbZhdin24zbjNivCkNvbW1lbnRbZmldPVNlbGFhIEludGVybmV0aW4gV1dXLXNpdnVqYQpDb21tZW50W2ZyXT1OYXZpZ3VlIHN1ciBJbnRlcm5ldApDb21tZW50W2h1XT1BIHZpbMOhZ2jDoWzDsyBiw7ZuZ8Opc3rDqXNlCkNvbW1lbnRbaXRdPUVzcGxvcmEgaWwgd2ViCkNvbW1lbnRbamFdPeOCpuOCp+ODluOCkumWsuimp+OBl+OBvuOBmQpDb21tZW50W2tvXT3sm7nsnYQg64+M7JWEIOuLpOuLmeuLiOuLpApDb21tZW50W25iXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtubF09VmVya2VuIGhldCBpbnRlcm5ldApDb21tZW50W25uXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtub109U3VyZiBww6UgbmV0dGV0CkNvbW1lbnRbcGxdPVByemVnbMSFZGFuaWUgc3Ryb24gV1dXIApDb21tZW50W3B0XT1OYXZlZ3VlIG5hIEludGVybmV0CkNvbW1lbnRbcHRfQlJdPU5hdmVndWUgbmEgSW50ZXJuZXQKQ29tbWVudFtydV090J7QsdC+0LfRgNC10LLQsNGC0LXQu9GMINCS0YHQtdC80LjRgNC90L7QuSDQn9Cw0YPRgtC40L3RiwpDb21tZW50W3NrXT1QcmVobGlhZGFuaWUgaW50ZXJuZXR1CkNvbW1lbnRbc3ZdPVN1cmZhIHDDpSB3ZWJiZW4KR2VuZXJpY05hbWU9V2ViIEJyb3dzZXIKR2VuZXJpY05hbWVbYmddPdCY0L3RgtC10YDQvdC10YIg0LHRgNCw0YPQt9GK0YAKR2VuZXJpY05hbWVbY2FdPU5hdmVnYWRvciB3ZWIKR2VuZXJpY05hbWVbY3NdPVdlYm92w70gcHJvaGzDrcW+ZcSNCkdlbmVyaWNOYW1lW2RlXT1XZWJicm93c2VyCkdlbmVyaWNOYW1lW2VsXT3OoM61z4HOuc63zrPOt8+Ezq7PgiDOuc+Dz4TOv8+NCkdlbmVyaWNOYW1lW2VzXT1OYXZlZ2Fkb3Igd2ViCkdlbmVyaWNOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjApHZW5lcmljTmFtZVtmaV09V1dXLXNlbGFpbgpHZW5lcmljTmFtZVtmcl09TmF2aWdhdGV1ciBXZWIKR2VuZXJpY05hbWVbaHVdPVdlYmLDtm5nw6lzesWRCkdlbmVyaWNOYW1lW2l0XT1Ccm93c2VyIFdlYgpHZW5lcmljTmFtZVtqYV0944Km44Kn44OW44O744OW44Op44Km44K2CkdlbmVyaWNOYW1lW2tvXT3sm7kg67iM65287Jqw7KCACkdlbmVyaWNOYW1lW25iXT1OZXR0bGVzZXIKR2VuZXJpY05hbWVbbmxdPVdlYmJyb3dzZXIKR2VuZXJpY05hbWVbbm5dPU5ldHRsZXNhcgpHZW5lcmljTmFtZVtub109TmV0dGxlc2VyCkdlbmVyaWNOYW1lW3BsXT1QcnplZ2zEhWRhcmthIFdXVwpHZW5lcmljTmFtZVtwdF09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtydV090JjQvdGC0LXRgNC90LXRgi3QsdGA0LDRg9C30LXRgApHZW5lcmljTmFtZVtza109SW50ZXJuZXRvdsO9IHByZWhsaWFkYcSNCkdlbmVyaWNOYW1lW3N2XT1XZWJibMOkc2FyZQpYLUdOT01FLUZ1bGxOYW1lPUZpcmVmb3ggV2ViIEJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtiZ1090JjQvdGC0LXRgNC90LXRgiDQsdGA0LDRg9C30YrRgCAoRmlyZWZveCkKWC1HTk9NRS1GdWxsTmFtZVtjYV09TmF2ZWdhZG9yIHdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbY3NdPUZpcmVmb3ggV2Vib3bDvSBwcm9obMOtxb5lxI0KWC1HTk9NRS1GdWxsTmFtZVtlbF09zqDOtc+BzrnOt86zzq7PhM63z4IgzpnPg8+Ezr/PjSBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZXNdPU5hdmVnYWRvciB3ZWIgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjCBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZmldPUZpcmVmb3gtc2VsYWluClgtR05PTUUtRnVsbE5hbWVbZnJdPU5hdmlnYXRldXIgV2ViIEZpcmVmb3gKWC1HTk9NRS1GdWxsTmFtZVtodV09RmlyZWZveCB3ZWJiw7ZuZ8Opc3rFkQpYLUdOT01FLUZ1bGxOYW1lW2l0XT1GaXJlZm94IEJyb3dzZXIgV2ViClgtR05PTUUtRnVsbE5hbWVbamFdPUZpcmVmb3gg44Km44Kn44OW44O744OW44Op44Km44K2ClgtR05PTUUtRnVsbE5hbWVba29dPUZpcmVmb3gg7Ju5IOu4jOudvOyasOyggApYLUdOT01FLUZ1bGxOYW1lW25iXT1GaXJlZm94IE5ldHRsZXNlcgpYLUdOT01FLUZ1bGxOYW1lW25sXT1GaXJlZm94IHdlYmJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtubl09RmlyZWZveCBOZXR0bGVzYXIKWC1HTk9NRS1GdWxsTmFtZVtub109RmlyZWZveCBOZXR0bGVzZXIKWC1HTk9NRS1GdWxsTmFtZVtwbF09UHJ6ZWdsxIVkYXJrYSBXV1cgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3B0XT1GaXJlZm94IE5hdmVnYWRvciBXZWIKWC1HTk9NRS1GdWxsTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbcnVdPdCY0L3RgtC10YDQvdC10YIt0LHRgNCw0YPQt9C10YAgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3NrXT1JbnRlcm5ldG92w70gcHJlaGxpYWRhxI0gRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3N2XT1XZWJibMOkc2FyZW4gRmlyZWZveApFeGVjPS91c3IvbGliL2ZpcmVmb3gvZmlyZWZveCAldQpUZXJtaW5hbD1mYWxzZQpYLU11bHRpcGxlQXJncz1mYWxzZQpUeXBlPUFwcGxpY2F0aW9uCkljb249L3Vzci9saWIvZmlyZWZveC9icm93c2VyL2Nocm9tZS9pY29ucy9kZWZhdWx0L2RlZmF1bHQxMjgucG5nCkNhdGVnb3JpZXM9TmV0d29yaztXZWJCcm93c2VyOwpNaW1lVHlwZT10ZXh0L2h0bWw7dGV4dC94bWw7YXBwbGljYXRpb24veGh0bWwreG1sO2FwcGxpY2F0aW9uL3htbDthcHBsaWNhdGlvbi92bmQubW96aWxsYS54dWwreG1sO2FwcGxpY2F0aW9uL3Jzcyt4bWw7YXBwbGljYXRpb24vcmRmK3htbDtpbWFnZS9naWY7aW1hZ2UvanBlZztpbWFnZS9wbmc7eC1zY2hlbWUtaGFuZGxlci9odHRwO3gtc2NoZW1lLWhhbmRsZXIvaHR0cHM7ClN0YXJ0dXBXTUNsYXNzPUZpcmVmb3gKU3RhcnR1cE5vdGlmeT10cnVlCg=="
                decoded = base64.b64decode(base64_bac)
                utf8decoded = decoded.decode("utf-8")
                f = open("/usr/share/applications/firefox-esr.desktop", "w")
                f.write(utf8decoded)
                f.close()
                print("işlem tamamlandı.")



            else:
                print("İşlemler iptal edildi.")
    if secenek == "N":
       filecheck = os.path.exists("/usr/share/applications/firefox-esr.desktop")
       filecheck2 = os.path.exists("/usr/share/applications/firefox.desktop")
   
       if filecheck and filecheck2 == True:
         print("/usr/share/applications konumunda 2 tane firefox desktop config dosyası bulundu hangisini düzenlemek istersiniz?")
         print("/usr/share/applications/firefox-esr.desktop : 1")
         print("/usr/share/applications/firefox.desktop     : 2")
         secenek = input("")
         if secenek == "1":
             os.system("nano /usr/share/applications/firefox-esr.desktop")
         else:
             if secenek == "2":

                os.system("nano /usr/share/applications/firefox.desktop")
       else:
         if filecheck == True:
           os.system("nano /usr/share/applications/firefox-esr.desktop") 
         else:
           if filecheck2 == True:
               os.system("nano /usr/share/applications/firefox.desktop")
           else:
                   
                   print("/usr/share/applications kısmında belirtilen firefox.desktop dosyası bulunamadı.")
                   print("dosyayı manuel olarak belirlemek ister misiniz? evet\hayır")
                   secenek = input("")
                   if secenek == "evet":
                       konum = input("konum: ")
                       konumkontrol = os.path.exists(konum)
                       if konumkontrol == True:
                          if os.system("nano " & konum) == 0:
                             print("komut başarıyla yürütüldü.")
                          else: 
                              print("komut yürütülemedi. nano yüklü olmayabilir.")
                       else:
                        print("belirtilen dosya bulunamadı.")


    if secenek == "E":
        print("firefox-esr'nin kapalı olduğun'dan emin misiniz? evet\hayır")
        eminim = input("")
        if eminim == "evet":

            print("Firefox ESR Kaldırılıyor...")
            firefoxdesktop = "/usr/share/applications/firefox-esr.desktop"
            if os.path.isfile(firefoxdesktop) and os.access(firefoxdesktop, os.R_OK):
                os.remove("/usr/share/applications/firefox-esr.desktop")

            firefoxkonum = "/usr/lib/firefox/firefox"
            firefoxkonum2 = "/usr/share/firefox-esr"
            if os.path.isfile(firefoxkonum2) and os.access(firefoxkonum2, os.R_OK):
                shutil.rmtree('usr/share/firefox-esr')
            if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
                shutil.rmtree('/usr/lib/firefox-esr')
            print("Firefox ESR Oturum'u kaldırılsın mı? evet/hayır")
            kaldırkaldırma = input("")
            if kaldırkaldırma == "evet":
                print("kullanıcı klasörünün adını yazın.")
                kullanıcıklasörü = input("")
                shutil.rmtree("/home/" + kullanıcıklasörü + "/.cache/mozilla")
                shutil.rmtree("/home/" + kullanıcıklasörü + "/.mozilla")
                print("Oturum dosyaları başarıyla kaldırıldı.")
        os.system("apt remove --purge firefox-esr")

        print("Kaldırma işlemi başarıyla tamamlandı.")
    if secenek == "R":
        print("firefox'un kapalı olduğun'dan emin misiniz? evet\hayır")
        eminim = input("")
        if eminim == "evet":

           print("Firefox Kaldırılıyor...")
           firefoxdesktop = "/usr/share/applications/firefox.desktop"
           if os.path.isfile(firefoxdesktop) and os.access(firefoxdesktop, os.R_OK):
               os.remove("/usr/share/applications/firefox.desktop")

           firefoxkonum = "/usr/lib/firefox/firefox"
           if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
                shutil.rmtree('/usr/lib/firefox')
           print("Firefox Oturum'u kaldırılsın mı? evet/hayır")
           kaldırkaldırma = input("")
           if kaldırkaldırma == "evet":
            print("kullanıcı klasörünün adını yazın.")
            kullanıcıklasörü = input("")
            shutil.rmtree("/home/" + kullanıcıklasörü + "/.cache/mozilla")
            shutil.rmtree("/home/" + kullanıcıklasörü + "/.mozilla")
            print("Oturum dosyaları başarıyla kaldırıldı.")
        os.system("apt remove --purge firefox")

        print("Kaldırma işlemi başarıyla tamamlandı.")
    if secenek == "X" or "x":
        os.system("exit")
    if secenek == "2":
        tar = './firefox.tar.bz2'
        if os.path.isfile(tar) and os.access(tar, os.R_OK):

             os.remove("firefox.tar.bz2")
        tar2 = './firefoxbeta.tar.bz2'
        if os.path.isfile(tar2) and os.access(tar2, os.R_OK):
             os.remove("firefoxbeta.tar.bz2")

        tar3 = './firefoxrelease.tar.bz2'
        if os.path.isfile(tar3) and os.access(tar3, os.R_OK):
            tar3 = './firefoxrelease.tar.bz2'
        print("işlem tamamlandı.")
    if secenek == "M":

        print("Kurulum için URL'yi yazın.")
        print("Alttakı URL ile istediğiniz sürümün tar2.gz uzantılı dosya bağlantısını kopyalayıp buraya yapıştırın.")
        print("URL : https://download-installer.cdn.mozilla.net/pub/firefox/releases/")
        URL = input("")
        tar = './firefox.tar.bz2'
        if os.path.isfile(tar) and os.access(tar, os.R_OK):
            print("Firefox Zaten İndirildi. Kurulum Başlatılıyor...")


            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")

            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = os.path.isdir('/usr/lib/firefox')
                if firefoxkonum == True:
                    shutil.rmtree('/usr/lib/firefox')

                print("Kurulum yapılıyor...")

                tf = tarfile.open("firefox.tar.bz2")
                tf.extractall()

                klasör1 = "firefox"

                klasör2 = "/usr/lib/"

                shutil.move(klasör1, klasör2)
                firefoxdesktop = "/usr/share/applications/firefox.desktop"
                if os.path.isfile(firefoxdesktop) and os.access(firefoxdesktop, os.R_OK):
                    os.remove("/usr/share/applications/firefox.desktop")
                base64_bac = "W0Rlc2t0b3AgRW50cnldCk5hbWU9RmlyZWZveApOYW1lW2JnXT1GaXJlZm94Ck5hbWVbY2FdPUZpcmVmb3gKTmFtZVtjc109RmlyZWZveApOYW1lW2VsXT1GaXJlZm94Ck5hbWVbZXNdPUZpcmVmb3gKTmFtZVtmYV09RmlyZWZveApOYW1lW2ZpXT1GaXJlZm94Ck5hbWVbZnJdPUZpcmVmb3gKTmFtZVtodV09RmlyZWZveApOYW1lW2l0XT1GaXJlZm94Ck5hbWVbamFdPUZpcmVmb3gKTmFtZVtrb109RmlyZWZveApOYW1lW25iXT1GaXJlZm94Ck5hbWVbbmxdPUZpcmVmb3gKTmFtZVtubl09RmlyZWZveApOYW1lW25vXT1GaXJlZm94Ck5hbWVbcGxdPUZpcmVmb3gKTmFtZVtwdF09RmlyZWZveApOYW1lW3B0X0JSXT1GaXJlZm94Ck5hbWVbcnVdPUZpcmVmb3gKTmFtZVtza109RmlyZWZveApOYW1lW3N2XT1GaXJlZm94CkNvbW1lbnQ9QnJvd3NlIHRoZSBXb3JsZCBXaWRlIFdlYgpDb21tZW50W2JnXT3QodGK0YDRhNC40YDQsNC90LUg0LIg0JzRgNC10LbQsNGC0LAKQ29tbWVudFtjYV09TmF2ZWd1ZXUgcGVyIGVsIHdlYgpDb21tZW50W2NzXT1Qcm9obMOtxb5lbsOtIHN0csOhbmVrIFdvcmxkIFdpZGUgV2VidQpDb21tZW50W2RlXT1JbSBJbnRlcm5ldCBzdXJmZW4KQ29tbWVudFtlbF09zqDOtc+BzrnOt86zzrfOuM61zq/PhM61IM+Dz4TOv869IM+AzrHOs866z4zPg868zrnOvyDOuc+Dz4TPjApDb21tZW50W2VzXT1OYXZlZ3VlIHBvciBsYSB3ZWIKQ29tbWVudFtmYV092LXZgdit2KfYqiDYtNio2qnZhyDYrNmH2KfZhtuMINin24zZhtiq2LHZhtiqINix2Kcg2YXYsdmI2LEg2YbZhdin24zbjNivCkNvbW1lbnRbZmldPVNlbGFhIEludGVybmV0aW4gV1dXLXNpdnVqYQpDb21tZW50W2ZyXT1OYXZpZ3VlIHN1ciBJbnRlcm5ldApDb21tZW50W2h1XT1BIHZpbMOhZ2jDoWzDsyBiw7ZuZ8Opc3rDqXNlCkNvbW1lbnRbaXRdPUVzcGxvcmEgaWwgd2ViCkNvbW1lbnRbamFdPeOCpuOCp+ODluOCkumWsuimp+OBl+OBvuOBmQpDb21tZW50W2tvXT3sm7nsnYQg64+M7JWEIOuLpOuLmeuLiOuLpApDb21tZW50W25iXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtubF09VmVya2VuIGhldCBpbnRlcm5ldApDb21tZW50W25uXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtub109U3VyZiBww6UgbmV0dGV0CkNvbW1lbnRbcGxdPVByemVnbMSFZGFuaWUgc3Ryb24gV1dXIApDb21tZW50W3B0XT1OYXZlZ3VlIG5hIEludGVybmV0CkNvbW1lbnRbcHRfQlJdPU5hdmVndWUgbmEgSW50ZXJuZXQKQ29tbWVudFtydV090J7QsdC+0LfRgNC10LLQsNGC0LXQu9GMINCS0YHQtdC80LjRgNC90L7QuSDQn9Cw0YPRgtC40L3RiwpDb21tZW50W3NrXT1QcmVobGlhZGFuaWUgaW50ZXJuZXR1CkNvbW1lbnRbc3ZdPVN1cmZhIHDDpSB3ZWJiZW4KR2VuZXJpY05hbWU9V2ViIEJyb3dzZXIKR2VuZXJpY05hbWVbYmddPdCY0L3RgtC10YDQvdC10YIg0LHRgNCw0YPQt9GK0YAKR2VuZXJpY05hbWVbY2FdPU5hdmVnYWRvciB3ZWIKR2VuZXJpY05hbWVbY3NdPVdlYm92w70gcHJvaGzDrcW+ZcSNCkdlbmVyaWNOYW1lW2RlXT1XZWJicm93c2VyCkdlbmVyaWNOYW1lW2VsXT3OoM61z4HOuc63zrPOt8+Ezq7PgiDOuc+Dz4TOv8+NCkdlbmVyaWNOYW1lW2VzXT1OYXZlZ2Fkb3Igd2ViCkdlbmVyaWNOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjApHZW5lcmljTmFtZVtmaV09V1dXLXNlbGFpbgpHZW5lcmljTmFtZVtmcl09TmF2aWdhdGV1ciBXZWIKR2VuZXJpY05hbWVbaHVdPVdlYmLDtm5nw6lzesWRCkdlbmVyaWNOYW1lW2l0XT1Ccm93c2VyIFdlYgpHZW5lcmljTmFtZVtqYV0944Km44Kn44OW44O744OW44Op44Km44K2CkdlbmVyaWNOYW1lW2tvXT3sm7kg67iM65287Jqw7KCACkdlbmVyaWNOYW1lW25iXT1OZXR0bGVzZXIKR2VuZXJpY05hbWVbbmxdPVdlYmJyb3dzZXIKR2VuZXJpY05hbWVbbm5dPU5ldHRsZXNhcgpHZW5lcmljTmFtZVtub109TmV0dGxlc2VyCkdlbmVyaWNOYW1lW3BsXT1QcnplZ2zEhWRhcmthIFdXVwpHZW5lcmljTmFtZVtwdF09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtydV090JjQvdGC0LXRgNC90LXRgi3QsdGA0LDRg9C30LXRgApHZW5lcmljTmFtZVtza109SW50ZXJuZXRvdsO9IHByZWhsaWFkYcSNCkdlbmVyaWNOYW1lW3N2XT1XZWJibMOkc2FyZQpYLUdOT01FLUZ1bGxOYW1lPUZpcmVmb3ggV2ViIEJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtiZ1090JjQvdGC0LXRgNC90LXRgiDQsdGA0LDRg9C30YrRgCAoRmlyZWZveCkKWC1HTk9NRS1GdWxsTmFtZVtjYV09TmF2ZWdhZG9yIHdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbY3NdPUZpcmVmb3ggV2Vib3bDvSBwcm9obMOtxb5lxI0KWC1HTk9NRS1GdWxsTmFtZVtlbF09zqDOtc+BzrnOt86zzq7PhM63z4IgzpnPg8+Ezr/PjSBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZXNdPU5hdmVnYWRvciB3ZWIgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjCBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZmldPUZpcmVmb3gtc2VsYWluClgtR05PTUUtRnVsbE5hbWVbZnJdPU5hdmlnYXRldXIgV2ViIEZpcmVmb3gKWC1HTk9NRS1GdWxsTmFtZVtodV09RmlyZWZveCB3ZWJiw7ZuZ8Opc3rFkQpYLUdOT01FLUZ1bGxOYW1lW2l0XT1GaXJlZm94IEJyb3dzZXIgV2ViClgtR05PTUUtRnVsbE5hbWVbamFdPUZpcmVmb3gg44Km44Kn44OW44O744OW44Op44Km44K2ClgtR05PTUUtRnVsbE5hbWVba29dPUZpcmVmb3gg7Ju5IOu4jOudvOyasOyggApYLUdOT01FLUZ1bGxOYW1lW25iXT1GaXJlZm94IE5ldHRsZXNlcgpYLUdOT01FLUZ1bGxOYW1lW25sXT1GaXJlZm94IHdlYmJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtubl09RmlyZWZveCBOZXR0bGVzYXIKWC1HTk9NRS1GdWxsTmFtZVtub109RmlyZWZveCBOZXR0bGVzZXIKWC1HTk9NRS1GdWxsTmFtZVtwbF09UHJ6ZWdsxIVkYXJrYSBXV1cgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3B0XT1GaXJlZm94IE5hdmVnYWRvciBXZWIKWC1HTk9NRS1GdWxsTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbcnVdPdCY0L3RgtC10YDQvdC10YIt0LHRgNCw0YPQt9C10YAgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3NrXT1JbnRlcm5ldG92w70gcHJlaGxpYWRhxI0gRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3N2XT1XZWJibMOkc2FyZW4gRmlyZWZveApFeGVjPS91c3IvbGliL2ZpcmVmb3gvZmlyZWZveCAldQpUZXJtaW5hbD1mYWxzZQpYLU11bHRpcGxlQXJncz1mYWxzZQpUeXBlPUFwcGxpY2F0aW9uCkljb249L3Vzci9saWIvZmlyZWZveC9icm93c2VyL2Nocm9tZS9pY29ucy9kZWZhdWx0L2RlZmF1bHQxMjgucG5nCkNhdGVnb3JpZXM9TmV0d29yaztXZWJCcm93c2VyOwpNaW1lVHlwZT10ZXh0L2h0bWw7dGV4dC94bWw7YXBwbGljYXRpb24veGh0bWwreG1sO2FwcGxpY2F0aW9uL3htbDthcHBsaWNhdGlvbi92bmQubW96aWxsYS54dWwreG1sO2FwcGxpY2F0aW9uL3Jzcyt4bWw7YXBwbGljYXRpb24vcmRmK3htbDtpbWFnZS9naWY7aW1hZ2UvanBlZztpbWFnZS9wbmc7eC1zY2hlbWUtaGFuZGxlci9odHRwO3gtc2NoZW1lLWhhbmRsZXIvaHR0cHM7ClN0YXJ0dXBXTUNsYXNzPUZpcmVmb3gKU3RhcnR1cE5vdGlmeT10cnVlCg=="
                decoded = base64.b64decode(base64_bac)
                utf8decoded = decoded.decode("utf-8")
                f = open("/usr/share/applications/firefox.desktop", "w")
                f.write(utf8decoded)
                f.close()
                print("işlem tamamlandı.")



            else:
                print("İşlemler iptal edildi.")
        else:

          
            print("Firefox İndiriliyor Lütfen Bekleyin...")

            r = requests.get(URL, allow_redirects=True)

            open('firefox.tar.bz2', "wb").write(r.content)

            print("Firefox Başarıyla İndirildi. Kurulum Başlatılıyor...")


            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")
            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = os.path.isdir('/usr/lib/firefox')
                if firefoxkonum == True:
                    shutil.rmtree('/usr/lib/firefox')
                ayarlar = ""
                print("Kurulum yapılıyor...")

                tf = tarfile.open("firefox.tar.bz2")
                tf.extractall()

                klasör1 = "firefox"

                klasör2 = "/usr/lib/"

                shutil.move(klasör1, klasör2)
                firefoxdesktop = "/usr/share/applications/firefox.desktop"
                if os.path.isfile(firefoxdesktop) and os.access(firefoxdesktop, os.R_OK):
                    os.remove("/usr/share/applications/firefox.desktop")

                base64_bac = "W0Rlc2t0b3AgRW50cnldCk5hbWU9RmlyZWZveApOYW1lW2JnXT1GaXJlZm94Ck5hbWVbY2FdPUZpcmVmb3gKTmFtZVtjc109RmlyZWZveApOYW1lW2VsXT1GaXJlZm94Ck5hbWVbZXNdPUZpcmVmb3gKTmFtZVtmYV09RmlyZWZveApOYW1lW2ZpXT1GaXJlZm94Ck5hbWVbZnJdPUZpcmVmb3gKTmFtZVtodV09RmlyZWZveApOYW1lW2l0XT1GaXJlZm94Ck5hbWVbamFdPUZpcmVmb3gKTmFtZVtrb109RmlyZWZveApOYW1lW25iXT1GaXJlZm94Ck5hbWVbbmxdPUZpcmVmb3gKTmFtZVtubl09RmlyZWZveApOYW1lW25vXT1GaXJlZm94Ck5hbWVbcGxdPUZpcmVmb3gKTmFtZVtwdF09RmlyZWZveApOYW1lW3B0X0JSXT1GaXJlZm94Ck5hbWVbcnVdPUZpcmVmb3gKTmFtZVtza109RmlyZWZveApOYW1lW3N2XT1GaXJlZm94CkNvbW1lbnQ9QnJvd3NlIHRoZSBXb3JsZCBXaWRlIFdlYgpDb21tZW50W2JnXT3QodGK0YDRhNC40YDQsNC90LUg0LIg0JzRgNC10LbQsNGC0LAKQ29tbWVudFtjYV09TmF2ZWd1ZXUgcGVyIGVsIHdlYgpDb21tZW50W2NzXT1Qcm9obMOtxb5lbsOtIHN0csOhbmVrIFdvcmxkIFdpZGUgV2VidQpDb21tZW50W2RlXT1JbSBJbnRlcm5ldCBzdXJmZW4KQ29tbWVudFtlbF09zqDOtc+BzrnOt86zzrfOuM61zq/PhM61IM+Dz4TOv869IM+AzrHOs866z4zPg868zrnOvyDOuc+Dz4TPjApDb21tZW50W2VzXT1OYXZlZ3VlIHBvciBsYSB3ZWIKQ29tbWVudFtmYV092LXZgdit2KfYqiDYtNio2qnZhyDYrNmH2KfZhtuMINin24zZhtiq2LHZhtiqINix2Kcg2YXYsdmI2LEg2YbZhdin24zbjNivCkNvbW1lbnRbZmldPVNlbGFhIEludGVybmV0aW4gV1dXLXNpdnVqYQpDb21tZW50W2ZyXT1OYXZpZ3VlIHN1ciBJbnRlcm5ldApDb21tZW50W2h1XT1BIHZpbMOhZ2jDoWzDsyBiw7ZuZ8Opc3rDqXNlCkNvbW1lbnRbaXRdPUVzcGxvcmEgaWwgd2ViCkNvbW1lbnRbamFdPeOCpuOCp+ODluOCkumWsuimp+OBl+OBvuOBmQpDb21tZW50W2tvXT3sm7nsnYQg64+M7JWEIOuLpOuLmeuLiOuLpApDb21tZW50W25iXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtubF09VmVya2VuIGhldCBpbnRlcm5ldApDb21tZW50W25uXT1TdXJmIHDDpSBuZXR0ZXQKQ29tbWVudFtub109U3VyZiBww6UgbmV0dGV0CkNvbW1lbnRbcGxdPVByemVnbMSFZGFuaWUgc3Ryb24gV1dXIApDb21tZW50W3B0XT1OYXZlZ3VlIG5hIEludGVybmV0CkNvbW1lbnRbcHRfQlJdPU5hdmVndWUgbmEgSW50ZXJuZXQKQ29tbWVudFtydV090J7QsdC+0LfRgNC10LLQsNGC0LXQu9GMINCS0YHQtdC80LjRgNC90L7QuSDQn9Cw0YPRgtC40L3RiwpDb21tZW50W3NrXT1QcmVobGlhZGFuaWUgaW50ZXJuZXR1CkNvbW1lbnRbc3ZdPVN1cmZhIHDDpSB3ZWJiZW4KR2VuZXJpY05hbWU9V2ViIEJyb3dzZXIKR2VuZXJpY05hbWVbYmddPdCY0L3RgtC10YDQvdC10YIg0LHRgNCw0YPQt9GK0YAKR2VuZXJpY05hbWVbY2FdPU5hdmVnYWRvciB3ZWIKR2VuZXJpY05hbWVbY3NdPVdlYm92w70gcHJvaGzDrcW+ZcSNCkdlbmVyaWNOYW1lW2RlXT1XZWJicm93c2VyCkdlbmVyaWNOYW1lW2VsXT3OoM61z4HOuc63zrPOt8+Ezq7PgiDOuc+Dz4TOv8+NCkdlbmVyaWNOYW1lW2VzXT1OYXZlZ2Fkb3Igd2ViCkdlbmVyaWNOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjApHZW5lcmljTmFtZVtmaV09V1dXLXNlbGFpbgpHZW5lcmljTmFtZVtmcl09TmF2aWdhdGV1ciBXZWIKR2VuZXJpY05hbWVbaHVdPVdlYmLDtm5nw6lzesWRCkdlbmVyaWNOYW1lW2l0XT1Ccm93c2VyIFdlYgpHZW5lcmljTmFtZVtqYV0944Km44Kn44OW44O744OW44Op44Km44K2CkdlbmVyaWNOYW1lW2tvXT3sm7kg67iM65287Jqw7KCACkdlbmVyaWNOYW1lW25iXT1OZXR0bGVzZXIKR2VuZXJpY05hbWVbbmxdPVdlYmJyb3dzZXIKR2VuZXJpY05hbWVbbm5dPU5ldHRsZXNhcgpHZW5lcmljTmFtZVtub109TmV0dGxlc2VyCkdlbmVyaWNOYW1lW3BsXT1QcnplZ2zEhWRhcmthIFdXVwpHZW5lcmljTmFtZVtwdF09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYgpHZW5lcmljTmFtZVtydV090JjQvdGC0LXRgNC90LXRgi3QsdGA0LDRg9C30LXRgApHZW5lcmljTmFtZVtza109SW50ZXJuZXRvdsO9IHByZWhsaWFkYcSNCkdlbmVyaWNOYW1lW3N2XT1XZWJibMOkc2FyZQpYLUdOT01FLUZ1bGxOYW1lPUZpcmVmb3ggV2ViIEJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtiZ1090JjQvdGC0LXRgNC90LXRgiDQsdGA0LDRg9C30YrRgCAoRmlyZWZveCkKWC1HTk9NRS1GdWxsTmFtZVtjYV09TmF2ZWdhZG9yIHdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbY3NdPUZpcmVmb3ggV2Vib3bDvSBwcm9obMOtxb5lxI0KWC1HTk9NRS1GdWxsTmFtZVtlbF09zqDOtc+BzrnOt86zzq7PhM63z4IgzpnPg8+Ezr/PjSBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZXNdPU5hdmVnYWRvciB3ZWIgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW2ZhXT3Zhdix2YjYsdqv2LEg2KfbjNmG2KrYsdmG2KrbjCBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbZmldPUZpcmVmb3gtc2VsYWluClgtR05PTUUtRnVsbE5hbWVbZnJdPU5hdmlnYXRldXIgV2ViIEZpcmVmb3gKWC1HTk9NRS1GdWxsTmFtZVtodV09RmlyZWZveCB3ZWJiw7ZuZ8Opc3rFkQpYLUdOT01FLUZ1bGxOYW1lW2l0XT1GaXJlZm94IEJyb3dzZXIgV2ViClgtR05PTUUtRnVsbE5hbWVbamFdPUZpcmVmb3gg44Km44Kn44OW44O744OW44Op44Km44K2ClgtR05PTUUtRnVsbE5hbWVba29dPUZpcmVmb3gg7Ju5IOu4jOudvOyasOyggApYLUdOT01FLUZ1bGxOYW1lW25iXT1GaXJlZm94IE5ldHRsZXNlcgpYLUdOT01FLUZ1bGxOYW1lW25sXT1GaXJlZm94IHdlYmJyb3dzZXIKWC1HTk9NRS1GdWxsTmFtZVtubl09RmlyZWZveCBOZXR0bGVzYXIKWC1HTk9NRS1GdWxsTmFtZVtub109RmlyZWZveCBOZXR0bGVzZXIKWC1HTk9NRS1GdWxsTmFtZVtwbF09UHJ6ZWdsxIVkYXJrYSBXV1cgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3B0XT1GaXJlZm94IE5hdmVnYWRvciBXZWIKWC1HTk9NRS1GdWxsTmFtZVtwdF9CUl09TmF2ZWdhZG9yIFdlYiBGaXJlZm94ClgtR05PTUUtRnVsbE5hbWVbcnVdPdCY0L3RgtC10YDQvdC10YIt0LHRgNCw0YPQt9C10YAgRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3NrXT1JbnRlcm5ldG92w70gcHJlaGxpYWRhxI0gRmlyZWZveApYLUdOT01FLUZ1bGxOYW1lW3N2XT1XZWJibMOkc2FyZW4gRmlyZWZveApFeGVjPS91c3IvbGliL2ZpcmVmb3gvZmlyZWZveCAldQpUZXJtaW5hbD1mYWxzZQpYLU11bHRpcGxlQXJncz1mYWxzZQpUeXBlPUFwcGxpY2F0aW9uCkljb249L3Vzci9saWIvZmlyZWZveC9icm93c2VyL2Nocm9tZS9pY29ucy9kZWZhdWx0L2RlZmF1bHQxMjgucG5nCkNhdGVnb3JpZXM9TmV0d29yaztXZWJCcm93c2VyOwpNaW1lVHlwZT10ZXh0L2h0bWw7dGV4dC94bWw7YXBwbGljYXRpb24veGh0bWwreG1sO2FwcGxpY2F0aW9uL3htbDthcHBsaWNhdGlvbi92bmQubW96aWxsYS54dWwreG1sO2FwcGxpY2F0aW9uL3Jzcyt4bWw7YXBwbGljYXRpb24vcmRmK3htbDtpbWFnZS9naWY7aW1hZ2UvanBlZztpbWFnZS9wbmc7eC1zY2hlbWUtaGFuZGxlci9odHRwO3gtc2NoZW1lLWhhbmRsZXIvaHR0cHM7ClN0YXJ0dXBXTUNsYXNzPUZpcmVmb3gKU3RhcnR1cE5vdGlmeT10cnVlCg=="
                decoded = base64.b64decode(base64_bac)
                utf8decoded = decoded.decode("utf-8")
                f = open("/usr/share/applications/firefox.desktop", "w")
                f.write(utf8decoded)
                f.close()
                print("işlem tamamlandı.")



            else:
                print("İşlemler iptal edildi.")
    


    if secenek == "1":
        x = 0
        a = 0
        if os.system("apt install python3-pip") == 0:
            print("python3-pip başarıyla kuruldu.")
        else:
            print("python3-pip kurulamadı.")
            a = 1
        if os.system("pip install requests")  == 0:
             print("requests başarıyla kuruldu.")
            
        else:
             print("requests kurulamadı.")
             x = 1
        if  os.system("pip install shutil") == 0:
            print("shutil başarıyla kuruldu.")
        else:
            print("shutil kurulamadı.")
            x = 1
        if  os.system("apt install nano") == 0:
            print("shutil başarıyla kuruldu.")
        else: 
            print("shutil kurulamadı.")
        if a == 1:
            print("apt ile bazı paketler hata yüzünden kurulamadı.")
            print("kurulması gereken paketler")
            print("python3-pip")
            print("nano")
            print("eğer farklı bir dağıtım kullanıyorsanız manuel kurabilirsiniz.")
        if x == 1:
            print("pip ile bazı paketler kurulamadı python3-pip yüklü olmayabilir.")
    

        print("islem tamamlandı.")
  




