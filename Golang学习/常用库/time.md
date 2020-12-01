### 作用
时间相关操作

### 用法
1.t1 := time.Now()  
    输出现在的时间

2.t2.Sub(t1)  // t1 t2均为时间格式
    t2减去t1的时间差

3.time.Sleep(n)  // n为int型
    休眠n ns（纳秒）  1ms = 10^6 ns
