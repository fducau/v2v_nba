import cv2
import os
import argparse
import logging

logging.log(1, 'Using OpenCV {}'.format(cv2.__version__))
parser = argparse.ArgumentParser()
parser.add_argument('--dataroot', type=str, 
					required=True,
					help='Path to videos folder to extrat frames from')
parser.add_argument('--outf', type=str,
					required=True,
					help='Output directory')
parser.add_argument('--v', action='store_true')
parser.add_argument('--savefreq', type=int, default=25,
					help='Save one pic every savefreq frames')

opt = parser.parse_args()
outf = opt.outf
dataroot = opt.dataroot
if opt.v:
	print_every = 1000


if not os.path.isdir(dataroot):
	raise OSError('Dataroot directory not found')
if not os.path.isdir(outf):
    os.mkdir(opt.outf)

dataroot_files = os.listdir(dataroot)
dataroot_vid_files = [os.path.join(dataroot, f) for f in dataroot_files if f[-3:] == 'mp4']

for i, vid_path in enumerate(dataroot_vid_files):
	vidcap = cv2.VideoCapture(vid_path)
	success, image = vidcap.read()
	count = 0
	success = True
	vid_name = os.path.split(vid_path)[-1]
	vid_name = vid_name[:-4]

	while success:
		success, image = vidcap.read()
		if count % opt.savefreq == 0:
			out_path = os.path.join(outf, 'vid_{}_frame_{}.png'.format(vid_name, str(count).zfill(10)))
			cv2.imwrite(out_path, image)
		if opt.v and count % print_every == 0:
			print('Saved {} frames'.format(count))
		count += 1
