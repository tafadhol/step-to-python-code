"""
halaman utama code python
"""
from gempa_terupdate import ekstraksi_data, tampilkan_data

if __name__=='__main__':
  print ('Aplikasi utama')
  result = ekstraksi_data()
  tampilkan_data(result)
