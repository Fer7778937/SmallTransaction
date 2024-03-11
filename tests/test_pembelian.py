from smalltransaction.pembelian import Pembelian


def total_harga():
    pembelian = Pembelian()
    assert pembelian.total_harga(2, 10000, 10) == 22000
