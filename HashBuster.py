import hashlib
import sys

def md5_kirma(hedef_md5):
    karakterler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=[]{}|;:,.<>?'
    toplam_kombinasyon = len(karakterler) ** 8  # 8 karakterli tüm kombinasyonların sayısı
    tamamlanan_kombinasyon = 0

    print("""
██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████║███████║███████╗███████║    ██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝
██╔══██║██╔══██║╚════██║██╔══██║    ██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║██║  ██║███████║██║  ██║    ██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                      
	""")

    for uzunluk in range(1, 9):
        for deneme in recursive_generate(karakterler, uzunluk):
            tamamlanan_kombinasyon += 1
            sys.stdout.write(f"\rŞifre kırılıyor... Tamamlanan: {tamamlanan_kombinasyon}/{toplam_kombinasyon} ({tamamlanan_kombinasyon * 100 / toplam_kombinasyon:.2f}%)")
            sys.stdout.flush()

            md5_hash = hashlib.md5(deneme.encode()).hexdigest()
            if md5_hash == hedef_md5:
                print("\n\nŞifre kırıldı!")
                return deneme

    return "\nŞifre bulunamadı"

def recursive_generate(karakterler, uzunluk, basamak=0, sonuc=""):
    if basamak == uzunluk:
        yield sonuc
    else:
        for karakter in karakterler:
            yield from recursive_generate(karakterler, uzunluk, basamak + 1, sonuc + karakter)

if __name__ == "__main__":
    hedef_md5 = input("Kırmak istediğiniz MD5 hash'ini girin: ")
    sifre = md5_kirma(hedef_md5)
    print("\nKırılan Şifre:", sifre)
