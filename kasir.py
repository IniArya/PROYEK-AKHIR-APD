from datetime import datetime
from utils import clear_screen
from data import produk

def tampilkan_produk():
    print("=== DAFTAR PRODUK ===")
    print("-" * 40)
    for id_produk, data in produk.items():
        print(f"{id_produk}. {data['nama']:<15} | Rp{data['harga']:,}")
    print("-" * 40)

def hitung_total(keranjang):
    return sum(item["harga"] for item in keranjang)

def tampilkan_keranjang(keranjang):
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    print("\n--- KERANJANG BELANJA ---")
    for i, item in enumerate(keranjang, 1):
        print(f"{i}. {item['nama']} - Rp{item['harga']:,}")

def struk_belanja(keranjang, uang_dibayar, diskon_member=0, diskon_belanja=0):
    clear_screen()
    print("=" * 40)
    print("         STRUK BELANJA")
    print("=" * 40)
    for item in keranjang:
        print(f"- {item['nama']:<20} Rp{item['harga']:,}")
    print("-" * 40)
    total = hitung_total(keranjang)
    total_diskon = 0
    if diskon_member > 0:
        diskon_member_rupiah = int(total * diskon_member / 100)
        total_diskon += diskon_member_rupiah
        print(f"Diskon Member ({diskon_member}%)        -Rp{diskon_member_rupiah:,}")
    if diskon_belanja > 0:
        diskon_belanja_rupiah = int(total * diskon_belanja / 100)
        total_diskon += diskon_belanja_rupiah
        print(f"Diskon Belanja ≥Rp500k ({diskon_belanja}%) -Rp{diskon_belanja_rupiah:,}")
    total_akhir = total - total_diskon
    print(f"Total Belanja              Rp{total:,}")
    print(f"Total Diskon               -Rp{total_diskon:,}")
    print(f"Total Bayar                Rp{total_akhir:,}")
    print(f"Uang Dibayar               Rp{uang_dibayar:,}")
    print(f"Kembalian                  Rp{uang_dibayar - total_akhir:,}")
    print("=" * 40)
    print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Terima kasih telah berbelanja!")
    print("=" * 40)
    input("\nTekan Enter untuk kembali ke menu...")

def simpan_struk_ke_file(keranjang, uang_dibayar, diskon_member=0, diskon_belanja=0):
    total = hitung_total(keranjang)
    total_diskon = 0
    if diskon_member > 0:
        diskon_member_rupiah = int(total * diskon_member / 100)
        total_diskon += diskon_member_rupiah
    if diskon_belanja > 0:
        diskon_belanja_rupiah = int(total * diskon_belanja / 100)
        total_diskon += diskon_belanja_rupiah
    total_akhir = total - total_diskon

    nama_file = f"struk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("         STRUK BELANJA\n")
        f.write("=" * 40 + "\n")
        for item in keranjang:
            f.write(f"- {item['nama']:<20} Rp{item['harga']:,}\n")
        f.write("-" * 40 + "\n")
        if diskon_member > 0:
            f.write(f"Diskon Member ({diskon_member}%)        -Rp{int(total * diskon_member / 100):,}\n")
        if diskon_belanja > 0:
            f.write(f"Diskon Belanja ≥Rp500k ({diskon_belanja}%) -Rp{int(total * diskon_belanja / 100):,}\n")
        f.write(f"Total Belanja              Rp{total:,}\n")
        f.write(f"Total Diskon               -Rp{total_diskon:,}\n")
        f.write(f"Total Bayar                Rp{total_akhir:,}\n")
        f.write(f"Uang Dibayar               Rp{uang_dibayar:,}\n")
        f.write(f"Kembalian                  Rp{uang_dibayar - total_akhir:,}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("Terima kasih telah berbelanja!\n")
    print(f"Struk disimpan di: {nama_file}")

def layanan_kasir(is_member_default=False):
    keranjang = []

    while True:
        clear_screen()
        print("=== LAYANAN KASIR ===")
        tampilkan_produk()
        tampilkan_keranjang(keranjang)
        print("\n0. Selesai & Checkout")
        print("99. Kembali ke Menu Utama")

        pilih = input("\nPilih produk: ").strip()

        if pilih == "0":
            if not keranjang:
                print("\nKeranjang masih kosong.")
                input("Tekan Enter untuk lanjut...")
                continue

            total = hitung_total(keranjang)
            print(f"\nTotal Belanja: Rp{total:,}")

            diskon_member = 0
            if is_member_default:
                diskon_member = 5
                print("\n✓ Anda adalah member (sudah login)")
                print("  Mendapatkan diskon member 5%")
            else:
                print("\n✗ Anda belanja sebagai tamu (tanpa login)")
                print("  Daftar & login untuk mendapatkan diskon member 5%!")

            diskon_belanja = 0
            if total >= 500000:
                diskon_belanja = 5
                print(f"\n✓ Total belanja ≥ Rp500.000")
                print(f"  Mendapatkan diskon belanja 5%")
            else:
                print(f"\n✗ Total belanja < Rp500.000")
                print(f"  Belanja ≥ Rp500.000 untuk diskon tambahan 5%")

            total_diskon = int(total * (diskon_member + diskon_belanja) / 100)
            total_akhir = total - total_diskon
            
            print(f"\n{'='*40}")
            print(f"Total Diskon: {diskon_member + diskon_belanja}% = Rp{total_diskon:,}")
            print(f"Total Bayar: Rp{total_akhir:,}")
            print(f"{'='*40}")

            while True:
                try:
                    uang_input = input("\nMasukkan uang pembayaran: Rp").strip()
                    if not uang_input:
                        print("Input tidak boleh kosong!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    
                    uang = int(uang_input)
                    
                    if uang < total_akhir:
                        print(f"\nUang tidak cukup! Kurang Rp{total_akhir - uang:,}")
                        input("Tekan Enter untuk lanjut...")
                    else:
                        break
                except ValueError:
                    print("\nInput harus berupa angka!")
                    input("Tekan Enter untuk lanjut...")

            struk_belanja(keranjang, uang_dibayar=uang, diskon_member=diskon_member, diskon_belanja=diskon_belanja)

            simpan_struk = input("\nSimpan struk ke file? (y/n): ").lower()
            if simpan_struk == "y":
                simpan_struk_ke_file(keranjang, uang_dibayar=uang, diskon_member=diskon_member, diskon_belanja=diskon_belanja)

            keranjang.clear()
            break

        elif pilih == "99":
            print("Kembali ke menu utama...")
            input("Tekan Enter untuk lanjut...")
            break

        elif pilih.isdigit() and int(pilih) in produk:
            item = produk[int(pilih)]
            keranjang.append(item)
            print(f"\n✓ {item['nama']} berhasil ditambahkan ke keranjang!")
            input("Tekan Enter untuk lanjut...")

        else:
            print("\n✗ Input tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    layanan_kasir()