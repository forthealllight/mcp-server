note = {
    "describe_cdn_config": r"""
    Args:
        body: A JSON structure
             Domain ( String ): 是  表示一个加速域名。您一次只能查询一个加速域名的配置详情。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        DomainConfig ( Object of DomainConfig ):
       "字段"： DomainConfig
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ServiceType ( String ): web
        Cname ( String ): www.example.com.volcgslb.com
        CreateTime ( Long ): 1636612244
        Domain ( String ): www.example.com
        HTTPS ( Object of HTTPS ):
        LockStatus ( String ): `on`
        Project ( String ): default
        ServiceRegion ( String ): outside_chinese_mainland
        Status ( String ): offline
        UpdateTime ( Long ): 1639621409
        ResourceTags ( Array of ResourceTags ):
       "字段"： HTTPS
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Switch ( Boolean ): true
        CertInfo ( Object of CertInfo ):
        CertInfoList ( Array of CertInfoList ):
        CertCheck ( Object of CertCheck ):
       "字段"： ResourceTags
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Key ( String ):
        Value ( String ):
       "字段"： CertInfo
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        CertId ( String ): cert-eb5d99026753499a8a34d2a4f0a08d92
        CertName ( String ): www.example.com
        Desc ( String ): Comment
        EffectiveTime ( Long ): 1655856000
        ExpireTime ( Long ): 1687478399
        Source ( String ): volc_cert_center
        EncryType ( String ): inter_cert
       "字段"： CertInfoList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        CertId ( String ): cert-602fc4eb6cbf4b9351b54bedf2bc5dc5
        CertName ( String ): www.example.com
        Desc ( String ): Comment
        EffectiveTime ( Long ): 1655856000
        ExpireTime ( Long ): 1687478399
        Source ( String ): volc_cert_center
        EncryType ( String ): inter_cert
       "字段"： CertCheck
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        CertInfoList ( Array of CertInfoList ):
        Switch ( Boolean ): true
    """,
    "list_cdn_domains": r"""
    Args:
        body: A JSON structure
             Domain ( String ): 否  表示一个字符串，用来对域名进行过滤，获取包含该字符串的域名。
             ServiceType ( String ): 否  表示一个业务类型，用来对域名进行过滤，获取该业务类型的域名。该参数有以下取值：
                   - download：表示文件下载。
                   - web：表示网页。
                   - video：表示音视频点播。
             ResourceTags ( Array of String ): 否  表示一个标签列表，用于对域名进行过滤，获取带有列表中任意标签的域名。列表中最多可以包含 10 个标签，每个标签的格式是 key:value。参见右边该参数的示例。
             Status ( String ): 否  表示一个域名状态，用来对域名进行过滤，获取该状态下的域名。该参数有以下取值：
                   - online：表示 "正常运行"。
                   - configuring：表示 "配置中"。
                   - offline：表示 "已下线"。
             Project ( String ): 否  表示一个项目，获取归属该项目的域名。
             OriginProtocol ( String ): 否  表示一个协议，获取回源请求使用该协议的域名。该参数有以下取值：
                   - http：表示 HTTP 协议。
                   - https：表示 HTTPS 协议。
                   - followclient：表示用户请求使用的协议。
             IPv6 ( Boolean ): 否  表示根据是否启用了 IPv6 特性来过滤域名。该参数有以下取值：
                   * true: 表示 IPv6 已启用。
                   * false: 表示 IPv6 未启用。
             HTTPS ( Boolean ): 否  表示根据是否启用了 HTTPS 特性来过滤域名。该参数有以下取值：
                   * true: 表示 HTTPS 已启用。
                   * false: 表示 HTTPS 未启用。
             PrimaryOrigin ( String ): 否  表示一个主源站，以获取主源站配置中包含该主源站的那些域名。该参数值可以是一个 IP 地址，也可以是一个域名。
             PageNum ( Long ): 否  表示一个页码，用以获取该页面上域名列表。该参数的默认值为 1。
                   CDN 对符合过滤条件的域名进行分页。您可以根据响应参数 Total 和请求参数 PageSize 计算该 API 返回的页数。
             PageSize ( Long ): 否  表示每页包含的域名数量。该参数的取值范围是 1-100，默认值是 10。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        PageNum ( Long ): 1
        PageSize ( Long ): 10
        Total ( Long ): 100
        Data ( Array of Data ):
       "字段"： Data
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Domain ( String ): www.example.com
        ServiceType ( String ): web
        Status ( String ): online
        Cname ( String ): www.example.com.volcgslb.com
        ServiceRegion ( String ): domestic
        CreateTime ( Long ): 1625587200
        UpdateTime ( Long ): 1601371409
        Project ( String ): default
        OriginProtocol ( String ): http
        IPv6 ( Boolean ):
        HTTPS ( Boolean ): true
        PrimaryOrigin ( Array of String ): 1.2.3.4,2.3.4.5
        BackupOrigin ( Array of String ): 1.2.3.4,2.3.4.5
        ResourceTags ( Array of ResourceTags ):
        CacheShared ( String ): target_host
        CacheSharedTargetHost ( String ): www.test.com
        IsConflictDomain ( Boolean ): false
        DomainLock ( Object of DomainLock ):
       "字段"： ResourceTags
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Key ( String ): userKey
        Value ( String ): userValue
       "字段"： DomainLock
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Remark ( String ): 域名锁定，不允许自助配置操作，域名下线
        Status ( String ): on
    """,
    "describe_origin_top_statistical_data": r"""
    Args:
        body: A JSON structure
             Domain ( String ): 是  指定一个域名进行数据统计。
             EndTime ( Long ): 是  指定一个结束时间。时间格式是 Unix 时间戳，精度是秒。
             Item ( String ): 是  指定一个统计对象。该参数的可用值如下：
                   * url：表示对回源请求 URL 进行统计。
             Metric ( String ): 是  指定一个统计指标。基于该指标的统计数据，对 Item 进行排序。您可以指定以下指标：
                   * flux：表示回源请求所产生的流量。单位是 Byte。
                   * pv：表示回源请求数。
                   * status_2xx：表示在回源请求的响应状态码中，范围在 200-299 内的状态码数量。
                   * status_3xx：表示范围在 300-399 内的状态码数量。
                   * status_4xx：表示范围在 400-499 内的状态码数量。
                   * status_5xx：表示范围在 500-599 内的状态码数量。
             StartTime ( Long ): 是  指定一个开始时间。时间格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。
                   您必须同时指定 StartTime 和 EndTime，或者都不指定。如果您不指定这两个参数，该页面展示最近 24 小时的数据。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Domain ( String ): www.example.com
        Item ( String ): url
        Metric ( String ): flux
        TopDataDetails ( Array of TopDataDetails ):
       "字段"： TopDataDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): https://www.example.com/birds/chickadee.png
        Value ( Double ): 2341
    """,
    "describe_district_data": r"""
    Args:
        body: A JSON structure
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示 CDN 向用户传输的数据量，单位是 bytes。
                   - bandwidth：表示基于 CDN 向用户传输的数据量而计算的带宽，单位是 bps。
                   - requests：表示 CDN 收到的用户请求数量。
                   - qps：表示 CDN 收到的用户请求的 QPS。
                   - response_time：表示 CDN 响应用户请求所耗费的平均时间，单位是毫秒（ms）。
                   - avg_speed：表示 CDN 向用户传输数据时的平均速度，单位是 Bps。
                   - status_all：在 CDN 对用户请求的响应中，该参数表示以下各类别的状态码数量：
                   	- 所有状态码的数量。
                   	- 2xx 状态码的数量。
                   	- 3xx 状态码的数量。
                   	- 4xx 状态码的数量。
                   	- 5xx 状态码的数量。
                   	- 每个状态码的数量。
                   - status_2xx：表示 2xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_3xx：表示 3xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_4xx：表示 4xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_5xx：表示 5xx 状态码的数量以及该类别下每个状态码的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 数据。
                   关于 Interval参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   - hour：表示时间粒度是 1 小时。
                   - day：表示时间粒度是 1 天。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min、hour。
                   - 如果 1 天 < 时间范围 <= 3 天，您可以指定的时间粒度有 5min、hour、day。
                   - 如果 3 天 < 时间范围 <= 31 天，您可以指定的时间粒度有 hour、day。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
             Location ( String ): 否  表示国家和地区的代码，用于对用户请求进行过滤。您可以指定一个或者多个代码，CDN 对来自这些国家和地区的用户请求统计 Metric 数据。多个国家和地区代码之间使用逗号（,）分隔。您最多可以指定 30 个国家和地区。
                   * 如果您指定了 Location，就不能指定 Province，反之亦然。
                   * 如果您不指定 Location，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与国家和地区的对应表。
             Province ( String ): 否  表示中国省级行政区的代码，用于对用户请求进行过滤。您可以指定一个或者多个代码，CDN 对来自这些省级行政区的用户请求统计 Metric 数据。多个代码之间使用逗号（,）分隔。您最多可以指定 10 个代码。
                   如果您不指定 Province，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与中国省级行政区的对应表。
             Isp ( String ): 否  表示请求所使用的中国网络运营商的代码，用于对用户请求进行过滤。例如，CT 表示中国电信。您可以指定一个或者多个代码，CDN 对使用这些网络运营商的用户请求统计 Metric 数据。多个代码之间使用逗号（,）分隔。您最多可以指定 5 个代码。
                   - 当 Location 是 CHN 或者您指定了 Province 时，您才能指定 Isp。
                   - 当您不指定 Isp 时，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与网络运营商的对应表。
             Protocol ( String ): 否  表示请求使用的一个应用层协议，用于对用户请求进行过滤。该参数的可用值如下：
                   - http：表示 HTTP 协议。
                   - https：表示 HTTPS 协议。
                   - quic：表示 QUIC 协议。
                   如果不指定 Protocol，表示不使用该参数对请求进行过滤。
             IpVersion ( String ): 否  表示请求使用的一个网络层协议，用于对用户请求进行过滤。该参数的可用值如下：
                   - IPv4：表示 IPv4 协议。
                   - IPv6：表示 IPv6 协议。
                   如果不指定 IpVersion，表示不使用该参数对请求进行过滤。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        Values ( Array of Values ):
       "字段"： Values
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        TimeStamp ( Long ): 1710273600
        Value ( Double ): 4567
    """,
    "describe_district_ranking": r"""
    Args:
        body: A JSON structure
             Item ( String ): 是  表示一个分组条件，用于对 Metric 数据进行汇总。该参数有以下取值：
                   - location：表示用户请求来自的国家和地区。
                   - province：表示用户请求来自的中国省级行政区。
                   - isp：表示用户请求使用的中国网络运营商。
                   当 Item 是 province 或 isp 时，Metric 数据是基于来自中国的请求而统计的。
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示内容分发网络向用户传输的数据量，单位是 bytes。
                   - bandwidth：表示基于内容分发网络向用户传输的数据量而计算的带宽峰值，单位是 bps。
                   - requests：表示内容分发网络收到的用户请求数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 和 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 的数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度只能是 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Item ( String ): location
        TopDataDetails ( Array of TopDataDetails ):
       "字段"： TopDataDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        ValueDetails ( Array of ValueDetails ):
       "字段"： ValueDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): CHN
        Ratio ( Double ): 0.9527
        Timestamp ( Long ): 1710419700
        Value ( Double ): 95270
    """,
    "describe_edge_status_code_ranking": r"""
    Args:
        body: A JSON structure
             Item ( String ): 是  表示一个分组条件。当前，该参数值只能是 domain，表示按 Domain 对 Metric 数据进行汇总。
             Metric ( String ): 是  对于 CDN 对用户请求的响应，该参数表示以下某个类别的状态码数量：
                   - status_2xx：表示 2xx 状态码数量。
                   - status_3xx：表示 3xx 状态码数量。
                   - status_4xx：表示 4xx 状态码数量。
                   - status_5xx：表示 5xx 状态码数量。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 和 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 的数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度有 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Item ( String ): domain
        Metric ( String ): status_4xx
        TopDataDetails ( Array of TopDataDetails ):
       "字段"： TopDataDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): www.example.com
        Status2xx ( Double ): 45678
        Status2xxRatio ( Double ): 0.47
        Status3xx ( Double ): 0
        Status3xxRatio ( Double ): 0
        Status4xx ( Double ): 3
        Status4xxRatio ( Double ): 0.0001
        Status5xx ( Double ): 0
        Status5xxRatio ( Double ): 0
    """,
    "describe_district_summary": r"""
    Args:
        body: A JSON structure
             Metric ( String ): 是  表示一个统计指标。该参数有以下取值：
                   - traffic：表示 CDN 向用户传输的数据量，单位是 bytes。
                   - bandwidth：表示基于 CDN 向用户传输的数据量而计算的带宽峰值，单位是 bps。
                   - requests：表示 CDN 收到的用户请求数量。
                   - qps：表示 CDN 收到的用户请求的 QPS 峰值。
                   - response_time：表示 CDN 响应用户请求所耗费的平均时间，单位是毫秒（ms）。
                   - avg_speed：表示 CDN 向用户传输数据时的平均速度，单位是 Bps。
                   - status_all：在 CDN 对用户请求的响应中，该参数表示以下类别的状态码数量：
                   	- 所有状态码的数量。
                   	- 2xx 状态码的数量。
                   	- 3xx 状态码的数量。
                   	- 4xx 状态码的数量。
                   	- 5xx 状态码的数量。
                   	- 每个状态码的数量。
                   - status_2xx：表示 2xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_3xx：表示 3xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_4xx：表示 4xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_5xx：表示 5xx 状态码的数量以及该类别下每个状态码的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度只能是 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
             Location ( String ): 否  表示国家和地区的代码，用于对用户请求进行过滤。您可以指定一个或者多个代码，CDN 对来自这些国家和地区的用户请求统计 Metric 数据。多个国家和地区代码之间使用逗号（,）分隔。您最多可以指定 30 个国家和地区。
                   * 如果您指定了 Location，就不能指定 Province，反之亦然。
                   * 如果您不指定 Location，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与国家和地区的对应表。
             Province ( String ): 否  表示中国省级行政区的代码，用于对用户请求进行过滤。您可以指定一个或者多个代码，CDN 对来自这些省级行政区的用户请求统计 Metric 数据。多个代码之间使用逗号（,）分隔。您最多可以指定 10 个代码。
                   如果您不指定 Province，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与中国省级行政区的对应表。
             Isp ( String ): 否  表示请求所使用的中国网络运营商的代码，用于对用户请求进行过滤。例如，CT 表示中国电信。您可以指定一个或者多个代码，CDN 对使用这些网络运营商的用户请求统计 Metric 数据。多个代码之间使用逗号（,）分隔。您最多可以指定 5 个代码。
                   - 当 Location 是 CHN 或者您指定了 Province 时，您才能指定 Isp。
                   - 当您不指定 Isp 时，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与网络运营商的对应表。
             Protocol ( String ): 否  表示请求使用的一个应用层协议，用于对用户请求进行过滤。该参数的可用值如下：
                   - http：表示 HTTP 协议。
                   - https：表示 HTTPS 协议。
                   - quic：表示 QUIC 协议。
                   如果不指定 Protocol，表示不使用该参数对请求进行过滤。
             IpVersion ( String ): 否  表示请求使用的一个网络层协议，用于对用户请求进行过滤。该参数的可用值如下：
                   - IPv4：表示 IPv4 协议。
                   - IPv6：表示 IPv6 协议。
                   如果不指定 IpVersion，表示不使用该参数对请求进行过滤。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        Value ( Double ): 3475788
    """,
    "describe_origin_data": r"""
    Args:
        body: A JSON structure
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示源站向内容分发网络传输的数据量，单位是 bytes。
                   - bandwidth：表示基于源站向内容分发网络传输的数据量而计算的带宽，单位是 bps。
                   - requests：表示回源请求数量。
                   - qps：表示回源请求的 QPS。
                   - status_all：在内容分发网络收到的源站响应中，该参数表示以下类别的状态码数量：
                   	- 所有状态码的数量。
                   	- 所有 2xx 状态码的数量。
                   	- 所有 3xx 状态码的数量。
                   	- 所有 4xx 状态码的数量。
                   	- 所有 5xx 状态码的数量。
                   	- 每个状态码的数量。
                   - status_2xx：表示所有 2xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_3xx：表示所有 3xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_4xx：表示所有 4xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_5xx：表示所有 5xx 状态码的数量以及该类别下每个状态码的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 数据。
                   关于 Interva参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   - hour：表示时间粒度是 1 小时。
                   - day：表示时间粒度是 1 天。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min、hour。
                   - 如果 1 天 < 时间范围 <= 3 天，您可以指定的时间粒度有 5min、hour、day。
                   - 如果 3 天 < 时间范围 <= 31 天，您可以指定的时间粒度有 hour、day。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        Values ( Array of Values ):
       "字段"： Values
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        TimeStamp ( Long ): 1710273600
        Value ( Double ): 4568
    """,
    "describe_edge_ranking": r"""
    Args:
        body: A JSON structure
             Item ( String ): 是  表示一个分组条件，用于对 Metric 数据进行汇总。该参数有以下取值：
                   - domain：表示按加速域名统计指标数据。
                   - billingRegion：表示按计费区域统计指标数据。
                   - project：表示按项目统计指标数据。在这个情况下，您不能指定 Domain。参见 项目数据是如何统计的。
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示 CDN 向用户传输的数据量，单位是 bytes。
                   - bandwidth：表示基于 CDN 向用户传输的数据量而计算的带宽峰值，单位是 bps。
                   - requests：表示 CDN 收到的用户请求数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             BillingRegion ( String ): 否  表示一个或多个计费区域，用于对用户请求进行过滤。该 API 对来自这些计费区域的用户请求统计 Metric 数据。多个计费区域之间使用逗号（,）分隔。该参数有以下取值：
                   - CHN：表示中国内地。
                   - EU：表示欧洲区。
                   - NA：表示北美区。
                   - SA：表示南美区。
                   - MEA：表示中东区和非洲区。
                   - AP1：表示亚太一区。
                   - AP2：表示亚太二区。
                   - AP3：表示亚太三区。
                   如果不指定 BillingRegion，表示不使用该参数对请求进行过滤。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 和 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 的数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度有 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。如果不指定 Project，表示所有项目。
                   对于 Project 和 Domain：
                   - 当您指定 Project，不指定 Domain 时，CDN 按 Item 统计指定项目的 Metric 数据。参见 项目数据是如何统计的。
                   - 其他情况下，CDN 按 Item 统计指定加速域名的 Metric 数据。
                   参见 Item、Project、Domain 的配置组合。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。您最多可以指定 50 个加速域名。多个域名之间使用逗号（,）分隔。如果不指定 Domain，表示所有加速域名。关于 Domain 参数的额外描述，参见 Project 参数。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Item ( String ): domain
        TopDataDetails ( Array of TopDataDetails ):
       "字段"： TopDataDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): requests
        ValueDetails ( Array of ValueDetails ):
       "字段"： ValueDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): www.example.com
        Ratio ( Double ): 0.978
        Timestamp ( Long ): 1710419700
        Value ( Double ): 456
    """,
    "describe_edge_data": r"""
    Args:
        body: A JSON structure
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示 CDN 向用户传输的数据量，单位是 bytes。
                   - bandwidth：表示基于 CDN 向用户传输的数据量而计算的带宽，单位是 bps。
                   - requests：表示 CDN 收到的用户请求数量。
                   - qps：表示 CDN 收到的用户请求的 QPS。
                   - traffic_hitrate：表示 CDN 的流量命中率，以数值形式显示。例如，0.9999 表示 99.99%。
                   - response_time：表示 CDN 响应用户请求所耗费的平均时间，单位是毫秒（ms）。
                   - avg_speed：表示 CDN 向用户传输数据时的平均速度，单位是 Bps。
                   - status_all：在 CDN 对用户请求的响应中，该参数表示以下类别的状态码数量：
                   	- 所有状态码的数量。
                   	- 2xx 状态码的数量。
                   	- 3xx 状态码的数量。
                   	- 4xx 状态码的数量。
                   	- 5xx 状态码的数量。
                   	- 每个状态码的数量。
                   - status_2xx：表示 2xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_3xx：表示 3xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_4xx：表示 4xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_5xx：表示 5xx 状态码的数量以及该类别下每个状态码的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 会基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   - hour：表示时间粒度是 1 小时。
                   - day：表示时间粒度是 1 天。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min、hour。
                   - 如果 1 天 < 时间范围 <= 3 天，您可以指定的时间粒度有 5min、hour、day。
                   - 如果 3 天 < 时间范围 <= 31 天，您可以指定的时间粒度有 hour、day。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
             BillingRegion ( String ): 否  表示一个或多个计费区域，用于对用户请求进行过滤。该 API 对来自这些计费区域的用户请求统计 Metric 数据。多个计费区域之间使用逗号（,）分隔。该参数有以下取值：
                   - CHN：表示中国内地。
                   - EU：表示欧洲区。
                   - NA：表示北美区。
                   - SA：表示南美区。
                   - MEA：表示中东区和非洲区。
                   - AP1：表示亚太一区。
                   - AP2：表示亚太二区。
                   - AP3：表示亚太三区。
                   如果不指定 BillingRegion，表示不使用该参数对请求进行过滤。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        Values ( Array of Values ):
       "字段"： Values
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        TimeStamp ( Long ): 1710273600
        Value ( Double ): 4567
    """,
    "describe_edge_summary": r"""
    Args:
        body: A JSON structure
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示内容分发网络向用户传输的数据量，单位是 bytes。
                   - bandwidth：表示基于内容分发网络向用户传输的数据量而计算的带宽峰值，单位是 bps。
                   - requests：表示内容分发网络收到的用户请求数量。
                   - qps：表示内容分发网络收到的用户请求的 QPS 峰值。
                   - traffic_hitrate：表示内容分发网络的流量命中率，以数值形式显示。例如，0.9999 表示 99.99%。
                   - response_time：表示内容分发网络响应用户请求所耗费的平均时间，单位是毫秒（ms）。
                   - avg_speed：表示内容分发网络向用户传输数据时的平均速度，单位是 Bps。
                   - status_all：在内容分发网络对用户请求的响应中，该参数表示以下类别的状态码数量：
                   	- 所有状态码的数量。
                   	- 2xx 状态码的数量。
                   	- 3xx 状态码的数量。
                   	- 4xx 状态码的数量。
                   	- 5xx 状态码的数量。
                   	- 每个状态码的数量。
                   - status_2xx：表示 2xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_3xx：表示 3xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_4xx：表示 4xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_5xx：表示 5xx 状态码的数量以及该类别下每个状态码的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度只能是 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
             BillingRegion ( String ): 否  表示一个或多个计费区域，用于对用户请求进行过滤。该 API 对来自这些计费区域的用户请求统计 Metric 数据。多个计费区域之间使用逗号（,）分隔。该参数有以下取值：
                   - CHN：表示中国内地。
                   - EU：表示欧洲区。
                   - NA：表示北美区。
                   - SA：表示南美区。
                   - MEA：表示中东区和非洲区。
                   - AP1：表示亚太一区。
                   - AP2：表示亚太二区。
                   - AP3：表示亚太三区。
                   如果不指定 BillingRegion，表示不使用该参数对请求进行过滤。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        Value ( Double ): 3475788
    """,
    "describe_origin_ranking": r"""
    Args:
        body: A JSON structure
             Item ( String ): 是  表示一个分组条件，用于对 Metric 数据进行汇总。该参数有以下取值：
                   - domain：表示按加速域名统计指标数据。
                   - project：表示按项目统计指标数据。在这个情况下，您不能指定 Domain。参见 项目数据是如何统计的。
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示源站向 CDN 传输的数据量，单位是 bytes。
                   - bandwidth：表示基于源站向 CDN 传输的数据量而计算的带宽峰值，单位是 bps。
                   - requests：表示回源请求的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 和 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 的数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度只能是 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。如果不指定 Project，表示所有项目。
                   对于 Project 和 Domain：
                   - 当您指定 Project，不指定 Domain 时，CDN 按 Item 统计指定项目的 Metric 数据。参见 项目数据是如何统计的。
                   - 其他情况下，CDN 按 Item 统计指定加速域名的 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对回源请求进行过滤。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示所有加速域名。关于 Domain 参数的额外描述，参见 Project 参数。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Item ( String ): domain
        TopDataDetails ( Array of TopDataDetails ):
       "字段"： TopDataDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): traffic
        ValueDetails ( Array of ValueDetails ):
       "字段"： ValueDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): www.example.com
        Ratio ( Double ): 0.867
        Timestamp ( Long ): 1710419700
        Value ( Double ): 457
    """,
    "describe_statistical_ranking": r"""
    Args:
        body: A JSON structure
             Item ( String ): 是  表示一个热门对象的类型作为分组和排序条件。 该 API 按 Item 对 Metric 数据进行汇总并对这些汇总数据进行排序。该参数有以下取值：
                   - region：表示请求客户端所在的国家或地区。
                   - url：表示请求 URL 中的路径。
                   - referer：表示请求中的 Referer 域名。
                   - ua：表示请求中的 User-Agent 字符串。
                   - clientip：表示客户端的 IP 地址。
                   - 当 Item 是 ua 时，您还需要指定 UaType 作为一个补充分组条件。
                   - 当 Item 是 region 时，您还需要指定 Area 作为一个补充分组条件。
             Metric ( String ): 是  表示一个指标。该参数的可用值受 Item 的影响。
                   - 当 Item 是 referer、ua 或 clientip 时，该参数有以下取值：
                   	- traffic：表示内容分发网络向用户传输的数据量，单位是 bytes。
                   	- requests：表示内容分发网络收到的用户请求的数量。
                   - 当 Item 是 url 时，该参数有以下取值：
                   	- traffic
                   	- requests
                   	- status_2xx：在内容分发网络对用户请求的响应中，该参数表示 2xx 状态码的数量。
                   	- status_3xx：表示 3xx 状态码的数量。
                   	- status_4xx：表示 4xx 状态码的数量。
                   	- status_5xx：表示 5xx 状态码的数量。
                   - 当 Item 是 region 时，该参数有以下取值。
                   	- clientip：表示独立客户端 IP 地址的数量。
                   	当 Item 是 region 时，该参数有默认值 clientip，并且可以不指定。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 和 EndTime 所表示的统计时间段不能超过 31 天。
                   * StartTime 和 EndTime 指定了统计时间段。但是实际统计时间段的开始时间和结束时间都是小时级别的。
                     例子：StartTime 表示的时间是 15:07，EndTime 表示的时间是 15:21，那么实际的统计时间段是 [15:00,16:00）。
                     需要留意的是，如果 EndTime 正好是整点，则实际的统计时间段还要再往后延长 1 小时。假设 StartTime 表示的时间是 15:07，EndTime 表示的时间是 16:00，那么实际的统计时间段是 [15:00,17:00)。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Domain ( String ): 是  表示一个加速域名，用于对用户请求进行过滤。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定一个其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
             UaType ( String ): 否  表示 User-Agent 字符串中的一个对象类型。当 Item 是 ua 时，该参数必须指定，作为一个补充分组条件。当 Item 不是 ua 时，该参数无效。
                   该参数有以下取值：
                   - browser：表示 User-Agent 字符串中的浏览器类型。
                   - system：表示 User-Agent 字符串中的操作系统类型。
                   - equipment：表示 User-Agent 字符串中客户端设备的类型。
             Area ( String ): 否  表示一个地域类型。该参数仅当 Item 是 region 时有效，作为一个补充分组条件，用于获取客户端 IP 地址数量的地区分布。该参数有以下取值：
                   - Global：表示全球国家和地区。
                   - China：表示中国省级行政区。
                   * 如果您不指定 Metric，Area 可以不被指定。
                   	* 如果不指定 Area，该 API 将返回按国家、地区、中国省级行政区域分布的独立客户端 IP 地址数量。
                   * 如果您指定了 Metric，Area 必须指定。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Item ( String ): region
        Metric ( String ): traffic
        RankingDataList ( Array of RankingDataList ):
        UaType ( String ): system
       "字段"： RankingDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): GS
        ItemKeyCN ( String ): 甘肃
        Value ( Double ): 777
    """,
    "describe_origin_status_code_ranking": r"""
    Args:
        body: A JSON structure
             Item ( String ): 是  表示一个分组条件。当前，该参数值只能是 domain，表示按 Domain 对 Metric 数据进行汇总。
             Metric ( String ): 是  对于 CDN 收到的源站响应，该参数表示以下某个类别的状态码数量：
                   - status_2xx：表示 2xx 状态码数量。
                   - status_3xx：表示 3xx 状态码数量。
                   - status_4xx：表示 4xx 状态码数量。
                   - status_5xx：表示 5xx 状态码数量。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 和 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 的数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度只能是 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Item ( String ): domain
        Metric ( String ): status_4xx
        TopDataDetails ( Array of TopDataDetails ):
       "字段"： TopDataDetails
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        ItemKey ( String ): www.example.com
        Status2xx ( Double ): 45678
        Status2xxRatio ( Double ): 0.47
        Status3xx ( Double ): 0
        Status3xxRatio ( Double ): 0
        Status4xx ( Double ): 3
        Status4xxRatio ( Double ): 0.0001
        Status5xx ( Double ): 0
        Status5xxRatio ( Double ): 0
    """,
    "describe_user_data": r"""
    Args:
        body: A JSON structure
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 是  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计独立客户端 IP 地址的数量。
                   关于 Interva参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - hour：表示时间粒度是 1 小时。
                   - day：表示时间粒度是 1 天。
             Domain ( String ): 是  表示一个加速域名，用于对用户请求进行过滤。
                   当子账号调用该 API 时，请留意以下说明：
                   - 子账号可以指定的加速域名是该子账号有权限访问的那些加速域名。子账号可以调用 ListCdnDomains 获取其有权限访问的加速域名。
             IpVersion ( String ): 否  表示请求使用的一个网络层协议，用于对用户请求进行过滤。该参数的可用值如下：
                   - IPv4：表示 IPv4 协议。
                   - IPv6：表示 IPv6 协议。
                   如果不指定 IpVersion，表示不使用该参数对请求进行过滤。
             Location ( String ): 否  表示一个国家或地区的代码，用于对用户请求进行过滤。CDN 对来自这些国家和地区的用户请求统计客户端 IP 地址的数量。
                   * 如果您指定了 Location，就不能指定 Province，反之亦然。
                   * 如果您不指定 Location，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与国家和地区的对应表。
             Province ( String ): 否  表示一个中国省级行政区的代码，用于对用户请求进行过滤。CDN 对来自这些省级行政区的用户请求统计客户端 IP 地址的数量。
                   如果您不指定 Province，表示不使用该参数对请求进行过滤。
                   您可以调用 DescribeCdnRegionAndIsp 获取代码与中国省级行政区的对应表。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        TimeStamp ( Long ): 1710950400
        Value ( Double ): 42
    """,
    "describe_origin_summary": r"""
    Args:
        body: A JSON structure
             Metric ( String ): 是  表示一个指标。该参数有以下取值：
                   - traffic：表示源站向内容分发网络传输的数据量，单位是 bytes。
                   - bandwidth：表示基于源站向内容分发网络传输的数据量而计算的带宽峰值，单位是 bps。
                   - requests：表示回源请求的数量。
                   - qps：表示回源请求的 QPS 峰值。
                   - status_all：在内容分发网络收到的源站响应中，该参数表示以下类别的状态码数量：
                   	- 所有状态码的数量。
                   	- 所有 2xx 状态码的数量。
                   	- 所有 3xx 状态码的数量。
                   	- 所有 4xx 状态码的数量。
                   	- 所有 5xx 状态码的数量。
                   	- 每个状态码的数量。
                   - status_2xx：表示所有 2xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_3xx：表示所有 3xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_4xx：表示所有 4xx 状态码的数量以及该类别下每个状态码的数量。
                   - status_5xx：表示所有 5xx 状态码的数量以及该类别下每个状态码的数量。
                   关于每个指标的详情以及统计方式，参见 指标的定义以及统计方式。
             StartTime ( Long ): 是  表示统计时间段的开始时间，格式是 Unix 时间戳，精度是秒。StartTime 必须早于或者等于 EndTime。同时，StartTime 与 EndTime 所表示的统计时间段不能超过 31 天。
             EndTime ( Long ): 是  表示统计时间段的结束时间，格式是 Unix 时间戳，精度是秒。
             Interval ( String ): 否  表示一个时间粒度。该 API 基于 Interval 将 StartTime 和 EndTime 所表示的统计时间段拆分成一系列的时间区间，然后对每个时间区间统计 Metric 数据。
                   关于 Interval 参数是如何用来拆分统计时间段，参考 统计时间段说明。
                   该参数有以下取值：
                   - 1min：表示时间粒度是 1 分钟。
                   - 5min：表示时间粒度是 5 分钟。
                   您可以指定的时间粒度受 StartTime 和 EndTime 所表示的时间范围的影响。
                   - 如果时间范围 <= 1 天，您可以指定的时间粒度有 1min、5min。
                   - 如果 1 天 < 时间范围 <= 31 天，您可以指定的时间粒度只能是 5min。
                   该参数的默认值是 5min。如果默认值不匹配时间范围，API 请求会失败。
             Project ( String ): 否  表示一个项目。
                   * 如果您指定了 Domain，该 API 对所有您指定的加速域名统计 Metric 数据。
                   * 如果您指定了 Project ，但未指定 Domain，该 API 对您指定的项目统计 Metric 数据。参见 项目数据是如何统计的。
                   * 如果您既未指定 Project ，也未指定 Domain，该 API 对所有加速域名统计 Metric 数据。
             Domain ( String ): 否  表示一个或多个加速域名，用于对用户请求进行过滤。该 API 对您指定的每个加速域名统计 Metric 数据。您最多可以指定 50 个加速域名。多个加速域名之间使用逗号（,）分隔。如果不指定 Domain，表示不使用该参数对请求进行过滤。
                   如果您指定了 Project，您指定的加速域名必须是属于该 Project 的。
                   当子用户调用该 API 时，请留意以下说明：
                   - 子用户只能指定其有权限访问的加速域名。子用户可以调用 ListCdnDomains 获取其有权限访问的加速域名。
                   - 如果不指定该参数，表示所有该子用户有权限访问的那些加速域名。
   Returns:
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        MetricDataList ( Array of MetricDataList ):
       "字段"： MetricDataList
        参数 ( 类型 ): 示例值
        ---- ( ---- ): ----
        Metric ( String ): bandwidth
        Value ( Double ): 3475788
    """,
    "create_domain_version": r"""
   Args:
      body: A JSON structure
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Domain ( String ): 是  表示要修改配置的加速域名。
            Message ( String ): 否  备注。
            OriginalVersion ( String ): 否  来源版本号。
            Origin ( Array of Origin ): 否  表示源站配置。
            OriginProtocol ( String ): 否  表示回源请求使用的协议。该参数有以下取值：
                  - http：表示回源请求使用 HTTP 协议。
                  - https：表示回源请求使用 HTTPS 协议。
                  - followclient：表示回源协议与用户请求使用的协议相同。
            AreaAccessRule ( Object of AreaAccessRule ): 否  表示 "地域访问控制" 特性的配置。
            BandwidthLimit ( Object of BandwidthLimit ): 否  表示 "带宽限速" 特性的配置。要使用该特性，请 提交工单。
            BrowserCache ( Array of BrowserCache ): 否  表示 "浏览器缓存" 特性的配置。在该配置中，您可以创建一个规则列表，说明如下：
                  - 每条规则包含匹配条件配置和操作配置。
                  - 列表中最多可以包含 50 条规则。
                  - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            Cache ( Array of Cache ): 否  表示 "缓存规则" 特性的配置。该特性默认为禁用，表示不创建自定义规则。
                  - 列表中最多可以包含 50 条规则。
                  - 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
                  CDN 中有一条 默认缓存规则，，用于匹配任何未能匹配其他规则的用户请求。该默认规则始终生效，并且优先级最低。您无需在配置该特性时指定该默认规则。
            CacheHost ( Object of CacheHost ): 否  表示 "共享缓存" 特性的配置。要使用该功能，请 提交工单。
                  如果您要对多个加速域名配置共享缓存，您需要调用该 API 对每个加速域名配置目标域名。
            CacheKey ( Array of CacheKey ): 否  表示 "缓存键值" 特性的配置。在该配置中，您可以创建一个规则列表，说明如下：
                  - 每条规则包含匹配条件配置和操作配置。
                  - 列表中最多可以包含 50 条规则。
                  - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
                  您必须在列表中添加以下默认规则，并且这条规则必须出现在列表的末尾。该默认规则用于匹配任何未能匹配其他规则的用户请求。在默认规则中，您可以调整 CacheKeyAction 的配置，但不能调整 Condition 的配置。
                  `json
                  {
                      "CacheKeyAction": {
                          "CacheKeyComponents": [
                              {
                                  "Action": "include",
                                  "IgnoreCase": true,
                                  "Object": "queryString",
                                  "Subobject": "*"
                              }
                          ]
                      },
                      "Condition": {
                          "ConditionRule": [
                              {
                                  "Name": "",
                                  "Object": "directory",
                                  "Operator": "match",
                                  "Type": "url",
                                  "Value": "/"
                              }
                          ]
                      }
                  }
                  `
            Compression ( Object of Compression ): 否  表示 "智能压缩" 特性的配置。
            CustomErrorPage ( Object of CustomErrorPage ): 否  表示 "自定义错误页面" 特性的配置。
            CustomizeAccessRule ( Object of CustomizeAccessRule ): 否  表示 "自定义头部黑白名单" 特性的配置。要使用该特性，请 提交工单。
            DownloadSpeedLimit ( Object of DownloadSpeedLimit ): 否  表示 "下载限速" 特性的配置。
            FollowRedirect ( Boolean ): 否  表示 "回源重定向跟随" 特性的配置。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
            HTTPS ( Object of HTTPS ): 否  表示 HTTPS 特性的配置。
            HttpForcedRedirect ( Object of HttpForcedRedirect ): 否  表示 "HTTPS 强制跳转到 HTTP" 特性的配置。
            IPv6 ( Object of IPv6 ): 否  表示 IPv6 配置。
            IpAccessRule ( Object of IpAccessRule ): 否  表示 "IP 黑白名单" 特性的配置。
                  该特性提供了两种配置方式：
                  - 常规配置：指定 RuleType 和 Ip 对当前加速域名进行配置。
                  - 全局配置：指定 SharedConfig 使用一个全局配置。全局配置是白名单功能。要使用此功能，请 提交工单。
                  您只能选择一种配置方式。
            MethodDeniedRule ( Object of MethodDeniedRule ): 否  表示 "禁用 HTTP Method" 特性的配置。
            NegativeCache ( Array of NegativeCache ): 否  表示 "状态码缓存" 特性的配置。在该配置中，您可以创建一个规则列表，说明如下：
                  - 每条规则包含过匹配条件配置和操作配置。
                  - 列表中最多可以包含 50 条规则。
                  - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            OriginAccessRule ( Object of OriginAccessRule ): 否  表示 "Origin 黑白名单" 特性的配置。
            OriginArg ( Array of OriginArg ): 否  表示 "回源参数" 配置的规则列表。
                  - 列表中最多可以包含 50 条规则。
                  - 每条规则包含一个匹配条件（Condition）和 CDN 执行操作（OriginArgAction）。
                  - 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
                  您必须在规则列表的最后添加以下这条默认规则。该默认规则用于匹配任何未能匹配其他规则的用户请求。您不可更改该规则中的 Condition，但可以更改 OriginArgAction 中的配置。
                  `json
                  {
                      "Condition": {
                          "ConditionRule": [
                              {
                                  "Object": "directory",
                                  "Operator": "match",
                                  "Type": "url",
                                  "Value": "/"
                              }
                          ]
                      },
                      "OriginArgAction": {
                          "OriginArgComponents": [
                              {
                                  "Action": "include",
                                  "Object": "queryString",
                                  "Subobject": "*"
                              }
                          ]
                      }
                  }
                  `
            OriginHost ( String ): 否  如果源站服务器上有多个站点，该参数表示回源请求访问的站点域名。该参数对所有源站配置生效，但是优先级低于源站配置中 OriginHost 参数。
                  该参数的默认值与 Domain 相同。
                  如果源站是一个对象存储桶，您无需指定该参数。其默认值与源站配置中的 Address 相同。
            OriginRange ( Boolean ): 否  表示 "回源 Range" 特性的配置。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。请求分片大小默认是 1 MB。
                  如果 Range 结构体中 Switch 为 true，则该特性为启用，即使 OriginRange 为 false。
            OriginRewrite ( Object of OriginRewrite ): 否  表示 "回源 URL 改写" 特性的配置。
            OriginSni ( Object of OriginSni ): 否  表示 "回源 SNI" 特性的配置。
            PageOptimization ( Object of PageOptimization ): 否  表示 "页面优化" 特性的配置。
            Quic ( Object of Quic ): 否  表示 QUIC 配置。
            RedirectionRewrite ( Object of RedirectionRewrite ): 否  表示 "URL 重定向改写" 特性的配置。
            RefererAccessRule ( Object of RefererAccessRule ): 否  表示 "Referer 黑白名单" 特性的配置。关于不同配置对请求匹配结果的影响，参见 配置示例。
            RemoteAuth ( Object of RemoteAuth ): 否  表示 "远程鉴权" 特性的配置。
            RequestHeader ( Array of RequestHeader ): 否  表示 "回源 HTTP 请求头" 特性的配置。
            ResponseHeader ( Array of ResponseHeader ): 否  表示 "HTTP 响应头" 特性的配置。
            ServiceRegion ( String ): 否  表示该加速域名的加速区域。该参数有以下取值：
                  - chinese_mainland：表示中国内地。
                  - global：表示全球。
                  - outside_chinese_mainland：表示全球（不含中国内地）。
                  该参数的默认值是 chinese_mainland。要指定另两个值，请 提交工单。
            SignedUrlAuth ( Object of SignedUrlAuth ): 否  表示 "URL 鉴权" 特性的配置。
            Timeout ( Object of Timeout ): 否  表示 "回源超时时间" 特性的配置。
            UaAccessRule ( Object of UaAccessRule ): 否  表示 "UA 黑白名单" 特性的配置。
            VideoDrag ( Object of VideoDrag ): 否  表示 "视频拖拽" 特性的配置。
            OriginIPv6 ( String ): 否  表示 "IPv6 回源" 的配置。该参数有以下取值：
                  - ipv6_first：表示 CDN 始终尝试获取源站域名的 IPv6 地址。如果无法获取该 IP 地址，CDN 才尝试获取源站域名的 IPv4 地址。
                  - ipv4_first：表示 CDN 始终尝试获取源站域名的 IPv4 地址。如果无法获取该 IP 地址，CDN 才尝试获取源站域名的 IPv6 地址。
                  - followclient：表示 CDN 尝试获取与用户请求相同类型的 IP 地址。
                  该参数的默认值是 followclient。
                  由于海外部分 CDN 回源节点不支持向 IPv6 地址发送回源请求，该功能仅适用于位于中国内地的回源节点。
            UrlNormalize ( Object of UrlNormalize ): 否  表示 "URL 标准化" 特性的配置。
            RequestBlockRule ( Object of RequestBlockRule ): 否  表示 "自定义拦截" 特性的配置。
            OriginCertCheck ( Object of OriginCertCheck ): 否  表示 "源站证书校验" 特性的配置。要使用此特性，请 提交工单。
                  该特性启用后，CDN 会校验源站证书的合法性，包括证书是否已被吊销、证书是否由可信 CA 签发、证书与源站域名是否匹配等。CDN 内置了常见可信 CA 的根证书。
                  该特性还支持双向认证，使源站对 CDN 身份进行校验。您需要在 CDN 中指定相应的客户端证书。
            ConditionalOrigin ( Object of ConditionalOrigin ): 否  表示 "条件源站" 特性的配置。要使用此特性，请 提交工单。
            OriginRetry ( Object of OriginRetry ): 否  表示 "回源重试设置" 特性的配置。要使用该功能，请 提交工单。
            RewriteHLS ( Object of RewriteHLS ): 否  表示 "标准 HLS 加密改写" 特性的配置。要使用该功能，请 提交工单。
            Websocket ( Object of Websocket ): 否  Websocket
            MultiRange ( Object of MultiRange ): 否  表示 "多重范围（Multi-range)" 特性的配置。
            RuleEngine ( Object of RuleEngine ): 否  规则引擎配置
            OfflineCache ( Object of OfflineCache ): 否  表示 "离线缓存" 特性的配置。要使用此特性，请 提交工单。
            OriginResponseHeader ( Array of OriginResponseHeader ): 否  表示 "源站响应头设置" 的配置。要使用该特性，请 提交工单。
            ProxyProtocol ( Object of ProxyProtocol ): 否  透传ProxyProtocol
            Range ( Object of Range ): 否  表示分片大小的设置。
            ServerSentEvent ( Object of ServerSentEvent ): 否  SSE协议
           "字段"： Origin
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginAction ( Object of OriginAction ): 是  表示源站配置，应用于所有用户请求。
           "字段"： AreaAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Area ( Array of String ): 否  表示一个国家和地区的列表，对该列表应用地域访问限制。当 Switch 是 true 时，该参数为必填。国家和地区的名称使用简写来表示。您可以调用 DescribeCdnRegionAndIsp 并指定 Area 为 Global 以获取国家和地区的简写。
            RuleType ( String ): 否  表示 Area 的类型。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - deny: 表示 Area 是一个黑名单。CDN 将阻止来自这些国家和地区的请求。
                  - allow: 表示 Area 是一个白名单。CDN 仅允许来自这些国家和地区的请求。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： BandwidthLimit
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            BandwidthLimitRule ( Object of BandwidthLimitRule ): 否  表示带宽限速的配置。当 Switch 是 true 时，该参数为必填。
           "字段"： BrowserCache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheAction ( Object of CacheAction ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheAction 中指定的操作。
           "字段"： Cache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheAction ( Object of CacheAction ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheAction 中指定的操作。
           "字段"： CacheHost
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheHostRule ( Array of CacheHostRule ): 否  表示一组共享缓存 HOST 的配置。当前您只能只能创建一个配置。当 Switch 是 true 时，该参数为必填。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： CacheKey
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheKeyAction ( Object of CacheKeyAction ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会为请求文件设置缓存键。该参数表示缓存键的配置。
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheKeyAction 中指定的操作。
                  CacheKey 中最后一条规则的 Condition 必须是以下设置。参见 请求示例。
                  `json
                  "Condition": {
                    "ConditionRule": [
                      {
                        "Object": "directory",
                        "Operator": "match",
                        "Type": "url",
                        "Value": "/"
                      }
                    ]
                  }
                  `
           "字段"： Compression
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            CompressionRules ( Array of CompressionRules ): 否  表示一组规则。每条规则包含匹配条件配置以及操作配置。
           "字段"： CustomErrorPage
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            ErrorPageRule ( Array of ErrorPageRule ): 否  表示一个配置规则的集合。您最多可以添加 50 条规则。
           "字段"： CustomizeAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CustomizeInstances ( Array of CustomizeInstances ): 是  表示一个规则列表。列表中的每条规则中定义了一个黑名单或者白名单的配置。
                  列表中最多可以包含 10 条规则。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： DownloadSpeedLimit
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            DownloadSpeedLimitRules ( Array of DownloadSpeedLimitRules ): 否  表示一个限速规则的列表。当 Switch 是 true 时，该参数为必填。该参数的其他说明如下：
                  - 每条规则包含匹配条件配置和限速配置。
                  - 列表中最多可以包含 50 条规则。
                  - 列表中规则的出现顺序表示规则的优先级排序。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
           "字段"： HTTPS
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  如果 Switch 是 true，您必须指定证书。
                  * 如果您指定的是单本证书，您需要指定 CertInfo。
                  * 如果您指定的是双证书，您需要指定 CertInfoList。
                  您指定的证书可以是托管在火山引擎证书中心，也可以是托管在 CDN。
            CertInfo ( Object of CertInfo ): 否  表示要与加速域名关联的单本证书。
                  * 如果该证书已托管在 CDN 或者火山引擎证书中心，您必须在 CertId 中指定该证书的 ID。
                  * 否则，您可以使用以下任意方法：
                  	* 调用 AddCertificate 将该证书上传到 CDN 或者火山引擎证书中心，然后调用 UpdateCdnConfig 关联上传的证书。
                  	* 调用 QuickApplyCertificate 在证书中心购买证书，然后调用 UpdateCdnConfig 关联上传的证书。
                  	* 在 Certificate 结构体中指定待上传的证书。上传后的证书托管在 CDN 并自动与您的加速域名关联。要使用该方法，请 提交工单。
            CertInfoList ( Array of CertInfoList ): 否  表示要与加速域名关联的双证书。要关联双证书，请 提交工单。
                  要关联的两本证书是必须已托管在 CDN 或者火山引擎证书中心。如果这两本证书中的任何一本还未上传，您可以调用 AddCertificate 将该证书上传到 CDN 或者火山引擎证书中心，然后调用 UpdateCdnConfig 关联这两本证书。
            DisableHttp ( Boolean ): 否  表示是否允许请求 URL 中 Scheme 是 HTTP 的请求。该参数有以下取值：
                  - true：表示允许 Scheme 是 HTTP 的请求。
                  - false：表示不允许 Scheme 是 HTTP 的请求。
                  该参数的默认值是 false。
            ForcedRedirect ( Object of ForcedRedirect ): 否  表示 "HTTP 强制跳转到 HTTPS" 特性的配置。
                  CDN 提供了两种协议重定向的特性。
                  * HTTP 重定向到 HTTPS，也就是 ForcedRedirect 特性。
                  * HTTPS 重定向到 HTTP，也就是 HttpForcedRedirect 特性。
                  这两个协议重定向特性是互斥的。也就是说，如果您启用了其中任意一个特性，就不能启用另一个。
            HTTP2 ( Boolean ): 否  表示是否为用户请求启用 HTTP/2 支持。该参数有以下取值：
                  - true：表示启用 HTTP/2。
                  - false：表示禁用 HTTP/2。
                  要启用该特性，您的加速域名必须已经启用了 HTTPS。
                  该参数的默认值是 false。
            Hsts ( Object of Hsts ): 否  表示 HSTS 特性的配置。
            OCSP ( Boolean ): 否  表示是否启用 "OCSP 装订" 特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  要启用该特性，您的加速域名必须启用了 HTTPS。该参数的默认值是 false。
            TlsVersion ( Array of String ): 否  表示 "TLS 版本" 特性的配置。该参数指定用户请求可以使用的 TLS 版本，有以下取值：
                  - tlsv1.0：表示 TLS 1.0。
                  - tlsv1.1：表示 TLS 1.1。
                  - tlsv1.2：表示 TLS 1.2。
                  - tlsv1.3：表示 TLS 1.3。
                  该参数的默认值是 ["tlsv1.1", "tlsv1.2", "tlsv1.3"]
            CertCheck ( Object of CertCheck ): 否  表示 "访问双向认证" 特性的配置。要配置 "访问双向认证"，请 提交工单。
            Keyless ( Object of Keyless ): 否  KeylessServer
           "字段"： HttpForcedRedirect
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            EnableForcedRedirect ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。启用后，CDN 会将收到的 HTTPS 请求重定向到 HTTP 请求。
                  - false：表示禁用该特性。CDN 不会将 HTTPS 请求重定向到 HTTP 请求。
                  要启用该特性，您的加速域名必须已启用 HTTPS。
            StatusCode ( String ): 是  表示当收到 HTTPS 请求时，CDN 返回的重定向状态码。该参数有以下取值：301、302、303、307、308。
                  该参数的默认值是 301。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
           "字段"： IPv6
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： IpAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Ip ( Array of String ): 是  表示黑名单或白名单中的 IP 地址。当 Switch 是 true 时，该参数为必填。您可以指定一个或者多个 IP 地址和 IP 地址网段。IP 地址和网段可以是 IPv4 或 IPv6 格式。您最多可输入 1,000 个地址。
                  如果您指定了 SharedConfig，就不能指定该参数。
            RuleType ( String ): 是  表示 IP 名单的类型。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - allow：表示白名单。
                  - deny：表示黑名单。
                  如果您指定了 SharedConfig，就不能指定该参数。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            SharedConfig ( Object of SharedConfig ): 否  表示一个全局配置。
                  如果您指定了该参数，就不能指定 RuleType 和 Ip。
            DenyStatusCode ( Long ): 否  拦截状态码
            IpSource ( Object of IpSource ): 否  IP判断来源
           "字段"： MethodDeniedRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            Methods ( String ): 否  表示被禁用的一个或多个 HTTP 请求方法。当 Switch 是 true 时，该参数为必填。多个方法使用逗号（,）分隔。该参数有以下取值：
                  - get：表示禁用 GET 请求方法。
                  - post：表示禁用 POST 请求方法。
                  - delete：表示禁用 DELETE 请求方法。
                  - put：表示禁用 PUT 请求方法。
                  - head：表示禁用 HEAD 请求方法。
                  - patch：表示 PATCH 请求方法。
                  - connect：表示 CONNECT 请求方法。
                  - options：表示 OPTIONS 请求方法。
           "字段"： NegativeCache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            NegativeCacheRule ( Object of NegativeCacheRule ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。
            Condition ( Object of Condition ): 否  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 NegativeCacheRule 中指定的操作。
           "字段"： OriginAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含 Origin 头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含 Origin 头部，则该请求被认为匹配您配置的 Origin 列表。
                  - false：表示如果请求不包含 Origin 头部，则该请求被认为不匹配您配置的 Origin 列表。
                  该参数的默认值是 false。
            IgnoreCase ( Boolean ): 是  表示 Origin 列表是否是大小写敏感的。该参数有以下取值：
                  - true: 表示 Origin 列表是大小写不敏感的。
                  - false: 表示 Origin 列表是大小写敏感的。
                  该参数的默认值是 true。
            Origins ( Array of String ): 是  表示一个 Origin 列表。列表中可以包含最多 100 个 Origins，总长度不能超过 3,000 个字符。Origin 可以是 IP 地址，CIDR 网段，域名和泛域名。域名可以是二级域名。IP 地址可以是 IPv4 和 IPv6 格式的地址。
            RuleType ( String ): 是  表示 Origin 列表的类型。该参数有以下取值：
                  - allow：表示白名单。
                  - deny：表示黑名单。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： OriginArg
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求满足该匹配条件，CDN 执行 OriginArgAction 中指定的操作。当前您必须且只能指定一个条件。
            OriginArgAction ( Object of OriginArgAction ): 是  表示在请求满足 Condition 时 CDN 执行的操作。
           "字段"： OriginRewrite
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginRewriteRule ( Array of OriginRewriteRule ): 否  表示一个规则列表。当 Switch 是 true 时，该参数为必填。
                  * 列表中最多可以包含 50 条规则。
                  * 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。
                  * 当收到一个用户请求时，CDN 按规则的优先级，从高到低尝试将请求与规则匹配。如果请求匹配了一条规则，CDN 就停止处理其余规则。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： OriginSni
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SniDomain ( String ): 否  指定回源 SNI 的域名。当 Switch 是 true 时，该参数为必填。该参数值的长度不能超过 1,024 个字符。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： PageOptimization
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OptimizationType ( Array of String ): 是  表示优化的对象。该参数有以下取值：
                  - html: 表示 HTML 页面。
                  - js: 表示 Javascript 代码。
                  - css: 表示 CSS 代码。
                  该参数的默认值是 html。如果您指定了 js 或者 js，html 也必须指定。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： Quic
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否为用户请求启用 QUIC。该参数有以下取值：
                  - true：表示启用 QUIC。
                  - false：表示禁用 QUIC。
                  要启用该特性，您的加速域名必须已启用 HTTPS。
           "字段"： RedirectionRewrite
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            RedirectionRule ( Array of RedirectionRule ): 否  表示一个 URL 重定向改写的规则的列表。当 Switch 是 true 时，该参数为必填。该列表最多可以包含 50 条规则。
                  列表中第一条规则的优先级最高。
                  当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
           "字段"： RefererAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含 Referer 头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含 Referer 头部，则该请求被认为匹配您配置的 Referer 列表。
                  - false：表示如果请求不包含 Referer 头部，则该请求被认为不匹配您配置的 Referer 列表。
                  该参数的默认值是 false。
            Referers ( Array of String ): 是  表示一个 Referer 列表，该参数的输入要求与 ReferersType 下 CommonType 类型的 Referers 的输入要求相同。建议您使用 ReferersType 来指定 Referer 列表。
                  另外，如果您指定了 SharedConfig，就不能指定该参数。
            ReferersType ( Object of ReferersType ): 是  表示一个 ReferersType 对象。其包含一个 CommonType 对象和一个 RegularType 对象，分别表示一个常规 Referer 列表和一个用于匹配 Referer 的正则表达式列表。您可以同时定义这两个对象。
                  如果您指定了 SharedConfig，就不能指定该参数。
            RuleType ( String ): 是  表示 Referer 名单的类型。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - allow：表示白名单。
                  - deny：表示黑名单。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            SharedConfig ( Object of SharedConfig ): 否  表示一个全局配置。要使用全局配置，请 提交工单。
                  如果您指定了该参数，除了 Switch 和 RuleType 以外，RefererAccessRule 下的其余参数都无需指定。
           "字段"： RemoteAuth
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            RemoteAuthRules ( Array of RemoteAuthRules ): 否  表示一个鉴权规则的列表。当前，列表中只能包含一条规则。该规则包含匹配条件配置和鉴权配置。当 Switch 是 true 时，该参数为必填。
           "字段"： RequestHeader
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RequestHeaderAction ( Object of RequestHeaderAction ): 是  表示一个请求头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： ResponseHeader
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ResponseHeaderAction ( Object of ResponseHeaderAction ): 是  表示 CDN 在响应用户请求的时候，对响应头的操作。
           "字段"： SignedUrlAuth
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            SignedUrlAuthRules ( Array of SignedUrlAuthRules ): 否  表示一个规则列表。每条规则包含匹配条件配置和鉴权配置。当前，列表中只能包含一条规则。当 Switch 是 true 时，该参数为必填。
           "字段"： Timeout
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。此时，TCP 请求和 HTTP 请求的超时时间使用默认值，分别是 2 秒和 60 秒。
                  该参数的默认值是 false。
            TimeoutRules ( Array of TimeoutRules ): 否  表示一组超时时间的配置。当前您只能指定一个配置。当 Switch 是 true 时，该参数为必填。
           "字段"： UaAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含 User-Agent 头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含 User-Agent 头部，则该请求被认为匹配您配置的 User-Agent 列表。
                  - false：表示如果请求不包含 User-Agent 头部，则该请求被认为不匹配您配置的 User-Agent 列表。
                  该参数的默认值是 false。
            IgnoreCase ( Boolean ): 是  表示 UA 字符串是否是大小写敏感的。该参数有以下取值：
                  - true: 表示 UA 字符串是大小写不敏感的。
                  - false: 表示 UA 字符串是大小写敏感的。
                  该参数的默认值是 false。
            RuleType ( String ): 是  表示指定的是黑名单还是白名单。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - deny: 表示指定的是黑名单。
                  - allow: 表示指定的是白名单。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            UserAgent ( Array of String ): 是  表示一个 UA 的列表。当 Switch 是 true 时，该参数为必填。该列表最多包含 1,000 个 UA。该参数的说明如下：
                  - 该参数值的长度不能超过 30,000 个字符。
                  - 如果 RuleType 是 allow，表示仅允许包含列表中的 UA 的请求访问加速域名。
                  - 如果 RuleType 是 deny，表示如果访问请求包含列表中的 UA，则不允许访问加速域名。
                  UA 能包含的字符有以下限制：
                  - UA 中可以使用 ` 表示一个或者多个字符。` 仅可以出现在 UA 的开头和末尾。
                  - UA 不能只包含 *或者空格。
                  - UA 如果包含符号，符号必须是被 HTML 编码的。
            SharedConfig ( Object of SharedConfig ): 否  表示一个全局配置。要使用全局配置，请 提交工单。
                  如果您指定了该参数，除了 Switch 和 RuleType，UaAccessRule 下的其余参数都无需指定。
           "字段"： VideoDrag
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： UrlNormalize
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            NormalizeObject ( Array of String ): 否  表示一个 URL 标准化选项列表。当 Switch 为 true 时，该参数为必填。列表中可以包含以下选项：
                  - dot_segments：表示将请求 URL 中的以下内容进行替换：
                  	- /./：替换为单个斜杠（/）。
                  	- /../：如果 /../ 前还有一个级别的目录，则删除 /../ 与该目录。如果 /../ 前没有目录，则保留原 URL。
                  - back_slashes：表示将请求 URL 中的反斜杠（）替换为单个斜杠（/）。
                  - successive_slashes：表示将请求 URL 中双斜杠（//）替换为单个斜杠（/）。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： RequestBlockRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BlockRule ( Array of BlockRule ): 是  表示一个规则列表。列表中最多可以包含 10 条规则。当 Switch 是 true 时，该参数为必填。
                  列表中第一条规则的优先级最高。
                  当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： OriginCertCheck
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
            CertInfoList ( Array of CertInfoList ): 否  表示一个 CA 证书列表，列表中的证书托管在 CDN，且不能是国密证书。CDN 使用该列表中的证书对来自源站的服务器证书进行校验。
                  当前，该列表中只能包含一本证书。
            ClientCertInfoList ( Array of ClientCertInfoList ): 否  仅当 Type 为 mutual 时，该参数有效。
                  该参数表示一个客户端证书列表，列表中的证书必须托管在 CDN，且不能是国密证书。源站使用该列表中的证书对 CDN 身份进行校验。
                  当前，该列表中只能包含一本证书。
            Type ( String ): 否  表示校验类型，有以下取值：
                  * unilateral：表示单向认证。
                  * mutual：表示双向认证。
                  该参数的默认值是 unilateral。
           "字段"： ConditionalOrigin
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginRules ( Array of OriginRules ): 否  表示一个规则列表。列表中的每条规则中定义了一组匹配条件以及 CDN 对满足匹配条件的请求所执行的操作。
                  列表中最多可以包含 20 条规则。
                  当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： OriginRetry
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            StatusCode ( String ): 否  表示范围在 400-599 之间的一个或者多个状态码。多个状态码之间使用分号（;）分隔。您可以输入 4xx 或者 5xx，表示所有以数字 4 或 数字 5 开头的状态码。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： RewriteHLS
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SignName ( String ): 否  表示签名参数的名称，长度不能超过 100 个字符。参数名称区分大小写，可以包含字母、数字、下划线（_）、中划线（-）、逗号（,）、句号（.）、感叹号（!）。
                  该参数的默认值是 DrmAuthToken。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： Websocket
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  无
            Timeout ( Long ): 否  无
           "字段"： MultiRange
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  * true：表示启用该特性。该特性启用后，CDN 允许指定了多重范围的 Range 请求。
                  * false：表示不启用该特性。如果收到一个指定了多重范围的 Range 请求，CDN 会拒绝该请求并返回 416 响应状态码。
                  该参数的默认值是 false。
           "字段"： RuleEngine
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Rules ( Array of Rules ): 否  无
            Switch ( Boolean ): 否  无
           "字段"： OfflineCache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Object ( String ): 否  表示该特性的触发条件，该参数有以下取值：
                  - request_error：表示回源请求异常。当回源请求出现异常时，CDN 没有获得源站的响应。
                  - error_code：表示源站响应状态码是 5xx。
                  - request_error,error_code：表示以上两个条件都包含。
            StatusCode ( String ): 否  表示一个或者多个响应状态码，范围是 500-599。多个状态码之间使用分号（;）分隔。您也可以输入 5xx，表示任意以数字 5 开头的状态码。
                  当 Object 是 error_code 或者 request_error,error_code 时，该参数才有效。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： OriginResponseHeader
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginResponseHeaderAction ( Object of OriginResponseHeaderAction ): 否  表示 CDN 在收到源站响应时，对响应头的操作。
           "字段"： ProxyProtocol
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  无
           "字段"： Range
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该设置。该参数有以下取值：
                  * true：表示启用该设置。
                  * false：表示禁用该设置。
                  该参数的默认值是 false。
            RangeSize ( Long ): 否  表示分片的大小。
                  * 如果 Unit 是 MB，该参数的取值范围是 1-40。
                  * 如果 Unit 是 KB，该参数值只能是 512。
                  该参数的默认值是 1。
            Unit ( String ): 否  表示 RangeSize 的单位。该参数有以下取值：
                  * KB
                  * MB
                  该参数的默认值是 MB。
           "字段"： ServerSentEvent
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  无
           "字段"： OriginAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginLines ( Array of OriginLines ): 是  表示一个源站列表。列表中最多可以包含 50 个源站。
           "字段"： BandwidthLimitRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BandwidthLimitAction ( Object of BandwidthLimitAction ): 否  表示限速行为的配置。
           "字段"： CacheAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示浏览器需要执行的操作。当前该参数值只能是 cache，表示缓存请求的文件。DefaultPolicy 中指定了如何缓存请求的文件。
            IgnoreCase ( Boolean ): 是  表示 Value 是否是大小写敏感的。
                  - true：表示大小写不敏感。
                  - false：表示大小写敏感。
                  该参数的默认值为 false。
            Ttl ( Long ): 是  表示浏览器需要缓存请求文件的时长，单位是秒。CDN 会在响应头中包含 Cache-Control: max-age 头部，头部值就是该参数值。
            DefaultPolicy ( String ): 否  表示浏览器该如何缓存请求的文件。该参数有以下取值：
                  - cache：表示需要缓存请求的文件。
                  - origin_first：表示遵循来自源站的缓存策略。该策略会包含在 CDN 的响应中。
                  - no_cache：表示不需要缓存请求的文件。
                  关于浏览器缓存策略的详细信息，参见 浏览器缓存策略。
           "字段"： Condition
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ConditionRule ( Array of ConditionRule ): 是  表示匹配条件列表。当前，列表中只能包含一个匹配条件。
           "字段"： CacheHostRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheHostAction ( Object of CacheHostAction ): 否  表示配置的详情。
           "字段"： CacheKeyAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheKeyComponents ( Array of CacheKeyComponents ): 是  缓存键是由请求中的 host、路径和查询字符串等部分组成。该参数表示其中各组成部分的配置。当前，您只能对缓存键中包含的查询字符串进行配置。
           "字段"： CompressionRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CompressionAction ( Object of CompressionAction ): 是  表示当用户请求满足 Condition 时，CDN 对请求文件执行的压缩操作的配置。
            Condition ( Object of Condition ): 否  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CompressionAction 中指定的操作。
                  需要留意的是，如果您指定了 CompressionFormat，Condition 必须为 null 或者不指定。
           "字段"： ErrorPageRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ErrorPageAction ( Object of ErrorPageAction ): 是  表示规则的相关配置。
           "字段"： CustomizeInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CustomizeRule ( Object of CustomizeRule ): 是  表示列表中一条规则的配置。
           "字段"： DownloadSpeedLimitRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DownloadSpeedLimitAction ( Object of DownloadSpeedLimitAction ): 是  表示限速配置。
            Condition ( Object of Condition ): 否  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 DownloadSpeedLimitAction 中指定的操作。
                  如果不指定该参数，CDN 对所有请求执行 DownloadSpeedLimitAction 中指定的操作。
           "字段"： CertInfo
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertId ( String ): 否  表示要关联的证书 ID。
                  您可以调用 ListCertInfo 获取您想要关联的证书 ID。
            Certificate ( Object of Certificate ): 否  表示一个待上传的证书。上传后的证书是托管在 CDN 的。
           "字段"： CertInfoList
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertId ( String ): 否  表示双证书中一本证书的 ID。
                  您可以调用 ListCertInfo 获取您想要指定的证书的 ID。
           "字段"： ForcedRedirect
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            EnableForcedRedirect ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。启用后，CDN 会将收到的 HTTP 请求重定向到 HTTPS 请求。
                  - false：表示禁用该特性。禁用后，CDN 不会将 HTTP 请求重定向到 HTTPS 请求。
                  要启用该特性，您的加速域名必须已启用 HTTPS。
            StatusCode ( String ): 是  表示当收到 HTTPS 请求时 CDN 的重定向响应状态码。该参数有以下取值：301、302、303、307、308。
                  该参数的默认值是 301。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
           "字段"： Hsts
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Subdomain ( String ): 否  表示 HSTS 配置是否也应用于加速域名的子域名。该参数有以下取值：
                  - include：表示 HSTS 配置应用于子域名站点。
                  - exclude：表示 HSTS 配置不应用于子域名站点。
                  该参数的默认值是 exclude。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
            Ttl ( Long ): 否  表示 Strict-Transport-Security 响应头在浏览器中的缓存过期时间，单位是秒。如果 Switch 是 true，该参数为必填。该参数的取值范围是 0 - 31,536,000。31,536,000 秒表示 365 天。如果该参数值为 0，其效果等同于禁用 HSTS 设置。
           "字段"： CertCheck
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertInfoList ( Array of CertInfoList ): 否  表示要与加速域名关联的一个 CA 证书列表。列表中最多包含两个 CA 证书。这些 CA 证书必须已托管在 CDN。CA 证书使用的加密算法可以是 RSA、ECC 或者 SM2。
                  如果要关联的证书还未上传，您可以调用 AddCertificate 将该证书上传到 CDN，然后调用 UpdateCdnConfig 关联该证书。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： Keyless
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertInfoList ( Array of CertInfoList ): 否  Keyless服务器证书校验-CA证书
            CheckType ( String ): 否  Keyless服务器证书校验
            ClientCertInfoList ( Array of ClientCertInfoList ): 否  Keyless服务器证书校验-客户端证书
            KeylessServer ( String ): 否  Keyless服务器地址
            Switch ( Boolean ): 否  Keyless开关
           "字段"： SharedConfig
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ConfigName ( String ): 否  表示一个全局配置的名称。该全局配置的 ConfigType 必须是 deny_ip_access_rule 或者 allow_ip_access_rule。
                  - deny_ip_access_rule：表示 IP 黑名单。
                  - allow_ip_access_rule：表示 IP 白名单。
                  您可以调用 ListSharedConfig 获取全局配置的列表。
           "字段"： IpSource
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SourceList ( Array of String ): 否  无
            Type ( String ): 否  无
           "字段"： NegativeCacheRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 执行的操作。当前该参数值只能是 cache，表示缓存源站的响应状态码。
            StatusCode ( String ): 是  指定一个需要缓存的状态码。状态码的范围是 400-599。您也可以指定 4xx 或者 5xx。4xx 表示 400 到 499 之间的所有状态码。5xx 表示 500 到 599 之间的所有状态码。
            Ttl ( Long ): 是  表示状态码的缓存时间。单位是秒。时间的范围是 1-315,360,000。315,360,000 表示 10 年。
            IgnoreCase ( Boolean ): 否  表示 Value 是否是大小写敏感的。
                  - true：表示大小写不敏感。
                  - false：表示大小写敏感。
                  该参数的默认值为 false。
           "字段"： OriginArgAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginArgComponents ( Array of OriginArgComponents ): 是  表示一个操作列表。这些操作定义了 CDN 如何处理回源请求中的查询参数。
                  当前，列表中只能包含一个操作。
           "字段"： OriginRewriteRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginRewriteAction ( Object of OriginRewriteAction ): 否  表示 CDN 执行的动作。
           "字段"： RedirectionRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RedirectionAction ( Object of RedirectionAction ): 是  表示一个 URL 重定向改写的规则。
           "字段"： ReferersType
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CommonType ( Object of CommonType ): 是  表示一个 CommonType 对象，其包含一个常规 Referer 列表。
            RegularType ( Object of RegularType ): 是  表示一个 RegularType 对象，其包含一个正则表达式列表用来匹配请求中的 Referer 头部。要使用该参数，请 提交工单。
           "字段"： RemoteAuthRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果一个请求满足匹配条件，CDN 对该请求执行 RemoteAuthRuleAction 中指定的操作。
            RemoteAuthRuleAction ( Object of RemoteAuthRuleAction ): 是  表示鉴权相关的配置。
                  当一个请求满足 Condition 中的匹配条件时，CDN 会将其发送至鉴权服务器进行鉴权，并基于鉴权的结果接受或者拒绝该请求。
           "字段"： RequestHeaderAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RequestHeaderInstances ( Array of RequestHeaderInstances ): 是  表示一个请求头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： ResponseHeaderAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ResponseHeaderInstances ( Array of ResponseHeaderInstances ): 是  表示一个响应头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： SignedUrlAuthRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Condition ( Object of Condition ): 是  表示匹配条件的配置。CDN 对符合条件的用户请求进行鉴权。
            SignedUrlAuthAction ( Object of SignedUrlAuthAction ): 是  表示签名计算的配置。
           "字段"： TimeoutRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            TimeoutAction ( Object of TimeoutAction ): 否  表示超时时间的配置。
           "字段"： BlockRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BlockAction ( Object of BlockAction ): 是  表示一条规则中 CDN 行为的配置。
            Condition ( Object of Condition ): 是  表示该规则中匹配条件的定义。
            RuleName ( String ): 是  表示规则的名称，长度不超过 20 个字符，可以包含字母、数字、下划线（_）、中划线（-）、汉字。一个汉字占 3 个字符。
           "字段"： ClientCertInfoList
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertId ( String ): 否  表示列表中一本客户端证书的 ID，以 cert_hosting 开头。
                  您可以调用 ListCertInfo 查询托管在 CDN 的客户端证书列表以获取您要指定的证书的 ID。
           "字段"： OriginRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Actions ( Object of Actions ): 否  表示一条规则中定义的操作配置。
            Condition ( Object of Condition ): 否  表示该规则中匹配条件的配置。
           "字段"： Rules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Id ( String ): 否  无
            Locked ( Boolean ): 否  无
            Name ( String ): 否  无
            Rule ( String ): 否  无
            DSLRule ( String ): 否  无
           "字段"： OriginResponseHeaderAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginResponseHeaderInstances ( Array of OriginResponseHeaderInstances ): 否  表示一个响应头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： OriginLines
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Address ( String ): 是  表示列表中一个源站的地址。该参数有以下说明：
                  - 如果 InstanceType 是 ip，您指定的是源站的 IP 地址。IP 地址可以是 IPv4 或 IPv6 地址。
                  - 如果 InstanceType 是 domain，您指定的是源站的域名。该域名不能是泛域名。
                  - 如果 InstanceType 是 tos，您指定的是存储桶域名，可以是云厂商分配的桶域名，也可以是您在云厂商处为存储桶设置的自定义域名。桶域名不能包含 https://，长度不能超过 100 个字符。存储桶可以来自火山引擎 TOS、阿里云 OSS、腾讯云 COS、AWS S3 或者任何使用鉴权方式与 S3 兼容的第三方对象存储服务，如七牛云、华为云等。
                  如果存储桶来自您账号下的 TOS 服务，在调用该 API 前，您需要在 CDN 控制台中打开该域名的配置页面。在该页面中，点击 授权 授权 CDN 访问您账号下的 TOS 服务。
            InstanceType ( String ): 是  表示源站的类型。该参数有以下取值：
                  - ip：表示 IP 地址。
                  - domain：表示域名。
                  - tos：表示对象存储桶。
                  在 CDN 向对象存储源站发送回源请求时，回源请求使用的方法与用户请求相同。默认情况下，用户请求可以使用的请求方法有 DELETE、GET、HEAD、POST、PUT、PATCH、OPTIONS、CONNECT。如果您不希望回源请求使用某些请求方法，例如您不希望回源请求使用 DELETE 方法，可能导致误删源站上的文件，建议您采取以下步骤：
                  1. 在存储桶所在的对象存储服务中设置权限，组织不符合预期的操作。
                  2. 在 CDN 的 MethodDeniedRule 特性中，指定 CDN 不支持的请求方法。
            OriginType ( String ): 是  表示源站的类别。该参数有以下取值：
                  - primary：表示主源站。
                  - backup：表示备源站。
                  源站列表中至少需要包含一个主源站。备源站是可选的。
            HttpPort ( String ): 否  表示 CDN 使用 HTTP 协议访问该源站时所访问的端口，取值范围是 1-65535，默认值是 80。如果源站服务器没有开放该端口，您无需指定该参数。
                  该参数仅当 InstanceType 为 ip 或 domain 时才有效。
            HttpsPort ( String ): 否  表示 CDN 使用 HTTPS 协议访问该源站时所访问的端口，取值范围是 1-65535，默认值是 443。如果源站服务器没有开放该端口，您无需指定该参数。
                  该参数仅当 InstanceType 为 ip 或 domain 时才有效。
            OriginHost ( String ): 否  表示回源请求访问的站点域名，适用于源站服务器上有多个站点的情况。
                  - 该参数的默认值与全局 OriginHost 相同，但优先级高于全局 OriginHost 参数。
                  - 该参数值的长度不能超过 1,024 个字符。
                  - 如果您在调用该 API 时，即没有修改 Address，也没有指定 OriginHost，OriginHost 不会被默认值覆盖，而是保持当前值。
            PrivateBucketAccess ( Boolean ): 否  表示存储桶是否是私有桶。该参数仅当 InstanceType 为 tos 时有效。该参数有以下取值：
                  - true：表示该存储桶是私有桶。
                  - false：表示该存储桶不是私有桶。
                  该参数的默认值是 false。
            PrivateBucketAuth ( Object of PrivateBucketAuth ): 否  表示访问存储桶的凭据。如果存储桶属于您火山引擎账号，您无需指定该参数。CDN 可以访问您账号下的 TOS 存储桶，无需凭证，即使存储桶是私有的。
            Region ( String ): 否  表示存储桶所在地域的信息，也就是存储桶的 region code。Region code 参与签名的计算。
                  如果 AuthType 是 aws_common 并且 PrivateBucketAccess 是 true，您必须指定该参数。
            Weight ( String ): 否  表示该源站的权重，取值范围是 1-100，默认值是 1。权重越大，该源站在 CDN 发送回源请求时被选择到的概率也越大。
                  该参数仅当 InstanceType 为 ip 或 domain 时才有效。
           "字段"： BandwidthLimitAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BandwidthThreshold ( Long ): 是  表示一个带宽阈值，单位是 bps。当您加速域名的带宽超过该阈值时，CDN 对加速域名启用 LimitType 所指定的带宽限制策略。该参数使用的进制是 1 Kbps = 1,000 bps。
            LimitType ( String ): 是  表示一个带宽限制策略。该参数有以下取值：
                  - downloadspeedlimit：表示 "单链接限速"。推荐使用该策略。
                  - speedlimit：表示 "IP 限速"。
                  - randomreject：表示 "拒绝请求"。
                  关于各策略限制带宽的方法，参见 配置带宽限制。
            SpeedLimitRate ( Long ): 否  表示数据传输速度的下限，单位是 B/S。在 CDN 逐次降低每个新请求或者每个 IP 地址的数据传输速度上限时，该上限不会低于 SpeedLimitRate。
                  - 如果 LimitType 是 downloadspeedlimit，该参数表示每个新请求的数据传输速度下限。
                  - 如果 LimitType 是 speedlimit，该参数表示每个 IP 地址的数据传输速度下限。
                  - 如果 LimitType 是 randomreject，该参数不适用。
                  该参数使用的进制是 1 KB/S = 1024 B/S。
            SpeedLimitRateMax ( Long ): 否  表示带宽限制策略启用时，CDN 对每个新请求或者每个 IP 地址设置的数据传输速度上限，单位是 B/S。在之后的每次带宽计算时，如果带宽依然超出阈值，该上限会逐次降低，直到带宽低于阈值或者该上限达到了 SpeedLimitRate。
                  - 如果 LimitType 是 downloadspeedlimit，该参数表示每个新请求的数据传输速度上限。
                  - 如果 LimitType 是 speedlimit，该参数表示每个 IP 地址的数据传输速度上限。
                  - 如果 LimitType 是 randomreject，该参数不适用。
                  该参数使用的进制是 1 KB/S = 1024 B/S。该参数的默认值是 SpeedLimitRate + 4,194,304。
           "字段"： ConditionRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Object ( String ): 是  表示匹配对象。该参数有以下取值：
                  - filetype：表示请求 URL 中的扩展名。
                  - directory：表示请求 URL 中的某个目录。
                  - path：表示请求 URL 中的完整路径。
                  - regex：表示请求 URL 中的路径，通过正则表达式匹配。
                  要指定 regex，请 提交工单。
            Operator ( String ): 是  表示匹配类型。该参数的值只能是 match，表示如果 Value 匹配了请求中的 Object，该请求就满足这个匹配条件。
            Type ( String ): 是  该参数值只能是 url，表示 "请求 URL"。
            Value ( String ): 是  表示一个或者多个匹配值，总长度不能超过 1,024 个字符。多个匹配值之间使用分号（;）分隔。匹配值不能包含以下字符：
                  - 双斜杠（//）、空格、美元符号（$）、问号（?）
                  同时，
                  - 如果 Object 是 filetype，每个匹配值表示一个请求 URL 后缀，无需以句点（.）开头，只能包含字母和数字。例如：png;txt。
                  - 如果 Object 是 directory，每个匹配值表示一个目录路径，以斜杠（/）开头和结尾。例如 /chs/foods/;/us/birds/。
                  - 如果 Object 是 path，每个匹配值表示一个 URL 路径，以斜杠（/）开头。每个匹配值中可以包含通配符（）表示一个或者多个字符。例如 /chs/foods/localsets;/us/birds/chickadee。
           "字段"： CacheHostAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheHost ( String ): 否  表示目标域名。 该目标域名必须是您账户下的一个加速域名。该参数指示 Domain 共享 CacheHost 的 CDN 缓存。
           "字段"： CacheKeyComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 如何在请求文件的缓存键中设置查询字符串。该参数有以下取值：
                  - exclude：表示缓存键不包含请求中的任何查询参数。
                  - include：表示缓存键包含请求中所有的查询参数。
                  - includePart：表示缓存键仅包含  Subobject 中指定的查询参数。
                  - excludePart：表示缓存键包含请求中除了 Subobject 中指定的查询参数之外的所有查询参数。
            IgnoreCase ( Boolean ): 是  表示 Subobject 是否是大小写敏感的。该参数有以下取值：
                  - true：表示大小写不敏感。
                  - false：表示大小写敏感。
                  该参数的默认值为 false，并且仅当 Action 是 includePart 或 excluePart 时有效。
            Object ( String ): 是  表示缓存键中的一个组成部分。当前该参数值只能是 querystring，表示查询字符串。
            Subobject ( String ): 是  该参数对应于 Action，表示 CDN 在缓存键中包含的具体查询参数。该参数的说明如下：
                  - 如果 Action 是 include 或者 exclude，Subobject 必须是 *，表示请求中的全部查询参数。
                  - 如果 Action 是 includePart 或者 excludePart，表示需要保留或者不保留的查询参数。多个查询参数之间使用分号（;）分隔。您指定的查询参数不能是 *，也不能包含双斜杠（//）、百分号（%）、空格。
           "字段"： CompressionAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CompressionType ( Array of String ): 是  表示 CDN 使用的压缩算法。该参数有以下取值：
                  - br：表示 Brotli 压缩算法。
                  - gzip：表示 Gzip 压缩算法。
                  您可以同时指定这两个算法。
                  需要留意的是，CDN 基于用户请求中 Accept-Encoding 头部来决定是否对请求文件进行压缩以及使用的压缩算法。
            CompressionFormat ( String ): 否  表示 CDN 基于请求中的 Content-Type 头部对请求进行匹配。该参数有以下取值：
                  * default：表示如果 Content-Type 头部值在下方的默认列表中，CDN 对请求文件执行 CompressionAction 中配置的操作。
                  * customize：表示如果 Content-Type 头部值在 CompressionFormat 指定的头部值中，CDN 对请求文件执行 CompressionAction 中配置的操作。
                  如果您需要 CDN 基于 Condition 中的匹配条件对请求进行匹配，您无需指定 CompressionFormat 或者指定 CompressionFormat 为 all。
                  默认列表
                  text/html、text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、text/javascript、image/tiff、image/svg+xml、application/json、application/xml、text/plain; charset=utf-8
            CompressionTarget ( String ): 否  表示 Content-Type 的过滤值。
                  - 如果 CompressionFormat 为 default 或者 all，该参数必须为 *。
                  - 如果 CompressionFormat 为 customize，您需要指定一个或者多个文件类型。多个文件类型之间以逗号（,）分隔。
            MinFileSizeKB ( Long ): 否  表示文件大小范围的最小值，CDN 仅对大小在 MinFileSizeKB 和 MaxFileSizeKB 所表示的范围内的文件进行压缩。该参数的取值范围是 0 - 2,147,483,647，单位是 KB，使用的进制是 1,024。该参数的默认值是 0。
            MaxFileSizeKB ( Long ): 否  表示文件大小范围的最大值，取值范围是 0 - 2,147,483,647，单位是 KB，使用的进制是 1,024。如果不指定该参数，表示您不限制文件大小的上限。
           "字段"： ErrorPageAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示实际的操作。当前您只能指定该参数值为 redirect。表示对客户端请求进行重定向。
            RedirectCode ( String ): 是  表示重定向的响应状态码。您可以根据需求选择合适的状态码。该参数的取值有 301、302、303、307、308。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
            RedirectUrl ( String ): 是  表示跳转的目标地址，长度不能超过 1,024 个字符。地址必须包含协议，域名以及路径，并且符合 URL 的规范。
            StatusCode ( String ): 是  表示一个状态码，取值范围是 400-599。您可以输入 4xx 或者 5xx。4xx 表示 400-499 之间的所有状态码。5xx 表示 500-599 之间的所有状态码。
           "字段"： CustomizeRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AccessAction ( Object of AccessAction ): 是  表示该规则中的黑名单或者白名单的配置。
           "字段"： DownloadSpeedLimitAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SpeedLimitRate ( Long ): 是  表示 CDN 在响应单个请求时的最大数据传输速度，单位是 B/S，使用的进制是 1,024。该参数的取值范围是 1-1,073,741,824,000,000。1,073,741,824,000,000 是 1,000,000 Gbps。
            SpeedLimitRateAfter ( Long ): 否  表示一个初始数据量，单位是 bytes，使用的进制是 1,024。该参数的取值范围是 0-1,073,741,824,000,000。
                  当 CDN 对一个请求开始传输数据时，在传输的数据量达到该初始数据量前，该限速规则不会启用。
                  如果该参数值是 0，表示在 CDN 对一个请求开始传输第一个字节时，该限速规则就启用了。
            SpeedLimitTime ( Object of SpeedLimitTime ): 否  表示限速规则启用的日期和时间段。
            DynamicLimitUnit ( String ): 否  动态限速类型时必填，表示动态限速单位，可选B/S、KB/S、MB/S
            LimitQueryName ( String ): 否  动态限速类型时必填，表示限速参数名称
            LimitType ( String ): 否  限速类型。非必填，不传为 normal ，表示固定限速值，dynamic_limit:表示动态限速
           "字段"： Certificate
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Certificate ( String ): 否  表示证书文件的内容。内容中的换行必须使用 rn 替换。该证书文件的扩展名是 .crt 或者 .pem，并且证书文件必须包含完整的证书链。
                  - 如果该证书使用的加密算法是 RSA 或者 ECC，该文件是您要上传的服务器证书的证书文件。文件名类似 .crt。
                  - 如果该证书使用的加密算法是 SM2，该文件是您要上传的国密证书的证书文件，用于验证签名。文件名类似 _sign.crt。
                  对于待上传的证书，该参数必填。
            PrivateKey ( String ): 否  表示私钥文件的内容。内容中的换行必须使用 rn 替换。该私钥文件的扩展名是 .key 或者 .pem。
                  - 如果该证书使用的加密算法是 RSA 或者 ECC，该文件是您要上传的服务器证书的私钥文件。文件名类似 .key。
                  - 如果该证书使用的加密算法是 SM2，该文件是您要上传的国密证书的私钥文件，用于生成签名。文件名类似 _sign.key。
                  对于待上传的证书，该参数必填。
            EncryptionCert ( String ): 否  表示国密证书的证书文件的内容。内容中的换行必须使用 rn 替换。该文件用于加密，扩展名是 .crt 或者 .pem。文件名类似 _encrypt.crt。
                  如果待上传的证书不是国密证书，该参数无效。
            EncryptionKey ( String ): 否  表示国密证书的私钥文件的内容。内容中的换行必须使用 rn 替换。该文件用于解密，扩展名是 .key 或者 .pem。文件名类似 _encrypt.key。
                  如果待上传的证书不是国密证书，该参数无效。
           "字段"： OriginArgComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 执行的操作。该参数有以下取值：
                  - include: 表示回源请求 URL 中包含用户请求 URL 中的全部查询参数。
                  - exclude：表示回源请求 URL 中不包含用户请求 URL 中的任何查询参数。
                  - addPart：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数，并额外包含 Subobject 中指定的查询参数。
                  - includePart：表示如果用户请求 URL 中包含 Subobject 中指定的查询参数，那么回源请求 URL 中包含这些指定的查询参数。
                  - excludePart：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数，除了Subobject 中指定的查询参数。
                  - set：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数。同时，对于您在 Subobject 中指定的查询参数和参数值，CDN 会执行以下操作:
                    - 如果这些查询参数在用户请求 URL 中，CDN 会在回源请求 URL 中将这些参数的值设置为您指定的值。
                    - 如果用户请求 URL 中不包含这些查询参数，CDN 会在回源请求 URL 中添加这些查询参数。
            Object ( String ): 是  表示 CDN 对哪个对象执行 Action。当前，该参数值只能是 queryString，表示请求 URL 中的查询字符串。
            Subobject ( String ): 是  表示一个或者多个查询参数。多个查询参数之间使用分号（;）分隔，总长度不能超过 1,024 个字符。Subobject 只能包含字母、数字、下划线（_）、逗号（,）、短横线（-）、句点（.）和感叹号（!）。
                  在匹配请求 URL 中的查询参数时，Subobject 中的参数是大小写敏感的。
                  Subobject 的额外说明如下：
                  * 当 Action 是  include 或 exclude 时，Subobject 必须是 *，表示请求 URL 中的所有查询参数。
                  * 当 Action 是  includePart 或 excludePart 时，Subobject 表示一个或者多个查询参数。例如 param1;param2。
                  * 当 Action 是  addPart 或 set 时，Subobject 表示一个或者多个查询参数和参数值，格式是 key=value。例如 param1=val1;param2=val2;param3=val3。
           "字段"： OriginRewriteAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SourcePath ( String ): 否  表示一个正则表达式，长度不能超过 1,024 个字符，用于匹配用户请求 URL 中的对象。
                  * 当 RewriteType 是 rewrite_path 时，该对象指的是请求 URL 中的路径。
                  * 当 RewriteType 是 rewrite_url 时，该对象指的是请求 URL 中的路径和查询字符串。
                  参见 配置示例。
                  假设您在调用该 API 时在 SourcePath 中使用 ? 表示查询字符串中开头的 ?。当您调用 DescribeCdnConfig 查看 SourcePath 的值时，您会发现 ? 变成了 ?。这个变化是符合预期的，因为 DescribeCdnConfig 返回内容是 JSON 格式，内容中的 ` 被转义成了 `。
            TargetPath ( String ): 否  表示改写后，回源请求 URL 中的对象，长度不能超过 1,024 个字符。
                  * 当 RewriteType 是 rewrite_path 时，该对象是回源请求 URL 中的路径。
                  * 当 RewriteType 是 rewrite_url 时，该对象是回源请求 URL 中的路径和查询字符串。
                  您可以在 TargetPath 中使用 $1、$2、$3 等捕获 SourcePath 中定义的组。
                  参见 配置示例。
            RewriteType ( String ): 否  表示改写类型。该参数有以下取值：
                  * rewrite_path：表示对请求 URL 中的路径进行改写。
                  * rewrite_url：表示对请求 URL 中的路径和查询字符串进行改写。
                  该参数的默认值是 rewrite_path。
           "字段"： RedirectionAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RedirectCode ( String ): 是  表示 URL 重定向的响应状态码。该参数的取值有 301、302、303、307、308。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
            SourcePath ( String ): 是  表示文件的原路径。也就是请求中包含的路径。路径必须以斜杠（/）开头并且不能包含双斜杠（//）、百分号（%）、空格。该参数值的长度不能超过 1,024 个字符。
            TargetHost ( String ): 是  表示目标路径所归属站点的域名或者 IP 地址。IP 地址必须是 IPv4 类型的地址。该参数值的长度不能超过 1,024 个字符。该参数的默认值就是您的加速域名。
            TargetPath ( String ): 是  表示跳转后的目标路径。路径必须以斜杠（/）开头并且不能包含双斜杠（//）、百分号（%）、空格。该参数值的长度不能超过 1,024 个字符。
            TargetProtocol ( String ): 是  表示 URL重定向后的新请求所使用的协议。该参数有以下取值：
                  - followclient：表示使用原请求的协议。
                  - http：表示新请求强制使用 HTTP 协议。
                  - https：表示新请求强制使用 HTTPS 协议。
            TargetQueryComponents ( Object of TargetQueryComponents ): 是  表示原请求 URL 中的查询参数的处理方式。
           "字段"： CommonType
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            IgnoreCase ( Boolean ): 否  表示 CommonType 下的 Referers 列表是否是大小写敏感的。该参数有以下取值：
                  - true: 表示大小写不敏感。
                  - false: 表示大小写敏感。
                  该参数的默认值是 true。
            Referers ( Array of String ): 是  表示一个常规 Referer 列表。在该列表中，您可以指定一个或者多个 IP 地址，CIDR 网段，域名和泛域名。域名可以是二级域名。IP 地址只能是 IPv4 格式的地址。您最多可输入 1,000 个 IP 地址。输入的域名不能包含 http:// 或 https://。该参数值的长度不能超过 30,000 个字符。
            IgnoreScheme ( Boolean ): 否  表示 CDN 是否对 Referer 中的 scheme 进行校验，也就是校验 Referer 是否包含 http:// 或者 https://。该参数有以下取值：
                  - true: 表示 CDN 不校验 Referer 是否包含 scheme。在这个情况下，无论 Referer 是否包含 scheme，CDN 都会将 Referer 与您配置的名单进行匹配校验。
                  - false: 表示 CDN 会先校验 Referer 是否包含 scheme。只有 Referer 包含 scheme，CDN 才会将 Referer 与您配置的名单进行匹配校验。否则，CDN 判定请求与您配置的名单不匹配。
                  该参数的默认值是 false。
                  另外，该配置对 RegularType 下的正则表达式列表不生效，因为 CDN 依赖正则表达式来判断 Referer 是否匹配正则名单。
            ContMainDomain ( Boolean ): 否  泛域名匹配包含主域名
           "字段"： RegularType
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Referers ( Array of String ): 是  表示一个用于匹配 Referer 的正则表达式列表。该参数值的长度不能超过 30,000 个字符。
           "字段"： RemoteAuthRuleAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AuthModeConfig ( Object of AuthModeConfig ): 是  表示鉴权服务器的配置。
            AuthResponseConfig ( Object of AuthResponseConfig ): 是  CDN 需要对鉴权服务器返回的鉴权状态码进行处理。该参数表示相关的配置。
            QueryStringRules ( Object of QueryStringRules ): 是  表示鉴权请求的参数设置。
            RequestBodyRules ( String ): 是  表示鉴权请求正文的规则。您可以不指定该参数或者设置该参数值为 default。default 表示请求正文为空（""）。
            RequestHeaderRules ( Object of RequestHeaderRules ): 是  表示鉴权请求头的设置。您最多可以设置 50 个请求头。
           "字段"： RequestHeaderInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  指定对请求头的操作。该参数有以下取值：
                  - set：表示设置一个头部。设置操作包括添加与修改。如果请求中已包含该头部，该头部的值会被覆盖。如果请求中没有包含该头部，该头部会被添加。
                  - delete，表示删除一个头部。
            Key ( String ): 是  指定一个头部的名称。名称的长度不能超过 1,024 个字符，不区分大小写。同时，名称不能包含以下字符：
                  - 下划线（_）、空格、双引号（"）
                  另外，头部名称不能使用这些 特定的名称。
            ValueType ( String ): 是  指定 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值：
                  - constant：表示 Key 的值是一个固定字符串。
                  - variable：表示 Key 的值来自一个变量。
                  - customize：表示 Key 的值是变量与固定字符串拼接后的一个字符串。
            Value ( String ): 否  表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。当 ValueType 是 constant 时，您需要指定一个字符串作为头部的值。该头部值的长度不能超过 1,024 个字符，不能包含美元符号（$）。
                  当 ValueType 是 variable 时，Key 的值可以是来自 该列表中的某个变量。除了名称包含下划线的变量，列表中的任何一个变量都可以作为 Key，并赋予一个字符串来替换其已有的值。也就是说，当您使用任意这些名称不包含下划线的变量作为 Key 时，其值是可以被覆盖的。
                  当 ValueType 是 customize 时，表示 Key 的值是列表中的变量与字符串拼接后的字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：aaa${http_host}bbb${msec}ccc
           "字段"： ResponseHeaderInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  指定对响应头的操作。该参数有以下取值：
                  - set：表示设置一个头部。设置操作包括添加与修改。如果源站响应中已包含该头部，该头部的值会被覆盖。如果源站响应中没有包含该头部，该头部会被添加。
                  - delete，表示删除一个头部。
            Key ( String ): 是  指定一个头部的名称。名称不能超过 1,024个字符，不区分大小写，不能包含以下字符：
                  - 下划线（_）、空格、双引号（"）
                  同时，头部名称不能使用这些 特定的名称。
            ValueType ( String ): 是  指定 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值：
                  - constant：表示 Key 的值是一个字符串。
                  - variable：表示 Key 的值来自一个变量。
                  - customize：表示 Key 的值是一个变量与字符串拼接后的字符串。
            AccessOriginControl ( Boolean ): 否  表示在 CDN 响应用户请求时，是否校验请求中的 Origin 头部。
                  该参数有以下取值：
                  - true：表示 CDN 会校验 Origin 头部。如果校验成功，CDN 会在响应中包含 Access-Control-Allow-Origin 头部。头部值与 Origin 头部值相同。如果校验失败，响应中不会包含 Access-Control-Allow-Origin 头部。
                  - false：表示 CDN 不会校验 Origin 头部。在响应中，CDN 会包含 Access-Control-Allow-Origin 头部。头部值是您配置的 Access-Control-Allow-Origin 的内容。
                  该参数的默认值是 false。
                  该参数仅在以下条件都满足的情况下有效：
                  - Action 是 set。
                  - Key 是 Access-Control-Allow-Origin。
                  - ValueType 是 constant。
            Value ( String ): 否  表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。当 ValueType 是 constant 时，您需要指定一个字符串作为头部的值。头部值的长度不能超过 1,024 个字符，不能包含美元符号（$）。
                  当 ValueType 是 variable 时，Key 的值可以是来自 该列表中的某个变量。除了名称包含下划线的变量，列表中的任何一个变量都可以作为 Key，并赋予一个字符串来替换其已有的值。也就是说，当您使用任意这些名称不包含下划线的变量作为 Key 时，其值是可以被覆盖的。
                  当 ValueType 是 customize 时，表示 Key 的值是列表中的变量与字符串拼接后的一个字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：${remote_addr}aaa${host}ccc
           "字段"： SignedUrlAuthAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Duration ( Long ): 是  表示签名的有效时间，单位是秒。该参数与请求中包含时间戳搭配使用，用来计算签名的过期时间。该参数的取值范围是 0-315,360,000。签名的过期时间 = 时间戳 + Duration。在 CDN 收到某个请求时，如果签名的过期时间小于当前时间，CDN 判定签名已过期。
            MasterSecretKey ( String ): 是  表示主密钥，长度为 6-40个字符。
            URLAuthType ( String ): 是  签名类型。该参数有以下取值：typea、typeb、typec、typed、typee，每种类型得鉴权说明见 配置 URL 鉴权 。
            BackupSecretKey ( String ): 否  表示备密钥。备密钥的长度为 6-40个字符。
            CustomVariableRules ( Object of CustomVariableRules ): 否  表示自定义签算变量。
            KeepOriginArg ( Boolean ): 否  表示 CDN 是否在回源请求中包含用户请求中的签名参数。仅当 URLAuthType 是 typea 或 typed 时，你可以设置该参数。并且，要设置该参数，请 提交工单。
                  该参数有以下取值：
                  * true：表示 CDN 在回源请求中包含签名参数。
                  * false：表示 CDN 在回源请求中不包含签名参数。
                  另外，
                  * 当 URLAuthType 是 typea 或 typed 时，该参数的默认值是 false。
                  * 当 URLAuthType 是 typeb 或 typec 时，该参数值必须是 false。
                  * 当 URLAuthType 是 typee 时，该参数值必须是 true。
            RewriteM3u8 ( Boolean ): 否  对于 HLS Manifest (.m3u8) 的请求，该参数表示 CDN 是否要修改 Manifest，从而为每个视频分片生成签名并将签名添加到 URI 中。
                  该参数有以下取值：
                  - true：表示需要修改 Manifest。
                  - false：表示不需要修改 Manifest。
                  该参数的默认值是 false。
                  当 URLAuthType 为 typee 时，该参数无效。
                  当前，CDN 不会修改压缩文件。因此，在以下任何情况下，CDN 都不会修改 Manifest。
                  * 源站响应中包含 Content-Encoding 头部。该标头表明该 Manifest 已被压缩。
                  * 用户请求匹配 "智能压缩" 特性中的规则。
            SignName ( String ): 否  表示签名参数的名称。该参数的说明如下：
                  - 可以包括英文字母、数字、下划线（_）、中划线（-）、句号（.）、逗号（,）、感叹号（!）。
                  - 长度不能超过 100 个字符。
                  - 至少包含一个字母或者数字。
                  - 不能与 TimeName 相同。
                  当 URLAuthType 为 typea、typed、typee 时，该参数为必填。对于其他类型，该参数不生效。
            SignatureRule ( Array of String ): 否  当 URLAuthType 为 typee 时，该参数为必填，表示需要纳入签名计算的字段。必须纳入签名计算的字段如下：
                  - key：表示MasterSecretKey或 BackupSecretKey 参数的值。
                  - uri：表示用户请求资源的 URI。如果 URI 包含中文字符，您需要对 URI 编码。
                  - TimeName：表示 TimeFormat 参数的值。
                  可选择纳入签名计算的字段如下：
                  - domain：表示加速域名。
                  - referer：表示用户请求携带的 referer 值。
                  - ua：表示用户请求携带的 User-Agent 值。
                  - ip：表示用户请求的客户端 IP。
                  - origin：表示用户请求携带的 Origin 值。
                  - 自定义变量：表示您在 CustomVariableInstances 中定义的变量名称。
                  CDN 按列表中字段出现顺序将这些字段拼接成一个字符串，然后计算该字符串的 MD5 值。该 MD5 值就是签名。
            TimeFormat ( String ): 否  表示 TimeName 使用的进制。该参数有以下取值：
                  - decimal：十进制。
                  - heximal：十六进制。
                  当 URLAuthType 为 typed、typee 时，该参数为必填。当 URLAuthType 为 typec 时，无论您是否设置该参数，该参数的值会被强制设置为 heximal。对于 URLAuthType 的其他值，该参数不生效。
            TimeName ( String ): 否  表示时间戳参数的名称。TimeName 的值可以包括英文字母、数字、下划线（_）、中划线（-）、句号（.）、逗号（,）、感叹号（!），长度为 1-100 个字符。TimenName 不能与 SignName 相同。
                  当 URLAuthType 为 typed、typee 时，该参数为必填。对于其他类型，该参数不生效。
            RewriteM3u8Rule ( Object of RewriteM3u8Rule ): 否  表示 "M3U8 改写" 功能的配置。该配置仅当以下条件都满足时才有效：
                  - RewriteM3u8 是 true。
                  - URLAuthType 不是 typee。
                  要设置该参数，请 提交工单。
            AuthAlgorithm ( String ): 否  表示签名计算使用的算法。该配置有以下取值：
                  - md5：表示 MD5 算法。
                  - sha256：表示 SHA-256 算法。
                  该参数的默认值是 md5。
           "字段"： TimeoutAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            HttpTimeout ( Long ): 否  表示 HTTP 请求的超时时间。该参数的取值范围是 5-60。
            TcpTimeout ( Long ): 否  表示 TCP 请求的超时时间。该参数的取值范围是 2-60。
           "字段"： BlockAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 如何处理匹配 Condition 的请求。该参数有以下取值：
                  - refuse：表示 CDN 拒绝请求并响应一个 4xx 的错误码。错误码在 StatusCode 中指定。
                  - redirect：表示 CDN 将请求重定向到 RedirectUrl 中指定的 URL。
            StatusCode ( String ): 是  表示对于匹配 Condition 的用户请求，CDN 的响应状态码。
                  - 当 Action 是 refuse 时，该参数表示一个 400-499 范围内的错误码。
                  - 当 Action 是 redirect 时，该参数有以下取值：
                  	- 301：表示响应状态码是 301。
                  	- 302：表示响应状态码是 302。
            ErrorPage ( String ): 否  - 当 Action 是 refuse 时，该参数是可选的，说明如下：
                  	- 如果指定该参数，该参数表示 "全局配置" 特性中的一个自定义响应页面的名称。也就是说，当 CDN 拒绝请求时，返回该自定义页面。需要留意的是，要使用 "全局配置"，请 提交工单。
                  	- 如果不指定该参数，表示 CDN 使用 StatusCode 中指定错误码的标准响应正文。
                  - 当 Action 是 redirect 时，该参数无效，可以不指定。
            RedirectUrl ( String ): 否  - 当 Action 是 redirect 时，该参数必填，表示重定向 URL。URL 必须以 http:// 或 https:// 开头，长度不能超过 1,024 个字符。
                  - 当 Action 是 refuse 时，该参数无效，可以不指定。
           "字段"： Actions
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginLines ( Array of OriginLines ): 否  表示一个源站列表。当前，列表中只能包含一个源站。
           "字段"： OriginResponseHeaderInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示 CDN 对响应头的操作。该参数有以下取值：
                  - set：表示设置一个头部。设置操作包括添加与修改。如果源站响应中已包含该头部，该头部的值会被覆盖。如果源站响应中没有包含该头部，该头部会被添加。
                  - delete：表示删除一个头部。
            Key ( String ): 否  表示一个头部的名称。名称不能超过 1,024 个字符，不区分大小写，不能包含汉字以及以下字符：
                  - 汉字、下划线（_）、空格、双引号（"）、冒号（:）
                  参见 常用头部。
            Value ( String ): 否  表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。
                  - 当 ValueType 是 constant 时，您需要指定一个固定字符串作为头部的值。头部值的长度不能超过 1,024 个字符，不能包含美元符号（$）。
                  - 当 ValueType 是 variable 时，Key 的值可以是来自 该列表中的某个变量。除了名称包含下划线的变量，列表中的任何一个变量都可以作为 Key，并赋予一个固定字符串来替换其已有的值。也就是说，当您使用任意这些名称不包含下划线的变量作为 Key 时，其值是可以被覆盖的。
                  - 当 ValueType 是 customize 时，表示 Key 的值是列表中的变量与固定字符串拼接后的字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：${remote_addr}aaa${host}ccc
            ValueType ( String ): 否  表示 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值：
                  - constant：表示 Key 的值是一个固定字符串。
                  - variable：表示 Key 的值来自一个变量。
                  - customize：表示 Key 的值是一个变量与固定字符串拼接后的字符串。
            Object ( String ): 否  表示该规则对哪些用户请求生效。该参数有以下取值：
                  - default：表示该规则仅对源站响应中包含以下响应码的用户请求生效：
                  	- 200、201、204、206、301、302、303、304、307、308
                  - all_request：表示该规则对所有用户请求生效。
                  该参数的默认值是 default。另外，当 Action 是 delete 时，该参数的值只能是 all_request。
           "字段"： PrivateBucketAuth
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示访问存储桶是否需要凭证。如果您指定了 PrivateBucketAuth 结构体，该参数值必须是 true。
            AuthType ( String ): 否  表示存储桶使用的是哪个对象存储服务所提供的鉴权方式。该参数有以下取值：
                  - tos：表示火山引擎 TOS。
                  - cos：表示腾讯云 COS。
                  - oss：表示阿里云 OSS。
                  - aws_common：表示 AWS S3 或者其他使用兼容 S3 鉴权方式的第三方对象存储服务。如果您要使用您在云厂商处为存储桶配置的自定义域名，请指定 AuthType 为 aws_common。
                  - aws: 含义与 aws_common 相同，不支持指定自定义域名，不推荐使用。
                  如果存储桶来自另一个主账号下的 TOS 服务，请设置 AuthType 为 aws_common.
            TosAuthInformation ( Object of TosAuthInformation ): 否  表示存储桶的访问凭证。当以下任意条件满足时，您必须指定该参数。
                  * AuthType 不是 tos。
                  * 存储桶来自另一个主账号下的 TOS 服务。
           "字段"： AccessAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含指定头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含指定头部，则该请求被认为匹配您配置的头部值列表。
                  - false：表示如果请求不包含指定头部，则该请求被认为不匹配您配置的头部值列表。
                  该参数的默认值是 false。
            ListRules ( Array of String ): 是  表示一个正则表达式列表，用于匹配请求头的值。
                  列表中的正则表达式不能超过 20 个，所有正则表达式总长度不能超过 1,024 个字符。正则表达式之间的关系是或。也就是说，如果一个用户请求中 RequestHeader 的值匹配任何一个正则表达式，该规则就匹配了这个请求。
            RequestHeader ( String ): 是  表示一个指定的请求头。头部名称不区分大小写，并且有以下要求：
                  - 名称的长度不超过 1,024 个字符，
                  - 名称不能是 Referer、User-Agent 或 Origin。
                  - 名称可以包含字母，数字，下划线（_），连字符（-）。
                  - 名称不能以数字开头。
            RuleType ( String ): 是  表示名单的类型。该参数有以下取值：
                  - allow：表示该规则中定义的是一个白名单。如果一个用户请求不匹配白名单，CDN 会拒绝该请求，响应 403 状态码。
                  - deny：表示该规则中定义的是一个黑名单。如果一个用户请求匹配了黑名单，CDN 会拒绝该请求，响应 403 状态码。
           "字段"： SpeedLimitTime
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DayWeek ( String ): 是  表示该限速规则启用的日期，有以下取值：monday，tuesday，wednesday，thursday，friday，saturday，sunday，unlimited。
                  unlimited 表示每天。您可以指定一个或多个日期，多个日期之间使用分号（;）分隔。
            BeginTime ( String ): 否  表示该限速规则启用的开始时间，格式是 mm:ss。
                  如果 DayWeek 是 unlimited, BeginTime 会被设置为 00:00，您无法更改。
            EndTime ( String ): 否  表示该限速规则启用的结束时间，格式是 mm:ss。
                  如果 DayWeek 是 unlimited, EndTime 会被设置为 23:59，您无法更改。
           "字段"： TargetQueryComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示原请求 URL 中的查询参数的处理方式。该参数有以下取值：
                  - include：表示在跳转后的 URL 中包含原请求 URL 中的所有查询参数。
                  - exclude：表示在跳转后的 URL 中不包含原请求 URL 中的任何查询参数。
                  - includePart：表示在跳转后的 URL 中包含原请求 URL 中特定的查询参数。
                  - excludePart：表示在跳转后的 URL 中不包含原请求 URL 中特定的查询参数。
            Value ( String ): 是  表示要保留或删除的查询参数。多个查询参数间使用英文分号（;）分隔。指定的查询参数不能包含双斜杠（//）、百分号（"）、空格。Value 的默认值是 *，表示所有的查询参数。
                  - 如果 Action 是 include 或者 exclude, 则 Value 必须为 *。
                  - 如果 Action 是 includePart 或者 excludePart，您可以指定一个或者多个查询参数。此时，您指定的查询参数不能是 *。
           "字段"： AuthModeConfig
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            MasterRemoteAddr ( String ): 是  表示鉴权服务器的主地址，长度不能超过 100 个字符。主地址的格式是 ://: 或 ://:，其中：
                  * ` 是 http 或者 https`。
                  * ` 不能是 localhost`。
                  * ` 不能是 127.0.0.1`。
                  * `` 是可选的。
            PathType ( String ): 是  表示鉴权请求的路径。鉴权地址和请求路径组成了完整的鉴权 URL。CDN 会把用户的请求转发到该鉴权 URL。该参数有以下取值：
                  - constant：表示鉴权请求中的路径与用户请求中的路径相同。
                  - variable：表示您需要在 pathValue 参数中指定一个鉴权请求中的路径。
            RequestMethod ( String ): 是  表示在发送鉴权请求时，CDN 所使用的请求方法。该参数有以下取值：
                  - default：表示鉴权请求所使用的方法与用户的请求相同。
                  - get：表示鉴权请求使用 GET 方法。
                  - post：表示鉴权请求使用 POST方法。
                  - head：表示鉴权请求使用 HEAD 方法。
            BackupRemoteAddr ( String ): 否  表示鉴权服务器的备地址。地址格式和要求与主地址相同。
            PathValue ( String ): 否  表示一个鉴权请求的路径，长度不能超过 100 个字符。路径必须以斜杠（/）开头，不能包含以下字符：
                  - 双斜杠（//）、百分号（%）、美元符号（$）、空格、问号（?）
           "字段"： AuthResponseConfig
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheAction ( Object of CacheAction ): 否  CDN 可以缓存鉴权状态码。该参数表示相关的配置。
            ResponseAction ( Object of ResponseAction ): 否  表示鉴权失败时，CDN 如何响应用户。
            StatusCodeAction ( Object of StatusCodeAction ): 否  表示 CDN 对鉴权状态码的处理方式。
            TimeOutAction ( Object of TimeOutAction ): 否  表示鉴权超时后，CDN 如何处理鉴权请求。
           "字段"： QueryStringRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            QueryStringComponents ( Object of QueryStringComponents ): 否  表示鉴权请求参数的设置策略。
            QueryStringInstances ( Array of QueryStringInstances ): 否  表示鉴权请求中额外的参数设置。您最多可以设置 50 个参数。
           "字段"： RequestHeaderRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RequestHeaderComponents ( Object of RequestHeaderComponents ): 否  表示鉴权请求头的设置策略。
            RequestHeaderInstances ( Array of RequestHeaderInstances ): 否  表示一组鉴权请求头的设置。
                  需要留意的是，在 CDN 发起鉴权请求时，请求中可能已经包含了以下头部：
                  - X-Forwarded-Protocol，X-Forwarded-Proto，X-Client-Scheme：这三个头部都表示用户请求所使用协议，没有区别。
                  - X-Real-IP：表示用户真实的 IP 地址。该头部的值不会受代理服务器的影响。
                  - X-Forwarded-For：表示用户的 IP 地址。如果用户的请求经过了代理服务器，该头部的值会变成代理服务器的 IP 地址。
                  不建议您在该参数中对这些头部进行设置。如果您设置了这些头部，这些头部的原始值会被覆盖。
            RequestHost ( String ): 否  表示鉴权请求中 HOST 头部的值。该参数的默认值是 default，表示 HOST 头部的值与您的加速域名相同。
           "字段"： CustomVariableRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CustomVariableInstances ( Array of CustomVariableInstances ): 是  表示一个变量列表。
           "字段"： RewriteM3u8Rule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DeleteParam ( Boolean ): 否  表示在改写分片 URI 时是否保留 URL 中原有的参数。该参数有以下取值：
                  - true：表示删除原有参数。
                  - false：表示保留原有参数。
                  该参数的默认值是 false。需要留意的是，该参数的设置影响签名的计算。参见 M3U8 改写功能的字段描述。
            KeepM3u8Param ( Boolean ): 否  表示是否将 HLS Manifest 请求中的不表示签名的查询参数添加到分片 URI 中。该参数有以下取值：
                  - true：表示在分片 URI 中添加查询参数。
                  - false：表示不添加查询参数。
                  该参数的默认值是 false。需要留意的是，该参数的设置影响签名的计算。参见 M3U8 改写功能的字段描述。
            RewriteTag ( Object of RewriteTag ): 否  表示 "标签改写" 的配置。
           "字段"： TosAuthInformation
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AccessKeyId ( String ): 否  表示访问凭证中的 AccessKey ID，在腾讯云称为 SecretId。
            AccessKeySecret ( String ): 否  表示访问凭证中的 AccessKey Secret，在腾讯云称为 SecretKey。
           "字段"： ResponseAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            StatusCode ( String ): 是  表示鉴权失败时，CDN 响应用户的状态码。您可以指定范围在 400-499 中的任意一个状态码。该参数的默认值是 403。
           "字段"： StatusCodeAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DefaultAction ( String ): 是  表示如果鉴权状态码既不是 FailCode，又不是 SuccessCode 时，CDN 处理鉴权请求的方式。该参数有以下取值：
                  - reject：表示 CDN 认为鉴权失败。
                  - pass：表示 CDN 认为鉴权成功。
            FailCode ( String ): 是  表示鉴权失败时的鉴权状态码。您可以指定范围在 400-499 中的一个或者多个状态码。多个状态码使用英文分号（;）分隔。您也可以指定 4xx 表示 400-499 中的任意一个状态码。该参数的默认值是 401。
            SuccessCode ( String ): 是  表示鉴权成功时的鉴权状态码。您可以指定范围在 200-299 中的一个或者多个状态码。多个状态码使用英文分号（;）分隔。您也可以指定 2xx 表示 200-299 中的任意一个状态码。该参数的默认值是 200。
           "字段"： TimeOutAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示鉴权超时后，CDN 处理鉴权请求的策略。该参数有以下取值：
                  - reject：表示 CDN 认为鉴权失败。
                  - pass：表示 CDN 认为鉴权成功。
            Time ( Long ): 是  表示鉴权超时的时间，单位是毫秒。该参数的默认值为 200，取值范围是 200 - 3600。
           "字段"： QueryStringComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示鉴权请求是否包含用户请求 URL 中的查询参数。该参数有以下取值：
                  - exclude：表示鉴权请求不包含任何查询参数。
                  - include：表示鉴权请求包含所有查询参数。
                  - includePart：表示鉴权请求包含指定的查询参数。
            Value ( String ): 否  表示 Action 参数所对应的参数值，长度不能超过1,024 个字符。该参数有以下取值：
                  - 如果 Action 是 exclude 或 include，Value 必须是 *。
                  - 如果 Action 是 includePart，您需要在 Value 参数中指定用户请求 URL 中的一个或者多个查询参数，多个查询参数使用英文分号（;）分隔。您不能指定 *。查询参数是区分大小写的，不能包含双引号（"），也不能包含空格。
                  该参数的默认值是 *。
           "字段"： QueryStringInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示如何设置鉴权请求参数。当前您只能设置 Action 为 set。set 表示设置参数。您需要在 Key 中指定您需要设置的鉴权请求参数。如果您指定的鉴权请求参数不存在，CDN 会在鉴权请求中添加该参数。如果您指定的鉴权请求参数已存在，CDN 会使用 Value 的值作为该鉴权请求参数的值。
            Key ( String ): 否  表示您需要设置的鉴权请求参数，长度不能超过 1,024 个字符，不能包含双引号（"），也不能包含空格。
            Value ( String ): 否  表示鉴权请求参数的值，长度不能超过 1,024 个字符，并且区分大小写。Value有以下取值：
                  - 当 ValueType 是 constant 时，表示鉴权请求参数的值是一个常量。您需要指定该常量值。常量值不能以美元符号（$）开头，也不能包含双引号（"）。
                  - 当 ValueType 是 variable 时，表示鉴权请求参数的值来自一个变量。您可以指定该变量列表中的变量。
                  - 当 ValueType 是 customize 时，表示鉴权请求参数的值是列表中的变量与固定字符串拼接后的字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：bind${request_uri}to${local_ip}done
            ValueType ( String ): 否  表示您在 Key 中设置的鉴权请求参数的类型。ValueType 有以下取值：
                  - constant：表示鉴权请求参数是一个常量。此时，您需要在 Value 中指定该常量的值。
                  - variable：表示鉴权请求参数的值来自一个变量。参见 Value 的说明。
                  - customize：表示鉴权请求参数的值是一个变量与固定字符串拼接后的字符串。
           "字段"： RequestHeaderComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示鉴权请求头是否包含用户请求头。该参数有以下取值：
                  - exclude：表示鉴权请求头中不包含任何用户请求头。
                  - include：表示鉴权请求头中包含所有用户请求头。
                  - includePart：表示鉴权请求头包含指定的用户请求头。
            Value ( String ): 否  表示 Action 参数所对应的参数值，长度不能超过 1,024 个字符。该参数有以下说明：
                  - 如果 Action 是 exclude 或 include，Value 必须是 *。
                  - 如果 Action 是 includePart，Value 参数的取值是用户请求中的一个或者多个头部。多个头部使用英文分号（;）分隔。其取值不能只是 *，不能包含以下字符：
                  	- 下划线（_）、空格、双引号（"）
                  该参数的默认值是 *。
           "字段"： CustomVariableInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Operator ( String ): 是  表示变量的匹配方式。该参数的取值只能是 match。
            Type ( String ): 是  表示变量的类型。该参数有以下取值：
                  - queryString：表示该变量是请求中的一个查询参数。
                  - requestHeader：表示该变量是请求中的一个头部字段。
            Value ( String ): 是  表示变量的名称，长度不超过 100 个字符。变量名称的要求如下：
                  - 如果 Type 是 queryString，变量名称可以包含以下字符：
                  	- 字母、数字、连字符（-）、逗号（,）、句号（.）、感叹号（!）
                  - 如果 Type 是 requestHeader，变量名称不能包含以下字符：
                  	- 下划线（_）、空格、双引号（"）、冒号（:）
           "字段"： RewriteTag
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否需要改写额外标签中的分片 URL。该参数有以下取值：
                  - true：表示需要改写额外标签。
                  - false：表示无额外标签需要改写。
            Tags ( Array of String ): 否  表示除默认标签外，需要对其下分片 URI 进行改写的额外标签列表。
    Returns:
        参数 ( 类型 ): 描述
        ---- ( ---- ): ----
        VersionId ( String ): 表示创建的版本号。
    """,
   "update_domain_version": r"""
   Args:
      body: A JSON structure
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Domain ( String ): 是  表示要修改配置的加速域名。
            Message ( String ): 否  备注。
            VersionId ( String ): 是  版本号。
            Origin ( Array of Origin ): 否  表示源站配置。
            OriginProtocol ( String ): 否  表示回源请求使用的协议。该参数有以下取值：
                  - http：表示回源请求使用 HTTP 协议。
                  - https：表示回源请求使用 HTTPS 协议。
                  - followclient：表示回源协议与用户请求使用的协议相同。
            AreaAccessRule ( Object of AreaAccessRule ): 否  表示 "地域访问控制" 特性的配置。
            BandwidthLimit ( Object of BandwidthLimit ): 否  表示 "带宽限速" 特性的配置。要使用该特性，请 提交工单。
            BrowserCache ( Array of BrowserCache ): 否  表示 "浏览器缓存" 特性的配置。在该配置中，您可以创建一个规则列表，说明如下：
                  - 每条规则包含匹配条件配置和操作配置。
                  - 列表中最多可以包含 50 条规则。
                  - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            Cache ( Array of Cache ): 否  表示 "缓存规则" 特性的配置。该特性默认为禁用，表示不创建自定义规则。
                  - 列表中最多可以包含 50 条规则。
                  - 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
                  CDN 中有一条 默认缓存规则，，用于匹配任何未能匹配其他规则的用户请求。该默认规则始终生效，并且优先级最低。您无需在配置该特性时指定该默认规则。
            CacheHost ( Object of CacheHost ): 否  表示 "共享缓存" 特性的配置。要使用该功能，请 提交工单。
                  如果您要对多个加速域名配置共享缓存，您需要调用该 API 对每个加速域名配置目标域名。
            CacheKey ( Array of CacheKey ): 否  表示 "缓存键值" 特性的配置。在该配置中，您可以创建一个规则列表，说明如下：
                  - 每条规则包含匹配条件配置和操作配置。
                  - 列表中最多可以包含 50 条规则。
                  - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
                  您必须在列表中添加以下默认规则，并且这条规则必须出现在列表的末尾。该默认规则用于匹配任何未能匹配其他规则的用户请求。在默认规则中，您可以调整 CacheKeyAction 的配置，但不能调整 Condition 的配置。
                  `json
                  {
                      "CacheKeyAction": {
                          "CacheKeyComponents": [
                              {
                                  "Action": "include",
                                  "IgnoreCase": true,
                                  "Object": "queryString",
                                  "Subobject": "*"
                              }
                          ]
                      },
                      "Condition": {
                          "ConditionRule": [
                              {
                                  "Name": "",
                                  "Object": "directory",
                                  "Operator": "match",
                                  "Type": "url",
                                  "Value": "/"
                              }
                          ]
                      }
                  }
                  `
            Compression ( Object of Compression ): 否  表示 "智能压缩" 特性的配置。
            CustomErrorPage ( Object of CustomErrorPage ): 否  表示 "自定义错误页面" 特性的配置。
            CustomizeAccessRule ( Object of CustomizeAccessRule ): 否  表示 "自定义头部黑白名单" 特性的配置。要使用该特性，请 提交工单。
            DownloadSpeedLimit ( Object of DownloadSpeedLimit ): 否  表示 "下载限速" 特性的配置。
            FollowRedirect ( Boolean ): 否  表示 "回源重定向跟随" 特性的配置。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
            HTTPS ( Object of HTTPS ): 否  表示 HTTPS 特性的配置。
            HttpForcedRedirect ( Object of HttpForcedRedirect ): 否  表示 "HTTPS 强制跳转到 HTTP" 特性的配置。
            IPv6 ( Object of IPv6 ): 否  表示 IPv6 配置。
            IpAccessRule ( Object of IpAccessRule ): 否  表示 "IP 黑白名单" 特性的配置。
                  该特性提供了两种配置方式：
                  - 常规配置：指定 RuleType 和 Ip 对当前加速域名进行配置。
                  - 全局配置：指定 SharedConfig 使用一个全局配置。全局配置是白名单功能。要使用此功能，请 提交工单。
                  您只能选择一种配置方式。
            MethodDeniedRule ( Object of MethodDeniedRule ): 否  表示 "禁用 HTTP Method" 特性的配置。
            NegativeCache ( Array of NegativeCache ): 否  表示 "状态码缓存" 特性的配置。在该配置中，您可以创建一个规则列表，说明如下：
                  - 每条规则包含过匹配条件配置和操作配置。
                  - 列表中最多可以包含 50 条规则。
                  - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            OriginAccessRule ( Object of OriginAccessRule ): 否  表示 "Origin 黑白名单" 特性的配置。
            OriginArg ( Array of OriginArg ): 否  表示 "回源参数" 配置的规则列表。
                  - 列表中最多可以包含 50 条规则。
                  - 每条规则包含一个匹配条件（Condition）和 CDN 执行操作（OriginArgAction）。
                  - 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
                  您必须在规则列表的最后添加以下这条默认规则。该默认规则用于匹配任何未能匹配其他规则的用户请求。您不可更改该规则中的 Condition，但可以更改 OriginArgAction 中的配置。
                  `json
                  {
                      "Condition": {
                          "ConditionRule": [
                              {
                                  "Object": "directory",
                                  "Operator": "match",
                                  "Type": "url",
                                  "Value": "/"
                              }
                          ]
                      },
                      "OriginArgAction": {
                          "OriginArgComponents": [
                              {
                                  "Action": "include",
                                  "Object": "queryString",
                                  "Subobject": "*"
                              }
                          ]
                      }
                  }
                  `
            OriginHost ( String ): 否  如果源站服务器上有多个站点，该参数表示回源请求访问的站点域名。该参数对所有源站配置生效，但是优先级低于源站配置中 OriginHost 参数。
                  该参数的默认值与 Domain 相同。
                  如果源站是一个对象存储桶，您无需指定该参数。其默认值与源站配置中的 Address 相同。
            OriginRange ( Boolean ): 否  表示 "回源 Range" 特性的配置。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。请求分片大小默认是 1 MB。
                  如果 Range 结构体中 Switch 为 true，则该特性为启用，即使 OriginRange 为 false。
            OriginRewrite ( Object of OriginRewrite ): 否  表示 "回源 URL 改写" 特性的配置。
            OriginSni ( Object of OriginSni ): 否  表示 "回源 SNI" 特性的配置。
            PageOptimization ( Object of PageOptimization ): 否  表示 "页面优化" 特性的配置。
            Quic ( Object of Quic ): 否  表示 QUIC 配置。
            RedirectionRewrite ( Object of RedirectionRewrite ): 否  表示 "URL 重定向改写" 特性的配置。
            RefererAccessRule ( Object of RefererAccessRule ): 否  表示 "Referer 黑白名单" 特性的配置。关于不同配置对请求匹配结果的影响，参见 配置示例。
            RemoteAuth ( Object of RemoteAuth ): 否  表示 "远程鉴权" 特性的配置。
            RequestHeader ( Array of RequestHeader ): 否  表示 "回源 HTTP 请求头" 特性的配置。
            ResponseHeader ( Array of ResponseHeader ): 否  表示 "HTTP 响应头" 特性的配置。
            ServiceRegion ( String ): 否  表示该加速域名的加速区域。该参数有以下取值：
                  - chinese_mainland：表示中国内地。
                  - global：表示全球。
                  - outside_chinese_mainland：表示全球（不含中国内地）。
                  该参数的默认值是 chinese_mainland。要指定另两个值，请 提交工单。
            SignedUrlAuth ( Object of SignedUrlAuth ): 否  表示 "URL 鉴权" 特性的配置。
            Timeout ( Object of Timeout ): 否  表示 "回源超时时间" 特性的配置。
            UaAccessRule ( Object of UaAccessRule ): 否  表示 "UA 黑白名单" 特性的配置。
            VideoDrag ( Object of VideoDrag ): 否  表示 "视频拖拽" 特性的配置。
            OriginIPv6 ( String ): 否  表示 "IPv6 回源" 的配置。该参数有以下取值：
                  - ipv6_first：表示 CDN 始终尝试获取源站域名的 IPv6 地址。如果无法获取该 IP 地址，CDN 才尝试获取源站域名的 IPv4 地址。
                  - ipv4_first：表示 CDN 始终尝试获取源站域名的 IPv4 地址。如果无法获取该 IP 地址，CDN 才尝试获取源站域名的 IPv6 地址。
                  - followclient：表示 CDN 尝试获取与用户请求相同类型的 IP 地址。
                  该参数的默认值是 followclient。
                  由于海外部分 CDN 回源节点不支持向 IPv6 地址发送回源请求，该功能仅适用于位于中国内地的回源节点。
            UrlNormalize ( Object of UrlNormalize ): 否  表示 "URL 标准化" 特性的配置。
            RequestBlockRule ( Object of RequestBlockRule ): 否  表示 "自定义拦截" 特性的配置。
            OriginCertCheck ( Object of OriginCertCheck ): 否  表示 "源站证书校验" 特性的配置。要使用此特性，请 提交工单。
                  该特性启用后，CDN 会校验源站证书的合法性，包括证书是否已被吊销、证书是否由可信 CA 签发、证书与源站域名是否匹配等。CDN 内置了常见可信 CA 的根证书。
                  该特性还支持双向认证，使源站对 CDN 身份进行校验。您需要在 CDN 中指定相应的客户端证书。
            ConditionalOrigin ( Object of ConditionalOrigin ): 否  表示 "条件源站" 特性的配置。要使用此特性，请 提交工单。
            OriginRetry ( Object of OriginRetry ): 否  表示 "回源重试设置" 特性的配置。要使用该功能，请 提交工单。
            RewriteHLS ( Object of RewriteHLS ): 否  表示 "标准 HLS 加密改写" 特性的配置。要使用该功能，请 提交工单。
            Websocket ( Object of Websocket ): 否  Websocket
            MultiRange ( Object of MultiRange ): 否  表示 "多重范围（Multi-range)" 特性的配置。
            RuleEngine ( Object of RuleEngine ): 否  规则引擎配置
            OfflineCache ( Object of OfflineCache ): 否  表示 "离线缓存" 特性的配置。要使用此特性，请 提交工单。
            OriginResponseHeader ( Array of OriginResponseHeader ): 否  表示 "源站响应头设置" 的配置。要使用该特性，请 提交工单。
            ProxyProtocol ( Object of ProxyProtocol ): 否  透传ProxyProtocol
            Range ( Object of Range ): 否  表示分片大小的设置。
            ServerSentEvent ( Object of ServerSentEvent ): 否  SSE协议
           "字段"： Origin
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginAction ( Object of OriginAction ): 是  表示源站配置，应用于所有用户请求。
           "字段"： AreaAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Area ( Array of String ): 否  表示一个国家和地区的列表，对该列表应用地域访问限制。当 Switch 是 true 时，该参数为必填。国家和地区的名称使用简写来表示。您可以调用 DescribeCdnRegionAndIsp 并指定 Area 为 Global 以获取国家和地区的简写。
            RuleType ( String ): 否  表示 Area 的类型。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - deny: 表示 Area 是一个黑名单。CDN 将阻止来自这些国家和地区的请求。
                  - allow: 表示 Area 是一个白名单。CDN 仅允许来自这些国家和地区的请求。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： BandwidthLimit
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            BandwidthLimitRule ( Object of BandwidthLimitRule ): 否  表示带宽限速的配置。当 Switch 是 true 时，该参数为必填。
           "字段"： BrowserCache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheAction ( Object of CacheAction ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheAction 中指定的操作。
           "字段"： Cache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheAction ( Object of CacheAction ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheAction 中指定的操作。
           "字段"： CacheHost
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheHostRule ( Array of CacheHostRule ): 否  表示一组共享缓存 HOST 的配置。当前您只能只能创建一个配置。当 Switch 是 true 时，该参数为必填。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： CacheKey
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheKeyAction ( Object of CacheKeyAction ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会为请求文件设置缓存键。该参数表示缓存键的配置。
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheKeyAction 中指定的操作。
                  CacheKey 中最后一条规则的 Condition 必须是以下设置。参见 请求示例。
                  `json
                  "Condition": {
                    "ConditionRule": [
                      {
                        "Object": "directory",
                        "Operator": "match",
                        "Type": "url",
                        "Value": "/"
                      }
                    ]
                  }
                  `
           "字段"： Compression
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            CompressionRules ( Array of CompressionRules ): 否  表示一组规则。每条规则包含匹配条件配置以及操作配置。
           "字段"： CustomErrorPage
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            ErrorPageRule ( Array of ErrorPageRule ): 否  表示一个配置规则的集合。您最多可以添加 50 条规则。
           "字段"： CustomizeAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CustomizeInstances ( Array of CustomizeInstances ): 是  表示一个规则列表。列表中的每条规则中定义了一个黑名单或者白名单的配置。
                  列表中最多可以包含 10 条规则。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： DownloadSpeedLimit
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            DownloadSpeedLimitRules ( Array of DownloadSpeedLimitRules ): 否  表示一个限速规则的列表。当 Switch 是 true 时，该参数为必填。该参数的其他说明如下：
                  - 每条规则包含匹配条件配置和限速配置。
                  - 列表中最多可以包含 50 条规则。
                  - 列表中规则的出现顺序表示规则的优先级排序。列表中第一条规则的优先级最高。
                  - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
           "字段"： HTTPS
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  如果 Switch 是 true，您必须指定证书。
                  * 如果您指定的是单本证书，您需要指定 CertInfo。
                  * 如果您指定的是双证书，您需要指定 CertInfoList。
                  您指定的证书可以是托管在火山引擎证书中心，也可以是托管在 CDN。
            CertInfo ( Object of CertInfo ): 否  表示要与加速域名关联的单本证书。
                  * 如果该证书已托管在 CDN 或者火山引擎证书中心，您必须在 CertId 中指定该证书的 ID。
                  * 否则，您可以使用以下任意方法：
                  	* 调用 AddCertificate 将该证书上传到 CDN 或者火山引擎证书中心，然后调用 UpdateCdnConfig 关联上传的证书。
                  	* 调用 QuickApplyCertificate 在证书中心购买证书，然后调用 UpdateCdnConfig 关联上传的证书。
                  	* 在 Certificate 结构体中指定待上传的证书。上传后的证书托管在 CDN 并自动与您的加速域名关联。要使用该方法，请 提交工单。
            CertInfoList ( Array of CertInfoList ): 否  表示要与加速域名关联的双证书。要关联双证书，请 提交工单。
                  要关联的两本证书是必须已托管在 CDN 或者火山引擎证书中心。如果这两本证书中的任何一本还未上传，您可以调用 AddCertificate 将该证书上传到 CDN 或者火山引擎证书中心，然后调用 UpdateCdnConfig 关联这两本证书。
            DisableHttp ( Boolean ): 否  表示是否允许请求 URL 中 Scheme 是 HTTP 的请求。该参数有以下取值：
                  - true：表示允许 Scheme 是 HTTP 的请求。
                  - false：表示不允许 Scheme 是 HTTP 的请求。
                  该参数的默认值是 false。
            ForcedRedirect ( Object of ForcedRedirect ): 否  表示 "HTTP 强制跳转到 HTTPS" 特性的配置。
                  CDN 提供了两种协议重定向的特性。
                  * HTTP 重定向到 HTTPS，也就是 ForcedRedirect 特性。
                  * HTTPS 重定向到 HTTP，也就是 HttpForcedRedirect 特性。
                  这两个协议重定向特性是互斥的。也就是说，如果您启用了其中任意一个特性，就不能启用另一个。
            HTTP2 ( Boolean ): 否  表示是否为用户请求启用 HTTP/2 支持。该参数有以下取值：
                  - true：表示启用 HTTP/2。
                  - false：表示禁用 HTTP/2。
                  要启用该特性，您的加速域名必须已经启用了 HTTPS。
                  该参数的默认值是 false。
            Hsts ( Object of Hsts ): 否  表示 HSTS 特性的配置。
            OCSP ( Boolean ): 否  表示是否启用 "OCSP 装订" 特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  要启用该特性，您的加速域名必须启用了 HTTPS。该参数的默认值是 false。
            TlsVersion ( Array of String ): 否  表示 "TLS 版本" 特性的配置。该参数指定用户请求可以使用的 TLS 版本，有以下取值：
                  - tlsv1.0：表示 TLS 1.0。
                  - tlsv1.1：表示 TLS 1.1。
                  - tlsv1.2：表示 TLS 1.2。
                  - tlsv1.3：表示 TLS 1.3。
                  该参数的默认值是 ["tlsv1.1", "tlsv1.2", "tlsv1.3"]
            CertCheck ( Object of CertCheck ): 否  表示 "访问双向认证" 特性的配置。要配置 "访问双向认证"，请 提交工单。
            Keyless ( Object of Keyless ): 否  KeylessServer
           "字段"： HttpForcedRedirect
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            EnableForcedRedirect ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。启用后，CDN 会将收到的 HTTPS 请求重定向到 HTTP 请求。
                  - false：表示禁用该特性。CDN 不会将 HTTPS 请求重定向到 HTTP 请求。
                  要启用该特性，您的加速域名必须已启用 HTTPS。
            StatusCode ( String ): 是  表示当收到 HTTPS 请求时，CDN 返回的重定向状态码。该参数有以下取值：301、302、303、307、308。
                  该参数的默认值是 301。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
           "字段"： IPv6
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： IpAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Ip ( Array of String ): 是  表示黑名单或白名单中的 IP 地址。当 Switch 是 true 时，该参数为必填。您可以指定一个或者多个 IP 地址和 IP 地址网段。IP 地址和网段可以是 IPv4 或 IPv6 格式。您最多可输入 1,000 个地址。
                  如果您指定了 SharedConfig，就不能指定该参数。
            RuleType ( String ): 是  表示 IP 名单的类型。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - allow：表示白名单。
                  - deny：表示黑名单。
                  如果您指定了 SharedConfig，就不能指定该参数。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            SharedConfig ( Object of SharedConfig ): 否  表示一个全局配置。
                  如果您指定了该参数，就不能指定 RuleType 和 Ip。
            DenyStatusCode ( Long ): 否  拦截状态码
            IpSource ( Object of IpSource ): 否  IP判断来源
           "字段"： MethodDeniedRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            Methods ( String ): 否  表示被禁用的一个或多个 HTTP 请求方法。当 Switch 是 true 时，该参数为必填。多个方法使用逗号（,）分隔。该参数有以下取值：
                  - get：表示禁用 GET 请求方法。
                  - post：表示禁用 POST 请求方法。
                  - delete：表示禁用 DELETE 请求方法。
                  - put：表示禁用 PUT 请求方法。
                  - head：表示禁用 HEAD 请求方法。
                  - patch：表示 PATCH 请求方法。
                  - connect：表示 CONNECT 请求方法。
                  - options：表示 OPTIONS 请求方法。
           "字段"： NegativeCache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            NegativeCacheRule ( Object of NegativeCacheRule ): 是  当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。
            Condition ( Object of Condition ): 否  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 NegativeCacheRule 中指定的操作。
           "字段"： OriginAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含 Origin 头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含 Origin 头部，则该请求被认为匹配您配置的 Origin 列表。
                  - false：表示如果请求不包含 Origin 头部，则该请求被认为不匹配您配置的 Origin 列表。
                  该参数的默认值是 false。
            IgnoreCase ( Boolean ): 是  表示 Origin 列表是否是大小写敏感的。该参数有以下取值：
                  - true: 表示 Origin 列表是大小写不敏感的。
                  - false: 表示 Origin 列表是大小写敏感的。
                  该参数的默认值是 true。
            Origins ( Array of String ): 是  表示一个 Origin 列表。列表中可以包含最多 100 个 Origins，总长度不能超过 3,000 个字符。Origin 可以是 IP 地址，CIDR 网段，域名和泛域名。域名可以是二级域名。IP 地址可以是 IPv4 和 IPv6 格式的地址。
            RuleType ( String ): 是  表示 Origin 列表的类型。该参数有以下取值：
                  - allow：表示白名单。
                  - deny：表示黑名单。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： OriginArg
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果请求满足该匹配条件，CDN 执行 OriginArgAction 中指定的操作。当前您必须且只能指定一个条件。
            OriginArgAction ( Object of OriginArgAction ): 是  表示在请求满足 Condition 时 CDN 执行的操作。
           "字段"： OriginRewrite
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginRewriteRule ( Array of OriginRewriteRule ): 否  表示一个规则列表。当 Switch 是 true 时，该参数为必填。
                  * 列表中最多可以包含 50 条规则。
                  * 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。
                  * 当收到一个用户请求时，CDN 按规则的优先级，从高到低尝试将请求与规则匹配。如果请求匹配了一条规则，CDN 就停止处理其余规则。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： OriginSni
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SniDomain ( String ): 否  指定回源 SNI 的域名。当 Switch 是 true 时，该参数为必填。该参数值的长度不能超过 1,024 个字符。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： PageOptimization
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OptimizationType ( Array of String ): 是  表示优化的对象。该参数有以下取值：
                  - html: 表示 HTML 页面。
                  - js: 表示 Javascript 代码。
                  - css: 表示 CSS 代码。
                  该参数的默认值是 html。如果您指定了 js 或者 js，html 也必须指定。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： Quic
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否为用户请求启用 QUIC。该参数有以下取值：
                  - true：表示启用 QUIC。
                  - false：表示禁用 QUIC。
                  要启用该特性，您的加速域名必须已启用 HTTPS。
           "字段"： RedirectionRewrite
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            RedirectionRule ( Array of RedirectionRule ): 否  表示一个 URL 重定向改写的规则的列表。当 Switch 是 true 时，该参数为必填。该列表最多可以包含 50 条规则。
                  列表中第一条规则的优先级最高。
                  当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
           "字段"： RefererAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含 Referer 头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含 Referer 头部，则该请求被认为匹配您配置的 Referer 列表。
                  - false：表示如果请求不包含 Referer 头部，则该请求被认为不匹配您配置的 Referer 列表。
                  该参数的默认值是 false。
            Referers ( Array of String ): 是  表示一个 Referer 列表，该参数的输入要求与 ReferersType 下 CommonType 类型的 Referers 的输入要求相同。建议您使用 ReferersType 来指定 Referer 列表。
                  另外，如果您指定了 SharedConfig，就不能指定该参数。
            ReferersType ( Object of ReferersType ): 是  表示一个 ReferersType 对象。其包含一个 CommonType 对象和一个 RegularType 对象，分别表示一个常规 Referer 列表和一个用于匹配 Referer 的正则表达式列表。您可以同时定义这两个对象。
                  如果您指定了 SharedConfig，就不能指定该参数。
            RuleType ( String ): 是  表示 Referer 名单的类型。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - allow：表示白名单。
                  - deny：表示黑名单。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            SharedConfig ( Object of SharedConfig ): 否  表示一个全局配置。要使用全局配置，请 提交工单。
                  如果您指定了该参数，除了 Switch 和 RuleType 以外，RefererAccessRule 下的其余参数都无需指定。
           "字段"： RemoteAuth
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            RemoteAuthRules ( Array of RemoteAuthRules ): 否  表示一个鉴权规则的列表。当前，列表中只能包含一条规则。该规则包含匹配条件配置和鉴权配置。当 Switch 是 true 时，该参数为必填。
           "字段"： RequestHeader
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RequestHeaderAction ( Object of RequestHeaderAction ): 是  表示一个请求头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： ResponseHeader
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ResponseHeaderAction ( Object of ResponseHeaderAction ): 是  表示 CDN 在响应用户请求的时候，对响应头的操作。
           "字段"： SignedUrlAuth
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            SignedUrlAuthRules ( Array of SignedUrlAuthRules ): 否  表示一个规则列表。每条规则包含匹配条件配置和鉴权配置。当前，列表中只能包含一条规则。当 Switch 是 true 时，该参数为必填。
           "字段"： Timeout
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。此时，TCP 请求和 HTTP 请求的超时时间使用默认值，分别是 2 秒和 60 秒。
                  该参数的默认值是 false。
            TimeoutRules ( Array of TimeoutRules ): 否  表示一组超时时间的配置。当前您只能指定一个配置。当 Switch 是 true 时，该参数为必填。
           "字段"： UaAccessRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含 User-Agent 头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含 User-Agent 头部，则该请求被认为匹配您配置的 User-Agent 列表。
                  - false：表示如果请求不包含 User-Agent 头部，则该请求被认为不匹配您配置的 User-Agent 列表。
                  该参数的默认值是 false。
            IgnoreCase ( Boolean ): 是  表示 UA 字符串是否是大小写敏感的。该参数有以下取值：
                  - true: 表示 UA 字符串是大小写不敏感的。
                  - false: 表示 UA 字符串是大小写敏感的。
                  该参数的默认值是 false。
            RuleType ( String ): 是  表示指定的是黑名单还是白名单。当 Switch 是 true 时，该参数为必填。该参数有以下取值：
                  - deny: 表示指定的是黑名单。
                  - allow: 表示指定的是白名单。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
            UserAgent ( Array of String ): 是  表示一个 UA 的列表。当 Switch 是 true 时，该参数为必填。该列表最多包含 1,000 个 UA。该参数的说明如下：
                  - 该参数值的长度不能超过 30,000 个字符。
                  - 如果 RuleType 是 allow，表示仅允许包含列表中的 UA 的请求访问加速域名。
                  - 如果 RuleType 是 deny，表示如果访问请求包含列表中的 UA，则不允许访问加速域名。
                  UA 能包含的字符有以下限制：
                  - UA 中可以使用 ` 表示一个或者多个字符。` 仅可以出现在 UA 的开头和末尾。
                  - UA 不能只包含 *或者空格。
                  - UA 如果包含符号，符号必须是被 HTML 编码的。
            SharedConfig ( Object of SharedConfig ): 否  表示一个全局配置。要使用全局配置，请 提交工单。
                  如果您指定了该参数，除了 Switch 和 RuleType，UaAccessRule 下的其余参数都无需指定。
           "字段"： VideoDrag
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： UrlNormalize
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            NormalizeObject ( Array of String ): 否  表示一个 URL 标准化选项列表。当 Switch 为 true 时，该参数为必填。列表中可以包含以下选项：
                  - dot_segments：表示将请求 URL 中的以下内容进行替换：
                  	- /./：替换为单个斜杠（/）。
                  	- /../：如果 /../ 前还有一个级别的目录，则删除 /../ 与该目录。如果 /../ 前没有目录，则保留原 URL。
                  - back_slashes：表示将请求 URL 中的反斜杠（）替换为单个斜杠（/）。
                  - successive_slashes：表示将请求 URL 中双斜杠（//）替换为单个斜杠（/）。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： RequestBlockRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BlockRule ( Array of BlockRule ): 是  表示一个规则列表。列表中最多可以包含 10 条规则。当 Switch 是 true 时，该参数为必填。
                  列表中第一条规则的优先级最高。
                  当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            Switch ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： OriginCertCheck
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
            CertInfoList ( Array of CertInfoList ): 否  表示一个 CA 证书列表，列表中的证书托管在 CDN，且不能是国密证书。CDN 使用该列表中的证书对来自源站的服务器证书进行校验。
                  当前，该列表中只能包含一本证书。
            ClientCertInfoList ( Array of ClientCertInfoList ): 否  仅当 Type 为 mutual 时，该参数有效。
                  该参数表示一个客户端证书列表，列表中的证书必须托管在 CDN，且不能是国密证书。源站使用该列表中的证书对 CDN 身份进行校验。
                  当前，该列表中只能包含一本证书。
            Type ( String ): 否  表示校验类型，有以下取值：
                  * unilateral：表示单向认证。
                  * mutual：表示双向认证。
                  该参数的默认值是 unilateral。
           "字段"： ConditionalOrigin
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginRules ( Array of OriginRules ): 否  表示一个规则列表。列表中的每条规则中定义了一组匹配条件以及 CDN 对满足匹配条件的请求所执行的操作。
                  列表中最多可以包含 20 条规则。
                  当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： OriginRetry
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            StatusCode ( String ): 否  表示范围在 400-599 之间的一个或者多个状态码。多个状态码之间使用分号（;）分隔。您可以输入 4xx 或者 5xx，表示所有以数字 4 或 数字 5 开头的状态码。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： RewriteHLS
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SignName ( String ): 否  表示签名参数的名称，长度不能超过 100 个字符。参数名称区分大小写，可以包含字母、数字、下划线（_）、中划线（-）、逗号（,）、句号（.）、感叹号（!）。
                  该参数的默认值是 DrmAuthToken。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： Websocket
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  无
            Timeout ( Long ): 否  无
           "字段"： MultiRange
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  * true：表示启用该特性。该特性启用后，CDN 允许指定了多重范围的 Range 请求。
                  * false：表示不启用该特性。如果收到一个指定了多重范围的 Range 请求，CDN 会拒绝该请求并返回 416 响应状态码。
                  该参数的默认值是 false。
           "字段"： RuleEngine
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Rules ( Array of Rules ): 否  无
            Switch ( Boolean ): 否  无
           "字段"： OfflineCache
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Object ( String ): 否  表示该特性的触发条件，该参数有以下取值：
                  - request_error：表示回源请求异常。当回源请求出现异常时，CDN 没有获得源站的响应。
                  - error_code：表示源站响应状态码是 5xx。
                  - request_error,error_code：表示以上两个条件都包含。
            StatusCode ( String ): 否  表示一个或者多个响应状态码，范围是 500-599。多个状态码之间使用分号（;）分隔。您也可以输入 5xx，表示任意以数字 5 开头的状态码。
                  当 Object 是 error_code 或者 request_error,error_code 时，该参数才有效。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
           "字段"： OriginResponseHeader
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginResponseHeaderAction ( Object of OriginResponseHeaderAction ): 否  表示 CDN 在收到源站响应时，对响应头的操作。
           "字段"： ProxyProtocol
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  无
           "字段"： Range
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否启用该设置。该参数有以下取值：
                  * true：表示启用该设置。
                  * false：表示禁用该设置。
                  该参数的默认值是 false。
            RangeSize ( Long ): 否  表示分片的大小。
                  * 如果 Unit 是 MB，该参数的取值范围是 1-40。
                  * 如果 Unit 是 KB，该参数值只能是 512。
                  该参数的默认值是 1。
            Unit ( String ): 否  表示 RangeSize 的单位。该参数有以下取值：
                  * KB
                  * MB
                  该参数的默认值是 MB。
           "字段"： ServerSentEvent
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  无
           "字段"： OriginAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginLines ( Array of OriginLines ): 是  表示一个源站列表。列表中最多可以包含 50 个源站。
           "字段"： BandwidthLimitRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BandwidthLimitAction ( Object of BandwidthLimitAction ): 否  表示限速行为的配置。
           "字段"： CacheAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示浏览器需要执行的操作。当前该参数值只能是 cache，表示缓存请求的文件。DefaultPolicy 中指定了如何缓存请求的文件。
            IgnoreCase ( Boolean ): 是  表示 Value 是否是大小写敏感的。
                  - true：表示大小写不敏感。
                  - false：表示大小写敏感。
                  该参数的默认值为 false。
            Ttl ( Long ): 是  表示浏览器需要缓存请求文件的时长，单位是秒。CDN 会在响应头中包含 Cache-Control: max-age 头部，头部值就是该参数值。
            DefaultPolicy ( String ): 否  表示浏览器该如何缓存请求的文件。该参数有以下取值：
                  - cache：表示需要缓存请求的文件。
                  - origin_first：表示遵循来自源站的缓存策略。该策略会包含在 CDN 的响应中。
                  - no_cache：表示不需要缓存请求的文件。
                  关于浏览器缓存策略的详细信息，参见 浏览器缓存策略。
           "字段"： Condition
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ConditionRule ( Array of ConditionRule ): 是  表示匹配条件列表。当前，列表中只能包含一个匹配条件。
           "字段"： CacheHostRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheHostAction ( Object of CacheHostAction ): 否  表示配置的详情。
           "字段"： CacheKeyAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheKeyComponents ( Array of CacheKeyComponents ): 是  缓存键是由请求中的 host、路径和查询字符串等部分组成。该参数表示其中各组成部分的配置。当前，您只能对缓存键中包含的查询字符串进行配置。
           "字段"： CompressionRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CompressionAction ( Object of CompressionAction ): 是  表示当用户请求满足 Condition 时，CDN 对请求文件执行的压缩操作的配置。
            Condition ( Object of Condition ): 否  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CompressionAction 中指定的操作。
                  需要留意的是，如果您指定了 CompressionFormat，Condition 必须为 null 或者不指定。
           "字段"： ErrorPageRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ErrorPageAction ( Object of ErrorPageAction ): 是  表示规则的相关配置。
           "字段"： CustomizeInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CustomizeRule ( Object of CustomizeRule ): 是  表示列表中一条规则的配置。
           "字段"： DownloadSpeedLimitRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DownloadSpeedLimitAction ( Object of DownloadSpeedLimitAction ): 是  表示限速配置。
            Condition ( Object of Condition ): 否  表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 DownloadSpeedLimitAction 中指定的操作。
                  如果不指定该参数，CDN 对所有请求执行 DownloadSpeedLimitAction 中指定的操作。
           "字段"： CertInfo
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertId ( String ): 否  表示要关联的证书 ID。
                  您可以调用 ListCertInfo 获取您想要关联的证书 ID。
            Certificate ( Object of Certificate ): 否  表示一个待上传的证书。上传后的证书是托管在 CDN 的。
           "字段"： CertInfoList
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertId ( String ): 否  表示双证书中一本证书的 ID。
                  您可以调用 ListCertInfo 获取您想要指定的证书的 ID。
           "字段"： ForcedRedirect
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            EnableForcedRedirect ( Boolean ): 是  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。启用后，CDN 会将收到的 HTTP 请求重定向到 HTTPS 请求。
                  - false：表示禁用该特性。禁用后，CDN 不会将 HTTP 请求重定向到 HTTPS 请求。
                  要启用该特性，您的加速域名必须已启用 HTTPS。
            StatusCode ( String ): 是  表示当收到 HTTPS 请求时 CDN 的重定向响应状态码。该参数有以下取值：301、302、303、307、308。
                  该参数的默认值是 301。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
           "字段"： Hsts
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Subdomain ( String ): 否  表示 HSTS 配置是否也应用于加速域名的子域名。该参数有以下取值：
                  - include：表示 HSTS 配置应用于子域名站点。
                  - exclude：表示 HSTS 配置不应用于子域名站点。
                  该参数的默认值是 exclude。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
            Ttl ( Long ): 否  表示 Strict-Transport-Security 响应头在浏览器中的缓存过期时间，单位是秒。如果 Switch 是 true，该参数为必填。该参数的取值范围是 0 - 31,536,000。31,536,000 秒表示 365 天。如果该参数值为 0，其效果等同于禁用 HSTS 设置。
           "字段"： CertCheck
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertInfoList ( Array of CertInfoList ): 否  表示要与加速域名关联的一个 CA 证书列表。列表中最多包含两个 CA 证书。这些 CA 证书必须已托管在 CDN。CA 证书使用的加密算法可以是 RSA、ECC 或者 SM2。
                  如果要关联的证书还未上传，您可以调用 AddCertificate 将该证书上传到 CDN，然后调用 UpdateCdnConfig 关联该证书。
            Switch ( Boolean ): 否  表示是否启用该特性。该参数有以下取值：
                  - true：表示启用该特性。
                  - false：表示禁用该特性。
                  该参数的默认值是 false。
           "字段"： Keyless
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertInfoList ( Array of CertInfoList ): 否  Keyless服务器证书校验-CA证书
            CheckType ( String ): 否  Keyless服务器证书校验
            ClientCertInfoList ( Array of ClientCertInfoList ): 否  Keyless服务器证书校验-客户端证书
            KeylessServer ( String ): 否  Keyless服务器地址
            Switch ( Boolean ): 否  Keyless开关
           "字段"： SharedConfig
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ConfigName ( String ): 否  表示一个全局配置的名称。该全局配置的 ConfigType 必须是 deny_ip_access_rule 或者 allow_ip_access_rule。
                  - deny_ip_access_rule：表示 IP 黑名单。
                  - allow_ip_access_rule：表示 IP 白名单。
                  您可以调用 ListSharedConfig 获取全局配置的列表。
           "字段"： IpSource
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SourceList ( Array of String ): 否  无
            Type ( String ): 否  无
           "字段"： NegativeCacheRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 执行的操作。当前该参数值只能是 cache，表示缓存源站的响应状态码。
            StatusCode ( String ): 是  指定一个需要缓存的状态码。状态码的范围是 400-599。您也可以指定 4xx 或者 5xx。4xx 表示 400 到 499 之间的所有状态码。5xx 表示 500 到 599 之间的所有状态码。
            Ttl ( Long ): 是  表示状态码的缓存时间。单位是秒。时间的范围是 1-315,360,000。315,360,000 表示 10 年。
            IgnoreCase ( Boolean ): 否  表示 Value 是否是大小写敏感的。
                  - true：表示大小写不敏感。
                  - false：表示大小写敏感。
                  该参数的默认值为 false。
           "字段"： OriginArgAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginArgComponents ( Array of OriginArgComponents ): 是  表示一个操作列表。这些操作定义了 CDN 如何处理回源请求中的查询参数。
                  当前，列表中只能包含一个操作。
           "字段"： OriginRewriteRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginRewriteAction ( Object of OriginRewriteAction ): 否  表示 CDN 执行的动作。
           "字段"： RedirectionRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RedirectionAction ( Object of RedirectionAction ): 是  表示一个 URL 重定向改写的规则。
           "字段"： ReferersType
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CommonType ( Object of CommonType ): 是  表示一个 CommonType 对象，其包含一个常规 Referer 列表。
            RegularType ( Object of RegularType ): 是  表示一个 RegularType 对象，其包含一个正则表达式列表用来匹配请求中的 Referer 头部。要使用该参数，请 提交工单。
           "字段"： RemoteAuthRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Condition ( Object of Condition ): 是  表示匹配条件的配置。如果一个请求满足匹配条件，CDN 对该请求执行 RemoteAuthRuleAction 中指定的操作。
            RemoteAuthRuleAction ( Object of RemoteAuthRuleAction ): 是  表示鉴权相关的配置。
                  当一个请求满足 Condition 中的匹配条件时，CDN 会将其发送至鉴权服务器进行鉴权，并基于鉴权的结果接受或者拒绝该请求。
           "字段"： RequestHeaderAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RequestHeaderInstances ( Array of RequestHeaderInstances ): 是  表示一个请求头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： ResponseHeaderAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            ResponseHeaderInstances ( Array of ResponseHeaderInstances ): 是  表示一个响应头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： SignedUrlAuthRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Condition ( Object of Condition ): 是  表示匹配条件的配置。CDN 对符合条件的用户请求进行鉴权。
            SignedUrlAuthAction ( Object of SignedUrlAuthAction ): 是  表示签名计算的配置。
           "字段"： TimeoutRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            TimeoutAction ( Object of TimeoutAction ): 否  表示超时时间的配置。
           "字段"： BlockRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BlockAction ( Object of BlockAction ): 是  表示一条规则中 CDN 行为的配置。
            Condition ( Object of Condition ): 是  表示该规则中匹配条件的定义。
            RuleName ( String ): 是  表示规则的名称，长度不超过 20 个字符，可以包含字母、数字、下划线（_）、中划线（-）、汉字。一个汉字占 3 个字符。
           "字段"： ClientCertInfoList
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CertId ( String ): 否  表示列表中一本客户端证书的 ID，以 cert_hosting 开头。
                  您可以调用 ListCertInfo 查询托管在 CDN 的客户端证书列表以获取您要指定的证书的 ID。
           "字段"： OriginRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Actions ( Object of Actions ): 否  表示一条规则中定义的操作配置。
            Condition ( Object of Condition ): 否  表示该规则中匹配条件的配置。
           "字段"： Rules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Id ( String ): 否  无
            Locked ( Boolean ): 否  无
            Name ( String ): 否  无
            Rule ( String ): 否  无
            DSLRule ( String ): 否  无
           "字段"： OriginResponseHeaderAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginResponseHeaderInstances ( Array of OriginResponseHeaderInstances ): 否  表示一个响应头的配置规则列表。每个规则都包含一个头部的相关操作设置。您最多可以添加 50 条规则。
           "字段"： OriginLines
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Address ( String ): 是  表示列表中一个源站的地址。该参数有以下说明：
                  - 如果 InstanceType 是 ip，您指定的是源站的 IP 地址。IP 地址可以是 IPv4 或 IPv6 地址。
                  - 如果 InstanceType 是 domain，您指定的是源站的域名。该域名不能是泛域名。
                  - 如果 InstanceType 是 tos，您指定的是存储桶域名，可以是云厂商分配的桶域名，也可以是您在云厂商处为存储桶设置的自定义域名。桶域名不能包含 https://，长度不能超过 100 个字符。存储桶可以来自火山引擎 TOS、阿里云 OSS、腾讯云 COS、AWS S3 或者任何使用鉴权方式与 S3 兼容的第三方对象存储服务，如七牛云、华为云等。
                  如果存储桶来自您账号下的 TOS 服务，在调用该 API 前，您需要在 CDN 控制台中打开该域名的配置页面。在该页面中，点击 授权 授权 CDN 访问您账号下的 TOS 服务。
            InstanceType ( String ): 是  表示源站的类型。该参数有以下取值：
                  - ip：表示 IP 地址。
                  - domain：表示域名。
                  - tos：表示对象存储桶。
                  在 CDN 向对象存储源站发送回源请求时，回源请求使用的方法与用户请求相同。默认情况下，用户请求可以使用的请求方法有 DELETE、GET、HEAD、POST、PUT、PATCH、OPTIONS、CONNECT。如果您不希望回源请求使用某些请求方法，例如您不希望回源请求使用 DELETE 方法，可能导致误删源站上的文件，建议您采取以下步骤：
                  1. 在存储桶所在的对象存储服务中设置权限，组织不符合预期的操作。
                  2. 在 CDN 的 MethodDeniedRule 特性中，指定 CDN 不支持的请求方法。
            OriginType ( String ): 是  表示源站的类别。该参数有以下取值：
                  - primary：表示主源站。
                  - backup：表示备源站。
                  源站列表中至少需要包含一个主源站。备源站是可选的。
            HttpPort ( String ): 否  表示 CDN 使用 HTTP 协议访问该源站时所访问的端口，取值范围是 1-65535，默认值是 80。如果源站服务器没有开放该端口，您无需指定该参数。
                  该参数仅当 InstanceType 为 ip 或 domain 时才有效。
            HttpsPort ( String ): 否  表示 CDN 使用 HTTPS 协议访问该源站时所访问的端口，取值范围是 1-65535，默认值是 443。如果源站服务器没有开放该端口，您无需指定该参数。
                  该参数仅当 InstanceType 为 ip 或 domain 时才有效。
            OriginHost ( String ): 否  表示回源请求访问的站点域名，适用于源站服务器上有多个站点的情况。
                  - 该参数的默认值与全局 OriginHost 相同，但优先级高于全局 OriginHost 参数。
                  - 该参数值的长度不能超过 1,024 个字符。
                  - 如果您在调用该 API 时，即没有修改 Address，也没有指定 OriginHost，OriginHost 不会被默认值覆盖，而是保持当前值。
            PrivateBucketAccess ( Boolean ): 否  表示存储桶是否是私有桶。该参数仅当 InstanceType 为 tos 时有效。该参数有以下取值：
                  - true：表示该存储桶是私有桶。
                  - false：表示该存储桶不是私有桶。
                  该参数的默认值是 false。
            PrivateBucketAuth ( Object of PrivateBucketAuth ): 否  表示访问存储桶的凭据。如果存储桶属于您火山引擎账号，您无需指定该参数。CDN 可以访问您账号下的 TOS 存储桶，无需凭证，即使存储桶是私有的。
            Region ( String ): 否  表示存储桶所在地域的信息，也就是存储桶的 region code。Region code 参与签名的计算。
                  如果 AuthType 是 aws_common 并且 PrivateBucketAccess 是 true，您必须指定该参数。
            Weight ( String ): 否  表示该源站的权重，取值范围是 1-100，默认值是 1。权重越大，该源站在 CDN 发送回源请求时被选择到的概率也越大。
                  该参数仅当 InstanceType 为 ip 或 domain 时才有效。
           "字段"： BandwidthLimitAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            BandwidthThreshold ( Long ): 是  表示一个带宽阈值，单位是 bps。当您加速域名的带宽超过该阈值时，CDN 对加速域名启用 LimitType 所指定的带宽限制策略。该参数使用的进制是 1 Kbps = 1,000 bps。
            LimitType ( String ): 是  表示一个带宽限制策略。该参数有以下取值：
                  - downloadspeedlimit：表示 "单链接限速"。推荐使用该策略。
                  - speedlimit：表示 "IP 限速"。
                  - randomreject：表示 "拒绝请求"。
                  关于各策略限制带宽的方法，参见 配置带宽限制。
            SpeedLimitRate ( Long ): 否  表示数据传输速度的下限，单位是 B/S。在 CDN 逐次降低每个新请求或者每个 IP 地址的数据传输速度上限时，该上限不会低于 SpeedLimitRate。
                  - 如果 LimitType 是 downloadspeedlimit，该参数表示每个新请求的数据传输速度下限。
                  - 如果 LimitType 是 speedlimit，该参数表示每个 IP 地址的数据传输速度下限。
                  - 如果 LimitType 是 randomreject，该参数不适用。
                  该参数使用的进制是 1 KB/S = 1024 B/S。
            SpeedLimitRateMax ( Long ): 否  表示带宽限制策略启用时，CDN 对每个新请求或者每个 IP 地址设置的数据传输速度上限，单位是 B/S。在之后的每次带宽计算时，如果带宽依然超出阈值，该上限会逐次降低，直到带宽低于阈值或者该上限达到了 SpeedLimitRate。
                  - 如果 LimitType 是 downloadspeedlimit，该参数表示每个新请求的数据传输速度上限。
                  - 如果 LimitType 是 speedlimit，该参数表示每个 IP 地址的数据传输速度上限。
                  - 如果 LimitType 是 randomreject，该参数不适用。
                  该参数使用的进制是 1 KB/S = 1024 B/S。该参数的默认值是 SpeedLimitRate + 4,194,304。
           "字段"： ConditionRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Object ( String ): 是  表示匹配对象。该参数有以下取值：
                  - filetype：表示请求 URL 中的扩展名。
                  - directory：表示请求 URL 中的某个目录。
                  - path：表示请求 URL 中的完整路径。
                  - regex：表示请求 URL 中的路径，通过正则表达式匹配。
                  要指定 regex，请 提交工单。
            Operator ( String ): 是  表示匹配类型。该参数的值只能是 match，表示如果 Value 匹配了请求中的 Object，该请求就满足这个匹配条件。
            Type ( String ): 是  该参数值只能是 url，表示 "请求 URL"。
            Value ( String ): 是  表示一个或者多个匹配值，总长度不能超过 1,024 个字符。多个匹配值之间使用分号（;）分隔。匹配值不能包含以下字符：
                  - 双斜杠（//）、空格、美元符号（$）、问号（?）
                  同时，
                  - 如果 Object 是 filetype，每个匹配值表示一个请求 URL 后缀，无需以句点（.）开头，只能包含字母和数字。例如：png;txt。
                  - 如果 Object 是 directory，每个匹配值表示一个目录路径，以斜杠（/）开头和结尾。例如 /chs/foods/;/us/birds/。
                  - 如果 Object 是 path，每个匹配值表示一个 URL 路径，以斜杠（/）开头。每个匹配值中可以包含通配符（）表示一个或者多个字符。例如 /chs/foods/localsets;/us/birds/chickadee。
           "字段"： CacheHostAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheHost ( String ): 否  表示目标域名。 该目标域名必须是您账户下的一个加速域名。该参数指示 Domain 共享 CacheHost 的 CDN 缓存。
           "字段"： CacheKeyComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 如何在请求文件的缓存键中设置查询字符串。该参数有以下取值：
                  - exclude：表示缓存键不包含请求中的任何查询参数。
                  - include：表示缓存键包含请求中所有的查询参数。
                  - includePart：表示缓存键仅包含  Subobject 中指定的查询参数。
                  - excludePart：表示缓存键包含请求中除了 Subobject 中指定的查询参数之外的所有查询参数。
            IgnoreCase ( Boolean ): 是  表示 Subobject 是否是大小写敏感的。该参数有以下取值：
                  - true：表示大小写不敏感。
                  - false：表示大小写敏感。
                  该参数的默认值为 false，并且仅当 Action 是 includePart 或 excluePart 时有效。
            Object ( String ): 是  表示缓存键中的一个组成部分。当前该参数值只能是 querystring，表示查询字符串。
            Subobject ( String ): 是  该参数对应于 Action，表示 CDN 在缓存键中包含的具体查询参数。该参数的说明如下：
                  - 如果 Action 是 include 或者 exclude，Subobject 必须是 *，表示请求中的全部查询参数。
                  - 如果 Action 是 includePart 或者 excludePart，表示需要保留或者不保留的查询参数。多个查询参数之间使用分号（;）分隔。您指定的查询参数不能是 *，也不能包含双斜杠（//）、百分号（%）、空格。
           "字段"： CompressionAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CompressionType ( Array of String ): 是  表示 CDN 使用的压缩算法。该参数有以下取值：
                  - br：表示 Brotli 压缩算法。
                  - gzip：表示 Gzip 压缩算法。
                  您可以同时指定这两个算法。
                  需要留意的是，CDN 基于用户请求中 Accept-Encoding 头部来决定是否对请求文件进行压缩以及使用的压缩算法。
            CompressionFormat ( String ): 否  表示 CDN 基于请求中的 Content-Type 头部对请求进行匹配。该参数有以下取值：
                  * default：表示如果 Content-Type 头部值在下方的默认列表中，CDN 对请求文件执行 CompressionAction 中配置的操作。
                  * customize：表示如果 Content-Type 头部值在 CompressionFormat 指定的头部值中，CDN 对请求文件执行 CompressionAction 中配置的操作。
                  如果您需要 CDN 基于 Condition 中的匹配条件对请求进行匹配，您无需指定 CompressionFormat 或者指定 CompressionFormat 为 all。
                  默认列表
                  text/html、text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、text/javascript、image/tiff、image/svg+xml、application/json、application/xml、text/plain; charset=utf-8
            CompressionTarget ( String ): 否  表示 Content-Type 的过滤值。
                  - 如果 CompressionFormat 为 default 或者 all，该参数必须为 *。
                  - 如果 CompressionFormat 为 customize，您需要指定一个或者多个文件类型。多个文件类型之间以逗号（,）分隔。
            MinFileSizeKB ( Long ): 否  表示文件大小范围的最小值，CDN 仅对大小在 MinFileSizeKB 和 MaxFileSizeKB 所表示的范围内的文件进行压缩。该参数的取值范围是 0 - 2,147,483,647，单位是 KB，使用的进制是 1,024。该参数的默认值是 0。
            MaxFileSizeKB ( Long ): 否  表示文件大小范围的最大值，取值范围是 0 - 2,147,483,647，单位是 KB，使用的进制是 1,024。如果不指定该参数，表示您不限制文件大小的上限。
           "字段"： ErrorPageAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示实际的操作。当前您只能指定该参数值为 redirect。表示对客户端请求进行重定向。
            RedirectCode ( String ): 是  表示重定向的响应状态码。您可以根据需求选择合适的状态码。该参数的取值有 301、302、303、307、308。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
            RedirectUrl ( String ): 是  表示跳转的目标地址，长度不能超过 1,024 个字符。地址必须包含协议，域名以及路径，并且符合 URL 的规范。
            StatusCode ( String ): 是  表示一个状态码，取值范围是 400-599。您可以输入 4xx 或者 5xx。4xx 表示 400-499 之间的所有状态码。5xx 表示 500-599 之间的所有状态码。
           "字段"： CustomizeRule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AccessAction ( Object of AccessAction ): 是  表示该规则中的黑名单或者白名单的配置。
           "字段"： DownloadSpeedLimitAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SpeedLimitRate ( Long ): 是  表示 CDN 在响应单个请求时的最大数据传输速度，单位是 B/S，使用的进制是 1,024。该参数的取值范围是 1-1,073,741,824,000,000。1,073,741,824,000,000 是 1,000,000 Gbps。
            SpeedLimitRateAfter ( Long ): 否  表示一个初始数据量，单位是 bytes，使用的进制是 1,024。该参数的取值范围是 0-1,073,741,824,000,000。
                  当 CDN 对一个请求开始传输数据时，在传输的数据量达到该初始数据量前，该限速规则不会启用。
                  如果该参数值是 0，表示在 CDN 对一个请求开始传输第一个字节时，该限速规则就启用了。
            SpeedLimitTime ( Object of SpeedLimitTime ): 否  表示限速规则启用的日期和时间段。
            DynamicLimitUnit ( String ): 否  动态限速类型时必填，表示动态限速单位，可选B/S、KB/S、MB/S
            LimitQueryName ( String ): 否  动态限速类型时必填，表示限速参数名称
            LimitType ( String ): 否  限速类型。非必填，不传为 normal ，表示固定限速值，dynamic_limit:表示动态限速
           "字段"： Certificate
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Certificate ( String ): 否  表示证书文件的内容。内容中的换行必须使用 rn 替换。该证书文件的扩展名是 .crt 或者 .pem，并且证书文件必须包含完整的证书链。
                  - 如果该证书使用的加密算法是 RSA 或者 ECC，该文件是您要上传的服务器证书的证书文件。文件名类似 .crt。
                  - 如果该证书使用的加密算法是 SM2，该文件是您要上传的国密证书的证书文件，用于验证签名。文件名类似 _sign.crt。
                  对于待上传的证书，该参数必填。
            PrivateKey ( String ): 否  表示私钥文件的内容。内容中的换行必须使用 rn 替换。该私钥文件的扩展名是 .key 或者 .pem。
                  - 如果该证书使用的加密算法是 RSA 或者 ECC，该文件是您要上传的服务器证书的私钥文件。文件名类似 .key。
                  - 如果该证书使用的加密算法是 SM2，该文件是您要上传的国密证书的私钥文件，用于生成签名。文件名类似 _sign.key。
                  对于待上传的证书，该参数必填。
            EncryptionCert ( String ): 否  表示国密证书的证书文件的内容。内容中的换行必须使用 rn 替换。该文件用于加密，扩展名是 .crt 或者 .pem。文件名类似 _encrypt.crt。
                  如果待上传的证书不是国密证书，该参数无效。
            EncryptionKey ( String ): 否  表示国密证书的私钥文件的内容。内容中的换行必须使用 rn 替换。该文件用于解密，扩展名是 .key 或者 .pem。文件名类似 _encrypt.key。
                  如果待上传的证书不是国密证书，该参数无效。
           "字段"： OriginArgComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 执行的操作。该参数有以下取值：
                  - include: 表示回源请求 URL 中包含用户请求 URL 中的全部查询参数。
                  - exclude：表示回源请求 URL 中不包含用户请求 URL 中的任何查询参数。
                  - addPart：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数，并额外包含 Subobject 中指定的查询参数。
                  - includePart：表示如果用户请求 URL 中包含 Subobject 中指定的查询参数，那么回源请求 URL 中包含这些指定的查询参数。
                  - excludePart：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数，除了Subobject 中指定的查询参数。
                  - set：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数。同时，对于您在 Subobject 中指定的查询参数和参数值，CDN 会执行以下操作:
                    - 如果这些查询参数在用户请求 URL 中，CDN 会在回源请求 URL 中将这些参数的值设置为您指定的值。
                    - 如果用户请求 URL 中不包含这些查询参数，CDN 会在回源请求 URL 中添加这些查询参数。
            Object ( String ): 是  表示 CDN 对哪个对象执行 Action。当前，该参数值只能是 queryString，表示请求 URL 中的查询字符串。
            Subobject ( String ): 是  表示一个或者多个查询参数。多个查询参数之间使用分号（;）分隔，总长度不能超过 1,024 个字符。Subobject 只能包含字母、数字、下划线（_）、逗号（,）、短横线（-）、句点（.）和感叹号（!）。
                  在匹配请求 URL 中的查询参数时，Subobject 中的参数是大小写敏感的。
                  Subobject 的额外说明如下：
                  * 当 Action 是  include 或 exclude 时，Subobject 必须是 *，表示请求 URL 中的所有查询参数。
                  * 当 Action 是  includePart 或 excludePart 时，Subobject 表示一个或者多个查询参数。例如 param1;param2。
                  * 当 Action 是  addPart 或 set 时，Subobject 表示一个或者多个查询参数和参数值，格式是 key=value。例如 param1=val1;param2=val2;param3=val3。
           "字段"： OriginRewriteAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            SourcePath ( String ): 否  表示一个正则表达式，长度不能超过 1,024 个字符，用于匹配用户请求 URL 中的对象。
                  * 当 RewriteType 是 rewrite_path 时，该对象指的是请求 URL 中的路径。
                  * 当 RewriteType 是 rewrite_url 时，该对象指的是请求 URL 中的路径和查询字符串。
                  参见 配置示例。
                  假设您在调用该 API 时在 SourcePath 中使用 ? 表示查询字符串中开头的 ?。当您调用 DescribeCdnConfig 查看 SourcePath 的值时，您会发现 ? 变成了 ?。这个变化是符合预期的，因为 DescribeCdnConfig 返回内容是 JSON 格式，内容中的 ` 被转义成了 `。
            TargetPath ( String ): 否  表示改写后，回源请求 URL 中的对象，长度不能超过 1,024 个字符。
                  * 当 RewriteType 是 rewrite_path 时，该对象是回源请求 URL 中的路径。
                  * 当 RewriteType 是 rewrite_url 时，该对象是回源请求 URL 中的路径和查询字符串。
                  您可以在 TargetPath 中使用 $1、$2、$3 等捕获 SourcePath 中定义的组。
                  参见 配置示例。
            RewriteType ( String ): 否  表示改写类型。该参数有以下取值：
                  * rewrite_path：表示对请求 URL 中的路径进行改写。
                  * rewrite_url：表示对请求 URL 中的路径和查询字符串进行改写。
                  该参数的默认值是 rewrite_path。
           "字段"： RedirectionAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RedirectCode ( String ): 是  表示 URL 重定向的响应状态码。该参数的取值有 301、302、303、307、308。
                  需要留意的是：
                  * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。
                  * 对于 303，新请求使用的方法是 GET。
                  * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。
            SourcePath ( String ): 是  表示文件的原路径。也就是请求中包含的路径。路径必须以斜杠（/）开头并且不能包含双斜杠（//）、百分号（%）、空格。该参数值的长度不能超过 1,024 个字符。
            TargetHost ( String ): 是  表示目标路径所归属站点的域名或者 IP 地址。IP 地址必须是 IPv4 类型的地址。该参数值的长度不能超过 1,024 个字符。该参数的默认值就是您的加速域名。
            TargetPath ( String ): 是  表示跳转后的目标路径。路径必须以斜杠（/）开头并且不能包含双斜杠（//）、百分号（%）、空格。该参数值的长度不能超过 1,024 个字符。
            TargetProtocol ( String ): 是  表示 URL重定向后的新请求所使用的协议。该参数有以下取值：
                  - followclient：表示使用原请求的协议。
                  - http：表示新请求强制使用 HTTP 协议。
                  - https：表示新请求强制使用 HTTPS 协议。
            TargetQueryComponents ( Object of TargetQueryComponents ): 是  表示原请求 URL 中的查询参数的处理方式。
           "字段"： CommonType
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            IgnoreCase ( Boolean ): 否  表示 CommonType 下的 Referers 列表是否是大小写敏感的。该参数有以下取值：
                  - true: 表示大小写不敏感。
                  - false: 表示大小写敏感。
                  该参数的默认值是 true。
            Referers ( Array of String ): 是  表示一个常规 Referer 列表。在该列表中，您可以指定一个或者多个 IP 地址，CIDR 网段，域名和泛域名。域名可以是二级域名。IP 地址只能是 IPv4 格式的地址。您最多可输入 1,000 个 IP 地址。输入的域名不能包含 http:// 或 https://。该参数值的长度不能超过 30,000 个字符。
            IgnoreScheme ( Boolean ): 否  表示 CDN 是否对 Referer 中的 scheme 进行校验，也就是校验 Referer 是否包含 http:// 或者 https://。该参数有以下取值：
                  - true: 表示 CDN 不校验 Referer 是否包含 scheme。在这个情况下，无论 Referer 是否包含 scheme，CDN 都会将 Referer 与您配置的名单进行匹配校验。
                  - false: 表示 CDN 会先校验 Referer 是否包含 scheme。只有 Referer 包含 scheme，CDN 才会将 Referer 与您配置的名单进行匹配校验。否则，CDN 判定请求与您配置的名单不匹配。
                  该参数的默认值是 false。
                  另外，该配置对 RegularType 下的正则表达式列表不生效，因为 CDN 依赖正则表达式来判断 Referer 是否匹配正则名单。
            ContMainDomain ( Boolean ): 否  泛域名匹配包含主域名
           "字段"： RegularType
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Referers ( Array of String ): 是  表示一个用于匹配 Referer 的正则表达式列表。该参数值的长度不能超过 30,000 个字符。
           "字段"： RemoteAuthRuleAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AuthModeConfig ( Object of AuthModeConfig ): 是  表示鉴权服务器的配置。
            AuthResponseConfig ( Object of AuthResponseConfig ): 是  CDN 需要对鉴权服务器返回的鉴权状态码进行处理。该参数表示相关的配置。
            QueryStringRules ( Object of QueryStringRules ): 是  表示鉴权请求的参数设置。
            RequestBodyRules ( String ): 是  表示鉴权请求正文的规则。您可以不指定该参数或者设置该参数值为 default。default 表示请求正文为空（""）。
            RequestHeaderRules ( Object of RequestHeaderRules ): 是  表示鉴权请求头的设置。您最多可以设置 50 个请求头。
           "字段"： RequestHeaderInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  指定对请求头的操作。该参数有以下取值：
                  - set：表示设置一个头部。设置操作包括添加与修改。如果请求中已包含该头部，该头部的值会被覆盖。如果请求中没有包含该头部，该头部会被添加。
                  - delete，表示删除一个头部。
            Key ( String ): 是  指定一个头部的名称。名称的长度不能超过 1,024 个字符，不区分大小写。同时，名称不能包含以下字符：
                  - 下划线（_）、空格、双引号（"）
                  另外，头部名称不能使用这些 特定的名称。
            ValueType ( String ): 是  指定 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值：
                  - constant：表示 Key 的值是一个固定字符串。
                  - variable：表示 Key 的值来自一个变量。
                  - customize：表示 Key 的值是变量与固定字符串拼接后的一个字符串。
            Value ( String ): 否  表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。当 ValueType 是 constant 时，您需要指定一个字符串作为头部的值。该头部值的长度不能超过 1,024 个字符，不能包含美元符号（$）。
                  当 ValueType 是 variable 时，Key 的值可以是来自 该列表中的某个变量。除了名称包含下划线的变量，列表中的任何一个变量都可以作为 Key，并赋予一个字符串来替换其已有的值。也就是说，当您使用任意这些名称不包含下划线的变量作为 Key 时，其值是可以被覆盖的。
                  当 ValueType 是 customize 时，表示 Key 的值是列表中的变量与字符串拼接后的字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：aaa${http_host}bbb${msec}ccc
           "字段"： ResponseHeaderInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  指定对响应头的操作。该参数有以下取值：
                  - set：表示设置一个头部。设置操作包括添加与修改。如果源站响应中已包含该头部，该头部的值会被覆盖。如果源站响应中没有包含该头部，该头部会被添加。
                  - delete，表示删除一个头部。
            Key ( String ): 是  指定一个头部的名称。名称不能超过 1,024个字符，不区分大小写，不能包含以下字符：
                  - 下划线（_）、空格、双引号（"）
                  同时，头部名称不能使用这些 特定的名称。
            ValueType ( String ): 是  指定 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值：
                  - constant：表示 Key 的值是一个字符串。
                  - variable：表示 Key 的值来自一个变量。
                  - customize：表示 Key 的值是一个变量与字符串拼接后的字符串。
            AccessOriginControl ( Boolean ): 否  表示在 CDN 响应用户请求时，是否校验请求中的 Origin 头部。
                  该参数有以下取值：
                  - true：表示 CDN 会校验 Origin 头部。如果校验成功，CDN 会在响应中包含 Access-Control-Allow-Origin 头部。头部值与 Origin 头部值相同。如果校验失败，响应中不会包含 Access-Control-Allow-Origin 头部。
                  - false：表示 CDN 不会校验 Origin 头部。在响应中，CDN 会包含 Access-Control-Allow-Origin 头部。头部值是您配置的 Access-Control-Allow-Origin 的内容。
                  该参数的默认值是 false。
                  该参数仅在以下条件都满足的情况下有效：
                  - Action 是 set。
                  - Key 是 Access-Control-Allow-Origin。
                  - ValueType 是 constant。
            Value ( String ): 否  表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。当 ValueType 是 constant 时，您需要指定一个字符串作为头部的值。头部值的长度不能超过 1,024 个字符，不能包含美元符号（$）。
                  当 ValueType 是 variable 时，Key 的值可以是来自 该列表中的某个变量。除了名称包含下划线的变量，列表中的任何一个变量都可以作为 Key，并赋予一个字符串来替换其已有的值。也就是说，当您使用任意这些名称不包含下划线的变量作为 Key 时，其值是可以被覆盖的。
                  当 ValueType 是 customize 时，表示 Key 的值是列表中的变量与字符串拼接后的一个字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：${remote_addr}aaa${host}ccc
           "字段"： SignedUrlAuthAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Duration ( Long ): 是  表示签名的有效时间，单位是秒。该参数与请求中包含时间戳搭配使用，用来计算签名的过期时间。该参数的取值范围是 0-315,360,000。签名的过期时间 = 时间戳 + Duration。在 CDN 收到某个请求时，如果签名的过期时间小于当前时间，CDN 判定签名已过期。
            MasterSecretKey ( String ): 是  表示主密钥，长度为 6-40个字符。
            URLAuthType ( String ): 是  签名类型。该参数有以下取值：typea、typeb、typec、typed、typee，每种类型得鉴权说明见 配置 URL 鉴权 。
            BackupSecretKey ( String ): 否  表示备密钥。备密钥的长度为 6-40个字符。
            CustomVariableRules ( Object of CustomVariableRules ): 否  表示自定义签算变量。
            KeepOriginArg ( Boolean ): 否  表示 CDN 是否在回源请求中包含用户请求中的签名参数。仅当 URLAuthType 是 typea 或 typed 时，你可以设置该参数。并且，要设置该参数，请 提交工单。
                  该参数有以下取值：
                  * true：表示 CDN 在回源请求中包含签名参数。
                  * false：表示 CDN 在回源请求中不包含签名参数。
                  另外，
                  * 当 URLAuthType 是 typea 或 typed 时，该参数的默认值是 false。
                  * 当 URLAuthType 是 typeb 或 typec 时，该参数值必须是 false。
                  * 当 URLAuthType 是 typee 时，该参数值必须是 true。
            RewriteM3u8 ( Boolean ): 否  对于 HLS Manifest (.m3u8) 的请求，该参数表示 CDN 是否要修改 Manifest，从而为每个视频分片生成签名并将签名添加到 URI 中。
                  该参数有以下取值：
                  - true：表示需要修改 Manifest。
                  - false：表示不需要修改 Manifest。
                  该参数的默认值是 false。
                  当 URLAuthType 为 typee 时，该参数无效。
                  当前，CDN 不会修改压缩文件。因此，在以下任何情况下，CDN 都不会修改 Manifest。
                  * 源站响应中包含 Content-Encoding 头部。该标头表明该 Manifest 已被压缩。
                  * 用户请求匹配 "智能压缩" 特性中的规则。
            SignName ( String ): 否  表示签名参数的名称。该参数的说明如下：
                  - 可以包括英文字母、数字、下划线（_）、中划线（-）、句号（.）、逗号（,）、感叹号（!）。
                  - 长度不能超过 100 个字符。
                  - 至少包含一个字母或者数字。
                  - 不能与 TimeName 相同。
                  当 URLAuthType 为 typea、typed、typee 时，该参数为必填。对于其他类型，该参数不生效。
            SignatureRule ( Array of String ): 否  当 URLAuthType 为 typee 时，该参数为必填，表示需要纳入签名计算的字段。必须纳入签名计算的字段如下：
                  - key：表示MasterSecretKey或 BackupSecretKey 参数的值。
                  - uri：表示用户请求资源的 URI。如果 URI 包含中文字符，您需要对 URI 编码。
                  - TimeName：表示 TimeFormat 参数的值。
                  可选择纳入签名计算的字段如下：
                  - domain：表示加速域名。
                  - referer：表示用户请求携带的 referer 值。
                  - ua：表示用户请求携带的 User-Agent 值。
                  - ip：表示用户请求的客户端 IP。
                  - origin：表示用户请求携带的 Origin 值。
                  - 自定义变量：表示您在 CustomVariableInstances 中定义的变量名称。
                  CDN 按列表中字段出现顺序将这些字段拼接成一个字符串，然后计算该字符串的 MD5 值。该 MD5 值就是签名。
            TimeFormat ( String ): 否  表示 TimeName 使用的进制。该参数有以下取值：
                  - decimal：十进制。
                  - heximal：十六进制。
                  当 URLAuthType 为 typed、typee 时，该参数为必填。当 URLAuthType 为 typec 时，无论您是否设置该参数，该参数的值会被强制设置为 heximal。对于 URLAuthType 的其他值，该参数不生效。
            TimeName ( String ): 否  表示时间戳参数的名称。TimeName 的值可以包括英文字母、数字、下划线（_）、中划线（-）、句号（.）、逗号（,）、感叹号（!），长度为 1-100 个字符。TimenName 不能与 SignName 相同。
                  当 URLAuthType 为 typed、typee 时，该参数为必填。对于其他类型，该参数不生效。
            RewriteM3u8Rule ( Object of RewriteM3u8Rule ): 否  表示 "M3U8 改写" 功能的配置。该配置仅当以下条件都满足时才有效：
                  - RewriteM3u8 是 true。
                  - URLAuthType 不是 typee。
                  要设置该参数，请 提交工单。
            AuthAlgorithm ( String ): 否  表示签名计算使用的算法。该配置有以下取值：
                  - md5：表示 MD5 算法。
                  - sha256：表示 SHA-256 算法。
                  该参数的默认值是 md5。
           "字段"： TimeoutAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            HttpTimeout ( Long ): 否  表示 HTTP 请求的超时时间。该参数的取值范围是 5-60。
            TcpTimeout ( Long ): 否  表示 TCP 请求的超时时间。该参数的取值范围是 2-60。
           "字段"： BlockAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示 CDN 如何处理匹配 Condition 的请求。该参数有以下取值：
                  - refuse：表示 CDN 拒绝请求并响应一个 4xx 的错误码。错误码在 StatusCode 中指定。
                  - redirect：表示 CDN 将请求重定向到 RedirectUrl 中指定的 URL。
            StatusCode ( String ): 是  表示对于匹配 Condition 的用户请求，CDN 的响应状态码。
                  - 当 Action 是 refuse 时，该参数表示一个 400-499 范围内的错误码。
                  - 当 Action 是 redirect 时，该参数有以下取值：
                  	- 301：表示响应状态码是 301。
                  	- 302：表示响应状态码是 302。
            ErrorPage ( String ): 否  - 当 Action 是 refuse 时，该参数是可选的，说明如下：
                  	- 如果指定该参数，该参数表示 "全局配置" 特性中的一个自定义响应页面的名称。也就是说，当 CDN 拒绝请求时，返回该自定义页面。需要留意的是，要使用 "全局配置"，请 提交工单。
                  	- 如果不指定该参数，表示 CDN 使用 StatusCode 中指定错误码的标准响应正文。
                  - 当 Action 是 redirect 时，该参数无效，可以不指定。
            RedirectUrl ( String ): 否  - 当 Action 是 redirect 时，该参数必填，表示重定向 URL。URL 必须以 http:// 或 https:// 开头，长度不能超过 1,024 个字符。
                  - 当 Action 是 refuse 时，该参数无效，可以不指定。
           "字段"： Actions
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            OriginLines ( Array of OriginLines ): 否  表示一个源站列表。当前，列表中只能包含一个源站。
           "字段"： OriginResponseHeaderInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示 CDN 对响应头的操作。该参数有以下取值：
                  - set：表示设置一个头部。设置操作包括添加与修改。如果源站响应中已包含该头部，该头部的值会被覆盖。如果源站响应中没有包含该头部，该头部会被添加。
                  - delete：表示删除一个头部。
            Key ( String ): 否  表示一个头部的名称。名称不能超过 1,024 个字符，不区分大小写，不能包含汉字以及以下字符：
                  - 汉字、下划线（_）、空格、双引号（"）、冒号（:）
                  参见 常用头部。
            Value ( String ): 否  表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。
                  - 当 ValueType 是 constant 时，您需要指定一个固定字符串作为头部的值。头部值的长度不能超过 1,024 个字符，不能包含美元符号（$）。
                  - 当 ValueType 是 variable 时，Key 的值可以是来自 该列表中的某个变量。除了名称包含下划线的变量，列表中的任何一个变量都可以作为 Key，并赋予一个固定字符串来替换其已有的值。也就是说，当您使用任意这些名称不包含下划线的变量作为 Key 时，其值是可以被覆盖的。
                  - 当 ValueType 是 customize 时，表示 Key 的值是列表中的变量与固定字符串拼接后的字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：${remote_addr}aaa${host}ccc
            ValueType ( String ): 否  表示 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值：
                  - constant：表示 Key 的值是一个固定字符串。
                  - variable：表示 Key 的值来自一个变量。
                  - customize：表示 Key 的值是一个变量与固定字符串拼接后的字符串。
            Object ( String ): 否  表示该规则对哪些用户请求生效。该参数有以下取值：
                  - default：表示该规则仅对源站响应中包含以下响应码的用户请求生效：
                  	- 200、201、204、206、301、302、303、304、307、308
                  - all_request：表示该规则对所有用户请求生效。
                  该参数的默认值是 default。另外，当 Action 是 delete 时，该参数的值只能是 all_request。
           "字段"： PrivateBucketAuth
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 是  表示访问存储桶是否需要凭证。如果您指定了 PrivateBucketAuth 结构体，该参数值必须是 true。
            AuthType ( String ): 否  表示存储桶使用的是哪个对象存储服务所提供的鉴权方式。该参数有以下取值：
                  - tos：表示火山引擎 TOS。
                  - cos：表示腾讯云 COS。
                  - oss：表示阿里云 OSS。
                  - aws_common：表示 AWS S3 或者其他使用兼容 S3 鉴权方式的第三方对象存储服务。如果您要使用您在云厂商处为存储桶配置的自定义域名，请指定 AuthType 为 aws_common。
                  - aws: 含义与 aws_common 相同，不支持指定自定义域名，不推荐使用。
                  如果存储桶来自另一个主账号下的 TOS 服务，请设置 AuthType 为 aws_common.
            TosAuthInformation ( Object of TosAuthInformation ): 否  表示存储桶的访问凭证。当以下任意条件满足时，您必须指定该参数。
                  * AuthType 不是 tos。
                  * 存储桶来自另一个主账号下的 TOS 服务。
           "字段"： AccessAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AllowEmpty ( Boolean ): 是  表示当用户请求不包含指定头部时，CDN 处理请求的方式。该参数有以下取值：
                  - true：表示如果请求不包含指定头部，则该请求被认为匹配您配置的头部值列表。
                  - false：表示如果请求不包含指定头部，则该请求被认为不匹配您配置的头部值列表。
                  该参数的默认值是 false。
            ListRules ( Array of String ): 是  表示一个正则表达式列表，用于匹配请求头的值。
                  列表中的正则表达式不能超过 20 个，所有正则表达式总长度不能超过 1,024 个字符。正则表达式之间的关系是或。也就是说，如果一个用户请求中 RequestHeader 的值匹配任何一个正则表达式，该规则就匹配了这个请求。
            RequestHeader ( String ): 是  表示一个指定的请求头。头部名称不区分大小写，并且有以下要求：
                  - 名称的长度不超过 1,024 个字符，
                  - 名称不能是 Referer、User-Agent 或 Origin。
                  - 名称可以包含字母，数字，下划线（_），连字符（-）。
                  - 名称不能以数字开头。
            RuleType ( String ): 是  表示名单的类型。该参数有以下取值：
                  - allow：表示该规则中定义的是一个白名单。如果一个用户请求不匹配白名单，CDN 会拒绝该请求，响应 403 状态码。
                  - deny：表示该规则中定义的是一个黑名单。如果一个用户请求匹配了黑名单，CDN 会拒绝该请求，响应 403 状态码。
           "字段"： SpeedLimitTime
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DayWeek ( String ): 是  表示该限速规则启用的日期，有以下取值：monday，tuesday，wednesday，thursday，friday，saturday，sunday，unlimited。
                  unlimited 表示每天。您可以指定一个或多个日期，多个日期之间使用分号（;）分隔。
            BeginTime ( String ): 否  表示该限速规则启用的开始时间，格式是 mm:ss。
                  如果 DayWeek 是 unlimited, BeginTime 会被设置为 00:00，您无法更改。
            EndTime ( String ): 否  表示该限速规则启用的结束时间，格式是 mm:ss。
                  如果 DayWeek 是 unlimited, EndTime 会被设置为 23:59，您无法更改。
           "字段"： TargetQueryComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示原请求 URL 中的查询参数的处理方式。该参数有以下取值：
                  - include：表示在跳转后的 URL 中包含原请求 URL 中的所有查询参数。
                  - exclude：表示在跳转后的 URL 中不包含原请求 URL 中的任何查询参数。
                  - includePart：表示在跳转后的 URL 中包含原请求 URL 中特定的查询参数。
                  - excludePart：表示在跳转后的 URL 中不包含原请求 URL 中特定的查询参数。
            Value ( String ): 是  表示要保留或删除的查询参数。多个查询参数间使用英文分号（;）分隔。指定的查询参数不能包含双斜杠（//）、百分号（"）、空格。Value 的默认值是 *，表示所有的查询参数。
                  - 如果 Action 是 include 或者 exclude, 则 Value 必须为 *。
                  - 如果 Action 是 includePart 或者 excludePart，您可以指定一个或者多个查询参数。此时，您指定的查询参数不能是 *。
           "字段"： AuthModeConfig
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            MasterRemoteAddr ( String ): 是  表示鉴权服务器的主地址，长度不能超过 100 个字符。主地址的格式是 ://: 或 ://:，其中：
                  * ` 是 http 或者 https`。
                  * ` 不能是 localhost`。
                  * ` 不能是 127.0.0.1`。
                  * `` 是可选的。
            PathType ( String ): 是  表示鉴权请求的路径。鉴权地址和请求路径组成了完整的鉴权 URL。CDN 会把用户的请求转发到该鉴权 URL。该参数有以下取值：
                  - constant：表示鉴权请求中的路径与用户请求中的路径相同。
                  - variable：表示您需要在 pathValue 参数中指定一个鉴权请求中的路径。
            RequestMethod ( String ): 是  表示在发送鉴权请求时，CDN 所使用的请求方法。该参数有以下取值：
                  - default：表示鉴权请求所使用的方法与用户的请求相同。
                  - get：表示鉴权请求使用 GET 方法。
                  - post：表示鉴权请求使用 POST方法。
                  - head：表示鉴权请求使用 HEAD 方法。
            BackupRemoteAddr ( String ): 否  表示鉴权服务器的备地址。地址格式和要求与主地址相同。
            PathValue ( String ): 否  表示一个鉴权请求的路径，长度不能超过 100 个字符。路径必须以斜杠（/）开头，不能包含以下字符：
                  - 双斜杠（//）、百分号（%）、美元符号（$）、空格、问号（?）
           "字段"： AuthResponseConfig
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CacheAction ( Object of CacheAction ): 否  CDN 可以缓存鉴权状态码。该参数表示相关的配置。
            ResponseAction ( Object of ResponseAction ): 否  表示鉴权失败时，CDN 如何响应用户。
            StatusCodeAction ( Object of StatusCodeAction ): 否  表示 CDN 对鉴权状态码的处理方式。
            TimeOutAction ( Object of TimeOutAction ): 否  表示鉴权超时后，CDN 如何处理鉴权请求。
           "字段"： QueryStringRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            QueryStringComponents ( Object of QueryStringComponents ): 否  表示鉴权请求参数的设置策略。
            QueryStringInstances ( Array of QueryStringInstances ): 否  表示鉴权请求中额外的参数设置。您最多可以设置 50 个参数。
           "字段"： RequestHeaderRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            RequestHeaderComponents ( Object of RequestHeaderComponents ): 否  表示鉴权请求头的设置策略。
            RequestHeaderInstances ( Array of RequestHeaderInstances ): 否  表示一组鉴权请求头的设置。
                  需要留意的是，在 CDN 发起鉴权请求时，请求中可能已经包含了以下头部：
                  - X-Forwarded-Protocol，X-Forwarded-Proto，X-Client-Scheme：这三个头部都表示用户请求所使用协议，没有区别。
                  - X-Real-IP：表示用户真实的 IP 地址。该头部的值不会受代理服务器的影响。
                  - X-Forwarded-For：表示用户的 IP 地址。如果用户的请求经过了代理服务器，该头部的值会变成代理服务器的 IP 地址。
                  不建议您在该参数中对这些头部进行设置。如果您设置了这些头部，这些头部的原始值会被覆盖。
            RequestHost ( String ): 否  表示鉴权请求中 HOST 头部的值。该参数的默认值是 default，表示 HOST 头部的值与您的加速域名相同。
           "字段"： CustomVariableRules
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            CustomVariableInstances ( Array of CustomVariableInstances ): 是  表示一个变量列表。
           "字段"： RewriteM3u8Rule
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DeleteParam ( Boolean ): 否  表示在改写分片 URI 时是否保留 URL 中原有的参数。该参数有以下取值：
                  - true：表示删除原有参数。
                  - false：表示保留原有参数。
                  该参数的默认值是 false。需要留意的是，该参数的设置影响签名的计算。参见 M3U8 改写功能的字段描述。
            KeepM3u8Param ( Boolean ): 否  表示是否将 HLS Manifest 请求中的不表示签名的查询参数添加到分片 URI 中。该参数有以下取值：
                  - true：表示在分片 URI 中添加查询参数。
                  - false：表示不添加查询参数。
                  该参数的默认值是 false。需要留意的是，该参数的设置影响签名的计算。参见 M3U8 改写功能的字段描述。
            RewriteTag ( Object of RewriteTag ): 否  表示 "标签改写" 的配置。
           "字段"： TosAuthInformation
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            AccessKeyId ( String ): 否  表示访问凭证中的 AccessKey ID，在腾讯云称为 SecretId。
            AccessKeySecret ( String ): 否  表示访问凭证中的 AccessKey Secret，在腾讯云称为 SecretKey。
           "字段"： ResponseAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            StatusCode ( String ): 是  表示鉴权失败时，CDN 响应用户的状态码。您可以指定范围在 400-499 中的任意一个状态码。该参数的默认值是 403。
           "字段"： StatusCodeAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            DefaultAction ( String ): 是  表示如果鉴权状态码既不是 FailCode，又不是 SuccessCode 时，CDN 处理鉴权请求的方式。该参数有以下取值：
                  - reject：表示 CDN 认为鉴权失败。
                  - pass：表示 CDN 认为鉴权成功。
            FailCode ( String ): 是  表示鉴权失败时的鉴权状态码。您可以指定范围在 400-499 中的一个或者多个状态码。多个状态码使用英文分号（;）分隔。您也可以指定 4xx 表示 400-499 中的任意一个状态码。该参数的默认值是 401。
            SuccessCode ( String ): 是  表示鉴权成功时的鉴权状态码。您可以指定范围在 200-299 中的一个或者多个状态码。多个状态码使用英文分号（;）分隔。您也可以指定 2xx 表示 200-299 中的任意一个状态码。该参数的默认值是 200。
           "字段"： TimeOutAction
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示鉴权超时后，CDN 处理鉴权请求的策略。该参数有以下取值：
                  - reject：表示 CDN 认为鉴权失败。
                  - pass：表示 CDN 认为鉴权成功。
            Time ( Long ): 是  表示鉴权超时的时间，单位是毫秒。该参数的默认值为 200，取值范围是 200 - 3600。
           "字段"： QueryStringComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示鉴权请求是否包含用户请求 URL 中的查询参数。该参数有以下取值：
                  - exclude：表示鉴权请求不包含任何查询参数。
                  - include：表示鉴权请求包含所有查询参数。
                  - includePart：表示鉴权请求包含指定的查询参数。
            Value ( String ): 否  表示 Action 参数所对应的参数值，长度不能超过1,024 个字符。该参数有以下取值：
                  - 如果 Action 是 exclude 或 include，Value 必须是 *。
                  - 如果 Action 是 includePart，您需要在 Value 参数中指定用户请求 URL 中的一个或者多个查询参数，多个查询参数使用英文分号（;）分隔。您不能指定 *。查询参数是区分大小写的，不能包含双引号（"），也不能包含空格。
                  该参数的默认值是 *。
           "字段"： QueryStringInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 否  表示如何设置鉴权请求参数。当前您只能设置 Action 为 set。set 表示设置参数。您需要在 Key 中指定您需要设置的鉴权请求参数。如果您指定的鉴权请求参数不存在，CDN 会在鉴权请求中添加该参数。如果您指定的鉴权请求参数已存在，CDN 会使用 Value 的值作为该鉴权请求参数的值。
            Key ( String ): 否  表示您需要设置的鉴权请求参数，长度不能超过 1,024 个字符，不能包含双引号（"），也不能包含空格。
            Value ( String ): 否  表示鉴权请求参数的值，长度不能超过 1,024 个字符，并且区分大小写。Value有以下取值：
                  - 当 ValueType 是 constant 时，表示鉴权请求参数的值是一个常量。您需要指定该常量值。常量值不能以美元符号（$）开头，也不能包含双引号（"）。
                  - 当 ValueType 是 variable 时，表示鉴权请求参数的值来自一个变量。您可以指定该变量列表中的变量。
                  - 当 ValueType 是 customize 时，表示鉴权请求参数的值是列表中的变量与固定字符串拼接后的字符串。在拼接的字符串中，变量使用 ${变量名} 表示。示例值：bind${request_uri}to${local_ip}done
            ValueType ( String ): 否  表示您在 Key 中设置的鉴权请求参数的类型。ValueType 有以下取值：
                  - constant：表示鉴权请求参数是一个常量。此时，您需要在 Value 中指定该常量的值。
                  - variable：表示鉴权请求参数的值来自一个变量。参见 Value 的说明。
                  - customize：表示鉴权请求参数的值是一个变量与固定字符串拼接后的字符串。
           "字段"： RequestHeaderComponents
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Action ( String ): 是  表示鉴权请求头是否包含用户请求头。该参数有以下取值：
                  - exclude：表示鉴权请求头中不包含任何用户请求头。
                  - include：表示鉴权请求头中包含所有用户请求头。
                  - includePart：表示鉴权请求头包含指定的用户请求头。
            Value ( String ): 否  表示 Action 参数所对应的参数值，长度不能超过 1,024 个字符。该参数有以下说明：
                  - 如果 Action 是 exclude 或 include，Value 必须是 *。
                  - 如果 Action 是 includePart，Value 参数的取值是用户请求中的一个或者多个头部。多个头部使用英文分号（;）分隔。其取值不能只是 *，不能包含以下字符：
                  	- 下划线（_）、空格、双引号（"）
                  该参数的默认值是 *。
           "字段"： CustomVariableInstances
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Operator ( String ): 是  表示变量的匹配方式。该参数的取值只能是 match。
            Type ( String ): 是  表示变量的类型。该参数有以下取值：
                  - queryString：表示该变量是请求中的一个查询参数。
                  - requestHeader：表示该变量是请求中的一个头部字段。
            Value ( String ): 是  表示变量的名称，长度不超过 100 个字符。变量名称的要求如下：
                  - 如果 Type 是 queryString，变量名称可以包含以下字符：
                  	- 字母、数字、连字符（-）、逗号（,）、句号（.）、感叹号（!）
                  - 如果 Type 是 requestHeader，变量名称不能包含以下字符：
                  	- 下划线（_）、空格、双引号（"）、冒号（:）
           "字段"： RewriteTag
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Switch ( Boolean ): 否  表示是否需要改写额外标签中的分片 URL。该参数有以下取值：
                  - true：表示需要改写额外标签。
                  - false：表示无额外标签需要改写。
            Tags ( Array of String ): 否  表示除默认标签外，需要对其下分片 URI 进行改写的额外标签列表。
    """,
    "describe_domain_env_version": r"""
    Args:
        body: A JSON structure
             参数 ( 类型 ): 是否必选  描述
             ---- ( ---- ): ----  ----
             Domain ( String ): 是  表示要查询的域名。
    Returns:
        参数 ( 类型 ): 描述
        ---- ( ---- ): ----
        LastProdVersion ( String ): 表示上一个发布到线上环境的版本号。
        LastStagingVersion ( String ): 表示上一个发布到预发布环境的版本号。
        ProdVersion ( String ): 表示发布到线上环境的版本号。
        StagingVersion ( String ): 表示发布到预发布环境的版本号。
            如果该参数值为空（""），表示没有任何版本发布到预发布环境。
    """,
    "describe_domain_version": r"""
    Args:
        body: A JSON structure
             参数 ( 类型 ): 是否必选  描述
             ---- ( ---- ): ----  ----
             Domain ( String ): 是  表示一个域名，获取该域名下指定版本中各 CDN 特性的配置。
             VersionId ( String ): 是  表示一个版本号。
                   您可以调用 ListDomainVersions 获取指定域名下的所有版本号。
   Returns:
        参数 ( 类型 ): 描述
        ---- ( ---- ): ----
        CreateTime ( Long ): 表示版本的创建时间，格式是 Unix 时间戳。
        Creator ( String ): 表示版本的创建者。
            * 域名下的第一个版本是系统创建的，该版本的 Creator 是 System。
            * 如果是 IAM 用户创建了该版本，Creator 就是这个 IAM 用户的账号。
        DomainConfig ( Object of DomainConfig ): 表示各 CDN 特性的配置。关于各 CDN 特性的配置说明，参见 UpdateCdnConfig。
        Env ( Array of String ): 表示版本发布到的环境，有以下取值：
            * prod：表示线上环境。
            * staging：表示预发布环境。
            如果该参数值为空（[]），表示版本尚未发布到任何环境。
        Message ( String ): 表示版本的备注。
            域名下的第一个版本是系统创建的，该版本的 Message 是 Built by system automatically。
        OriginalVersion ( String ): 表示该版本复制于哪个版本。
            域名下的第一个版本是系统创建的，该版本的 OriginalVersion 是空（""）。
        ReleaseTime ( Long ): 表示该版本最近一次的发布时间，格式是 Unix 时间戳。
            对于刚创建的域名，ReleaseTime 与 CreateTime 相同。
        UpdateTime ( Long ): 表示版本的最近更新时间，格式是 Unix 时间戳。
        VersionId ( String ): 表示该版本的版本号。
       "字段"： DomainConfig
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Origin ( Array of Origin ): 表示源站配置。 
        OriginProtocol ( String ): 表示回源请求使用的协议。该参数有以下取值： 
            - http：表示回源请求使用 HTTP 协议。 
            - https：表示回源请求使用 HTTPS 协议。 
            - followclient：表示回源协议与用户请求使用的协议相同。 
        ServiceType ( String ): 表示该域名的业务类型。该参数有以下取值： 
            - download：表示文件下载。 
            - web：表示网页。 
            - video：表示音视频点播。 
        AreaAccessRule ( Object of AreaAccessRule ): 表示 "地域访问控制" 特性的配置。 
        BrowserCache ( Array of BrowserCache ): 表示 "浏览器缓存" 特性的配置。该配置包含一个规则列表，说明如下： 
            - 每条规则包含匹配条件配置和操作配置。 
            - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。 
            - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
        Cache ( Array of Cache ): 表示 "缓存规则" 特性的配置。该特性默认为禁用，表示不创建自定义规则。 
            - 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。  
            - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
            CDN 中有一条 默认缓存规则，，用于匹配任何未能匹配其他规则的用户请求。该默认规则始终生效，并且优先级最低。 
        CacheHost ( Object of CacheHost ): 表示 "共享缓存" 特性的配置。 
        CacheKey ( Array of CacheKey ): 表示 "缓存键值" 特性的配置。该配置中包含一个规则列表，说明如下： 
            - 每条规则包含匹配条件配置和操作配置。 
            - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。 
            - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
        Cname ( String ): 表示内容分发网络为该加速域名分配的 CNAME。 
        Compression ( Object of Compression ): 表示 "智能压缩" 特性的配置。 
        CreateTime ( Long ): 表示该加速域名的创建时间，格式是 Unix 时间戳。 
        CustomErrorPage ( Object of CustomErrorPage ): 表示 "自定义错误页面" 特性的配置。 
        CustomizeAccessRule ( Object of CustomizeAccessRule ): 表示 "自定义头部黑白名单" 特性的配置。 
        Domain ( String ): 表示该加速域名。 
        DownloadSpeedLimit ( Object of DownloadSpeedLimit ): 表示 "下载限速" 特性的配置。 
        FollowRedirect ( Boolean ): 表示 "回源重定向跟随" 特性的配置。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        HTTPS ( Object of HTTPS ): 表示 HTTPS 特性的配置。 
        HttpForcedRedirect ( Object of HttpForcedRedirect ): 表示 "HTTPS 强制跳转到 HTTP" 特性的配置。 
        IPv6 ( Object of IPv6 ): 表示 IPv6 配置。 
        IpAccessRule ( Object of IpAccessRule ): 表示 "IP 黑白名单" 特性的配置。 
            该特性提供了两种配置方式： 
            - 常规配置：指定 RuleType 和 Ip 对当前加速域名进行配置。 
            - 全局配置：指定 SharedConfig 使用一个全局配置。 
        LockStatus ( String ): 表示该域名的配置是否允许被变更。该参数有以下取值： 
            - on：表示允许。 
            - off：表示不允许。 
        MethodDeniedRule ( Object of MethodDeniedRule ): 表示 "禁用 HTTP Method" 特性的配置。 
        NegativeCache ( Array of NegativeCache ): 表示 "状态码缓存" 特性的配置。该配置包含一个规则列表，说明如下： 
            - 每条规则包含过匹配条件配置和操作配置。 
            - 规则在列表中出现的顺序表示规则的优先级。列表中第一条规则的优先级最高。 
            - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
        OriginAccessRule ( Object of OriginAccessRule ): 表示 "Origin 黑白名单" 特性的配置。 
        OriginArg ( Array of OriginArg ): 表示 "回源参数" 配置的规则列表。 
            - 每条规则包含一个匹配条件（Condition）和 CDN 执行操作（OriginArgAction）。 
            - 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。 
            - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
        OriginHost ( String ): 如果源站服务器上有多个站点，该参数表示回源请求访问的站点域名。该参数对所有源站配置生效，但是优先级低于源站配置中 OriginHost 参数。 
        OriginRange ( Boolean ): 表示 "回源 Range" 特性的配置。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
            请求分片大小默认是 1 MB。 
            如果 Range 结构体中 Switch 为 true，则该特性为启用，即使 OriginRange 为 false。 
        OriginRewrite ( Object of OriginRewrite ): 表示 "回源 URL 改写" 特性的配置。 
        OriginSni ( Object of OriginSni ): 表示 "回源 SNI" 特性的配置。 
        PageOptimization ( Object of PageOptimization ): 表示 "页面优化" 特性的配置。 
        Project ( String ): 表示该加速域名归属的项目。 
        Quic ( Object of Quic ): 表示 QUIC 配置。 
        RedirectionRewrite ( Object of RedirectionRewrite ): 表示 "URL 重定向改写" 特性的配置。 
        RefererAccessRule ( Object of RefererAccessRule ): 表示 "Referer 黑白名单" 特性的配置。关于不同配置对请求匹配结果的影响，参见 配置示例。 
        RemoteAuth ( Object of RemoteAuth ): 表示 "远程鉴权" 特性的配置。 
        RequestHeader ( Array of RequestHeader ): 表示 "回源 HTTP 请求头" 特性的配置。 
        ResponseHeader ( Array of ResponseHeader ): 表示 "HTTP 响应头" 特性的配置。 
        ServiceRegion ( String ): 表示该加速域名的加速区域。该参数有以下取值： 
            - chinese_mainland：表示中国内地。 
            - global：表示全球。 
            - outside_chinese_mainland：表示全球（不含中国内地）。 
        SignedUrlAuth ( Object of SignedUrlAuth ): 表示 "URL 鉴权" 特性的配置。 
        Status ( String ): 表示该加速域名的状态。该参数有以下取值： 
            - online：表示状态是 正常运行。 
            - configuring：表示状态是 配置中。 
            - offline：表示状态是 已下线。 
        Timeout ( Object of Timeout ): 表示 "回源超时时间" 特性的配置。 
        UaAccessRule ( Object of UaAccessRule ): 表示 "UA 黑白名单" 特性的配置。 
        UpdateTime ( Long ): 表示该域名配置的最近一次的更新时间，格式是 Unix 时间戳。如果该域名配置在创建后未被更新，该参数值与 CreateTime 的值相同。 
        VideoDrag ( Object of VideoDrag ): 表示 "视频拖拽" 特性的配置。 
        OriginIPv6 ( String ): 表示 "IPv6 回源" 的配置。该参数有以下取值： 
            - ipv6_first：表示 CDN 始终尝试获取源站域名的 IPv6 地址。如果无法获取该 IP 地址，CDN 才尝试获取源站域名的 IPv4 地址。 
            - ipv4_first：表示 CDN 始终尝试获取源站域名的 IPv4 地址。如果无法获取该 IP 地址，CDN 才尝试获取源站域名的 IPv6 地址。 
            - followclient：表示 CDN 尝试获取与用户请求相同类型的 IP 地址。 
            由于海外部分 CDN 回源节点不支持向 IPv6 地址发送回源请求，该功能仅适用于位于中国内地的回源节点。 
        RequestBlockRule ( Object of RequestBlockRule ): 表示 "自定义拦截" 特性的配置。 
        UrlNormalize ( Object of UrlNormalize ): 表示 "URL 标准化" 特性的配置。 
        OriginCertCheck ( Object of OriginCertCheck ): 表示 "源站证书校验" 特性的配置。 
            该特性启用后，CDN 会校验源站证书的合法性，包括证书是否已被吊销、证书是否由可信 CA 签发、证书与源站域名是否匹配等。CDN 内置了常见可信 CA 的根证书。 
            该特性还支持双向认证，使源站对 CDN 身份进行校验。 
        ConditionalOrigin ( Object of ConditionalOrigin ): 表示 "条件源站" 特性的配置。 
        OriginRetry ( Object of OriginRetry ): 表示 "回源重试设置" 特性的配置。 
        RewriteHLS ( Object of RewriteHLS ): 表示 "标准 HLS 加密改写" 特性的配置。 
        MultiRange ( Object of MultiRange ): 表示 "多重范围（Multi-range)" 特性的配置。 
        RuleEngine ( Object of RuleEngine ): 详情参见 规则引擎配置。 
        OfflineCache ( Object of OfflineCache ): 表示 "离线缓存" 特性的配置。 
        OriginResponseHeader ( Array of OriginResponseHeader ): 表示 "源站响应头设置" 的配置。 
        Range ( Object of Range ): 表示分片大小的设置。 
       "字段"： Origin
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginAction ( Object of OriginAction ): 表示源站配置，应用于所有用户请求。 
       "字段"： AreaAccessRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Area ( Array of String ): 表示一个国家和地区的列表，对该列表应用地域访问限制。国家和地区的名称使用简写来表示。您可以调用 DescribeCdnRegionAndIsp 并指定 Area 为 Global 以获取国家和地区的简写。 
        RuleType ( String ): 表示 Area 的类型。该参数有以下取值： 
            - deny: 表示 Area 是一个黑名单。CDN 将阻止来自这些国家和地区的请求。 
            - allow: 表示 Area 是一个白名单。CDN 仅允许来自这些国家和地区的请求。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： BrowserCache
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheAction ( Object of CacheAction ): 当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheAction 中指定的操作。 
       "字段"： Cache
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheAction ( Object of CacheAction ): 当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheAction 中指定的操作。 
       "字段"： CacheHost
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheHostRule ( Array of CacheHostRule ): 表示一组共享缓存 HOST 的配置。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： CacheKey
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheKeyAction ( Object of CacheKeyAction ): 当一个请求满足 Condition 中的匹配条件时，CDN 会为请求文件设置缓存键。该参数表示缓存键的配置。 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CacheKeyAction 中指定的操作。 
       "字段"： Compression
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        CompressionRules ( Array of CompressionRules ): 表示一组规则。每条规则包含匹配条件配置以及操作配置。 
       "字段"： CustomErrorPage
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        ErrorPageRule ( Array of ErrorPageRule ): 表示一个配置规则的集合。 
       "字段"： CustomizeAccessRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CustomizeInstances ( Array of CustomizeInstances ): 表示一个规则列表。列表中的每条规则中定义了一个黑名单或者白名单的配置。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： DownloadSpeedLimit
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        DownloadSpeedLimitRules ( Array of DownloadSpeedLimitRules ): 表示一个限速规则的列表。该参数的其他说明如下： 
            - 每条规则包含匹配条件配置和限速配置。 
            - 列表中规则的出现顺序表示规则的优先级排序。列表中第一条规则的优先级最高。 
            - 当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
       "字段"： HTTPS
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        CertInfo ( Object of CertInfo ): 表示要与加速域名关联的单本证书的信息。 
        CertInfoList ( Array of CertInfoList ): 表示要与加速域名关联的双证书。 
        DisableHttp ( Boolean ): 表示是否允许请求 URL 中 Scheme 是 HTTP 的请求。该参数有以下取值： 
            - true：表示允许 Scheme 是 HTTP 的请求。 
            - false：表示不允许 Scheme 是 HTTP 的请求。 
        ForcedRedirect ( Object of ForcedRedirect ): 表示 "HTTP 强制跳转到 HTTPS" 特性的配置。 
            CDN 提供了两种协议重定向的特性。 
            * HTTP 重定向到 HTTPS，也就是 ForcedRedirect 特性。 
            * HTTPS 重定向到 HTTP，也就是 HttpForcedRedirect 特性。 
            这两个协议重定向特性是互斥的。 
        HTTP2 ( Boolean ): 表示是否为用户请求启用 HTTP/2 支持。该参数有以下取值： 
            - true：表示启用 HTTP/2。 
            - false：表示禁用 HTTP/2。 
        Hsts ( Object of Hsts ): 表示 HSTS 特性的配置。 
        OCSP ( Boolean ): 表示是否启用 "OCSP 装订" 特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        TlsVersion ( Array of String ): 表示 "TLS 版本" 特性的配置。该参数指定用户请求可以使用的 TLS 版本，有以下取值： 
            - tlsv1.0：表示 TLS 1.0。 
            - tlsv1.1：表示 TLS 1.1。 
            - tlsv1.2：表示 TLS 1.2。 
            - tlsv1.3：表示 TLS 1.3。 
        CertCheck ( Object of CertCheck ): 表示 "访问双向认证" 特性的配置。 
       "字段"： HttpForcedRedirect
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        EnableForcedRedirect ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。启用后，CDN 会将收到的 HTTPS 请求重定向到 HTTP 请求。 
            - false：表示禁用该特性。CDN 不会将 HTTPS 请求重定向到 HTTP 请求。 
        StatusCode ( String ): 表示当收到 HTTPS 请求时，CDN 返回的重定向状态码。该参数有以下取值：301、302、303、307、308。 
            需要留意的是： 
            * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。 
            * 对于 303，新请求使用的方法是 GET。 
            * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。 
       "字段"： IPv6
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： IpAccessRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Ip ( Array of String ): 表示黑名单或白名单中的 IP 地址。 
        RuleType ( String ): 表示 IP 名单的类型。该参数有以下取值： 
            - allow：表示白名单。 
            - deny：表示黑名单。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        SharedConfig ( Object of SharedConfig ): 表示一个全局配置。 
        DenyStatusCode ( Long ): 表示 CDN 在拒绝请求时响应的状态码，如果该配置不指定，则 CDN 响应 403 状态码。 
        IpSource ( Object of IpSource ): 表示客户端 IP 地址获取方式的配置。 
       "字段"： MethodDeniedRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        Methods ( String ): 表示被禁用的一个或多个 HTTP 请求方法。该参数有以下取值： 
            - get：表示禁用 GET 请求方法。 
            - post：表示禁用 POST 请求方法。 
            - delete：表示禁用 DELETE 请求方法。 
            - put：表示禁用 PUT 请求方法。 
            - head：表示禁用 HEAD 请求方法。 
            - patch：表示 PATCH 请求方法。 
            - connect：表示 CONNECT 请求方法。 
            - options：表示 OPTIONS 请求方法。 
       "字段"： NegativeCache
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        NegativeCacheRule ( Object of NegativeCacheRule ): 当一个请求满足 Condition 中的匹配条件时，CDN 会对请求文件执行指定的操作。该参数定义了该操作相关的配置。 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 NegativeCacheRule 中指定的操作。 
       "字段"： OriginAccessRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AllowEmpty ( Boolean ): 表示当用户请求不包含 Origin 头部时，CDN 处理请求的方式。该参数有以下取值： 
            - true：表示如果请求不包含 Origin 头部，则该请求被认为匹配您配置的 Origin 列表。 
            - false：表示如果请求不包含 Origin 头部，则该请求被认为不匹配您配置的 Origin 列表。 
        IgnoreCase ( Boolean ): 表示 Origin 列表是否是大小写敏感的。该参数有以下取值： 
            - true: 表示 Origin 列表是大小写不敏感的。 
            - false: 表示 Origin 列表是大小写敏感的。 
        Origins ( Array of String ): 表示一个 Origin 列表。 
        RuleType ( String ): 表示 Origin 列表的类型。该参数有以下取值： 
            - allow：表示白名单。 
            - deny：表示黑名单。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： OriginArg
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求满足该匹配条件，CDN 执行 OriginArgAction 中指定的操作。 
        OriginArgAction ( Object of OriginArgAction ): 表示在请求满足 Condition 时 CDN 执行的操作。 
       "字段"： OriginRewrite
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginRewriteRule ( Array of OriginRewriteRule ): 表示一个规则列表。当 Switch 是 true 时，该参数为必填。 
            * 列表中规则的顺序定义了规则的优先级。列表中第一条规则的优先级最高。 
            * 当收到一个用户请求时，CDN 按规则的优先级，从高到低尝试将请求与规则匹配。如果请求匹配了一条规则，CDN 就停止处理其余规则。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： OriginSni
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        SniDomain ( String ): 表示回源 SNI 的域名。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： PageOptimization
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OptimizationType ( Array of String ): 表示优化的对象。该参数有以下取值： 
            - html: 表示 HTML 页面。 
            - js: 表示 Javascript 代码。 
            - css: 表示 CSS 代码。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： Quic
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否为用户请求启用 QUIC。该参数有以下取值： 
            - true：表示启用 QUIC。 
            - false：表示禁用 QUIC。 
       "字段"： RedirectionRewrite
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        RedirectionRule ( Array of RedirectionRule ): 表示一个 URL 重定向改写的规则的列表。列表中第一条规则的优先级最高。 
            当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
       "字段"： RefererAccessRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AllowEmpty ( Boolean ): 表示当用户请求不包含 Referer 头部时，CDN 处理请求的方式。该参数有以下取值： 
            - true：表示如果请求不包含 Referer 头部，则该请求被认为匹配您配置的 Referer 列表。 
            - false：表示如果请求不包含 Referer 头部，则该请求被认为不匹配您配置的 Referer 列表。 
        Referers ( Array of String ): 表示一个 Referer 列表，该参数的输入要求与 ReferersType 下 CommonType 类型的 Referers 的输入要求相同。 ReferersType 是推荐使用的。 
            另外，如果指定了 SharedConfig，就不能指定该参数。 
        ReferersType ( Object of ReferersType ): 表示一个 ReferersType 对象。其包含一个 CommonType 对象和一个 RegularType 对象，分别表示一个常规 Referer 列表和一个用于匹配 Referer 的正则表达式列表。这两个对象可以同时定义。 
            如果指定了 SharedConfig，就不能指定该参数。 
        RuleType ( String ): 表示 Referer 名单的类型。该参数有以下取值： 
            - allow：表示白名单。 
            - deny：表示黑名单。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        SharedConfig ( Object of SharedConfig ): 表示一个全局配置。 
            如果指定了该参数，除了 Switch 和 RuleType 以外，RefererAccessRule 下的其余参数都无需指定。 
       "字段"： RemoteAuth
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        RemoteAuthRules ( Array of RemoteAuthRules ): 表示一个鉴权规则的列表。规则包含匹配条件配置和鉴权配置。 
       "字段"： RequestHeader
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        RequestHeaderAction ( Object of RequestHeaderAction ): 表示头部的相关操作设置。 
       "字段"： ResponseHeader
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        ResponseHeaderAction ( Object of ResponseHeaderAction ): 表示 CDN 在响应用户请求的时候，对响应头的操作。 
       "字段"： SignedUrlAuth
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        SignedUrlAuthRules ( Array of SignedUrlAuthRules ): 表示一个规则列表。每条规则包含匹配条件配置和鉴权配置。 
       "字段"： Timeout
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。此时，TCP 请求和 HTTP 请求的超时时间使用默认值，分别是 2 秒和 60 秒。 
        TimeoutRules ( Array of TimeoutRules ): 表示一组超时时间的配置。 
       "字段"： UaAccessRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AllowEmpty ( Boolean ): 表示当用户请求不包含 User-Agent 头部时，CDN 处理请求的方式。该参数有以下取值： 
            - true：表示如果请求不包含 User-Agent 头部，则该请求被认为匹配您配置的 User-Agent 列表。 
            - false：表示如果请求不包含 User-Agent 头部，则该请求被认为不匹配您配置的 User-Agent 列表。 
        IgnoreCase ( Boolean ): 表示 UA 字符串是否是大小写敏感的。该参数有以下取值： 
            - true: 表示 UA 字符串是大小写不敏感的。 
            - false: 表示 UA 字符串是大小写敏感的。 
        RuleType ( String ): 表示指定的是黑名单还是白名单。该参数有以下取值： 
            - deny: 表示指定的是黑名单。 
            - allow: 表示指定的是白名单。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        UserAgent ( Array of String ): 表示一个 UA 的列表。 
        SharedConfig ( Object of SharedConfig ): 表示一个全局配置。 
       "字段"： VideoDrag
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： RequestBlockRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        BlockRule ( Array of BlockRule ): 表示一个规则列表。 
            列表中第一条规则的优先级最高。 
            当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： UrlNormalize
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        NormalizeObject ( Array of String ): 表示一个 URL 标准化选项列表。列表中可包含的选项值说明如下： 
            - dot_segments：表示将请求 URL 中的以下内容进行替换： 
            	- /./：替换为单个斜杠（/）。 
            	- /../：如果 /../ 前还有一个级别的目录，则删除 /../ 与该目录。如果 /../ 前没有目录，则保留原 URL。 
            - back_slashes：表示将请求 URL 中的反斜杠（）替换为单个斜杠（/）。 
            - successive_slashes：表示将请求 URL 中连续斜杠（//）替换为单个斜杠（/）。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： OriginCertCheck
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        CertInfoList ( Array of CertInfoList ): 表示一个 CA 证书列表。列表中的证书不能是国密证书，证书来源可以是 CDN 托管或者火山引擎证书中心。CDN 使用该列表中的证书对来自源站的服务器证书进行校验。 
        ClientCertInfoList ( Array of ClientCertInfoList ): 仅当 Type 为 mutual 时，该参数有效。 
            该参数表示一个客户端证书列表。列表中的证书不能是国密证书，证书来源可以是 CDN 托管或者火山引擎证书中心。源站使用该列表中的证书对 CDN 身份进行校验。 
        Type ( String ): 表示校验类型，有以下取值： 
            * unilateral：表示单向认证。 
            * mutual：表示双向认证。 
       "字段"： ConditionalOrigin
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginRules ( Array of OriginRules ): 表示一个规则列表。列表中的每条规则中定义了一组匹配条件以及 CDN 对满足匹配条件的请求所执行的操作。 
            当收到一个用户请求时，CDN 按规则的优先级，从高到低将规则与请求匹配。如果一条规则匹配了请求，CDN 就停止处理其余规则。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： OriginRetry
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        StatusCode ( String ): 表示范围在 400-599 之间的一个或者多个状态码。状态码可以是 4xx 或者 5xx，表示所有以数字 4 或 数字 5 开头的状态码。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： RewriteHLS
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        SignName ( String ): 表示签名参数的名称。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： MultiRange
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            * true：表示启用该特性。该特性启用后，CDN 允许指定了多重范围的 Range 请求。 
            * false：表示不启用该特性。如果收到一个指定了多重范围的 Range 请求，CDN 会拒绝该请求并返回 416 响应状态码。 
       "字段"： OfflineCache
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Object ( String ): 表示该特性的触发条件，该参数有以下取值： 
            - request_error：表示回源请求异常。当回源请求出现异常时，CDN 无法从源站获取文件，并且 CDN 没有获得任何来自源站的响应状态码。 
            - error_code：表示 CDN 无法从源站获取文件，并且源站的响应状态码是 5xx。 
            - request_error,error_code：表示以上两个条件都包含。 
        StatusCode ( String ): 表示一个或者多个响应状态码。 
            当 Object 是 error_code 或者 request_error,error_code 时，该参数才有效。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： OriginResponseHeader
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginResponseHeaderAction ( Object of OriginResponseHeaderAction ): 表示 CDN 在收到源站响应时，对响应头的操作。 
       "字段"： Range
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        RangeSize ( Long ): 表示分片的大小。 
        Switch ( Boolean ): 表示是否启用该设置。该参数有以下取值： 
            * true：表示启用该设置。 
            * false：表示禁用该设置。 
        Unit ( String ): 表示 RangeSize 的单位。该参数有以下取值： 
            * KB 
            * MB 
       "字段"： OriginAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginLines ( Array of OriginLines ): 表示一个源站列表。列表中最多可以包含 50 个源站。 
       "字段"： CacheAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示浏览器需要执行的操作。该参数值始终是 cache，表示缓存请求的文件。DefaultPolicy 中指定了如何缓存请求的文件。 
        IgnoreCase ( Boolean ): 表示 Value 是否是大小写敏感的。 
            - true：表示大小写不敏感。 
            - false：表示大小写敏感。 
        Ttl ( Long ): 表示浏览器需要缓存请求文件的时长，单位是秒。CDN 会在响应头中包含 Cache-Control: max-age 头部，头部值就是该参数值。 
        DefaultPolicy ( String ): 表示浏览器该如何缓存请求的文件。该参数有以下取值： 
            - cache：表示需要缓存请求的文件。 
            - origin_first：表示遵循来自源站的缓存策略。该策略会包含在 CDN 的响应中。 
            - no_cache：表示不需要缓存请求的文件。 
            关于浏览器缓存策略的详细信息，参见 浏览器缓存策略。 
       "字段"： Condition
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        ConditionRule ( Array of ConditionRule ): 表示匹配条件列表。 
       "字段"： CacheHostRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheHostAction ( Object of CacheHostAction ): 表示配置的详情。 
       "字段"： CacheKeyAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheKeyComponents ( Array of CacheKeyComponents ): 缓存键是由请求中的 host、路径和查询字符串等部分组成。该参数表示其中各组成部分的配置。 
       "字段"： CompressionRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CompressionAction ( Object of CompressionAction ): 表示当用户请求满足 Condition 时，CDN 对请求文件执行的压缩操作的配置。 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 CompressionAction 中指定的操作。 
            需要留意的是，如果 CompressionFormat 指定了，Condition 的值为 null 或者不指定。 
       "字段"： ErrorPageRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        ErrorPageAction ( Object of ErrorPageAction ): 表示规则的相关配置。 
       "字段"： CustomizeInstances
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CustomizeRule ( Object of CustomizeRule ): 表示列表中一条规则的配置。 
       "字段"： DownloadSpeedLimitRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        DownloadSpeedLimitAction ( Object of DownloadSpeedLimitAction ): 表示限速配置。 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果请求匹配了某个条件，CDN 对该请求执行 DownloadSpeedLimitAction 中指定的操作。 
            如果不指定该参数，CDN 对所有请求执行 DownloadSpeedLimitAction 中指定的操作。 
       "字段"： CertInfo
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CertId ( String ): 表示要关联的证书 ID。 
        Certificate ( Object of Certificate ): 表示一个待上传的证书。上传后的证书是托管在 CDN 的。 
       "字段"： CertInfoList
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CertId ( String ): 表示双证书中的一本证书的 ID。 
       "字段"： ForcedRedirect
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        EnableForcedRedirect ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。启用后，CDN 会将收到的 HTTP 请求重定向到 HTTPS 请求。 
            - false：表示禁用该特性。禁用后，CDN 不会将 HTTP 请求重定向到 HTTPS 请求。 
        StatusCode ( String ): 表示当收到 HTTPS 请求时 CDN 的重定向响应状态码。该参数有以下取值：301、302、303、307、308。 
            需要留意的是： 
            * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。 
            * 对于 303，新请求使用的方法是 GET。 
            * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。 
       "字段"： Hsts
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Subdomain ( String ): 表示 HSTS 配置是否也应用于加速域名的子域名。该参数有以下取值： 
            - include：表示 HSTS 配置应用于子域名站点。 
            - exclude：表示 HSTS 配置不应用于子域名站点。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
        Ttl ( Long ): 表示 Strict-Transport-Security 响应头在浏览器中的缓存过期时间，单位是秒。如果该参数值为 0，其效果等同于禁用 HSTS 设置。 
       "字段"： CertCheck
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CertInfoList ( Array of CertInfoList ): 表示与加速域名关联的一个 CA 证书列表。列表中的 CA 证书托管在 CDN。CA 证书使用的加密算法可以是 RSA、ECC 或者 SM2。 
        Switch ( Boolean ): 表示是否启用该特性。该参数有以下取值： 
            - true：表示启用该特性。 
            - false：表示禁用该特性。 
       "字段"： SharedConfig
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        ConfigName ( String ): 表示一个全局配置的名称。该全局配置的 ConfigType 是 deny_ip_access_rule 或者 allow_ip_access_rule。 
            - deny_ip_access_rule：表示 IP 黑名单。 
            - allow_ip_access_rule：表示 IP 白名单。 
       "字段"： IpSource
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        SourceList ( Array of String ): 表示携带客户端 IP 地址的头部列表，有以下取值： 
            * x-forwarded-for  
            * x-real-ip 
        Type ( String ): 表示客户端 IP 地址的获取方式。该参数有以下取值： 
            * default：表示采用常规方式获取 IP 地址，也就是通过协议层获取 IP 地址。 
            * custom：表示从 SourceList 指定的头部中获取 IP 地址。但如果指定的头部不存在或者值为空，则采用常规方式获取 IP 地址。 
       "字段"： NegativeCacheRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示 CDN 执行的操作。该参数值始终是 cache，表示缓存源站的响应状态码。 
        StatusCode ( String ): 指定一个需要缓存的状态码，可以是 4xx 或者 5xx。4xx 表示 400 到 499 之间的所有状态码。5xx 表示 500 到 599 之间的所有状态码。 
        Ttl ( Long ): 表示状态码的缓存时间。单位是秒。 
        IgnoreCase ( Boolean ): 表示 Value 是否是大小写敏感的。 
            - true：表示大小写不敏感。 
            - false：表示大小写敏感。 
       "字段"： OriginArgAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginArgComponents ( Array of OriginArgComponents ): 表示一个操作列表。这些操作定义了 CDN 如何处理回源请求中的查询参数。 
       "字段"： OriginRewriteRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginRewriteAction ( Object of OriginRewriteAction ): 表示 CDN 执行的动作。 
       "字段"： RedirectionRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        RedirectionAction ( Object of RedirectionAction ): 表示一个 URL 重定向改写的规则。 
       "字段"： ReferersType
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CommonType ( Object of CommonType ): 表示一个 CommonType 对象，其包含一个常规 Referer 列表。 
        RegularType ( Object of RegularType ): 表示一个 RegularType 对象，其包含一个正则表达式列表用来匹配请求中的 Referer 头部。 
       "字段"： RemoteAuthRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Condition ( Object of Condition ): 表示匹配条件的配置。如果一个请求满足匹配条件，CDN 对该请求执行 RemoteAuthRuleAction 中指定的操作。 
        RemoteAuthRuleAction ( Object of RemoteAuthRuleAction ): 表示鉴权相关的配置。 
            当一个请求满足 Condition 中的匹配条件时，CDN 会将其发送至鉴权服务器进行鉴权，并基于鉴权的结果接受或者拒绝该请求。 
       "字段"： RequestHeaderAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        RequestHeaderInstances ( Array of RequestHeaderInstances ): 表示一个请求头的配置规则列表。每个规则都包含一个头部的相关操作设置。 
       "字段"： ResponseHeaderAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        ResponseHeaderInstances ( Array of ResponseHeaderInstances ): 表示一个响应头的配置规则列表。每个规则都包含一个头部的相关操作设置。 
       "字段"： SignedUrlAuthRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Condition ( Object of Condition ): 表示匹配条件的配置。CDN 对符合条件的用户请求进行鉴权。 
        SignedUrlAuthAction ( Object of SignedUrlAuthAction ): 表示签名计算的配置。 
       "字段"： TimeoutRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        TimeoutAction ( Object of TimeoutAction ): 表示超时时间的配置。 
       "字段"： BlockRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        BlockAction ( Object of BlockAction ): 表示一条规则中 CDN 行为的配置。 
        Condition ( Object of Condition ): 表示该规则中匹配条件的定义。 
        RuleName ( String ): 表示规则的名称。 
       "字段"： ClientCertInfoList
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CertId ( String ): 表示列表中一本客户端证书的 ID，以 cert_hosting 开头。 
       "字段"： OriginRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Actions ( Object of Actions ): 表示一条规则中定义的操作配置。 
        Condition ( Object of Condition ): 表示该规则中匹配条件的配置。 
       "字段"： OriginResponseHeaderAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginResponseHeaderInstances ( Array of OriginResponseHeaderInstances ): 表示一个响应头的配置规则列表。每个规则都包含一个头部的相关操作设置。 
       "字段"： OriginLines
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Address ( String ): 表示列表中一个源站的地址。 
        InstanceType ( String ): 表示源站的类型。该参数有以下取值： 
            - ip：表示 IP 地址。 
            - domain：表示域名。 
            - tos：表示对象存储桶。 
        OriginType ( String ): 表示源站的类别。该参数有以下取值： 
            - primary：表示主源站。 
            - backup：表示备源站。 
        HttpPort ( String ): 表示 CDN 使用 HTTP 协议访问该源站时所访问的端口。 
        HttpsPort ( String ): 表示 CDN 使用 HTTPS 协议访问该源站时所访问的端口。 
        OriginHost ( String ): 表示回源请求访问的站点域名，适用于源站服务器上有多个站点的情况。该参数的优先级高于全局 OriginHost 参数。 
        PrivateBucketAccess ( Boolean ): 表示存储桶是否是私有桶。该参数有以下取值： 
            - true：表示该存储桶是私有桶。 
            - false：表示该存储桶不是私有桶。 
        PrivateBucketAuth ( Object of PrivateBucketAuth ): 表示访问存储桶的凭据。 
        Region ( String ): 表示存储桶所在地域的信息，也就是存储桶的 region code。Region code 参与签名的计算。 
        Weight ( String ): 表示该源站的权重。权重越大，该源站在 CDN 发送回源请求时被选择到的概率也越大。 
       "字段"： ConditionRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Object ( String ): 表示匹配对象。该参数有以下取值： 
            - filetype：表示请求 URL 中的扩展名。 
            - directory：表示请求 URL 中的某个目录。 
            - path：表示请求 URL 中的完整路径。 
            - regex：表示请求 URL 中的路径，通过正则表达式匹配。 
        Operator ( String ): 表示匹配类型。该参数的值始终是 match，表示如果 Value 匹配了请求中的 Object，该请求就满足这个匹配条件。 
        Type ( String ): 该参数值始终是 url，表示 "请求 URL"。 
        Value ( String ): 表示一个或者多个匹配值。 
       "字段"： CacheHostAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheHost ( String ): 表示目标域名。 该目标域名是您账户下的一个加速域名。该参数指示 Domain 共享 CacheHost 的 CDN 缓存。 
       "字段"： CacheKeyComponents
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示 CDN 如何在请求文件的缓存键中设置查询字符串。该参数有以下取值： 
            - exclude：表示缓存键不包含请求中的任何查询参数。 
            - include：表示缓存键包含请求中所有的查询参数。 
            - includePart：表示缓存键仅包含 Subobject 中指定的查询参数。 
            - excludePart：表示缓存键包含请求中除了 Subobject 中指定的查询参数之外的所有查询参数。 
        IgnoreCase ( Boolean ): 表示 Subobject 是否是大小写敏感的。该参数有以下取值： 
            - true：表示大小写不敏感。 
            - false：表示大小写敏感。 
        Object ( String ): 表示缓存键中的一个组成部分。该参数值始终是 querystring，表示查询字符串。 
        Subobject ( String ): 该参数对应于 Action，表示 CDN 在缓存键中包含的具体查询参数。该参数的说明如下： 
            - 如果 Action 是 include 或者 exclude，Subobject 的值是 *，表示请求中的全部查询参数。 
            - 如果 Action 是 includePart 或者 excludePart，Subobject 表示需要保留或者不保留的查询参数。 
       "字段"： CompressionAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CompressionType ( Array of String ): 表示 CDN 使用的压缩算法。该参数有以下取值： 
            - br：表示 Brotli 压缩算法。 
            - gzip：表示 Gzip 压缩算法。 
            需要留意的是，CDN 基于用户请求中 Accept-Encoding 头部来决定是否对请求文件进行压缩以及使用的压缩算法。 
        CompressionFormat ( String ): 表示 CDN 基于请求中的 Content-Type 头部对请求进行匹配。该参数有以下取值： 
            * default：表示如果 Content-Type 头部值在下方的默认列表中，CDN 对请求文件执行 CompressionAction 中配置的操作。 
            * customize：表示如果 Content-Type 头部值在 CompressionFormat 指定的头部值中，CDN 对请求文件执行 CompressionAction 中配置的操作。 
            如果该参数未指定或者值为 all，表示 CDN 基于 Condition 中的匹配条件对请求进行匹配。 
            默认列表 
            text/html、text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、text/javascript、image/tiff、image/svg+xml、application/json、application/xml、text/plain; charset=utf-8 
        CompressionTarget ( String ): 表示 Content-Type 的过滤值。 
            - 如果 CompressionFormat 为 default 或者 all，该参数为 *。 
            - 如果 CompressionFormat 为 customize，该参数表示一个或者多个文件类型。 
        MinFileSizeKB ( Long ): 表示文件大小范围的最小值，CDN 仅对大小在 MinFileSizeKB 和 MaxFileSizeKB 所表示的范围内的文件进行压缩。该参数的单位是 KB，使用的进制是 1,024。 
        MaxFileSizeKB ( Long ): 表示文件大小范围的最大值，单位是 KB，使用的进制是 1,024。如果该参数不指定，表示不限制文件大小的上限。 
       "字段"： ErrorPageAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示实际的操作。该参数值始终为 redirect。表示对客户端请求进行重定向。 
        RedirectCode ( String ): 表示重定向的响应状态码。该参数的取值有 301、302、303、307、308。 
            需要留意的是： 
            * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。 
            * 对于 303，新请求使用的方法是 GET。 
            * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。 
        RedirectUrl ( String ): 表示跳转的目标地址。 
        StatusCode ( String ): 表示一个状态码，状态码可以是 4xx 或者 5xx。4xx 表示 400-499 之间的所有状态码。5xx 表示 500-599 之间的所有状态码。 
       "字段"： CustomizeRule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AccessAction ( Object of AccessAction ): 表示该规则中的黑名单或者白名单的配置。 
       "字段"： DownloadSpeedLimitAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        SpeedLimitRate ( Long ): 表示 CDN 在响应单个请求时的数据传输速度阈值，单位是 B/S，使用的进制是 1,024。 
            当 LimitType 是 dynamic_limit 时，CDN 优先从 LimitQueryName 所指定的查询参数中获取速度阈值。如果该查询参数不存在或者值为空，则 CDN 使用 SpeedLimitRate 作为速度阈值。 
        SpeedLimitRateAfter ( Long ): 表示一个初始数据量，单位是 bytes，使用的进制是 1,024。 
            当 CDN 对一个请求开始传输数据时，在传输的数据量达到该初始数据量前，该限速规则不会启用。 
            如果该参数值是 0，表示在 CDN 对一个请求开始传输第一个字节时，该限速规则就启用了。 
        SpeedLimitTime ( Object of SpeedLimitTime ): 表示限速规则启用的日期和时间段。 
        DynamicLimitUnit ( String ): 当 LimitType 是 dynamic_limit 时，该参数有效，表示速度的单位。该参数有以下取值： 
            * B/S 
            * KB/S 
            * MB/S 
        LimitQueryName ( String ): 当 LimitType 是 dynamic_limit 时，该参数有效，表示指定的查询参数名称。 
        LimitType ( String ): 表示如何设置数据传输速度的阈值。该参数有以下取值： 
            * normal：表示阈值是固定的，在 SpeedLimitRate 中指定。 
            * dynamic_limit：表示从 LimitQueryName 所指定的查询参数中获取阈值。 
       "字段"： Certificate
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Certificate ( String ): 表示证书文件的内容。 
        PrivateKey ( String ): 表示私钥文件的内容。 
        EncryptionCert ( String ): 表示国密证书的证书文件的内容，用于加密。 
        EncryptionKey ( String ): 表示国密证书的私钥文件的内容，用于解密。 
       "字段"： OriginArgComponents
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示 CDN 执行的操作。该参数有以下取值： 
            - include: 表示回源请求 URL 中包含用户请求 URL 中的全部查询参数。 
            - exclude：表示回源请求 URL 中不包含用户请求 URL 中的任何查询参数。 
            - addPart：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数，并额外包含 Subobject 中指定的查询参数。 
            - includePart：表示如果用户请求 URL 中包含 Subobject 中指定的查询参数，那么回源请求 URL 中包含这些指定的查询参数。 
            - excludePart：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数，除了Subobject 中指定的查询参数。 
            - set：表示回源请求 URL 中包含用户请求 URL 中的全部查询参数。同时，对于您在 Subobject 中指定的查询参数和参数值，CDN 会执行以下操作: 
              - 如果这些查询参数在用户请求 URL 中，CDN 会在回源请求 URL 中将这些参数的值设置为您指定的值。 
              - 如果用户请求 URL 中不包含这些查询参数，CDN 会在回源请求 URL 中添加这些查询参数。 
        Object ( String ): 表示 CDN 对哪个对象执行 Action。该参数值始终是 queryString，表示请求 URL 中的查询字符串。 
        Subobject ( String ): 表示一个或者多个查询参数。 
            在匹配请求 URL 中的查询参数时，Subobject 中的参数是大小写敏感的。 
            Subobject 的额外说明如下： 
            * 当 Action 是  include 或 exclude 时，Subobject 是 *，表示请求 URL 中的所有查询参数。 
            * 当 Action 是  includePart 或 excludePart 时，Subobject 表示一个或者多个查询参数。例如 param1;param2。 
            * 当 Action 是  addPart 或 set 时，Subobject 表示一个或者多个查询参数和参数值，格式是 key=value。例如 param1=val1;param2=val2;param3=val3。 
       "字段"： OriginRewriteAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        SourcePath ( String ): 表示一个正则表达式，用于匹配用户请求 URL 中的对象。 
            * 当 RewriteType 是 rewrite_path 时，该对象指的是请求 URL 中的路径。 
            * 当 RewriteType 是 rewrite_url 时，该对象指的是请求 URL 中的路径和查询字符串。 
            参见 配置示例。 
        TargetPath ( String ): 表示改写后，回源请求 URL 中的对象。 
            * 当 RewriteType 是 rewrite_path 时，该对象是回源请求 URL 中的路径。 
            * 当 RewriteType 是 rewrite_url 时，该对象是回源请求 URL 中的路径和查询字符串。 
            TargetPath 中的 $1、$2、$3 等用于捕获 SourcePath 中定义的组。 
            参见 配置示例。 
        RewriteType ( String ): 表示改写类型。该参数有以下取值： 
            * rewrite_path：表示对请求 URL 中的路径进行改写。 
            * rewrite_url：表示对请求 URL 中的路径和查询字符串进行改写。 
       "字段"： RedirectionAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        RedirectCode ( String ): 表示 URL 重定向的响应状态码。该参数的取值有 301、302、303、307、308。 
            需要留意的是： 
            * 对于 301 和 302，如果原请求使用的方法不是 GET，那么客户端向新的URL发送请求时，新请求使用的方法可能变成 GET。 
            * 对于 303，新请求使用的方法是 GET。 
            * 对于 307 和 308，新请求使用的方法与原请求相同，不会被改变。 
        SourcePath ( String ): 表示文件的原路径。也就是请求中包含的路径。 
        TargetHost ( String ): 表示目标路径所归属站点的域名或者 IP 地址。 
        TargetPath ( String ): 表示跳转后的目标路径。 
        TargetProtocol ( String ): 表示 URL重定向后的新请求所使用的协议。该参数有以下取值： 
            - followclient：表示使用原请求的协议。 
            - http：表示新请求强制使用 HTTP 协议。 
            - https：表示新请求强制使用 HTTPS 协议。 
        TargetQueryComponents ( Object of TargetQueryComponents ): 表示原请求 URL 中的查询参数的处理方式。 
       "字段"： CommonType
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        IgnoreCase ( Boolean ): 表示 CommonType 下的 Referers 列表是否是大小写敏感的。该参数有以下取值： 
            - true: 表示大小写不敏感。 
            - false: 表示大小写敏感。 
        Referers ( Array of String ): 表示一个常规 Referer 列表， 
        IgnoreScheme ( Boolean ): 表示是否校验请求中 Referer 头部的 scheme，也就是校验 Referer 是否包含 http:// 或者 https://。该参数有以下取值： 
            - true: 表示不校验 Referer 是否包含 scheme。在这个情况下，无论请求中的 Referer 是否包含 scheme，CDN 都会将 Referer 与您配置的名单进行匹配。 
            - false: 表示 CDN 会先校验 Referer 是否包含 scheme。如果 Referer 不包含 scheme，CDN 判定请求与您配置的名单不匹配。 
            该配置对 RegularType 下的 Referers 列表不生效，因为 CDN 依赖正则表达式来判断 Referer 是否匹配正则名单。 
        ContMainDomain ( Boolean ): 如果 CommonType 下 Referers 列表中包含泛域名，该参数表示泛域名是否可以匹配主域名。该参数有以下取值： 
            * true：表示泛域名可以匹配主域名。 
            * false：表示泛域名不匹配主域名。 
            示例 
            Referers 是一个黑名单，包含 *.example.com。对于来自 example.com 的请求， 
            * 如果 ContMainDomain 为 true，则该请求匹配 Referers。 
            * 如果 ContMainDomain 为 false，则该请求不匹配 Referers。 
       "字段"： RegularType
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Referers ( Array of String ): 表示一个用于匹配 Referer 的正则表达式列表。 
       "字段"： RemoteAuthRuleAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AuthModeConfig ( Object of AuthModeConfig ): 表示鉴权服务器的配置。 
        AuthResponseConfig ( Object of AuthResponseConfig ): CDN 需要对鉴权服务器返回的鉴权状态码进行处理。该参数表示相关的配置。 
        QueryStringRules ( Object of QueryStringRules ): 表示鉴权请求的参数设置。 
        RequestBodyRules ( String ): 表示鉴权请求正文的规则。如果该参数值为 default，表示请求正文为空（""）。 
        RequestHeaderRules ( Object of RequestHeaderRules ): 表示鉴权请求头的设置。 
       "字段"： RequestHeaderInstances
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示对请求头的操作。该参数有以下取值： 
            - set：表示设置一个头部。设置操作包括添加与修改。如果请求中已包含该头部，该头部的值会被覆盖。如果请求中没有包含该头部，该头部会被添加。 
            - delete，表示删除一个头部。 
        Key ( String ): 表示一个头部的名称。 
        ValueType ( String ): 表示 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值： 
            - constant：表示 Key 的值是一个固定字符串。 
            - variable：表示 Key 的值来自一个变量。 
            - customize：表示 Key 的值是变量与固定字符串拼接后的一个字符串。 
        Value ( String ): 表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。 
       "字段"： ResponseHeaderInstances
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示对响应头的操作。该参数有以下取值： 
            - set：表示设置一个头部。设置操作包括添加与修改。如果源站响应中已包含该头部，该头部的值会被覆盖。如果源站响应中没有包含该头部，该头部会被添加。 
            - delete，表示删除一个头部。 
        Key ( String ): 表示一个头部的名称。 
        ValueType ( String ): 表示 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值： 
            - constant：表示 Key 的值是一个字符串。 
            - variable：表示 Key 的值来自一个变量。 
            - customize：表示 Key 的值是一个变量与字符串拼接后的字符串。 
        AccessOriginControl ( Boolean ): 表示在 CDN 响应用户请求时，是否校验请求中的 Origin 头部。 
            该参数有以下取值： 
            - true：表示 CDN 会校验 Origin 头部。如果校验成功，CDN 会在响应中包含 Access-Control-Allow-Origin 头部。头部值与 Origin 头部值相同。如果校验失败，响应中不会包含 Access-Control-Allow-Origin 头部。 
            - false：表示 CDN 不会校验 Origin 头部。在响应中，CDN 会包含 Access-Control-Allow-Origin 头部。头部值是您配置的 Access-Control-Allow-Origin 的内容。 
            该参数仅在以下条件都满足的情况下有效： 
            - Action 是 set。 
            - Key 是 Access-Control-Allow-Origin。 
            - ValueType 是 constant。 
        Value ( String ): 表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。 
       "字段"： SignedUrlAuthAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Duration ( Long ): 表示签名的有效时间，单位是秒。该参数与请求中包含时间戳搭配使用，用来计算签名的过期时间。签名的过期时间 = 时间戳 + Duration。在 CDN 收到某个请求时，如果签名的过期时间小于当前时间，CDN 判定签名已过期。 
        MasterSecretKey ( String ): 表示主密钥， 
        URLAuthType ( String ): 表示签名类型。该参数有以下取值：typea、typeb、typec、typed、typee，每种类型得鉴权说明见 配置 URL 鉴权 。 
        BackupSecretKey ( String ): 表示备密钥。 
        CustomVariableRules ( Object of CustomVariableRules ): 表示自定义签算变量，仅当 URLAuthType 为 typee 时有效。 
        KeepOriginArg ( Boolean ): 表示 CDN 是否在回源请求中包含用户请求中的签名参数。仅当 URLAuthType 是 typea 或 typed 时，该参数有效。 
            该参数有以下取值： 
            * true：表示 CDN 在回源请求中包含签名参数。 
            * false：表示 CDN 在回源请求中不包含签名参数。 
        RewriteM3u8 ( Boolean ): 对于 HLS Manifest (.m3u8) 的请求，该参数表示 CDN 是否要修改 Manifest，从而为每个视频分片生成签名并将签名添加到 URI 中。 
            该参数有以下取值： 
            - true：表示需要修改 Manifest。 
            - false：表示不需要修改 Manifest。 
            当前，CDN 不会修改压缩文件。因此，在以下任何情况下，CDN 都不会修改 Manifest。 
            * 源站响应中包含 Content-Encoding 头部。该标头表明该 Manifest 已被压缩。 
            * 用户请求匹配 "智能压缩" 特性中的规则。 
        SignName ( String ): 表示签名参数的名称。 
            当 URLAuthType 为 typeb、typec 时，该参数不生效。 
        SignatureRule ( Array of String ): 当 URLAuthType 为 typee 时，该参数有效，表示需要纳入签名计算的字段。 
            必须纳入的字段如下： 
            - key：表示MasterSecretKey或 BackupSecretKey 参数的值。 
            - uri：表示用户请求资源的 URI。 
            - TimeName：表示 TimeFormat 参数的值。 
            可选择纳入签名计算的字段如下： 
            - domain：表示加速域名。 
            - referer：表示用户请求携带的 referer 值。 
            - ua：表示用户请求携带的 User-Agent 值。 
            - ip：表示用户请求的客户端 IP。 
            - origin：表示用户请求携带的 Origin 值。 
            - 自定义变量：表示 CustomVariableInstances 中定义的变量名称。 
            CDN 按列表中字段出现顺序将这些字段拼接成一个字符串，然后计算该字符串的 MD5 值。该 MD5 值就是签名。 
        TimeFormat ( String ): 表示 TimeName 使用的进制。该参数有以下取值： 
            - decimal：十进制。 
            - heximal：十六进制。 
            当 URLAuthType 为 typed、typee 时，该参数有效。当 URLAuthType 为 typec 时，无论该参数是否设置，该参数的值会被强制设置为 heximal。对于 URLAuthType 的其他值，该参数不生效。 
        TimeName ( String ): 表示时间戳参数的名称。 
            当 URLAuthType 为 typed、typee 时，该参数有效。对于其他类型，该参数不生效。 
        RewriteM3u8Rule ( Object of RewriteM3u8Rule ): 表示 "M3U8 改写" 功能的配置。该配置仅当 RewriteM3u8 是 true 时才有效。 
        AuthAlgorithm ( String ): 表示签名计算使用的算法。该配置有以下取值： 
            - md5：表示 MD5 算法。 
            - sha256：表示 SHA-256 算法。 
        DeleteAuthCacheAndOrigin ( Boolean ): 表示 CDN 是否在回源请求和缓存键中包含用户请求中的签名参数，仅当 URLAuthType 是 typee 时有效。 
            该参数有以下取值： 
            * true：表示回源请求和缓存键中均不包含签名参数。 
            * false：表示回源请求和缓存键中均包含签名参数。 
       "字段"： TimeoutAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        HttpTimeout ( Long ): 表示 HTTP 请求的超时时间，单位是秒。 
        TcpTimeout ( Long ): 表示 TCP 请求的超时时间，单位是秒。 
       "字段"： BlockAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示 CDN 如何处理匹配 Condition 的请求。该参数有以下取值： 
            - refuse：表示 CDN 拒绝请求并响应一个 4xx 的错误码。错误码在 StatusCode 中指定。 
            - redirect：表示 CDN 将请求重定向到 RedirectUrl 中指定的 URL。 
        StatusCode ( String ): 表示对于匹配 Condition 的用户请求，CDN 的响应状态码。 
        ErrorPage ( String ): - 当 Action 是 refuse 时，该参数的说明如下： 
            	- 该参数表示 "全局配置" 特性中的一个自定义响应页面的名称。也就是说，当 CDN 拒绝请求时，返回该自定义页面。 
            	- 如果该参数未指定，表示 CDN 使用 StatusCode 中指定错误码的标准响应正文。 
            - 当 Action 是 redirect 时，该参数无效。 
        RedirectUrl ( String ): - 当 Action 是 redirect 时，该参数表示重定向 URL。 
            - 当 Action 是 refuse 时，该参数无效。 
       "字段"： Actions
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        OriginLines ( Array of OriginLines ): 表示一个源站配置列表。 
       "字段"： OriginResponseHeaderInstances
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示 CDN 对响应头的操作。该参数有以下取值： 
            - set：表示设置一个头部。设置操作包括添加与修改。如果源站响应中已包含该头部，该头部的值会被覆盖。如果源站响应中没有包含该头部，该头部会被添加。 
            - delete：表示删除一个头部。 
        Key ( String ): 表示一个头部的名称。 
            参见 常用头部。 
        Value ( String ): 表示 Key 的值。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。 
        ValueType ( String ): 表示 Key 的取值类型。该参数仅当 Action 是 set 的时候才有效。如果 Action 不是 set，该参数无效。该参数有以下取值： 
            - constant：表示 Key 的值是一个固定字符串。 
            - variable：表示 Key 的值来自一个变量。 
            - customize：表示 Key 的值是一个变量与固定字符串拼接后的字符串。 
        Object ( String ): 表示该规则对哪些用户请求生效。该参数有以下取值： 
            - default：表示该规则仅对源站响应中包含以下响应码的用户请求生效： 
            	- 200、201、204、206、301、302、303、304、307、308 
            - all_request：表示该规则对所有用户请求生效。 
       "字段"： PrivateBucketAuth
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 该参数值是 true。 
        AuthType ( String ): 表示存储桶使用的是哪个对象存储服务所提供的鉴权方式。该参数有以下取值： 
            - tos：表示火山引擎 TOS。 
            - cos：表示腾讯云 COS。 
            - oss：表示阿里云 OSS。 
            - aws：表示 AWS S3。该取值用于兼容存量配置。 
            - aws_common：表示 AWS S3 和 S3 兼容的鉴权方式。 
        TosAuthInformation ( Object of TosAuthInformation ): 表示存储桶的访问凭证（AccessKey）。 
            当 AuthType 是 tos 时： 
            * 如果您指定了 TosAuthInformation，CDN 使用 AccessKey 访问存储桶。 
            * 如果 TosAuthInformation 未指定，CDN 使用跨服务授权方式访问存储桶。 
       "字段"： AccessAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AllowEmpty ( Boolean ): 表示当用户请求不包含指定头部时，CDN 处理请求的方式。该参数有以下取值： 
            - true：表示如果请求不包含指定头部，则该请求被认为匹配您配置的头部值列表。 
            - false：表示如果请求不包含指定头部，则该请求被认为不匹配您配置的头部值列表。 
        ListRules ( Array of String ): 表示一个正则表达式列表，用于匹配请求头的值。 
            列表中正则表达式之间的关系是或。也就是说，如果一个用户请求中 RequestHeader 的值匹配任何一个正则表达式，该规则就匹配了这个请求。 
        RequestHeader ( String ): 表示一个指定的请求头。头部名称不区分大小写。 
        RuleType ( String ): 表示名单的类型。该参数有以下取值： 
            - allow：表示该规则中定义的是一个白名单。如果一个用户请求不匹配白名单，CDN 会拒绝该请求，响应 403 状态码。 
            - deny：表示该规则中定义的是一个黑名单。如果一个用户请求匹配了黑名单，CDN 会拒绝该请求，响应 403 状态码。 
       "字段"： SpeedLimitTime
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        DayWeek ( String ): 表示该限速规则启用的日期，有以下取值：monday，tuesday，wednesday，thursday，friday，saturday，sunday，unlimited。unlimited 表示每天。 
            您可以指定一个或多个日期，多个日期之间使用分号（;）分隔。 
        BeginTime ( String ): 表示该限速规则启用的开始时间，格式是 mm:ss。 
            如果 DayWeek 是 unlimited, BeginTime 为 00:00。 
        EndTime ( String ): 表示该限速规则启用的结束时间，格式是 mm:ss。 
            如果 DayWeek 是 unlimited, EndTime 为 23:59。 
       "字段"： TargetQueryComponents
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示原请求 URL 中的查询参数的处理方式。该参数有以下取值： 
            - include：表示在跳转后的 URL 中包含原请求 URL 中的所有查询参数。 
            - exclude：表示在跳转后的 URL 中不包含原请求 URL 中的任何查询参数。 
            - includePart：表示在跳转后的 URL 中包含原请求 URL 中特定的查询参数。 
            - excludePart：表示在跳转后的 URL 中不包含原请求 URL 中特定的查询参数。 
        Value ( String ): 表示要保留或删除的查询参数。 
            如果 Action 是 include 或者 exclude, 则 Value 为 *，表示所有的查询参数。 
       "字段"： AuthModeConfig
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        MasterRemoteAddr ( String ): 表示鉴权服务器的主地址。 
        PathType ( String ): 表示鉴权请求的路径。鉴权地址和请求路径组成了完整的鉴权 URL。CDN 会把用户的请求转发到该鉴权 URL。该参数有以下取值： 
            - constant：表示鉴权请求中的路径与用户请求中的路径相同。 
            - variable：表示鉴权请求中的路径在 pathValue 参数中指定。 
        RequestMethod ( String ): 表示在发送鉴权请求时，CDN 所使用的请求方法。该参数有以下取值： 
            - default：表示鉴权请求所使用的方法与用户的请求相同。 
            - get：表示鉴权请求使用 GET 方法。 
            - post：表示鉴权请求使用 POST方法。 
            - head：表示鉴权请求使用 HEAD 方法。 
        BackupRemoteAddr ( String ): 表示鉴权服务器的备地址。 
        PathValue ( String ): 表示鉴权请求的路径. 
       "字段"： AuthResponseConfig
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CacheAction ( Object of CacheAction ): CDN 可以缓存鉴权状态码。该参数表示相关的配置。 
        ResponseAction ( Object of ResponseAction ): 表示鉴权失败时，CDN 如何响应用户。 
        StatusCodeAction ( Object of StatusCodeAction ): 表示 CDN 对鉴权状态码的处理方式。 
        TimeOutAction ( Object of TimeOutAction ): 表示鉴权超时后，CDN 如何处理鉴权请求。 
       "字段"： QueryStringRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        QueryStringComponents ( Object of QueryStringComponents ): 表示鉴权请求参数的设置策略。 
        QueryStringInstances ( Array of QueryStringInstances ): 表示鉴权请求中额外的参数设置。 
       "字段"： RequestHeaderRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        RequestHeaderComponents ( Object of RequestHeaderComponents ): 表示鉴权请求头的设置策略。 
        RequestHeaderInstances ( Array of RequestHeaderInstances ): 表示一组鉴权请求头的设置。 
            需要留意的是，在 CDN 发起鉴权请求时，请求中可能已经包含了以下头部： 
            - X-Forwarded-Protocol，X-Forwarded-Proto，X-Client-Scheme：这三个头部都表示用户请求所使用协议，没有区别。 
            - X-Real-IP：表示用户真实的 IP 地址。该头部的值不会受代理服务器的影响。 
            - X-Forwarded-For：表示用户的 IP 地址。如果用户的请求经过了代理服务器，该头部的值会变成代理服务器的 IP 地址。 
            如果该参数中设置了这些头部，这些头部的原始值会被覆盖。 
        RequestHost ( String ): 表示鉴权请求中 HOST 头部的值。如果该参数的值是 default，表示 HOST 头部的值与您的加速域名相同。 
       "字段"： CustomVariableRules
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        CustomVariableInstances ( Array of CustomVariableInstances ): 表示一个变量列表。 
       "字段"： RewriteM3u8Rule
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        DeleteParam ( Boolean ): 表示在改写分片 URI 时是否保留 URL 中原有的参数。该参数有以下取值： 
            - true：表示删除原有参数。 
            - false：表示保留原有参数。 
            需要留意的是，该参数的设置影响签名的计算。参见 M3U8 改写功能的字段描述。 
        KeepM3u8Param ( Boolean ): 表示是否将 HLS Manifest 请求中的不表示签名的查询参数添加到分片 URI 中。该参数有以下取值： 
            - true：表示在分片 URI 中添加查询参数。 
            - false：表示不添加查询参数。 
            需要留意的是，该参数的设置影响签名的计算。参见 M3U8 改写功能的字段描述。 
        RewriteTag ( Object of RewriteTag ): 表示 "标签改写" 的配置。 
       "字段"： TosAuthInformation
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        AccessKeyId ( String ): 表示访问凭证中的 AccessKey ID，在腾讯云称为 SecretId。 
        AccessKeySecret ( String ): 表示访问凭证中的 AccessKey Secret，在腾讯云称为 SecretKey。 
       "字段"： ResponseAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        StatusCode ( String ): 表示鉴权失败时，CDN 响应用户的状态码。 
       "字段"： StatusCodeAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        DefaultAction ( String ): 表示如果鉴权状态码既不是 FailCode，又不是 SuccessCode 时，CDN 处理鉴权请求的方式。该参数有以下取值： 
            - reject：表示 CDN 认为鉴权失败。 
            - pass：表示 CDN 认为鉴权成功。 
        FailCode ( String ): 表示鉴权失败时的鉴权状态码。 
        SuccessCode ( String ): 表示鉴权成功时的鉴权状态码。 
       "字段"： TimeOutAction
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示鉴权超时后，CDN 处理鉴权请求的策略。该参数有以下取值： 
            - reject：表示 CDN 认为鉴权失败。 
            - pass：表示 CDN 认为鉴权成功。 
        Time ( Long ): 表示鉴权超时的时间，单位是毫秒。 
       "字段"： QueryStringComponents
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示鉴权请求是否包含用户请求 URL 中的查询参数。该参数有以下取值： 
            - exclude：表示鉴权请求不包含任何查询参数。 
            - include：表示鉴权请求包含所有查询参数。 
            - includePart：表示鉴权请求包含指定的查询参数。 
        Value ( String ): 表示 Action 参数所对应的参数值。 
       "字段"： QueryStringInstances
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示如何设置鉴权请求参数。该参数值始终为 set。set 表示设置参数。Key 中指定了需要设置的鉴权请求参数。如果指定的鉴权请求参数不存在，CDN 会在鉴权请求中添加该参数。如果您指定的鉴权请求参数已存在，CDN 会使用 Value 的值作为该鉴权请求参数的值。 
        Key ( String ): 表示您需要设置的鉴权请求参数。 
        Value ( String ): 表示鉴权请求参数的值。 
        ValueType ( String ): 表示 Key 中设置的鉴权请求参数的类型。ValueType 有以下取值： 
            - constant：表示鉴权请求参数是一个常量。 
            - variable：表示鉴权请求参数的值来自一个变量。 
            - customize：表示鉴权请求参数的值是一个变量与固定字符串拼接后的字符串。 
       "字段"： RequestHeaderComponents
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Action ( String ): 表示鉴权请求头是否包含用户请求头。该参数有以下取值： 
            - exclude：表示鉴权请求头中不包含任何用户请求头。 
            - include：表示鉴权请求头中包含所有用户请求头。 
            - includePart：表示鉴权请求头包含指定的用户请求头。 
        Value ( String ): 表示 Action 参数所对应的参数值。 
       "字段"： CustomVariableInstances
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Operator ( String ): 表示变量的匹配方式。该参数的取值始终是 match。 
        Type ( String ): 表示变量的类型。该参数有以下取值： 
            - queryString：表示该变量是请求中的一个查询参数。 
            - requestHeader：表示该变量是请求中的一个头部字段。 
        Value ( String ): 表示变量的名称。 
       "字段"： RewriteTag
        参数 ( 类型 ): 描述 
        ---- ( ---- ): ---- 
        Switch ( Boolean ): 表示是否需要改写额外标签中的分片 URL。该参数有以下取值： 
            * true: 表示需要改写额外标签。 
            * false：表示无额外标签需要改写。 
        Tags ( Array of String ): 表示除默认标签外，需要对其下分片 URI 进行改写的额外标签列表。 
    """,
    "list_domain_versions": r"""
    Args:
        body: A JSON structure
             参数 ( 类型 ): 是否必选  描述
             ---- ( ---- ): ----  ----
             Domain ( String ): 是  表示一个域名，获取该域名下的所有预发布版本。
             PageNum ( Long ): 否  表示页号，展示该分页上的版本。该参数的默认值是 1。
             PageSize ( Long ): 否  表示分页包含的版本数量，默认值是 10。
   Returns:
        参数 ( 类型 ): 描述
        ---- ( ---- ): ----
        TotalCount ( Long ): 表示域名下的版本数量。
        Versions ( Array of Versions ): 表示版本列表。
       "字段"： Versions
        参数 ( 类型 ): 描述
        ---- ( ---- ): ----
        CreateTime ( Long ): 表示版本的创建时间，格式是 Unix 时间戳。
        Creator ( String ): 表示版本的创建者。
            * 域名下的第一个版本是系统创建的，该版本的 Creator 是 System。
            * 如果是 IAM 用户创建了该版本，Creator 就是这个 IAM 用户的账号。
        Env ( Array of String ): 表示版本发布到的环境，有以下取值：
            * prod：表示线上环境。
            * staging：表示预发布环境。
            如果该参数值为空（[]），表示版本尚未发布到任何环境。
        Message ( String ): 表示版本的备注。
            域名下的第一个版本是系统创建的，该版本的 Message 是 Built by system automatically。
        OriginalVersion ( String ): 表示该版本复制于哪个版本。
            域名下的第一个版本是系统创建的，该版本的 OriginalVersion 是空（""）。
        ReleaseTime ( Long ): 表示该版本最近一次的发布时间，格式是 Unix 时间戳。
            对于刚创建的域名，ReleaseTime 与 CreateTime 相同。
        UpdateTime ( Long ): 表示版本的最近更新时间，格式是 Unix 时间戳。
        VersionId ( String ): 表示该版本的版本号。
    """,
    "release_domain_version": r"""
    Args:
       body: A JSON structure
            参数 ( 类型 ): 是否必选  描述
            ---- ( ---- ): ----  ----
            Domain ( String ): 否  表示一个域名，发布该域名下的指定版本。
            Env ( Array of String ): 否  表示版本发布到的环境，有以下取值：
                  * prod：表示线上环境。
                  * staging：表示预发布环境。
                  该参数的默认值是 ["prod"]。
            VersionId ( String ): 否  表示待发布的版本号。
                  您可以调用 ListDomainVersions 获取域名下的所有版本号。
    """,

}
