# Python 套件
套件 a.k.a 別人寫好的 code，可以讓你快速完成看似很複雜的功能。當上工程師的第一步就從好好利用前人的智慧開始。這邊會教你怎麼使用套件管理軟體，並安裝接下來會用到的套件們。

## Step 0
首先我們要先安裝 Mac 上的套件管理軟體 [Homebrew](https://brew.sh/index_zh-tw)。
### Homebrew 可以做什麼？
Homebrew 可以在 Mac 上安裝系統沒有的套件，例如 Wget 這種工程師常用的軟體。
### 安裝 Homebrew
打開你的終端機貼上
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Step 1
在安裝完 Homebrew 後，就可以重新安裝 Python。這邊要安裝 Python3 跟 Python3 的套件管理軟體 -- PIP。  
一樣打開 terminal 打上 
```
brew install python3 
```

接著貼上下面指令看看有沒有安裝成功
```
python3 --version && pip3 --version
```

到這邊事前準備就完成了！