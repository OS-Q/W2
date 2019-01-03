# W2：[数字信号](https://github.com/OS-Q/W2) 

[![sites](OS-Q/OS-Q.png)](http://www.OS-Q.com)

#### 归属信号采集：[M1](https://github.com/OS-Q/M1)

#### 关于系统架构：[OS-Q](https://github.com/OS-Q/OS-Q)

## [平台描述](https://github.com/OS-Q/W2/wiki) 

数字信号采集平台，通过驱动相应板载数字传感器获得数据

### [共用资源](https://github.com/OS-Q/W2/wiki) 


---

- 边缘设备命名规则：体系 Q：[1,4] -> 节点 M：[1,12] -> 平台 W：[1,52] -> 设备 D：[1,365]

- naming patterns：system Q[1,4] -> node M[1,12] -> platform W[1,52] -> device D[1,365]

## [包含设备](https://github.com/OS-Q/W2/wiki) 

#### D8：[温湿采集](https://github.com/OS-Q/D8)

用于采集分布的温湿度信息

#### D9：[光强采集](https://github.com/OS-Q/D9)

用于采集各种光线辐照强度

#### D10：[压力采集](https://github.com/OS-Q/D10)

用于采集压力数据，包括气压

#### D11：[气体采集](https://github.com/OS-Q/D11)

集成设备用于识别气体成分数据

#### D12：[声强采集](https://github.com/OS-Q/D12)

用于采集声音强度数据

#### D13：[运动采集](https://github.com/OS-Q/D13)

包括运动加速度和震动等数据

#### D14：[状态采集](https://github.com/OS-Q/D14)

用于采集设备的姿态和方位

## [同级平台](https://github.com/OS-Q/M1/wiki)

#### W1：[模拟信号](https://github.com/OS-Q/W1)

用于模拟信号的采集转换

#### -> W2：[数字信号](https://github.com/OS-Q/W2)

用于数字信号驱动和采集

#### W3：[阈值监控](https://github.com/OS-Q/W3)

用于实时监控阈值被触发

#### W4：[特殊平台](https://github.com/OS-Q/W4)

用于处理特殊信号的采集

---

####  qitas@qitas.cn
###  [Q redefined the scope of Operation System](http://www.OS-Q.com)
####  2019-1-1
