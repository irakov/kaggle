COMMONS_DIR = ../common
DATA_DIR = .
COOKIES_FILE = cookies.txt
WGET_COMMAND = wget --load-cookies $(COOKIES_FILE) --directory-prefix=$(DATA_DIR)/
DOWNLOAD_PATH = http://www.kaggle.com/c/digit-recognizer/download

$(COOKIES_FILE):
	$(COMMONS_DIR)/kaggle_login.py $(COOKIES_FILE)

login: $(COOKIES_FILE)

train.csv:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/train.csv
test.csv:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/test.csv
knn_benchmark.csv:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/knn_benchmark.csv
knn_benchmark.R:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/knn_benchmark.R
rf_benchmark.csv:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/rf_benchmark.csv
rf_benchmark.R:
	${WGET_COMMAND} $(DOWNLOAD_PATH)/rf_benchmark.R

get-data: login train.csv test.csv knn_benchmark.csv knn_benchmark.R rf_benchmark.csv rf_benchmark.R
