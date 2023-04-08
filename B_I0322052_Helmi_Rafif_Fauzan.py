hargarumah =  {
    "T45/84" : 550000000,
    "T55/112" : 850000000, 
    "T60/120"  : 950000000 
}
bunga = 0.06
notaris = 2000000
provisi = 1500000
pnbp = 650000
baliknama = 1500000
ppembelian = 0.025
#cpb = cicilan pokok bulanan
#cibb = cicilan bunga bulanan
#tc = total ciiclan setiap bulan

print("Pilih jenis rumah yang diinginkan ")
print("T45/84 = 550 Juta ")
print("T55/112 = 850 Juta ")
print("T60/120 = 950 Juta ")
tipe = (input("Masukkan tipe rumah pilihan"))
dp = float(input("Masukkan uang muka(DP)"))
waktu = int(input("Masukkan Lama waktu cicil (5-30 tahun)"))
print("=========================================================================")               
print ("Anda memilih rumah tipe", tipe, "dengan uang muka sebesar Rp", dp, "rupiah selama", waktu, "tahun" )
print("========== '' '===============================================================")

hutang = (hargarumah[tipe] - dp)
cpb = round(hutang/waktu/12,2)
cibb = round((hutang*bunga*waktu)/(waktu*12),2)
tc = cpb + cibb
pajak = (ppembelian* hargarumah[tipe])
total = dp + tc + notaris + provisi + pajak + pnbp + baliknama


print("Repot 1 \nTotal hutang yang anda miliki Rp",hutang,"\nCicilan pokok bulanan sebesar Rp", cpb, "/bulan \nCicilan bunga bulanan sebesar Rp",cibb, "\nTotal cicilan setiap bulan Rp", tc)
print("=========================================================================")
print("Report 2 \nUang muka Rp", dp, "\nCicilan bulan pertama Rp", tc, "\nBiaya notaris Rp", notaris,"\nBiaya provisi Rp", provisi,"\nPajak pembelian (2.5% Harga) Rp", pajak,"\nBiaya PNBP Rp", pnbp,"\nBiaya Balik Nama Rp", baliknama,"\n\nMaka, Total Pembayaran Pertama Rp",total )

