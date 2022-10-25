给爱妻写的小助手
python3

环境搭建：

    1、下载安装python3、pycharm、nodejs

    2、pip安装
        pip install -r requirements.txt
        pip install pypinyin //拼音
        pip install openpyxl // word处理
        pip install pypiwin32 //windows 专用模块
        pip install requests // 网络请求
        pip install pyinstaller // 打包

    3、目录解析
        ├── src 代码
        |    ├── cripts 脚本目录
        |    ├── tmp     临时放的东西
        |    ├── tools   工具
        |    ├── views   页面
        ├── app.py 根window
        ├── README 说明书
        └── requirements.txt 存放软件依赖的外部Python包列表
    4、打包
        pyinstaller -F -w main.py

        -F，-onefile     dist中产生单个的可执行文件                 eg:pyinstaller -F demo.py
        -D，--onedir     产生一个目录（包含多个文件）作为可执行程序 　　eg:pyinstaller -D demo.py
        -a，--ascii	不包含 Unicode 字符集支持
        -d，--debug	产生 debug 版本的可执行文件
        -w，--windowed，--noconsolc   指定程序运行时不显示命令行窗口（仅对 Windows 有效）  eg:pyinstaller -w demo.py
        -c，--nowindowed，--console   指定使用命令行窗口运行程序（仅对 Windows 有效）  　　eg:pyinstaller -c demo.py
        -o DIR，--out=DIR	指定 spec 文件的生成目录。如果没有指定，则默认使用当前目录来生成 spec 文件
        -p DIR，--path=DIR   设置 Python 导入模块的路径（和设置 PYTHONPATH 环境变量的作用相似）。也可使用路径分隔符（Windows 使用分号，Linux 使用冒号）来分隔多个路径
                                eg:pyinstaller -p E:\python\Lib\site-packages demo.py
        -n NAME，--name=NAME	指定项目（产生的 spec）名字。如果省略该选项，那么第一个脚本的主文件名将作为 spec 的名字