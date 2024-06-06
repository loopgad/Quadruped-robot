

YOLOv5 [release v6.2](https://github.com/ultralytics/yolov5/releases) 带来对分类模型训练、验证和部署的支持！详情请查看 [发行说明](https://github.com/ultralytics/yolov5/releases/v6.2) 或访问我们的 [YOLOv5 分类 Colab 笔记本](https://github.com/ultralytics/yolov5/blob/master/classify/tutorial.ipynb) 以快速入门。

<details>
  <summary>分类网络模型</summary>

<br>

我们使用 4xA100 实例在 ImageNet 上训练了 90 个 epochs 得到 YOLOv5-cls 分类模型，我们训练了 ResNet 和 EfficientNet 模型以及相同的默认训练设置以进行比较。我们将所有模型导出到 ONNX FP32 以进行 CPU 速度测试，并导出到 TensorRT FP16 以进行 GPU 速度测试。为了便于重现，我们在 Google 上进行了所有速度测试 [Colab Pro](https://colab.research.google.com/signup) 。


