# pairwise-instance-step-rate

## 领域

游戏、图形与多媒体

## 主题

实例化属性步进率

## 说明

divisor 按属性、上传完成绑定与同帧长度。

初始状态下 `graphics/instance_step_rate.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
