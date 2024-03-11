from smalltransaction.stok_barang import Stok_barang


def test_stok_barang():
    test_stok_barang = Stok_barang()
    assert test_stok_barang.hasil_dari_stok(10, 7) == 3
