"""
halaman utama code python
Gempa terupdate dari BMKG
"""
import gempa_terupdate

if __name__=='__main__':
  print ('Aplikasi utama')
  result = gempa_terupdate.ekstraksi_data()
  gempa_terupdate.tampilkan_data(result)
