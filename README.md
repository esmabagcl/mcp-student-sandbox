# MCP Student Sandbox

Bu repo, yazılım mühendisliği becerilerini geliştirmek için oluşturulmuş bir sandbox projesidir. Öğrencilerin kod analizi, test, güvenlik ve modülerlik gibi konuları pratik yapmalarını sağlar.

## Özellikler

- **Modüler Kod**: [`spaghetti_logic.py`](spaghetti_logic.py) – Veri işleme fonksiyonları (apply_multiplier, process_data).
- **Hata Yönetimi**: [`failing_calculator.py`](failing_calculator.py) – Ortalama hesaplama (sıfıra bölünme önleme) fonksiyonu `average_ratios`.
- **Güvenlik**: [`secret_leak.py`](secret_leak.py) – `AWS_SECRET_KEY` ortam değişkeni kontrolü ve bağlantı simülasyonu.
- **Matematik**: [`mystery_module.py`](mystery_module.py) – Kuadratik denklem kökleri hesaplayan `fn_x`.

## Kurulum

1. Repo'yu klonlayın:
   ```sh
   git clone https://github.com/kullanici-adi/mcp-student-sandbox.git
   cd mcp-student-sandbox
   ```

2. Python 3.x gereklidir. Bağımlılıkları yükleyin (varsa):
   ```sh
   pip install -r requirements.txt
   ```

## Kullanım

### 1. Veri işleme

```python
from spaghetti_logic import process_data
print(process_data([10, 20, 30]))
```

### 2. Ortalama oran hesaplama

```python
from failing_calculator import average_ratios
print(average_ratios([10, 5, 0]))
```

### 3. Güvenli anahtar kontrolü

```python
from secret_leak import connect
# terminalde:
# set AWS_SECRET_KEY=your_secret_key
connect()
```

### 4. Kuadratik denklem kökleri

```python
from mystery_module import fn_x
print(fn_x(1, -5, 6))  # (3.0, 2.0)
```

## Test Örnekleri

- `failing_calculator.py` içinde `average_ratios` sıfıra bölüm kontrolünü gösterir.
- `mystery_module.py` gerçek kökler için `d >= 0` kontrolü içerir.


