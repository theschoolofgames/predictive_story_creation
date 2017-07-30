#!/bin/sh

DATA_DIR=cbt_data
if [ ! -d "$DATA_DIR" ]; then
	wget http://www.thespermwhale.com/jaseweston/babi/CBTest.tgz
	tar -zxvf CBTest.tgz && mv CBTest $DATA_DIR
	rm CBTest.tgz
fi

cp $DATA_DIR/data/cbt_train.txt $DATA_DIR/input.txt

cd char-rnn-tensorflow && python train.py --data_dir=../$DATA_DIR/
