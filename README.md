# MCP Student Sandbox

Bu repo, yazılım mühendisliği becerilerini geliştirmek için oluşturulmuş bir sandbox projesidir. Öğrencilerin kod analizi, test, güvenlik ve modülerlik gibi konuları pratik yapmalarını sağlar.

## Özellikler

- **Modüler Kod**: [`spaghetti_logic.py`](mcp-student-sandbox/spaghetti_logic.py) – Veri işleme fonksiyonları.
- **Hata Yönetimi**: [`failing_calculator.py`](mcp-student-sandbox/failing_calculator.py) – Ortalama hesaplama (sıfıra bölünme önleme).
- **Güvenlik**: [`secret_leak.py`](mcp-student-sandbox/secret_leak.py) – Güvenli anahtar yönetimi (environment variables).
- **Matematik**: [`mystery_module.py`](mcp-student-sandbox/mystery_module.py) – Kuadratik denklem kökleri hesaplama.

## Kurulum

1. Repo'yu klonlayın:
   ```sh
   git clone https://github.com/kullanici-adi/mcp-student-sandbox.git
   cd mcp-student-sandbox
   ```

2. Python 3.x gereklidir. Bağımlılıkları yükleyin (varsa):
   ```sh
   pip install -r requirements.txt  # Eğer requirements.txt varsa
   ```

## Kullanım

- **Veri İşleme**: [`process_data`](mcp-student-sandbox/spaghetti_logic.py) fonksiyonunu çalıştırın.
- **Hesaplama**: [`average_ratios`](mcp-student-sandbox/failing_calculator.py) ile test edin.
- **Güvenlik**: [`connect`](mcp-student-sandbox/secret_leak.py) için AWS_SECRET_KEY environment variable'ını ayarlayın.
- **Matematik**: [`fn_x`](mcp-student-sandbox/mystery_module.py) ile kökleri hesaplayın (örneğin, `fn_x(1, -3, 2)` → (2.0, 1.0)).

Örnek çalıştırma:
```python
from mcp-student-sandbox.mystery_module import fn_x
print(fn_x(1, -5, 6))  # Çıktı: (3.0, 2.0)
```

## Katkıda Bulunma

1. Fork edin.
2. Branch oluşturun: `git checkout -b feature/yeni-ozellik`.
3. Commit edin: `git commit -m "Yeni özellik eklendi"`.
4. Push edin ve Pull Request açın.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Sorularınız için GitHub Issues kullanın veya [email@example.com](mailto:email@example.com) adresine yazın.