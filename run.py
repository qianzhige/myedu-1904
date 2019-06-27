import pytest
from day04 import Shell

if __name__ == '__main__':

    shell = Shell.Shell()
    # pytest.main(['-s','-q','./day04'])

    # pytest.main(['-s','-q','--alluredir','/Report/xml','./day04'])

    #run在里面的'./'当前目录里面

    # pytest.main(['-s', '-q', './'])

    pytest.main(['-s','-q','--alluredir','./Report/xml','./day04'])

    shell.invoke('allure generate ./Report/xml -o ./Report/html --clean')

    # 数据驱动测试  实战
