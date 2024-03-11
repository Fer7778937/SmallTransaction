class Stok_barang:

    def __init__(self):
        pass

    def Pengurangan_stok(self, stok_awal, stok_terjual):
        stok_sisa = stok_awal - stok_terjual

        if stok_sisa < 5:
            print("Barang akan segera habis!")

        return stok_sisa
