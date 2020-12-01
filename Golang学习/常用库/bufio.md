### 作用
读取字符串，读取文件内容等

### 用法
1.br := bufio.NewReader(file)  // file为已经打开的文件
    读取文件内容

2.line, isPrefix, err := br.ReadLine()
    读取一行内容
    line为字符数组，isPrefix为真表示内容太长



