# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class SYSDICT(Base):
    __tablename__ = 'SYS_DICT'

    KEY_ = Column(String(50), primary_key=True, info='KEY')
    LABEL = Column(String(50), server_default=FetchedValue(), info='LABEL')
    INTRO = Column(String(50), server_default=FetchedValue(), info='INTRO')
    REVISION = Column(Integer, info='REVISION')



t_SYS_DICT_ITEM = Table(
    'SYS_DICT_ITEM', metadata,
    Column('DICT_KEY', String(50), server_default=FetchedValue(), info='DICT_KEY'),
    Column('KEY_', String(50), server_default=FetchedValue(), info='KEY_'),
    Column('LABEL', String(50), server_default=FetchedValue(), info='LABEL'),
    Column('SORT_', String(50), server_default=FetchedValue(), info='SORT_'),
    Column('INTRO', String(50), server_default=FetchedValue(), info='INTRO'),
    Column('REVISION', Integer, info='REVISION')
)



class VAvatar(Base):
    __tablename__ = 'V_Avatar'

    id = Column(Integer, primary_key=True, info='ID')
    avatarStatus = Column(String(1), nullable=False, info='图片的状态')
    farmat = Column(String(10), nullable=False, info='图片格式')
    name = Column(String(20), nullable=False, unique=True, info='图片名称不带后缀')
    createTime = Column(DateTime, nullable=False, info='创建时间')



class VCustomer(Base):
    __tablename__ = 'V_Customer'

    uuid = Column(String(128), primary_key=True, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    nickName = Column(String(50))
    password = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    tel = Column(String(20))
    address = Column(String(255))
    remark = Column(String(255))



class VEncryption(Base):
    __tablename__ = 'V_Encryption'

    type = Column(String(10), nullable=False, unique=True)
    key = Column(String(255), primary_key=True)
    iv = Column(String(255))
    initTime = Column(DateTime, nullable=False)
    exp = Column(Integer, nullable=False)
    remark = Column(String(255))



class VLeaf(Base):
    __tablename__ = 'V_Leafs'

    leafId = Column(Integer, primary_key=True, info='用户节点Id')
    nodeId = Column(String(128), info='网络节点Id')
    userId = Column(String(128), info='用户Id')
    leafStatus = Column(Integer, info='状态')
    creatTime = Column(String(900), info='创建时间')
    modifyTime = Column(String(900), info='修改时间')
    lastConnectTime = Column(String(900), info='更新时间')



class VLeafsConfig(Base):
    __tablename__ = 'V_Leafs_Config'

    leafId = Column(String(128), primary_key=True, info='用户节点ID')
    ipv4 = Column(String(32), info='IPv4')
    ipv6 = Column(String(128), info='IPv6')
    nftConfig = Column(String(32), info='nft配置')
    routeConfig = Column(DateTime, info='route配置')
    wgConfig = Column(String(255), info='wg配置')



class VNetwork(Base):
    __tablename__ = 'V_Network'

    networkId = Column(String(128), primary_key=True, info='网络ID')
    networkName = Column(String(50), nullable=False, info='网络名称')
    description = Column(String(255), info='描述')
    networkStatus = Column(String(32), nullable=False, info='状态')
    createTime = Column(DateTime, nullable=False, info='创建时间')
    modifyTime = Column(DateTime, nullable=False, info='修改时间')



class VNode(Base):
    __tablename__ = 'V_Nodes'

    nodeId = Column(String(128), primary_key=True, info='节点ID')
    nodeName = Column(String(50), nullable=False, info='节点名称')
    description = Column(String(255), info='描述')
    nodeStatus = Column(String(32), nullable=False, info='节点状态')
    nodeType = Column(String(10), nullable=False, info='节点类型')
    host = Column(String(128), info='地址')
    port = Column(Integer, info='端口')
    networkId = Column(String(128), nullable=False, info='网络ID')
    createTime = Column(DateTime, nullable=False, info='创建时间')
    modifyTime = Column(DateTime, info='修改时间')
    lastOnlineTime = Column(DateTime, info='最后在线时间')
    lastOfflineTime = Column(DateTime, info='最后离线时间')



class VNodesConfig(Base):
    __tablename__ = 'V_Nodes_Config'

    nodeId = Column(String(128), primary_key=True, info='节点ID')
    nftConfig = Column(String(900), info='nft配置')
    routeConfig = Column(String(900), info='route配置')
    wgConfig = Column(String(900), info='wg配置')



class VOperator(Base):
    __tablename__ = 'V_Operator'

    uuid = Column(String(128), primary_key=True)
    username = Column(String(50), nullable=False)
    nickName = Column(String(50), server_default=FetchedValue())
    password = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    tel = Column(String(20), server_default=FetchedValue())
    remark = Column(String(255), server_default=FetchedValue())



class VRole(Base):
    __tablename__ = 'V_Role'

    roleId = Column(Integer, primary_key=True)
    roleName = Column(String(20), nullable=False)
    createTime = Column(DateTime, nullable=False)
    lastModifyTime = Column(DateTime)



class VUserInfo(Base):
    __tablename__ = 'V_UserInfo'

    uuid = Column(String(128), primary_key=True)
    userStatus = Column(Integer, nullable=False, info='0:, 1:, 2:, 3:, 4:, 5:,')
    createTime = Column(DateTime, nullable=False)
    lastLoginTime = Column(DateTime)
    lastLogoutTime = Column(DateTime)
    lastModifyTime = Column(DateTime)
    lastLockTime = Column(DateTime)
    userIntro = Column(String(255), info='个性签名')
    avatarId = Column(Integer, info='头像ID')



class VUserRole(Base):
    __tablename__ = 'V_UserRole'

    id = Column(Integer, primary_key=True, info='ID')
    uuid = Column(String(128), nullable=False, info='UUID')
    roleId = Column(Integer, nullable=False, info='角色ID')
    createBy = Column(String(128), nullable=False, info='创建人')
    createTime = Column(DateTime, nullable=False, info='创建时间')
    lastModifyBy = Column(String(128), info='最后修改人')
    lastModifyTime = Column(DateTime, info='最后修改时间')
