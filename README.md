# 怎么使用

## python版本

**3.8**

## 下载chrome引擎

https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/

选择适合您电脑的版本

**设置chromedriver为环境变量**

- windows

  > 1.下载Chromedriver：（下载路径： https://sites.google.com/a/chromium.org/chromedriver/downloads）
  > 2.将chromedriver.exe拷贝至谷歌浏览器目录（如 C:\Program Files\Google\Chrome\Application）
  > 以及python根目录（C:\Python27）。
  > 3.将谷歌浏览器环境变量添加到path（C:\Users\HD003\AppData\Local\Google\Chrome\Application）。

- linux&Mac OS

> 将下载好的chrome driver添加到$PATH

## 安装依赖

```
在目录下运行
sudo pip install -r requirements.txt
```

## 如何运行

```shell
python ./demo.py
```

