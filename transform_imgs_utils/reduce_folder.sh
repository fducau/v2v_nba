#!/bin/bash
cd /home/paperspace/repos/v2v_nba/data/frames_fake/

for FILE in *.png
do 
    echo $FILE
    convert $FILE -resize 512x512 ../frames_fake_256x256/img/$FILE
done


# cd ../celeba_180x220

# for FILE in *.jpg
# do
#   echo $FILE
#   convert $FILE -filter Catrom -resize 25% ../celeba_55x45/$FILE
#done



 #convert ./img_align_celeba/00000*.jpg -filter Catrom -resize 25% ./img_align_celeba_resized_25/out%d.jpg