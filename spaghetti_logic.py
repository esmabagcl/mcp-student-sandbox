def apply_multiplier(data, multiplier=1.15):
    """Veriye çarpan uygular ve sonucu döndürür."""
    return [d * multiplier for d in data]

def print_results(results):
    """Sonuçları yazdırır."""
    for val in results:
        print(f"Total: {val:.2f}")

def log_results(results, filename="log.txt"):
    """Sonuçları dosyaya yazar."""
    try:
        with open(filename, "a") as f:
            f.write(str(results) + "\n")
    except IOError as e:
        print(f"Log yazma hatası: {e}")

def process_data(data):
    """Veriyi işler: dönüştürür, yazdırır ve loglar."""
    results = apply_multiplier(data)
    print_results(results)
    log_results(results)
    return results