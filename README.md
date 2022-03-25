[Gitee](https://gitee.com/haujet/blink-prompt.git)　|　Github 

# 眨眼提示

## ⭐ 简介

功能：每过 n 秒钟让屏幕眨一下眼睛，以此让屏幕提醒用户：该眨眼了

## 📝 背景

人在正常视物的时候，每分钟眨眼约20次。但认真在看屏幕时，最少的时候一分钟只眨眼2次到3次。眨眼的次数变少会使眼睛暴露在空气中的时间变长，让眼睛干涩，易患上干眼症。

程序目的：每过「间隔时长」，就让屏幕瞬间黑一下，提醒用户眨一下眼

程序原理：在屏幕上叠加一个黑色全屏贴图，将它的透明度设为 0，每过「间隔时长」，就将透明度设为「显现透明度」，再经过「显现时长」，就将透明度设回 0，其中，「显现透明度」可以控制黑屏的深浅：

* 当它为 1 时，就是全黑
* 当它为 0.1 时，就是稍微暗一下

## ✨ 特性

目前就是一个 python 脚本，安装 python，再 `pip install PySide2` 之后，就可以直接运行脚本了。

## 💡 使用

将仓库克隆下来，进入仓库文件夹，先安装依赖库：

```
pip install -r requirements.txt
```

然后就可以以模块的方式运行：

```
python -m src
```

或者进入 `src` 文件夹，直接运行：

```
python __main__.py
```

## 🔋 打赏

如果你愿意，可以以打赏的方式为我充电：

![sponsor](assets/sponsor.png)

## 😀 交流

如果有软件方面的反馈可以提交 issues，或者加入 [QQ 群：1146626791](https://qm.qq.com/cgi-bin/qm/qr?k=DgiFh5cclAElnELH4mOxqWUBxReyEVpm&jump_from=webapi) 