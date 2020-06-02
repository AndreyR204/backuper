# Backuper
Утилита для резервного копирования файлов на FTP и Yandex Disk
## Install
git clone
pip install -r requirements.txt
## Получение токена
Для работы с Yandex Disk необходим токен.
Для получения войдите в своем браузере в аккаунт Яндекса, а затем перецдите по ссылке https://oauth.yandex.ru/authorize?
   response_type=token&client_id=0a706e70bd154b66b89b55bf0f22b106
   и скопируйте токен в backuper.
## Usage
В начале работы программе требуется провести первоначальную настройку.
Для первого запуска используйте команду python main.py --set1
python main.py [-h] [--set1] [--set2] [--list LIST] [--time1 TIME1]
               [--time2 TIME2] [--stop] [--status STATUS]
