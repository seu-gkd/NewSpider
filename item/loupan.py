class LouPan(object):

    def __init__(self, city, region):
        self.city = city
        self.region = region
        # 小区名
        self.xiaoqu = ''
        # 单价
        self.price = ''
        # 总价
        self.total = ''
        # url
        self.url = ''

        ## 基本信息
        # 物业类型
        self.propertyType = ''
        # 参考价格
        self.referencePrice = ''
        # 项目特色
        self.projectFeatures = ''
        # 区域位置
        self.regionallocation = ''
        # 楼盘地址
        self.propertyaddress = ''
        # 售楼处地址
        self.salesOfficeAddress = ''
        # 开发商
        self.developer = ''

        ## 规划信息
        # 建筑类型
        self.buildingType = ''
        # 绿化率
        self.landscapingRatio = ''
        # 占地面积
        self.siteArea = ''
        # 容积率
        self.floorAreaRatio = ''
        # 建筑面积
        self.buildingArea = ''
        # 产权年限
        self.yearofpropertyRights = ''
        # 规划户数
        self.numPlan = ''
        # 楼盘户型
        self.designType = ''

        ## 配套信息
        # 物业公司
        self.propertyCompany = ''
        # 车位配比
        self.parkingRatio = ''
        # 物业费
        self.propertycosts = ''
        # 供暖方式
        self.heatingMethod = ''
        # 供水方式
        self.waterSupplyMethod = ''
        # 供电方式
        self.powerSupply = ''
        # 车位
        self.parkingSpace = ''
        # 周边信息
        self.nearby = ''

        ## 其他
        # 面积
        self.area = ''
        # 图片
        self.date = ''

    def text(self):
        if self.city == '':
            if self.region == '':
                self.region = '暂无信息'
            if self.xiaoqu == '':
                self.xiaoqu = '暂无信息'
            if self.price == '':
                self.price = '暂无信息'
            if self.total == '':
                self.total = '暂无信息'
            if self.url == '':
                self.url = '暂无信息'
            if self.propertyType == '':
                self.propertyType = '暂无信息'
            if self.referencePrice == '':
                self.referencePrice = '暂无信息'
            if self.projectFeatures == '':
                self.projectFeatures = '暂无信息'
            if self.regionallocation == '':
                self.regionallocation = '暂无信息'
            if self.propertyaddress == '':
                self.propertyaddress = '暂无信息'
            if self.salesOfficeAddress == '':
                self.salesOfficeAddress = '暂无信息'
            if self.developer == '':
                self.developer = '暂无信息'
            if self.buildingType == '':
                self.buildingType = '暂无信息'
            if self.landscapingRatio == '':
                self.landscapingRatio = '暂无信息'
            if self.siteArea == '':
                self.siteArea = '暂无信息'
            if self.floorAreaRatio == '':
                self.floorAreaRatio = '暂无信息'
            if self.buildingArea == '':
                self.buildingArea = '暂无信息'
            if self.yearofpropertyRights == '':
                self.yearofpropertyRights = '暂无信息'
            if self.numPlan == '':
                self.numPlan = '暂无信息'
            if self.designType == '':
                self.designType = '暂无信息'
            if self.propertyCompany == '':
                self.propertyCompany = '暂无信息'
            if self.parkingRatio == '':
                self.parkingRatio = '暂无信息'
            if self.propertycosts == '':
                self.propertycosts = '暂无信息'
            if self.heatingMethod == '':
                self.heatingMethod = '暂无信息'
            if self.waterSupplyMethod == '':
                self.waterSupplyMethod = '暂无信息'
            if self.powerSupply == '':
                self.powerSupply = '暂无信息'
            if self.parkingSpace == '':
                self.parkingSpace = '暂无信息'
            if self.nearby == '':
                self.nearby = '暂无信息'
            if self.area == '':
                self.area = '暂无信息'

        return str(self.date) + "," + \
               str(self.city) + "," + \
               str(self.region) + "," + \
               str(self.xiaoqu) + "," + \
               str(self.price) + "," + \
               str(self.total) + "," + \
               str(self.url) + "," + \
            \
               str(self.propertyType) + "," + \
               str(self.referencePrice) + "," + \
               str(self.projectFeatures) + "," + \
               str(self.regionallocation) + "," + \
               str(self.propertyaddress) + "," + \
               str(self.salesOfficeAddress) + "," + \
               str(self.developer) + "," + \
            \
               str(self.buildingType) + "," + \
               str(self.landscapingRatio) + "," + \
               str(self.siteArea) + "," + \
               str(self.floorAreaRatio) + "," + \
               str(self.buildingArea) + "," + \
               str(self.yearofpropertyRights) + "," + \
               str(self.numPlan) + "," + \
               str(self.designType) + "," + \
            \
               str(self.propertyCompany) + "," + \
               str(self.parkingRatio) + "," + \
               str(self.propertycosts) + "," + \
               str(self.heatingMethod) + "," + \
               str(self.waterSupplyMethod) + "," + \
               str(self.powerSupply) + "," + \
               str(self.parkingSpace) + "," + \
               str(self.nearby) + "," + \
            \
               str(self.area)

    def feature(self):
        return "date,city,region,xiaoqu,price,total,url," \
               "propertyType,referencePrice,projectFeatures,regionallocation,propertyaddress,salesOfficeAddress,developer," \
               "buildingType,landscapingRatio,siteArea,floorAreaRatio,buildingArea,yearofpropertyRights,numPlan,designType," \
               "propertyCompany,parkingRatio,propertycosts,heatingMethod,waterSupplyMethod,powerSupply,parkingSpace,nearby,area"


    # Date, city, region, xiaoqu, price, total, url, propertyType, referencePrice, projectFeatures, regionallocation, propertyaddress, salesOfficeAddress, developer, buildingType, landscapingRatio, siteArea, floorAreaRatio, buildingArea, yearofpropertyRights, numPlan, designType, propertyCompany, parkingRatio, propertycosts, heatingMethod, waterSupplyMethod, powerSupply, parkingSpace, nearby, area,