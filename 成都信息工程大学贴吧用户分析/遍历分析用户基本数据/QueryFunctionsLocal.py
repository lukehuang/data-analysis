import datetime

#
#
#从本地csv文件获取数据的版本
#
#全局变量，用来存放数据集，需要使用setDataSet函数设置数据集

DATA_SET = []
MAX_DATE = []
MIN_DATE = []
#result中的子项目结构：
#[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
#   0          1           2        3           4         5

#设置数据集
def setDataSet(dbs):
    DATA_SET.append( dbs )
    datalist = []
    for post in DATA_SET[0]:
        ##result中的子项目结构：
        #[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
        #   0          1           2        3           4         5
        #print(post[4])
        datalist.append(datetime.datetime.strptime(post[4],"%Y-%m-%d %H:%M:%S"))
    MAX_DATE.append(max(datalist))
    MIN_DATE.append(min(datalist))

#该函数用来查询指定字段在数据库中的出现次数
def countSergent(value):
    latestdate = queryDatasourceLatestTime()
    begdate = latestdate - datetime.timedelta(days=30)
    count30 = [x[2] for x in DATA_SET[0] if x[2]==value and datetime.datetime.strptime(x[4],"%Y-%m-%d %H:%M:%S")>begdate]
    ##[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
    count = [x[2] for x in DATA_SET[0] if x[2]==value]
    #print(count,len(DATA_SET[0]))
    return len(count),len(count30)

#从数据库查询包含指定字词的所有数据集
#返回值：包含指定字词的数据集列表
def queryWordContainListbyKeyword(word):
    ##[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
    datalist = [x[3] for x in DATA_SET[0] if x[3].find(word)>-1]
    return datalist

#从数据库查询指定作者的所有帖子信息
#返回值：指定作者的所有回帖信息
# [ [主题帖链接,贴吧名,作者,帖子内容,发帖时间,回复给sb,所在页面],[......],..... ]
def queryWordContainListbyAuthor(author):
    ##[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
    datalist = [x for x in DATA_SET[0] if x[2]==author]
    return datalist

#从数据库查询回复给指定用户的所有其它用户列表
#返回值：用户列表 
# [ "1","2",....]
def queryUserListbyReplyto(author):
    ##[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
    datalist = [x[2] for x in DATA_SET[0] if x[5]==author]
    return datalist

#从数据库查询指定用户回复给指定用户的帖子列表
#返回值：贴子列表
# [ "1","2",....]
def queryContentListbyAuthorToReplyto(fromauthor,toauthor):
    ##[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
    datalist = [x[3] for x in DATA_SET[0] if x[2]==fromauthor and x[5]==toauthor]
    return datalist

#从数据库查询最大日期
#返回值：一个最大日期
def queryDatasourceLatestTime():
    return MAX_DATE[0]

#从数据库查询小日期
#返回值：一个最小日期
def queryDatasourceEarlyTime():
    return MIN_DATE[0]

#从数据库查询指定作者的指定日期之间的数据集
#返回值：指定日期之间的数据集列表
# [ [主题帖链接,贴吧名,作者,帖子内容,发帖时间,回复给sb,所在页面],[......],..... ]
def queryContainListAfterTime(author,earlydatestr):
    earlydate = datetime.datetime.strptime(earlydatestr,"%Y-%m-%d %H:%M:%S")
    ##[帖子ID    储存贴吧名   回帖作者  回帖内容    回帖日期    回帖目标]
    datalist = [x for x in DATA_SET[0] if datetime.datetime.strptime(x[4],"%Y-%m-%d %H:%M:%S")>earlydate and author == x[2]]
    return datalist

