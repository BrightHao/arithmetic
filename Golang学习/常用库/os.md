### 作用
- 操作系统的相关操作

### 用法
1.file, err := os.Open(infile)  // infile 文件名
    打开文件
    后续使用 bufio.NewReader(file)进行文件的读取

2.file, err := os.Create(outfile)  // outfile 文件名
    创建文件

3.file.WriteString(str)
    向文件中写入字符串

4.file.Close()
    关闭文件，一般在函数中使用 defer file.Close()
