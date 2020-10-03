# Minecraft 文言文資源包

![logo](https://mcwiki-1301161188.cos.ap-hongkong.myqcloud.com/github/minecraft-lzh/logo1.png)

## 作用

這個資源包為Minecraft新增了一個語言：文言文。

## 使用

請在[release頁面](https://github.com/dianliang233/minecraft-lzh/releases)選擇版本下載，像其他資源包一樣復制到你對應的 `.minecraft/resourcepacks/` 目錄中（[MCBBS上的教程](https://www.mcbbs.net/thread-880869-1-1.html)）（MultiMC、HMCl或其他分離版本的啟動器請自行查找）。資源包新建了一個語言，安裝啟用後在語言設置中選擇“**文言（華夏）**”即可體驗。

### 版本差異

* 無後綴：未翻譯的部分使用英文。
* `_compatible` ：兼容版本（避免 Mod 漢化失效）。未翻譯的部分使用繁體中文。
* `_leaveblank` ：留空版本。未翻譯的部分留空。
* `_legacy` ：舊版本。用於1.12.2及以下。

請根據需求選擇下載。在目前仍處於早期階段的情況下，我們推薦您使用兼容版本。

### 自行打包

我們提供了一個自動構建腳本（正式打包也使用）。

1. 下載源碼：

``` bash
git clone https://github.com/Teahouse-Studios/minecraft-lzh.git
```

2. 進入文件夾：

``` bash
cd minecraft-lzh
```

3. 運行Python命令：

``` bash
python preset_build.py
```

在 `builds` 文件夾中會出現 `lzh.zip` 、 `lzh_compatible.zip` 、 `lzh_leaveblank.zip` 和 `lzh_legacy.zip` 四個資源包，名稱和作用如上所述。

如果只需要常規的資源包，運行：

``` bash
python build.py normal
```

如果只需要加載兼容版本的資源包，運行：

``` bash
python build.py compat
```

更詳細的用法請運行：

``` bash
python build.py -h
```

## 貢獻

您有幾種方法對此項目進行貢獻：

* 大部分翻譯需要標準譯名，列表[見此](https://minecraft-zh.gamepedia.com/User:Miemie_method)。
* 修改這個Repoistory，並提出Pull Request。
  * 當您的貢獻足夠多，我們將會邀請您成為Collaborator。

### 要求

> 一、正文書繁體，以承古風。常言不為限。  
> 二、君子之善，以禮相重。勿廣告、行淫、言辱等不雅之語。

### 授權

若您在本項目作出貢獻，即表示您同意將您的貢獻的版權贈予我們的團隊，並允許我們對其進行包括但不限於再分發、商用和對其可使用範圍進行限制。

## 協議

本資源包以GPL v3.0協議授權。

茶館工作室出品

版權所有© Minecraft 文言文資源包團隊。保留部分權力。Minecraft 文言文資源包團隊隸屬於茶館工作室。

A Teahouse Studios Work

Copyright Minecraft-lzh Resourcepack Team. Some rights reserved. Minecraft-lzh Rresourcepack Team is affiliated to Teahouse Studios.
