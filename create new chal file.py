import os

def create_folder_and_file():
    # Menerima input nama folder dari pengguna
    folder_name = input("Masukkan nama folder yang ingin dibuat: ")

    # Membuat path lengkap untuk folder baru
    path = os.path.join(os.getcwd(), folder_name)

    try:
        # Membuat folder
        os.makedirs(path, exist_ok=True)
        print(f"Folder '{folder_name}' telah dibuat.")

        # Membuat file main.py di dalam folder tersebut
        file_path = os.path.join(path, "main.py")
        with open(file_path, 'w') as file:
            file.write("# Tulis kode Python Anda di sini\n")
        print(f"File 'main.py' telah dibuat di dalam folder '{folder_name}'.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Memanggil fungsi
create_folder_and_file()
