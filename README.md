# defect_product

2023年度山东大学软件学院暑期项目实训——工业品缺陷检测

即2023夏季英特尔oneAPI校园黑客松竞赛参赛作品

## 项目简介

针对工业品组装后可能出现缺少螺丝（缺陷）情况的出现，利用深度学习实现自动化检测

本项目针对实际工业的应用环境，通过图像分类的AI算法模型，识别合格和不合格物品，基于训练好的深度学习模型，建立Web服务：提供上传图片，同时识别图片中物品是否有缺陷的功能。

会议记录：详见Conference_Record.md

成员日志记录：详见log文件夹

## 团队成员

- 组长：李岩霖
- 组员：王秀宇，张新钧，王修智，方正，周星驰，玄小龙，刘川东
- 校内指导教师：戴鸿君
- 企业指导教师：张建宇，郑艳飞

## 技术路线

- 后端使用Flask，Web前端使用Vue，微信小程序开发
- 基于Tensorflow的迁移学习，使用Intel的深度学习模型推理优化方法
- 将后端部署在服务器上运行

## 开发计划

- 第一周（6.19，6.20，6.21，6.25）

  研究和学习阶段。团队分为后端算法组，前端开发组，项目管理组和文档研读组，这一阶段主要工作是学习新知识，找到若干适合解决该问题的模型

- 第二周（6.20-6.30）

  原型开发阶段。上游任务尽可能快的搭建出一个demo给下游任务，然后迭代

- 第三周（7.3-7.7）

  迭代和测试阶段，继续完善和丰富项目内容

- 第四周（7.10-7.13）

  项目的收尾阶段

## 代码导读

- WeChatProject：微信小程序前端页面
- VueProject：Web前端页面
- FlaskProject：flask后端以及Tensorflow模型训练算法，以及软件测试代码、模型量化代码
