
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    # print(str_name)
    
    # if(b_only_download):
        # download_source(str_name,"https://github.com/madler/zlib.git")
        # return
        
    # STR_CGG = ''
    # if(dict_config['static']):
        # STR_CGG += ''
    # else:
        # STR_CGG += ''
        
    source_dir = os.getcwd() + '/../prebuild/crashrpt-code-4616504670be5a425a525376648d912a72ce18f2'
    
    configure(str_name,dict_config,"","",source_dir)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    