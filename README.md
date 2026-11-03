# 小牛电商系统 接口自动化测试项目

基于 **pytest + requests + Allure** 的接口自动化测试项目，覆盖小牛电商系统核心接口（登录、商品、购物车、订单），共 **34 条自动化用例**。

## 技术栈

| 技术 | 用途 |
|---|---|
| Python 3.13 | 编程语言 |
| pytest | 测试框架（用例管理、断言、参数化） |
| requests | HTTP 接口请求 |
| allure-pytest + allure | Allure 测试报告（仪表盘、分类、历史趋势） |

## 目录结构

```
PythonTestCode/
├── config.ini            # 配置：服务器地址、账号密码（换环境只改这里）
├── conftest.py           # pytest 入口（项目根目录定位）
├── pytest.ini            # pytest 配置（测试路径、报告参数）
├── README.md             # 项目说明（本文件）
├── common/
│   ├── request_util.py   # 公共封装：登录函数、读取配置
│   ├── log_util.py       # 日志工具（输出到 logs/test.log）
│   └── read_data.py      # 数据读取（JSON 数据驱动）
├── data/
│   └── test_api_login.xlsx   # 登录测试数据（Excel 数据驱动）
├── logs/
│   └── test.log          # 运行日志
├── scripts/
│   └── test_api.py       # 接口测试用例（34 条）
├── report/               # pytest-html 报告输出
├── allure-results/       # Allure 原始数据（运行生成）
└── allure-report/        # Allure HTML 报告（生成）
```

## 快速开始

### 1. 安装依赖

```bash
pip install pytest requests allure-pytest
```

Allure 命令行工具（生成报告用，需要 Java 环境）：

```bash
npm install -g allure-commandline --registry=https://registry.npmmirror.com
```

### 2. 运行测试

```bash
python -m pytest
```

### 3. 查看报告

**pytest-html 报告**：运行后打开 `report/login_report.html`

**Allure 报告**：

```bash
allure generate allure-results -o allure-report --clean
allure serve allure-results    # 启动本地服务，浏览器自动打开
```

## 测试内容

覆盖 4 个模块、34 条用例：

| 模块 | 用例数 | 覆盖场景 |
|---|---|---|
| 登录接口 | 4 条 | 正确登录、错误密码、错误用户名（数据驱动） |
| 商品接口 | 3 条 | 带 token 查询、不带 token 返回 401、商品存在性 |
| 购物车接口 | 2 条 | 带 token 加购、不带 token 返回 401 |
| 订单接口 | 2 条 | 不带 token 返回 401、下单成功（自给自足） |

## 框架设计特点

- **配置分层**：服务器地址、账号密码放 `config.ini`，换环境只改配置文件
- **数据驱动**：测试数据放 JSON 文件，参数化读取，新增数据不用改代码
- **日志记录**：登录请求/响应写入 `logs/test.log`，失败可追溯
- **用例独立**：下单用例自给自足（先清购物车→加购→下单），不依赖环境残留数据
- **框架分层**：配置层 → 公共层（common）→ 用例层（scripts）

## 运行效果

Allure 报告：**34 条用例、通过率 100%**、4 秒 266 毫秒跑完。
