lsmod | grep ^v4l2loopback || sudo modprobe v4l2loopback exclusive_caps=1 max_buffers=2

gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -s 1280x720 -f v4l2 /dev/video2
