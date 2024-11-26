cd /home/pi/belaIV/belai
make junkless release
cd ..

mkfifo belain
mkfifo belaout

cat belain | ./belai/belai > belaout &
cat belaout | python py/main.py > belain &

python py/gumb.py
pkill -P $$
exec ./pokreni.sh

