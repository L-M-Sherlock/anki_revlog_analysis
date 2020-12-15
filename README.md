# Anki revlog 数据清理与分析

## 获取原始数据

### 数据库查看工具

Anki 的数据库用的是 SQLite，推荐使用 DB Browser for SQLite 来查看和导出复习数据

下载地址：http://www.sqlitebrowser.org/dl/

### 打开 Anki 数据库

下载并安装好上面这个工具之后，按照以下步骤即可打开 Anki 数据库：

1. 打开 DB Browser，文件 > 打开数据库

![image-20201215212401770](Anki%20revlog%20%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86%E4%B8%8E%E5%88%86%E6%9E%90.assets/image-20201215212401770.png)

2. 找到你 Anki 本地数据库的位置，通常这个位置是 `C:\Users\你电脑的用户名\AppData\Roaming\Anki2\你 Anki 本地配置的名称\`

记得把右下角这个改成所有文件，因为 Anki 的数据库后缀不是 db 也不是 sqlite。

改好后如果你找到的位置是对的，那么就能看到 `collection.anki2` 的文件了

![image-20201215212530874](Anki%20revlog%20%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86%E4%B8%8E%E5%88%86%E6%9E%90.assets/image-20201215212530874.png)

3. 提取数据

打开后转到执行 SQL，输入以下 SQL 语句：

```sql
SELECT id, cid, ease, lastIvl, type
FROM revlog
WHERE type != 2
;
```

然后点

![image-20201215213157758](Anki%20revlog%20%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86%E4%B8%8E%E5%88%86%E6%9E%90.assets/image-20201215213157758.png)

就能得到以下结果

![image-20201215212944362](Anki%20revlog%20%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86%E4%B8%8E%E5%88%86%E6%9E%90.assets/image-20201215212944362.png)

再点击

![image-20201215213226185](Anki%20revlog%20%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86%E4%B8%8E%E5%88%86%E6%9E%90.assets/image-20201215213226185.png)

就能将数据导出成 csv 格式，用 excel 打开就能看到这样的数据：

![image-20201215213406428](Anki%20revlog%20%E6%95%B0%E6%8D%AE%E6%B8%85%E7%90%86%E4%B8%8E%E5%88%86%E6%9E%90.assets/image-20201215213406428.png)

里面没有敏感数据，大家可以安心分享。