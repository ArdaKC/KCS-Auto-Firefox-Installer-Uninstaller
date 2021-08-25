import os
import requests
import tarfile
import shutil
import base64

language = "1"
if language == "1":
    print("KCS Auto Firefox Installer & Uninstaller 2021.1.0-*")
    print("Hangi Firefox Sürümünü Kurmak İstiyorsunuz?")
    print("Firefox Release                    : 1")
    print("Firefox Beta                       : 2")
    print("Manuel URL ile İndir & Kur         : 3")
    print("Gerekli Paketleri Kur              : 4")
    print("İndirilmiş TAR Dosyalarını Temizle : 5")
    print("Firefox ESR'yi kaldır              : 6")
    print("Firefox'u kaldır.                  : R")
    print("Çıkış yap                          : X")

    secenek = input("")
    if secenek == "6":
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
    if secenek == "5":
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
    if secenek == "3":

        print("Kurulum için URL'yi yazın.")
        print("Firefox URL'sini buradan alabilirsiniz.")
        print("URL : https://download-installer.cdn.mozilla.net/pub/firefox/")
        URL = input("")
        tar = './firefox.tar.bz2'
        if os.path.isfile(tar) and os.access(tar, os.R_OK):
            print("Firefox Zaten İndirildi. Kurulum Başlatılıyor...")


            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")

            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = "/usr/lib/firefox/firefox"
                if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
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
                print("İşlemler iptal edildi firefox kapatılmadı.")
        else:
            print("Firefox İndiriliyor Lütfen Bekleyin...")
            url = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/92.0b8/linux-x86_64/en-US/firefox-92.0b8.tar.bz2"
            r = requests.get(url, allow_redirects=True)

            open('firefox.tar.bz2', "wb").write(r.content)

            print("Firefox Başarıyla İndirildi. Kurulum Başlatılıyor...")


            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")
            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = "/usr/lib/firefox/firefox"
                ayarlar = ""
                if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
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
                print("İşlemler iptal edildi firefox kapatılmadı.")
    if secenek == "2":
        tar = './firefoxbeta.tar.bz2'
        if os.path.isfile(tar) and os.access(tar, os.R_OK):
            print("Firefox Zaten İndirildi. Kurulum Başlatılıyor...")


            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")

            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = "/usr/lib/firefox/firefox"
                if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
                    shutil.rmtree('/usr/lib/firefox')

                print("Kurulum yapılıyor...")

                tf = tarfile.open("firefoxbeta.tar.bz2")
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
                print("İşlemler iptal edildi firefox kapatılmadı.")
        else:
            print("Firefox Beta Sürümü İndiriliyor Lütfen Bekleyin...")
            url = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/92.0b8/linux-x86_64/en-US/firefox-92.0b8.tar.bz2"
            r = requests.get(url, allow_redirects=True)

            open('firefoxbeta.tar.bz2', "wb").write(r.content)

            print("Firefox Başarıyla İndirildi. Kurulum Başlatılıyor...")
            print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")
            eminmisin = input("")
            if eminmisin == "tamam":
                firefoxkonum = "/usr/lib/firefox/firefox"
                ayarlar = ""
                if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
                    shutil.rmtree('/usr/lib/firefox')

                print("Kurulum yapılıyor...")

                tf = tarfile.open("firefoxbeta.tar.bz2")
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
                print("İşlemler iptal edildi firefox kapatılmadı.")


    if secenek == "4":
        os.system("apt install python3-pip")
        os.system("pip install requests")
        os.system("pip install tarfile")
        os.system("pip install shutil")
        print("islem tamamlandı.")
    if secenek == "1":

             tar = './firefoxrelease.tar.bz2'
             if os.path.isfile(tar) and os.access(tar, os.R_OK):
                 print("Firefox Zaten İndirildi. Kurulum Başlatılıyor...")
                 print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")

                 eminmisin = input("")
                 if eminmisin == "tamam":
                   firefoxkonum = "/usr/lib/firefox/firefox"
                   if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):

                         shutil.rmtree('/usr/lib/firefox')

                   print("Kurulum yapılıyor...")
                   os.system("killall firefox")
                   tf = tarfile.open("firefoxrelease.tar.bz2")
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
                   print("İşlemler iptal edildi firefox kapatılmadı.")
             else:
                print("Firefox Release Sürümü İndiriliyor Lütfen Bekleyin...")
                url = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/91.0.1/linux-x86_64/en-US/firefox-91.0.1.tar.bz2"
                r = requests.get(url, allow_redirects=True)

                open('firefoxrelease.tar.bz2', "wb").write(r.content)

                print("Firefox Başarıyla İndirildi. Kurulum Başlatılıyor...")
                print("Eğer güncelleme olarak bu işlemi yapıyorsanız firefox'un kapalı olduğun'dan emin ol : tamam")
                eminmisin = input("")
                if eminmisin == "tamam":
                    firefoxkonum = "/usr/lib/firefox/firefox"
                    ayarlar = ""
                    if os.path.isfile(firefoxkonum) and os.access(firefoxkonum, os.R_OK):
                          shutil.rmtree('/usr/lib/firefox')

                    print("Kurulum yapılıyor...")
                    os.system("killall firefox")
                    tf = tarfile.open("firefoxrelease.tar.bz2")
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
                    print("İşlemler iptal edildi firefox kapatılmadı.")









