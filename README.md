The sentinel-2 datasets is hard to download so I code.

## Dependencies
This script is based on Python3 and you should install some packages:
- MGRS

## Prepare
This script is based on aws service so you should already have an aws account. If you already have the account, run this:
```aws configure```
and configure the AWS Access Key ID, AWS Secret Access Key, Default region name.

## Run
Run this for downloading:
```
python download.py longitude latitude year month place
```
to download the whole month data for the given longitude and latitude. The place argument just used to ensure the place you download. An example here:
```
python download.py 110.082386 24.412226 2016 3 xiangelila
```
