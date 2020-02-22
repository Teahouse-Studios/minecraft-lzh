# Minecraft 文言文資源包

大部分翻译需要标准译名，请点击此处帮助我们修改标准译名：https://minecraft-zh.gamepedia.com/User:Miemie_method 。对已有的文言译名产生质疑请移步该页面的讨论页，谢谢。

## 关于安装
### 几个版本的区别
- 无后缀：未翻译的部分使用英文。
- `_compatible`：兼容版本。未翻译的部分使用繁体中文。
- `_leaveblank`：留空版本。未翻译的部分留空。

请根据需求选择下载。
### 自己打包
#### 步骤
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
