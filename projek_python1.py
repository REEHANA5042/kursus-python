
def SELAMAT_DATANG():
    """Print "SELAMAT DATANG KEPADA PELANGGAN YANG DIHORMATI" and return none"""
    print("SELAMAT DATANG KEPADA PELANGGAN YANG DIHORMATI")




    nama=str(input("Masukkan nama penuh anda:"))
    umur=int(input("Masukkan umur anda:"))
    hobi=str(input("Masukkan hobi anda:")) 

    if nama =="":
        nama=str(input("Masukkan nama anda:"))
    else:
        if umur<=12:
            print("Umur anda mesti melebihi 12.")
            umur=int(input("Masukkan umur anda:"))
            hobi=str(input("Masukkan hobi anda:"))
        else:
            print("Salam Sejahtera",nama,".Anda berumur",umur,"tahun. Hobi anda adalah",hobi,". Terima Kasih,Jumpa Lagi.")


SELAMAT_DATANG()