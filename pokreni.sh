cat belain | ./belai/belai > belaout &
cat belaout | python py/main.py > belain &

python py/gumb.py
pkill -P $$
exec ./pokreni.sh

