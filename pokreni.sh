mkfifo belain
mkfifo belaout

cd belai
make junkless release
cd ..

cat belaout | python py/main.py > belain &
cat belain | ./belai/belai > belaout &

