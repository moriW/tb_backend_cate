# tb_backend_cate

Get Taobao Backend Spu Category with __ALL attribute__ and __ALL specifications__ 

淘宝的部分后端类目 以及全部类目的 __属性__ 和 __规格__

旨在为做电商的朋友们帮点小忙, 后端的spu 和 sku分类是个挺大的问题, 如果有这个数据 应该会简单很多


## Step

> I personally recommend run script on `iPython`

1. Download [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


2. Set Chrome Driver Path On `iPython`

```python
chrome_driver_path = './chromedriver'
```

3. run script in main.py
```python
from main import *
```

4. login on the chrome tab 

5. chose a category and run the script
```python
run3()
```

PS: It may __STOP__ when the launch page is the old one

PPS: It also __STOP__ when the category need some certify to launch



## 步骤

> 个人推荐`iPython`交互环境下运行

1. 下载[Chrome 驱动](https://sites.google.com/a/chromium.org/chromedriver/downloads)

2. 环境内设置驱动路径

```python
chrome_driver_path = './chromedriver'
```

3. 执行main
```python
from main import *
```

4. 在打开的页面中登录账号

5. 选定好类目然后执行代码
```python
run3()
```