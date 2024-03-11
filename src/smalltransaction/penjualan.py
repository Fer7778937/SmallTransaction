class Penjualan:

    def __init__(self):
        pass

    def Total_harga(self, jumlah, harga):
        total = jumlah * harga

        if total > 200000:
            diskon = 15000
            total -= diskon
        elif total > 100000:
            diskon = 5000
            total -= diskon

        return total
