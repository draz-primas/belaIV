mkfifo belain
mkfifo belaout

cd belai
make junkless release
cd ..

cat belain | ./belai/belai > belaout &
cat belaout | python py/main.py > belain &

