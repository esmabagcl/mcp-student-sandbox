import os

# DOĞRU YÖNTEM: Şifreyi kodun içine yazmak yerine 
# Bilgisayarın çevre değişkenlerinden (Environment Variables) çekiyoruz.
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "KEY_NOT_FOUND")

def connect():
    if AWS_SECRET_KEY == "KEY_NOT_FOUND":
        print("Hata: Güvenlik anahtarı sistemde tanımlı değil!")
    else:
        print(f"Bağlantı başarılı. Anahtar güvenli bir şekilde yüklendi.")