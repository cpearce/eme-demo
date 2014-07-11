# Downloads media required for EME Demo.

import os
import urllib

media = [
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-85.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-86.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-87.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-88.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-89.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-8b.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-8c.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-8d.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car-20120827-manifest.mpd',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-85.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-86.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-87.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-88.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-89.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-8b.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-8c.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-8d.mp4',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-manifest.mpd',
  'http://yt-dash-mse-test.commondatastorage.googleapis.com/media/car_cenc-20120827-manifest_vidonly.mpd'
]

if os.path.exists('media') is False:
  os.mkdir('media')

for url in media:
  file_name = 'media' + os.sep + url.split('/')[-1]
  if os.path.exists(file_name) is False:
    print('DOWNLOADING ' + url)
    urllib.urlretrieve(url, file_name)
