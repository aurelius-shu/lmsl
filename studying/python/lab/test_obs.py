from obs import ObsClient

# 创建ObsClient实例
obsClient = ObsClient(access_key_id='', secret_access_key='', server='')
# 使用访问OBS
# 调用putContent接口上传对象到桶内
resp = obsClient.putContent('', '', '')
if resp.status < 300:
    # 输出请求Id
    print('requestId:', resp.requestId)
else:
    # 输出错误码
    print('errorCode:', resp.errorCode)
    # 输出错误信息
    print('errorMessage:', resp.errorMessage)

# 关闭obsClient
obsClient.close()