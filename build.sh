#!/bin/bash

mkfifo belain
mkfifo belaout

cd belai
make junkless release

echo "exec `pwd`/pokreni.sh" >> ../pokreni.sh
