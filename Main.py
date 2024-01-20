from library import Check, Help
import os
import pyperclip as cop
import re

print((Check.check_normal_start())[::-1])

print(f'Monica File Manager $make$@{(Check.errors())[::-1]}')                                                                                                           #regtute$make if you see the name is different to the $make$ you is download apirate
print('Monica_文件管理器$email$@tuyiwei0213@foxmail.com')
print('|----------------------------------------|')
while 1:
    inputv = input('>>:')
    inputvl = inputv.split()
    command = inputvl[0]

    # def config():

    def help_func():
        Help.helps(inputv.split('$')[1])


    def op_func():
        # global contl
        # contl = 0
        leng = len(inputvl)
        modes = 'r'
        if leng >= 2:
            file = inputvl[1]
            if leng >= 3:
                modes = inputvl[2]
            
                
            if leng >= 4:
                code = inputvl[3]
            else:
                code = 'utf-8'
            
        else:
            print('单独的命令! error alone')
            print('你可以输入help$想要了解的指令 或 help$list来显示帮助')
        # print(modes)
        count = 1
        if modes == 'r':
            # print('run')
            with open(file, mode=modes, encoding=code) as f:
                # lines = f.readlines()
                # print(len(lines))
                new = []
                # new1 = []
                for line in f:
                    text = f'█{count}█>>' + line
                    new.append(text)
                    
                    count +=1
                
                # print(count)
                new1 = new[:]
                # print(type(new1))
                
                new1[count-2] = new[count-2].replace('█>>', '██>')
                count1 = count - 1
                # print(new)
                for i in new1:
                    print(i, end='')
                while 1:
                    cont = input('\n>文件控制台>:')
                    contl = cont.split()
                    contl_w = cont.split('@!')
                    command_w = contl_w[0]
                    command_1 = contl[0]
                    
                    if command_1 == 'c':
                        num = int(contl[1])
                        count1 = num
                        # print(new)
                        new1 = new[:]
                        new1[num-1] = new[num-1].replace('█>>', '██>')
                        os.system('cls')
                        for i in new1:
                            print(i, end='')
                    elif command_1 == 'cp':
                        cop.copy(new[count1-1].replace(f'█{str(count1)}█>>', ''))
                    elif command_w == 'w':
                        value = contl_w[1]
                        new1[count1-1] = f'█{str(count1)}██>{value}\n'
                        new[count1-1] = f'█{str(count1)}█>>{value}\n'
                        os.system('cls')
                        for i in new1:
                            print(i, end='')
                    elif command_1 == 'save':
                        file_name = contl[1]
                        values = ''
                        for i in new1:
                            new_string = re.sub(r'█(\d)█>>', '', i)
                            new_string = re.sub(r'█(\d)██>', '', new_string)
                            values += new_string
                        with open(file_name, mode='w', encoding=code) as f1:
                            
                            f1.write(values)

        if modes == 'w':
            values1 = input('>File Choose>:')
            inputvl1 = values1.split()
            print(inputvl1)
            
            # inputvl.remove('op')
            writes = input('请输入>')
            for files in inputvl1:
                with open(files, mode='w', encoding=code) as f:
                    f.write(writes)


    if command == 'op':
        # print(command)
        # x = input()
        op_func()
    elif inputv.split('$')[0] == 'help':
        help_func()
    else:
        print('输入help$命令 来查看帮助 或是使用 help$list显示帮助列表')
        



    # print('\r1111' , end='', flush=True)
    # print('\r2222' , end='', flush=True) regtute$
    # print('\r8888' , end='', flush=True)
# x = input()
        
        # debug↑                                                                                                                                                                        #regtute$make if you see the name is different to the $make$ you is download apirate