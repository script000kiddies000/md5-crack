import requests as s

wordlist = input("masukkan nama file: ")
list = open(wordlist).readlines()
for md5 in list:
  md5 = md5.replace('\n','')
  hasil = s.get(f"http://www.nitrxgen.net/md5db/{md5}").text
  hasil = f"{md5}  {hasil}\n"
  open(f'hasil_{wordlist}.txt','a').write(hasil)
