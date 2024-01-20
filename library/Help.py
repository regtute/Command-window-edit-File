update_date = '2024-1-20'

def help_list():
    print(f'---Helper---{update_date}-update--\n')

    print('--$@op')

    print('带*为选填')
    print('你可以通过 op (file_name) (*mode) (*encoding来使用)')
    print('特殊: 01$: op w w 来批量覆盖文件\n\n')

    
    print('--$@op w')
    print('你可以通过 op w w来批量覆盖文件')
    print('输入后,输入文件名(空格分隔)或是将多个文件拖入命令窗口')
    print('再输入需要写入的内容即可\n\n')

    print('--$ cp')
    print('你可以通过 cp 复制选中行(在已经用op打开指定文件的情况下)\n\n')

    print('--$ c')
    print('选中行 c 行号  --(在已经用op打开指定文件的情况下)\n\n')

    print('--$ w')
    print('写选中行 w@!(内容) --(在已经用op打开指定文件的情况下)\n\n')

    print('--$ save')
    print('保存文件 save (文件名.后缀名) --(在已经用op打开指定文件的情况下)')
def helps(s):
    if s == 'list':
        help_list()
        
    else:
        print(f'---Helper---{update_date}-update--')

        sl = s.split()
        if sl[0] == 'op':
            if len(sl) >= 2:
                if sl[1] == 'w':
                    print('你可以通过 op w w来批量覆盖文件')
                    print('输入后,输入文件名(空格分隔)或是将多个文件拖入命令窗口')
                    print('再输入需要写入的内容即可')
                
            else:
                print('带*为选填')
                print('你可以通过 op (file_name) (*mode) (*encoding来使用)')
                print('特殊: 01$: op w w 来批量覆盖文件')

        if sl[0] == 'cp':
            print('你可以通过 cp 复制选中行(在已经用op打开指定文件的情况下)')
        
        if sl[0] == 'c':
            print('选中行 c 行号  --(在已经用op打开指定文件的情况下)')
        if sl[0] == 'w':
            print('写选中行 w@!(内容) --(在已经用op打开指定文件的情况下)')
        if sl[0] == 'save':
            print('保存文件 save (文件名.后缀名) --(在已经用op打开指定文件的情况下)')

        print(f'---Helper---{update_date}-update--')