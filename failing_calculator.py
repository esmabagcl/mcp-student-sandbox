def average_ratios(numbers):
    """Sayıların 100'e bölünmüş oranlarının ortalamasını hesaplar. 0 değerlerini atlar."""
    total = 0
    count = 0
    for num in numbers:
        if num == 0:
            print(f"Uyarı: 0 değeri atlandı (sıfıra bölünme önlendi).")
            continue
        total += 100 / num
        count += 1
    if count == 0:
        raise ValueError("Geçerli sayı yok (tümü 0).")
    return total / count

print(average_ratios([10, 5, 0]))