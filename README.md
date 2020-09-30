# Vue-Separate-Js
[![Python](https://img.shields.io/badge/python-3-orange)](https://www.python.org/downloads/release/python-370/)
[![Twitter](https://img.shields.io/twitter/url?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fhaoleiqin%2FVue-Separate-Js)
[![GitHub stars](https://img.shields.io/github/stars/haoleiqin/Vue-Separate-Js)](https://github.com/haoleiqin/Vue-Separate-Js/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/haoleiqin/Vue-Separate-Js)](https://github.com/haoleiqin/Vue-Separate-Js/issues)

将JS从Vue中分离出来作为单JS文件

#### 1.复制需要分离的.vue文件进 dist文件夹中
#### 2.两种分离形式
#####  a.分离为 <script src="./index.js"></script> 方式,运行 python src_type.py
#####  b.分离为 import js form './index.js'; export default js;

#### 1.copy the .vue file to dist/ directory
#### 2.run python main.py
#### 3.check the result in dist/ directory

```
PS:
do not include // </script>  or /** </script> **/

the script tag can not include in comments

```

Python 3

![1](https://github.com/haoleiqin/Vue-Separate-Js/blob/master/res/img/1.png?raw=true)

![2](https://github.com/haoleiqin/Vue-Separate-Js/blob/master/res/img/2.png?raw=true)

![3](https://github.com/haoleiqin/Vue-Separate-Js/blob/master/res/img/3.png?raw=true)
