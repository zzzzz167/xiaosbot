import platform
os = platform.system()
print(os)
print(platform.platform())
print(platform.version())
print(platform.architecture())


def get_platform():
    '''获取操作系统名称及版本号'''
    return platform.platform()


def get_version():
    '''获取操作系统版本号'''
    return platform.version()


def get_architecture():
    '''获取操作系统的位数'''
    return platform.architecture()


def get_machine():
    '''计算机类型'''
    return platform.machine()


def get_node():
    '''计算机的网络名称'''
    return platform.node()


def get_processor():
    '''计算机处理器信息'''
    return platform.processor()


def get_system():
    '''获取操作系统类型'''
    return platform.system()


def get_uname():
    '''汇总信息'''
    return platform.uname()


def get_python_build():
    ''' the Python build number and date as strings'''
    return platform.python_build()


def get_python_compiler():
    '''Returns a string identifying the compiler used for compiling Python'''
    return platform.python_compiler()


def get_python_branch():
    '''Returns a string identifying the Python implementation SCM branch'''
    return platform.python_branch()


def get_python_implementation():
    return platform.python_implementation()


def get_python_version():
    '''Returns the Python version as string 'major.minor.patchlevel'
    '''
    return platform.python_version()


def get_python_revision():
    '''Returns a string identifying the Python implementation SCM revision.'''
    return platform.python_revision()


def get_python_version_tuple():
    return platform.python_version_tuple()


print('获取操作系统名称及版本号 : [{}]'.format(get_platform()))
print('获取操作系统版本号 : [{}]'.format(get_version()))
print('获取操作系统的位数 : [{}]'.format(get_architecture()))
print('计算机类型 : [{}]'.format(get_machine()))
print('计算机的网络名称 : [{}]'.format(get_node()))
print('计算机处理器信息 : [{}]'.format(get_processor()))
print('获取操作系统类型 : [{}]'.format(get_system()))
print('汇总信息 : [{}]'.format(get_uname()))
print('The Python build number and date as strings : [{}]'.format(
    get_python_build()))
print('Returns a string identifying the compiler used for compiling \
    Python : [{}]'.format(get_python_compiler()))
print('Returns a string identifying the Python implementation SCM branch : [\
    {}]'.format(get_python_branch()))
print('Returns a string identifying the Python implementation : [{}\
    ]'.format(get_python_implementation()))
print('The version of Python ： [{}]'.format(get_python_version()))
print('Python implementation SCM revision : [{}\
    ]'.format(get_python_revision()))
print('Python version as tuple : [{}]'.format(get_python_version_tuple()))
