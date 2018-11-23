关于
=======

本项目使用Pytorch识别简单的数字验证码，目的在于学习机器学习。
其中生成验证码的代码来自博客园：https://www.cnblogs.com/king-lps/p/8724361.html

使用
=======

安装依赖
------

执行::

 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

安装本项目需要的Python依赖包。

验证码生成
------

在项目根目录创建src文件夹，执行::

 python gen_captcha.py

即可在项目根目录中看到label.txt的答案文本，以及src文件夹中看到生成的验证码图片。

验证码识别
-----

TODO
