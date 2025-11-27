from utils import clear_screen, tampilkan_header
from data import produk
from kasir import layanan_kasir 

def menu_user(username):
    while True:
        clear_screen()
        tampilkan_header()
        print(f"Selamat datang, {username}!")
        print("\n=== MENU USER ===")
        print("1. Lihat Produk")
        print("2. Belanja (Kasir)")
        print("3. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear_screen()
            from utils import tampilkan_produk
            tampilkan_produk(produk)
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            layanan_kasir(is_member_default=True)
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")
