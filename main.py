import json
from datetime import datetime
from pathlib import Path


def durum_belirle(error_sayisi):
    if error_sayisi >= 5:
        return "KRITIK"
    elif error_sayisi >= 3:
        return "UYARI"
    else:
        return "NORMAL"


def hata_orani_hesapla(error_sayisi, toplam_log):
    if toplam_log == 0:
        return 0

    return error_sayisi / toplam_log * 100


def loglari_say(satirlar):
    error_sayisi = 0
    warning_sayisi = 0
    info_sayisi = 0

    for satir in satirlar:
        if "ERROR" in satir:
            error_sayisi += 1
        elif "WARNING" in satir:
            warning_sayisi += 1
        elif "INFO" in satir:
            info_sayisi += 1

    return error_sayisi, warning_sayisi, info_sayisi


log_dosyasi = Path("sample.log")

try:
    satirlar = log_dosyasi.read_text(
        encoding="utf-8"
    ).splitlines()
except FileNotFoundError:
    print("HATA: sample.log dosyasi bulunamadi.")
    raise SystemExit(1)


error_sayisi, warning_sayisi, info_sayisi = loglari_say(satirlar)

toplam_log = error_sayisi + warning_sayisi + info_sayisi
error_orani = hata_orani_hesapla(error_sayisi, toplam_log)
durum = durum_belirle(error_sayisi)


print("TOPLAM LOG:", toplam_log)
print(f"ERROR ORANI: %{error_orani:.1f}")
print("ERROR sayisi:", error_sayisi)
print("WARNING sayisi:", warning_sayisi)
print("INFO sayisi:", info_sayisi)
print("DURUM:", durum)


rapor_zamani = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

rapor = (
    f"RAPOR ZAMANI: {rapor_zamani}\n"
    f"TOPLAM LOG: {toplam_log}\n"
    f"ERROR ORANI: %{error_orani:.1f}\n"
    f"ERROR sayisi: {error_sayisi}\n"
    f"WARNING sayisi: {warning_sayisi}\n"
    f"INFO sayisi: {info_sayisi}\n"
    f"DURUM: {durum}\n"
)

rapor_verisi = {
    "rapor_zamani": rapor_zamani,
    "toplam_log": toplam_log,
    "error_orani": error_orani,
    "error_sayisi": error_sayisi,
    "warning_sayisi": warning_sayisi,
    "info_sayisi": info_sayisi,
    "durum": durum,
}

json_raporu = json.dumps(
    rapor_verisi,
    ensure_ascii=False,
    indent=4,
)

Path("rapor.json").write_text(
    json_raporu,
    encoding="utf-8",
)

print("JSON raporu kaydedildi.")

kaydedilen_json = json.loads(
    Path("rapor.json").read_text(encoding="utf-8")
)

jsonl_dosyasi = Path("rapor_gecmisi.jsonl")

with jsonl_dosyasi.open("a", encoding="utf-8") as dosya:
    dosya.write(
        json.dumps(rapor_verisi, ensure_ascii=False) + "\n"
    )

son_satir = jsonl_dosyasi.read_text(
    encoding="utf-8"
).splitlines()[-1]

son_kayit = json.loads(son_satir)

assert son_kayit["toplam_log"] == toplam_log
assert son_kayit["durum"] == durum

print("JSONL gecmis kaydi dogrulandi.")

assert kaydedilen_json["toplam_log"] == toplam_log
assert kaydedilen_json["durum"] == durum

print("JSON icerigi dogrulandi.")


Path("rapor.txt").write_text(rapor, encoding="utf-8")
print("Rapor, rapor.txt dosyasina kaydedildi.")

gecmis_dosyasi = Path("rapor_gecmisi.txt")

with gecmis_dosyasi.open("a", encoding="utf-8") as dosya:
    dosya.write("\n" + rapor + "\n")

print("Rapor gecmise eklendi.")


assert durum_belirle(2) == "NORMAL"
assert durum_belirle(4) == "UYARI"
assert durum_belirle(5) == "KRITIK"

assert hata_orani_hesapla(5, 8) == 62.5
assert hata_orani_hesapla(0, 0) == 0

assert loglari_say(
    ["ERROR test", "WARNING test", "INFO test"]
) == (1, 1, 1)

assert loglari_say([]) == (0, 0, 0)

print("TUM OTOMATIK TESTLER BASARILI.")
