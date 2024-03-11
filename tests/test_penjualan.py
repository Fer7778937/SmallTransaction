from smalltransaction.penjualan import Penjualan


def test_penjualan():
    penjualan = Penjualan()
    assert penjualan.total_harga(50, 9000, 15000) == 435000
