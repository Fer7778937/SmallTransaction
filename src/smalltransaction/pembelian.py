class Pembelian:

    def __init__(self):
        pass

    def total_harga(self, jumlah, harga, pajak):
        total_tanpa_pajak = jumlah * harga
        total_dengan_pajak = (
            total_tanpa_pajak + (pajak * total_tanpa_pajak / 100)
        )

        # Berikan diskon 10% jika jumlah melebihi 10
        diskon = 10 if jumlah > 10 else 0

        total_dengan_diskon = (
            total_dengan_pajak - (diskon * total_dengan_pajak / 100)
        )
        return total_dengan_diskon
