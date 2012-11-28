COMMONS_DIR = ../common
COOKIES_DIR = security
COOKIES_FILE = ${COOKIES_DIR}/cookies.txt
DATA_DIR = data
WGET_COMMAND = wget --load-cookies $(COOKIES_FILE) --directory-prefix=$(DATA_DIR)/
DOWNLOAD_PATH = http://www.kaggle.com/c/digit-recognizer/download


all: ndarrays

init:
	if [ ! -d ${DATA_DIR} ]; then mkdir ${DATA_DIR}; fi
	if [ ! -d ${COOKIES_DIR} ]; then mkdir ${COOKIES_DIR}; fi

$(COOKIES_FILE):
	$(COMMONS_DIR)/kaggle_login.py $(COOKIES_FILE)

login: $(COOKIES_FILE)

${DATA_DIR}/train.csv:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/train.csv
${DATA_DIR}/test.csv:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/test.csv

get-data: init login  ${DATA_DIR}/train.csv ${DATA_DIR}/test.csv

%.npy:
	./make-ndarrays.py ${DATA_DIR}

ndarrays: get-data ${DATA_DIR}/train_labels.npy ${DATA_DIR}/train_data.npy ${DATA_DIR}/test_data.npy
