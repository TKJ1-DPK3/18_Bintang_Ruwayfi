print("=========================")
print("  SERVER STATUS CHECKER  ")
print("=========================")

nama_server = input("Nama Server  : ")
suhu_cpu = int(input("Suhu CPU   : "))

if suhu_cpu < 40:
  status = "Suhu Terlalu Rendah"
elif suhu_cpu <= 59:
  status = "Suhu Normal"
elif suhu_cpu <= 79:
  status = "Suhu Cukup Tinggi"
else:
  status = "PERINGATAN! Suhu Terlalu Tinggi"

print("\nOutput : ")
print(f"Server  : {nama_server}")
print(f"Suhu    : {suhu_cpu}Derajat Celcius")
print(f"Status  : {status}")
print("Perhatikan Temperatur Server")
