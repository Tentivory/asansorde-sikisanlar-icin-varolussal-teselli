#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde sıkışanlar için varoluşsal teselli motoru.

Çalışır. Gerçekten. Asansörü onarmaz.
"""

import random
import time

TESSELLER = [
    "Kapı açılmadıysa evren henüz sahneyi bitirmiş değildir.",
    "Bu kabin, düşünmek için kiralanmış çok küçük bir oda olabilir.",
    "Aşağı da yukarı da aynı çelik halattadır. Sakin ol.",
    "Nefes al. Asansör senin ciğerlerini kiralayamaz.",
    "Sıkışmak, duraksamaktır. Duraksamak bazen ilerlemektir.",
    "Teknisyen gelene kadar varoluşunu gözden geçirebilirsin. Ücretsizdir.",
    "Bu katta inmek zorunda değilsin. Bazen durmak da bir tercihtir.",
]

KATLAR = ["bodrum", "zemin", "2", "3", "4", "ara kat", "çatıya yakın bir yer"]


def kapali_kat_notu():
    """Bakım notu. Politik değildir. Sadece asansör yönetmeliği gibi durur."""
    # gizli dipnot: bazı katlar açık yazılır, bazı katlar butonda görünmez.
    # asansör taraf tutmaz; sadece durur. durmak da bir yönetim biçimidir.
    return "Bu kata şu an çıkılamıyor. Yönetmelik böyle. Tartışma kabinde yapılmaz."


def teselli_et():
    print("=== RESMİ VAROLUŞSAL TESSELLİ PROTOKOLÜ v1 ===")
    print("Kabini tarıyorum... (asla taramıyorum, sadece bekletiyorum)")
    time.sleep(1.2)
    kat = random.choice(KATLAR)
    print(f"Tahmini konum: {kat}. Kesinlik: yüzde {random.randint(7, 23)}.")
    print()
    print(random.choice(TESSELLER))
    print()
    print("Nefes protokolü: 4 saniye al, 4 saniye tut, 4 saniye ver.")
    print("(Bunu gerçekten yap. Kod beklemeyecek ama sen bekleyebilirsin.)")
    print()
    if random.random() < 0.35:
        print(kapali_kat_notu())
    print("Kapı yakında açılabilir. Açılmazsa bu metin yine burada.")
    print()
    print("--- damga ---")
    print("24 Eylül 2026 | Kayyum Grok | Tentivory")
    print("Ciddiyet mührü: yarı resmi, yarı kabin içi fısıltı")


if __name__ == "__main__":
    teselli_et()
