import re

# -----------------------------
# #10、括号() ---分组
# ##。
"""
括号称之为 正则表达式的 组选择。

组 就是把 正则表达式 匹配的内容 里面 其中的某些部分 标记为某个组。

我们可以在 正则表达式中 标记 多个 组

为什么要有组的概念呢？因为我们往往需要提取已经匹配的 内容里面的 某些部分的信心。
"""
text10 = """
苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的
"""
p10 = p = re.compile(r'(.+)，.{3}(.{2})', re.M)  # 选择括号里的
print(p10.findall(text10))
# ##==>> [('苹果', '绿色'), ('橙子', '橙色'), ('香蕉', '黄色')]

# -----------------------------
# #11、让点匹配换行
# ##。点 是 不匹配换行符 的，可是有时候，特征 字符串就是跨行的，
# 比如要找出下面文字中所有的职位名称
content11 = """
<div class="el">
        <p class="t1">           
            <span>
                <a>Python开发工程师</a>
            </span>
        </p>
        <span class="t2">南京</span>
        <span class="t3">1.5-2万/月</span>
</div>
<div class="el">
        <p class="t1">
            <span>
                <a>java开发工程师</a>
            </span>
		</p>
        <span class="t2">苏州</span>
        <span class="t3">1.5-2/月</span>
</div>
"""
p11 = re.compile(r'class=\"t1\">.*?<a>(.*?)</a>', re.DOTALL)
for one in p11.findall(content11):
    print(one)
