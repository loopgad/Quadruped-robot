
## <div align="center">四足机器人视觉</div>


<details>
  <summary>目标检测</summary>

<br>
目录

- [题目](#题目)
- [数据集要求](#数据集要求)
- [题目要求](#题目要求)
- [链接](#链接)

#### 题目
  使用YOLOv5n模型实现六种动物的识别，五种动物包括鸟、猫咪、狗、马、大象和长颈鹿

#### 数据集要求
**Image**：
   - 分辨率640*640
**Label**：
   - 列1 - 目标类别id,列2 - 目标中心位置x,列3 - 目标中心位置y,列4 - 目标宽度w,列5 - 目标高度h。
   - x，y，w，h是小于1的浮点数，因为是经过对图像进行了归一化处理得到的值，也就是目标的真实的x，w值除以图像的宽度，y，h除以图像的高度。
**Classes**：
   - 一行代表一个类别，行号代表类别id。可以使用classes.json文件来描述数据集的类别信息，这样方便我们通过classes.json文件生成classes.txt用于训练，呈现时使用中文标签。


#### 题目要求

**视频录制**：录制一段识别包含鸟、猫咪、狗、马、大象和长颈鹿的随机3种动物的视频。
   - 视频要求：确保视频时长5-10秒，视频格式为指定格式（例如MP4），命名为“动物识别题视频”。
**文件夹命名和压缩打包**：
   - 将所有相关文件（视频、技术方案文档等）放入一个文件夹中，按照指定方式命名（例如"队伍名称"）。
   - 使用压缩软件将文件夹压缩成一个压缩包（例如"队伍名称.zip"），总压缩文件大小不超过200M。
**文件结构**： 
```
/队伍名称/
├── 技术方案文档.docx
├── 动物识别题视频.mp4
└── 其他文件
```

#### 链接
- [YOLOv5视频教程](https://www.bilibili.com/video/BV15F4m1E7MS/?spm_id_from=333.880.my_history.page.click&vd_source=eea65351cdee42099badad80d9c6eac3)
- [YOLOv5官方使用文档](https://docs.ultralytics.com/)
  
</details>


<details>
  <summary>opencv</summary>

<br>
  使用opencv库实现图形识别计数和QR码识别
  
</details>


## <div align="center">ROS</div>
