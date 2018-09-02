#!/bin/bash

cd /home/maa/ecs_20180904/data/trim_data/
characters=($(find . -maxdepth 1 -type d))

for character in "${characters[@]}"; do
	if [ "$character" = "." ]; then
		continue
	fi
	echo ${character}

	data_num=`find ${character} -type f | wc -l`
	#echo $data_num
	test_num=`echo "scale=0; $data_num * 0.2" | bc | sed s/\.[0-9,]*$//g`
	echo ${test_num}

	out_dir='/home/maa/ecs_20180904/data/data/'

	#if [ -e ${out_dir}train/${character}]; then
	#	echo "already exist"
	#else
	#	mkdir ${out_dir}train/${character}
	#fi

	#if [ -e ${out_dir}test/${character}]; then
	#	echo "already exist"
	#else
	#	mkdir ${out_dir}test/${character}
	#fi

	
	ls ${character} | sort -R | tail -n $test_num

	ls ${character} | sort -R | tail -n $test_num | xargs -i mv ${character}/{} /home/maa/ecs_20180904/data/data/test/${character}
	ls ${character} | xargs -i mv ${character}/{} /home/maa/ecs_20180904/data/data/train/${character}


done
