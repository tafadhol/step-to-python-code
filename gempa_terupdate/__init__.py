def ekstraksi_data():
    """
    tanggal : 29 Februari 2024, 00:44:36 WIB
    magnitudo : 4.2
    Kedalaman : 14 km
    Lokasi : 5.14 LU - 94.70 BT
    Pusat gempa: Pusat gempa berada di laut 101 km BaratDaya JANTHO-ACEH BESAR
    Dirasakan : Dirasakan (Skala MMI): II Banda Ace
    :return:
    """

    hasil= dict()
    hasil['tanggal']='29 Februari 2024'
    hasil['waktu']='00:44:36 WIB'
    hasil['kedalaman']='14 Km WIB'
    hasil['lokasi']={'lu': 5.14, 'bt': 94.70}
    hasil['pusat_gempa']='pusat gempa berada di laut 101 km BaratDaya TANTHO-ACEH BESAR'
    hasil['dirasakan']='Dirasakan (skala MMI): II Banda aceh'


    return hasil


def tampilkan_data(result):
    print('gempa terkini berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi : LU= {result['lokasi']['lu']}, BT= {result['lokasi']['bt']}")
    print(f"Pusat_gempa {result['pusat_gempa']}")
    print(f"Dirasakan {result['dirasakan']}")
