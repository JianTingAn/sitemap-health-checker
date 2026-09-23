# Sitemap 健康检查器

面向百度蜘蛛抓取引导的 Sitemap 检查工具，用于发现 XML 格式、重复 URL、失效链接和更新时间异常。

## 核心功能
- 检查 Sitemap URL 结构和重复项
- 统计 URL 数量、状态码与更新时间
- 标记失效链接和不可访问页面
- 输出适合定时任务处理的 JSON 数据

## 使用
```powershell
python tool.py --demo
python tool.py --input sample.csv --json
```
建议把规范、稳定、可访问的 URL 放入 Sitemap，并在 robots.txt 中声明地址。本项目不保证收录结果。

官网：https://jta.mobi  
QQ群：1039545483

## 许可证
MIT License
