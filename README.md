<p align="center">
  <img src="https://mcwiki-1301161188.cos.ap-hongkong.myqcloud.com/github/minecraft-lzh/logo1.png" width="150">
</p>

<h1 align="center">Minecraft 文言文資源包</h1>

## 安装
### 版本差异
- 无后缀：未翻译的部分使用英文。
- `_compatible`：兼容版本。未翻译的部分使用繁体中文。
- `_leaveblank`：留空版本。未翻译的部分留空。

请根据需求选择下载。
### 自行打包
我们提供了一个自动构建脚本（正式打包也使用）。
1. 下载源码：
``` bash
git clone https://github.com/dianliang/minecraft-lzh.git
```
2. 进入文件夹：
``` bash
cd minecraft-lzh
```
3. 运行Python命令：
``` bash
python build.py all
```
在文件夹中会出现`lzh.zip`、`lzh_compatible.zip`和`lzh_leaveblank.zip`四个资源包，名称和作用如上所述。

如果只需要常规的资源包，运行：
``` bash
python build.py normal
```
如果只需要加载兼容版本的资源包，运行：
``` bash
python build.py compatible
```
# 贡献
您有几种方法对此项目进行贡献：
- 大部分翻译需要标准译名，列表![见此](https://minecraft-zh.gamepedia.com/User:Miemie_method)。
- 修改这个Repoistory，并提出Pull Request。
   - 当您的贡献足够多，我们将会邀请您成为Collaborator。
## 授权
若您在本项目作出贡献，即表示您同意将您的贡献的版权赠予我们的团队，并允许我们对其进行包括但不限于再分发、商用和对其可使用范围进行限制。
# 协议
本资源包以GPL v3.0协议授权。

<p align="center">版权所有 Minecraft 文言文资源包团队 · 保留部分权力</p>
<p align="center">Copyright Minecraft-lzh Resourcepack Team · Some rights reserved</p>
