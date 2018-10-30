import mgrs
import sys
import os

sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3] #year
sys.argv[4] #month
sys.argv[5] #地名

latitude = sys.argv[2]
longitude = sys.argv[1]

m = mgrs.MGRS()
position_under_mgrs_bytes = m.toMGRS(latitude, longitude)
position_under_mgrs = str(position_under_mgrs_bytes, encoding= "utf-8")
print(position_under_mgrs)
utm_code = position_under_mgrs[0:2]
latitude_band = position_under_mgrs[2]
square =  position_under_mgrs[3:5]

year = sys.argv[3]
month = sys.argv[4]


os.system("aws s3 sync s3://sentinel-s2-l1c/tiles/%s/%s/%s/%s/%s/ ./images/%s%s%s --request-payer" % (utm_code, latitude_band, square, year, month,sys.argv[5],year, month))
