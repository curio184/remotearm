# remotearm

今回構築する開発環境
------------

Raspberry Piに、VSCodeとPythonを利用したRaspberry Piの開発環境を構築する。

設定項目 | 説明
------------- | -------------
Pythonのバージョン | Python 3.7.2
VSCodeのバージョン | Community Build版 VSCode
VSCodeのワークスペースのパス | /home/pi/source/remotearm/
Python仮想環境のパス | /home/pi/source/remotearm/.venv/py372/


プロジェクトを作成する
------------

サンプルプロジェクトを用意したのでcloneしてください。

```
$ mkdir ~/source
$ cd ~/source
$ git clone https://github.com/curio184/remotearm.git
```


Python実行環境の構築
------------

今回はPython3.7.2をインストールする。

```
Python3.7.2のソースをダウンロードする
$ mkdir /home/pi/tmp
$ cd /home/pi/tmp
$ wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
$ tar axvf ./Python-3.7.2.tgz
$ cd ./Python-3.7.2

ビルドツール・ライブラリをインストールする
$ sudo apt update
$ sudo apt install build-essential libbz2-dev libdb-dev libreadline-dev libffi-dev libgdbm-dev liblzma-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev uuid-dev tk-dev

Python3.7.2をビルドする
$ LDFLAGS="-L/usr/lib/arm-linux-gnueabihf" ./configure --enable-shared
$ make
$ sudo make install

Pythonのバージョンを確認する
$ python3.7 --version
Python 3.7.2

pipをアップデートする
$ sudo python3.7 -m pip install --upgrade pip

(不要であれば)Python3.7.2のソースを削除する
$ sudo rm -R /home/pi/tmp
```


Pythonの仮想環境を構築する
------------

```
Python3.7.2の仮想環境を構築する。
$ mkdir -p /home/pi/source/remotearm/.venv
$ cd /home/pi/source/remotearm/.venv
$ python3.7 -m venv py372
$ source py372/bin/activate
$ python --version
Python 3.7.2

基本パッケージのインストール
$ pip install --upgrade pip
$ pip install pylint
$ pip install autopep8
$ pip install rope
$ pip install ptvsd

Raspi制御パッケージのインストール
$ pip install RPi.GPIO

サーボモータードライバ「pca9685」のライブラリ
$ pip install adafruit-pca9685
```


VSCode実行環境の構築
------------

```
Community Build版のVSCodeをインストールする
$ sudo apt install code-oss -y --allow-unauthenticated
```

VSCodeでプロジェクトを起動する
------------

OpenProject.shをクリックします。

VSCodeの拡張機能をインストールする
------------

```
・Japanese Language Pack for Visual Studio Code
　(ms-ceintl.vscode-language-pack-ja)
・Bookmarks
　(alefragnani.bookmarks)
・Python
　(ms-python.python)
・autoDocstring
　(njpwerner.autodocstring)
・GitLens
　(eamodio.gitlens)
```
