import requests
import datetime
# 最后修改于 2022-11-30 by:一介布衣 12-13
def _time():
    _time=datetime.datetime.now().strftime('%Y-%m-%d')
    return _time
body={}

# http://www.360duguanli.com/pointwx/index.html?userid=0990146e-a614-11e8-b221-5254002a76db&userName=%E7%9F%B3%E6%99%93%E8%92%99&role=2&companyCode=TQJT&menu=a,b,b1,b2,b3,b4,b5,c,c1,c2,c3,c4,c5,c6,c7,c8,d,e,f,g,h,i,j,k,l,m#/buckle/reg

id = {
"傅艳":"0cb53d54-a614-11e8-b221-5254002a76db",
"冯丽娜":"2cd927b367eb42aba8b45659185f96ab",
"冷同飞":"0a9b5c28-a614-11e8-b221-5254002a76db",
"初少佩":"d8441c96538d408e8fe499aa4afa7122",
"张彩惠":"0a5d2745-a614-11e8-b221-5254002a76db",
"杨永康":"0a65e155-a614-11e8-b221-5254002a76db",
"柴晓惠":"0aaa045f-a614-11e8-b221-5254002a76db",
"毛元珍":"dd7428c7a8324db4a5a80905e5eb78c0",
"王杰":"0a105643-a614-11e8-b221-5254002a76db",
"王美君":"0c45a15b-a614-11e8-b221-5254002a76db",
"石晓蒙":"0990146e-a614-11e8-b221-5254002a76db",
"范作凯":"7cf81365583b4ca6bd47c20c450e7e28",
"刘慧":"078ec109-a614-11e8-b221-5254002a76db",
"崔宁":"0c3d784f-a614-11e8-b221-5254002a76db",
"王峰":"07872c9b-a614-11e8-b221-5254002a76db",
"余亚蕾":"09b35c2c-a614-11e8-b221-5254002a76db",
"姜磊":"09f86dcc-a614-11e8-b221-5254002a76db",
"王超":"0969ea1b-a614-11e8-b221-5254002a76db",
"金鹏":"0a448abd-a614-11e8-b221-5254002a76db",
"战卫卫":"0ac196b0-a614-11e8-b221-5254002a76db",
"杜磊强":"0c973c19-a614-11e8-b221-5254002a76db",
"王明霞":"07eea484-a614-11e8-b221-5254002a76db",
"邵晓芬":"11963b4740ef4eb4a19924efcbefc2b7",
"王丹丹":"0ad9c696-a614-11e8-b221-5254002a76db",
"石玉兰":"05e56585-a614-11e8-b221-5254002a76db",
"矫美霞":"7ab22dda77c348b697e0100ef0ae911b",
"张丽丽":"0977f955-a614-11e8-b221-5254002a76db",
"李琛霞":"083d71e8-a614-11e8-b221-5254002a76db",
"张勇杰":"14d13490b83345789b01ab3c419f62e6",
"张召鹏":"9729ced948304b3ba6fe291cabfce762",
"尚梦梦":"6d9f337249a34608b039a5a560a2d994",
"张远":"a8a70ad2a25b4b68b0c482dd0a72066a",
"窦朝财":"082dea36-a614-11e8-b221-5254002a76db",
"杜磊强":"09542411-a614-11e8-b221-5254002a76db",
"纪红专":"7b77f65d-a616-11e8-b221-5254002a76db",
"王明霞":"07eea484-a614-11e8-b221-5254002a76db",
"金城":"0a4cca19-a614-11e8-b221-5254002a76db",
"吴非非":"0a6d88c1-a614-11e8-b221-5254002a76db",
"唐莉娜":"0a17c81e-a614-11e8-b221-5254002a76db",
"贾伟伟":"0cada285-a614-11e8-b221-5254002a76db",
"杨德斌":"09627472-a614-11e8-b221-5254002a76db",
"王聪聪":"0c5f1839-a614-11e8-b221-5254002a76db",
"代琦":"9b66271b00e34077a86789ab8f866cf3",
"车礼刚":"07b48d61-a614-11e8-b221-5254002a76db",
"王文利":"073b7259-a614-11e8-b221-5254002a76db",
"李京":"07713564-a614-11e8-b221-5254002a76db",
"陈知芹":"073369b4-a614-11e8-b221-5254002a76db",
"胡国玲":"0919fdd4-a614-11e8-b221-5254002a76db",
"赵晓丽":"07c412c8-a614-11e8-b221-5254002a76db",
"陈甜甜":"07e5c757-a614-11e8-b221-5254002a76db",
"李伟健":"066f19a4-a614-11e8-b221-5254002a76db",
"尚鑫":"07cbea81-a614-11e8-b221-5254002a76db",
"辛淑珍":"08882de6-a614-11e8-b221-5254002a76db",
"杨金萍":"05d78a0f-a614-11e8-b221-5254002a76db",
"代瑞燕":"15a12407d57e4c5892de72c6e769b891",
"李瑞晓":"0805aa70-a614-11e8-b221-5254002a76db",
"杨静":"7ed6b01e84b44a889fa782767a67df29",
"杨竹青":"f7f6394e06464ddaaf5609a692dcc86c",
"杨立城":"a40d474be8b14ee3bcd8f53aff155cfe",
"郭春光":"83b1e6a9505c4acfab5be6d283221d65",
"王显军":"be542aafc1c5490e91b34796249c8382",
"柳杨":"08a63585-a614-11e8-b221-5254002a76db",
"孙杨杨":"ee953bcef79944c59f7244f6d601c4d2",
"张瑛":"5d165196627140258d0b605b959889e2",
"季彩惠":"08ccd16f-a614-11e8-b221-5254002a76db",
"尹婷婷":"a208b796bbc84be387cdef64615ce5e2",
"曲亚男":"089f198e-a614-11e8-b221-5254002a76db",
"于建林":"081de6ec-a614-11e8-b221-5254002a76db",
"梁波":"b0b78d81bc9e4ef0bd4e858b57779093",
"陈娜":"362ac6f7395d4075a187d5c723e5c5d2",
"苗晓艳":"17055029b95a412eaca7d587868fc0ef",
"刘海静":"29a5c0481a29415d8e6396dfb002b02b",
"于汉道":"0a08bc96-a614-11e8-b221-5254002a76db",
"李聪":"4eda40efc79143fd87d584ebbff33ba9",
"万青旭":"c21efdff05854a41a06d8751d6387ba5",
"史旭东":"09e878e0-a614-11e8-b221-5254002a76db",
"官艳林":"09ca25ef-a614-11e8-b221-5254002a76db",
"李超":"ef2d922b1cf14b3595d4e7d8b48dcfb9",
"袁丽娜":"09e083ce-a614-11e8-b221-5254002a76db",
"朱明友":"09ab5779-a614-11e8-b221-5254002a76db",
"权新建":"2b986fe5a4bd480f9e7bb788eb505f26",
"李吉孟":"7b3cb23c-a616-11e8-b221-5254002a76db",
"张磊":"09d92326-a614-11e8-b221-5254002a76db",
"刘振涛":"7ad0e8cb-a616-11e8-b221-5254002a76db",
"艾振章":"08fb2b68-a614-11e8-b221-5254002a76db",
"王春会":"ca7e34852b254bc4b64e44531471031e",
"徐帅":"092201ed-a614-11e8-b221-5254002a76db",
"刘咏暄":"9ec4d422848140099970123b3b506b67",
"林大伟":"2d3ab69e7fcd4d9c891988a63c307c97",
"付晶":"d7053717c3c14f2780ce646e1bbb273b",
"王春莉":"f69623d0fd8c4081af7efffe2f69637a",
"王丰建":"7c00b84f-a616-11e8-b221-5254002a76db",
"徐洪强":"0c581c1b-a614-11e8-b221-5254002a76db",
"曹军":"08675ecc-a614-11e8-b221-5254002a76db",
"苗欣雅":"a4bd75ec44944085a59e16292e5a0845",
"方士超":"08579076-a614-11e8-b221-5254002a76db",
"王磊":"cde57fac5e384f13a8ef899ce0332be5",
"纪延春":"58b8e2ee20b64967b3dcc053f66ca8ac",
"石明涛":"0941f699-a614-11e8-b221-5254002a76db",
"石藏宗":"7f20b2c0b60e46c1be83f60d0afedb99",
}
def _post(tag,name,name1,name2,name3):
    try:
        print(id[name])
    except:
        print('找不到-'+name)
        return
    try:
        print(id[name1])
    except:
        print('找不到-'+name1)
        return
    try:
        print(id[name2])
    except:
        print('找不到-'+name2)
        return
    #取当前日期
    time = _time()
    # time = '2022-08-29'

    body['url'] = "http://82.156.9.53/wx/cp/points/buckle/addBuckle/savebuckle"
    body['headers'] = {
        'Host': '82.156.9.53',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.360duguanli.com',
        'Referer': 'http://www.360duguanli.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    if name3 == '金鹏':
        bpoints = '35'
    else:
        bpoints = '50'
    print(bpoints)
    body['data'] = {
        'userId': id[name3],
        'companyCode': 'TQJT',
        'subject': '',
        'subjectId': tag,  #自定义事件
        # 'flowId': 'fe1999b1f9ca45d69b2772fcfb4c4632',   #未知
        'context': '',
        'targetId': id[name], #给谁加
        'recordDate': time,
        'apoints': '0',
        'bpoints': bpoints,
        'firstAuditById': id[name1],   #初审
        'secondAuditById': id[name2],  #终审
        'copyById': '',
        'copyByName': '',
        'remark': '',
        'bpointsIcon': 'true',
        'caseTypeValue': '1',
    }
    response = requests.post(url=body['url'],data=body['data'],headers=body['headers'])
    print(response.text)


#### 石晓蒙 #####
def post_all():
	print(_time())
	_post('积极帮助车主找发动机号','杨永康','战卫卫','杜磊强','石晓蒙')
	_post('积极帮助车主卸车牌','杨永康','战卫卫','杜磊强','石晓蒙')
	# _post('积极打印出库单','刘慧','车礼刚','王明霞','石晓蒙')
	# _post('积极转发朋友圈广告','刘慧','车礼刚','王明霞','石晓蒙')
	_post('工作积极主动','张彩惠','战卫卫','杜磊强','石晓蒙')
	# _post('积极受理窗口业务','张彩惠','战卫卫','杜磊强','石晓蒙')
	_post('积极清理区域卫生','冷同飞','战卫卫','杜磊强','石晓蒙')
	# _post('帮助客户打印发票','冷同飞','战卫卫','杜磊强','石晓蒙')
	_post('帮助同事打印免检贴','傅艳','战卫卫','杜磊强','石晓蒙')
	_post('热心服务客户','傅艳','战卫卫','杜磊强','石晓蒙')
	_post('帮助车主复印材料','柴晓惠','战卫卫','杜磊强','石晓蒙')
	_post('主动沟通工作','柴晓惠','战卫卫','杜磊强','石晓蒙')
	_post('积极出库物资','毛元珍','王亚平','王亚平','石晓蒙')
	_post('积极核对物资表','毛元珍','王亚平','王亚平','石晓蒙')
	_post('积极帮助客户封证','王美君','战卫卫','杜磊强','石晓蒙')
	_post('积极预约审车','王美君','战卫卫','杜磊强','石晓蒙')
	_post('帮助为车主办理过户','初少佩','战卫卫','杜磊强','石晓蒙')
	# _post('帮助给同事打饭','初少佩','战卫卫','杜磊强','石晓蒙')
	_post('积极联系招生','王杰','战卫卫','杜磊强','石晓蒙')
	# _post('积极预约审车','王杰','战卫卫','杜磊强','石晓蒙')
	_post('积极拍摄书画视频','石晓蒙','王亚平','王亚平','石晓蒙')
	_post('积极整理直播话术','石晓蒙','王亚平','王亚平','石晓蒙')
	_post('主动与同事打招呼','王超','金城','杜磊强','石晓蒙')
	_post('乐于助人帮助同事审车','王超','金城','杜磊强','石晓蒙')
	_post('积极耐心为客户服务','金鹏','金城','杜磊强','石晓蒙')
	_post('积极转发朋友圈广告审车','金鹏','金城','杜磊强','石晓蒙')
	_post('积极帮助同事审车','余亚蕾','王亚平','王亚平','石晓蒙')
	_post('积极与同事沟通工作','余亚蕾','王亚平','王亚平','石晓蒙')
	# _post('帮同事给审车客户查询信息','唐莉娜','金城','杜磊强','石晓蒙')
	_post('热心帮助同事拿物资','崔宁','车礼刚','王明霞','石晓蒙')
	# _post('帮助同事捎资料','崔宁','车礼刚','王明霞','石晓蒙')
	_post('帮助同事核对物资表','王峰','车礼刚','王明霞','石晓蒙')
	_post('工作认真负责','王峰','车礼刚','王明霞','石晓蒙')
	_post('积极对接工作','王丹丹','杨金萍','王明霞','石晓蒙')
	# _post('积极转发朋友圈招生','王丹丹','杨金萍','王明霞','石晓蒙')
	# _post('帮助同事解决问题','石玉兰','杨金萍','王明霞','石晓蒙')
	# _post('积极宣传业务','石玉兰','杨金萍','王明霞','石晓蒙')
	_post('及时转发业务宣传信息','矫美霞','纪红专','石藏宗','石晓蒙')
	_post('帮助查询学员信息','矫美霞','纪红专','石藏宗','石晓蒙')
	_post('积极帮助同事招生','张丽丽','金城','杜磊强','石晓蒙')
	_post('积极帮助车主打证','张丽丽','金城','杜磊强','石晓蒙')
	_post('帮助同事递交材料签字','张勇杰','王亚平','王亚平','石晓蒙')
	_post('积极帮助同事设计','尚梦梦','陈甜甜','王明霞','石晓蒙')
	# _post('帮助同事查询解答问题','尚梦梦','陈甜甜','王明霞','石晓蒙')
	_post('帮助同事联系学员练车','窦朝财','艾振章','杜磊强','石晓蒙')
	_post('积极为学员预约考试','窦朝财','艾振章','杜磊强','石晓蒙')
	_post('帮助同事上门提车审车','杨德斌','金城','杜磊强','石晓蒙')
	_post('帮助解答审车问题','杨德斌','金城','杜磊强','石晓蒙')
	# _post('积极统计物资数量','胡国玲','车礼刚','王明霞','石晓蒙')
	# _post('帮助同事递交申请单','胡国玲','车礼刚','王明霞','石晓蒙')
	_post('积极给学员讲解学车流程','季彩惠','艾振章','杜磊强','石晓蒙')
	_post('热情服务客户','曲亚男','艾振章','杜磊强','石晓蒙')
	# _post('认真学习岗位知识','苗晓艳','战卫卫','杜磊强','石晓蒙')
	# _post('积极为车主办理过户','苗晓艳','战卫卫','杜磊强','石晓蒙')
	# _post('积极给顾客解答过户相关问题','刘海静','战卫卫','杜磊强','石晓蒙')
	# _post('积极上传档案信息','刘海静','战卫卫','杜磊强','石晓蒙')
	# _post('积极给车主查验车辆','苗欣雅','战卫卫','杜磊强','石晓蒙')
	# _post('帮助车主卸车牌','苗欣雅','战卫卫','杜磊强','石晓蒙')
	_post('对待工作积极热情','邵晓芬','战卫卫','杜磊强','石晓蒙')
	_post('帮助解答过户问题','邵晓芬','战卫卫','杜磊强','石晓蒙')
	_post('帮助学员预约考试','林大伟','方士超','石藏宗','石晓蒙')
	_post('帮助学员预约考试','王磊','纪延春','石藏宗','石晓蒙')
	_post('帮助查询学员报名情况','王春莉','徐帅','石藏宗','石晓蒙')
	_post('帮助查询学员报名情况','付晶','徐帅','石藏宗','石晓蒙')
	_post('帮助查询学员学车情况','王春莉','徐帅','石藏宗','石晓蒙')
	_post('帮助查询学员报名情况','刘咏暄','纪红专','石藏宗','石晓蒙')

	##### 邵晓芬 #####
	_post('帮助同事传送资料','石晓蒙','王亚平','王亚平','邵晓芬')
	_post('积极给同事解答问题','石晓蒙','王亚平','王亚平','邵晓芬')
	_post('对待工作积极热情','邵晓芬','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','邵晓芬','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答审车问题','王超','金城','杜磊强','邵晓芬')
	_post('帮助查验车辆','杨永康','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','王美君','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','吴非非','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','张彩惠','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','初少佩','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','冷同飞','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','柴晓惠','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','毛元珍','战卫卫','王亚平','邵晓芬')
	_post('帮助解答过户问题','王杰','战卫卫','杜磊强','邵晓芬')
	_post('帮助解答过户问题','傅艳','战卫卫','杜磊强','邵晓芬')
	_post('积极学习下发政策','杨永康','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','王美君','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','吴非非','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','张彩惠','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','初少佩','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','冷同飞','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','柴晓惠','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','毛元珍','王亚平','王亚平','邵晓芬')
	_post('积极学习上级下发的最新政策','王杰','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','傅艳','战卫卫','杜磊强','邵晓芬')
	_post('积极学习上级下发的最新政策','苗欣雅','战卫卫','杜磊强','邵晓芬')
	_post('帮助同事审车检查车辆近况','代琦','王亚平','王亚平','邵晓芬')
	_post('帮助同事审车检查车辆近况','唐莉娜','金城','杜磊强','邵晓芬')
	_post('帮助同事审车检查车辆近况','贾伟伟','金城','杜磊强','邵晓芬')
	_post('帮助同事出库物资','崔宁','车礼刚','王明霞','邵晓芬')
	_post('帮助同事出库物资','刘慧','车礼刚','王明霞','邵晓芬')
	_post('帮助同事出库物资','李京','车礼刚','王明霞','邵晓芬')
	_post('帮助同事出库物资','胡国玲','车礼刚','王明霞','邵晓芬')
	_post('帮助同事出库物资','王文利','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','崔宁','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','刘慧','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','李京','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','王峰','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','陈知芹','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','胡国玲','车礼刚','王明霞','邵晓芬')
	_post('帮助同事搬送物资','王文利','车礼刚','王明霞','邵晓芬')
	_post('帮助同事传送资料','赵晓丽','陈甜甜','王明霞','邵晓芬')
	_post('帮助同事传送资料','杨竹青','王亚平','王亚平','邵晓芬')
	_post('帮助同事传送资料','尚梦梦','陈甜甜','王明霞','邵晓芬')
	_post('帮助同事传送资料','李伟健','陈甜甜','王明霞','邵晓芬')
	_post('帮助同事传送资料','尚鑫','陈甜甜','王明霞','邵晓芬')
	_post('帮助同事传送资料','张勇杰','王亚平','王亚平','邵晓芬')
	_post('帮助同事传送资料','辛淑珍','陈甜甜','王明霞','邵晓芬')
	_post('帮助同事查询工资','石玉兰','杨金萍','王明霞','邵晓芬')
	_post('帮助同事查询工资','王丹丹','杨金萍','王明霞','邵晓芬')
	_post('帮助同事计算工资资料','石玉兰','杨金萍','王明霞','邵晓芬')
	_post('帮助同事计算工资资料','王丹丹','杨金萍','王明霞','邵晓芬')
	_post('帮助查询学员学车情况','矫美霞','纪红专','石藏宗','邵晓芬')
	_post('帮助查询学员学车情况','刘咏暄','纪红专','石藏宗','邵晓芬')
	_post('帮助查询学员学车情况','林大伟','方士超','石藏宗','邵晓芬')
	_post('帮助查询学员学车情况','付晶','徐帅','石藏宗','邵晓芬')
	_post('帮助查询学员学车情况','王春莉','徐帅','石藏宗','邵晓芬')
	_post('帮助查询学员报名情况','矫美霞','纪红专','石藏宗','邵晓芬')
	_post('帮助查询学员报名情况','刘咏暄','纪红专','石藏宗','邵晓芬')
	_post('帮助查询学员报名情况','林大伟','方士超','石藏宗','邵晓芬')
	_post('帮助查询学员报名情况','付晶','徐帅','石藏宗','邵晓芬')
	_post('帮助查询学员报名情况','王春莉','徐帅','石藏宗','邵晓芬')
	_post('帮助同事查询学员报名情况','王丰建','艾振章','杜磊强','邵晓芬')
	_post('帮助同事查询学员报名情况','徐洪强','石明涛','杜磊强','邵晓芬')
	_post('帮助查询学员报名情况','曹军','艾振章','杜磊强','邵晓芬')

	#金鹏
	_post('积极帮助同事审车','于汉道','贾伟伟','金城','金鹏')
	_post('积极帮助审车','于汉道','贾伟伟','金城','金鹏')
	_post('帮助同事审车','李聪','贾伟伟','金城','金鹏')
	_post('积极审车','李聪','贾伟伟','金城','金鹏')
	_post('积极帮助同事倒水','代琦','贾伟伟','金城','金鹏')
	_post('积极帮助同事打饭','代琦','贾伟伟','金城','金鹏')
	_post('积极帮助客户','万青旭','贾伟伟','金城','金鹏')
	_post('积极帮助登录','万青旭','贾伟伟','金城','金鹏')
	_post('积极清理卫生','史旭东','贾伟伟','金城','金鹏')
	_post('积极宣传业务','史旭东','贾伟伟','金城','金鹏')
	_post('帮助维修车辆','王显军','余亚蕾','金城','金鹏')
	_post('积极帮助学员审车','王显军','余亚蕾','金城','金鹏')
	_post('积极帮助客户审车','官艳林','余亚蕾','金城','金鹏')
	_post('积极帮助提车','官艳林','余亚蕾','金城','金鹏')
	_post('积极帮助整理档案','李超','余亚蕾','金城','金鹏')
	_post('积极帮助查资料','李超','余亚蕾','金城','金鹏')
	_post('帮助查资料','袁丽娜','余亚蕾','金城','金鹏')
	_post('积极帮助学员','袁丽娜','余亚蕾','金城','金鹏')
	_post('积极帮助做好检测','唐莉娜','余亚蕾','金城','金鹏')
	_post('帮助朋友审车','唐莉娜','朱明友','金城','金鹏')
	_post('积极帮助同事拿文件','张召鹏','朱明友','金城','金鹏')
	_post('积极帮助整理资料','张召鹏','朱明友','金城','金鹏')
	_post('做好检测工作','金鹏','金城','杜磊强','金鹏')
	_post('积极帮助打印资料','金鹏','金城','杜磊强','金鹏')
	_post('积极打印文件','余亚蕾','王亚平','王亚平','金鹏')
	_post('积极帮助换水','余亚蕾','王亚平','王亚平','金鹏')
	_post('积极帮助清理车间卫生','刘慧','金城','车礼刚','金鹏')
	_post('积极完成宣传','刘慧','金城','车礼刚','金鹏')
	_post('积极转发朋友圈','胡国玲','金城','车礼刚','金鹏')
	_post('积极工作','胡国玲','金城','车礼刚','金鹏')
	_post('积极联系审车','郭春光','金城','车礼刚','金鹏')
	_post('积极做好回复','郭春光','金城','车礼刚','金鹏')
	_post('帮助客户提车','权新建','余亚蕾','金城','金鹏')
	_post('积极打扫厕所','权新建','余亚蕾','金城','金鹏')
	_post('积极帮助查流水','王超','朱明友','金城','金鹏')
	_post('积极帮助处理违章','李吉孟','朱明友','金城','金鹏')
	_post('积极帮助学员约考','李吉孟','朱明友','金城','金鹏')
	_post('积极帮助联系教练','王丹丹','金城','杨金萍','金鹏')
	_post('积极帮助宣传审车','张磊','金城','艾振章','金鹏')
	_post('积极宣传审车','张磊','金城','艾振章','金鹏')
	_post('积极帮助学员解决问题','刘振涛','金城','艾振章','金鹏')
	_post('积极帮助整理行驶证','刘振涛','金城','艾振章','金鹏')
	_post('积极帮助学员联系教练','陈娜','金城','艾振章','金鹏')
	_post('帮助学员联系教练','陈娜','金城','艾振章','金鹏')
	_post('积极帮助解决问题','王春会','金城','徐帅','金鹏')
	_post('积极帮助咨询保险','王春会','金城','徐帅','金鹏')
	_post('积极帮助解决问题','石晓蒙','王亚平','王亚平','金鹏')
	_post('积极帮助整理资料','石晓蒙','王亚平','王亚平','金鹏')
	_post('提醒工作','王杰','金城','战卫卫','金鹏')
	_post('帮助提醒工作','王杰','金城','战卫卫','金鹏')

## start
import time

#test
# post_all()

while True:
	now_time=datetime.datetime.now().strftime('%H:%M')
	time.sleep(1)
	print(now_time)
	if now_time =='10:00':
		print('时间到-提交作业')
		post_all()
		time.sleep(120)

	

