import time
import datetime as dt
from dateutil import tz
from easyquant import DefaultLogHandler
from easyquant import StrategyTemplate
import time

class Strategy(StrategyTemplate):
    name = 'jijintaoli'
    logfileName =  './logfile/'+name+time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))+'.log'   
    def init(self):
        # 通过下面的方式来获取时间戳
        now_dt = self.clock_engine.now_dt
        now = self.clock_engine.now
        now = time.time()

        # 注册时钟事件
        clock_type = "盘尾"
        moment = dt.time(14, 56, 30, tzinfo=tz.tzlocal())
        self.clock_engine.register_moment(clock_type, moment)

        # 注册时钟间隔事件, 不在交易阶段也会触发, clock_type == minute_interval
        minute_interval = 1.5
        self.clock_engine.register_interval(minute_interval, trading=False)

    def formatSock(self,data,sname):

        strRet = sname+ '\r\n'
        for i in range(10,0,-1):
            strRet = strRet+('ask%-2d:%-8.2f   %8.f\r\n'% (i,data['ask%d'%i],data['ask%d_volume'%i]/100))
        strRet = strRet + '-----------\r\n'
        for i in range(1,11):
            strRet = strRet+('bid%-2d:%-8.2f   %8.f\r\n'% (i , data['bid%d'%i], data['bid%d_volume'%i]/100))

        name = {'buy','close','now','sell'}
        for x in name:
            strRet = strRet + '%-5s:%6.2f\r\n'% (x,data[x])
        return strRet

    def strategy(self, event):
        # 使用 self.user 来操作账户，用法同 easytrader 用法
        # 使用 self.log.info('message') 来打印你所需要的 log
        self.log.info('\n\n套利1')
        for s in event.data:
            #self.log.info(self.formatSock(event.data[s],str(s)))
            self.log.info((event.data[s]))
        # self.log.info('行情数据: 比亚迪价格: %s' % event.data['000002'])
        # data1 = event.data['000002']
        #self.log.info(self.formatSock(event.data['002461']))
        self.log.info('检查持仓 ')
        self.log.info(self.user.balance)

        #self.log.info('\n')

    def clock(self, event):
        """在交易时间会定时推送 clock 事件
        :param event: event.data.clock_event 为 [0.5, 1, 3, 5, 15, 30, 60] 单位为分钟,  ['open', 'close'] 为开市、收市
            event.data.trading_state  bool 是否处于交易时间
        """
        if event.data.clock_event == 'open':
            # 开市了
            self.log.info('open')
        elif event.data.clock_event == 'close':
            # 收市了
            self.log.info('close')
        elif event.data.clock_event == 5:
            # 5 分钟的 clock
            self.log.info("5分钟")

    def log_handler(self):
        """自定义 log 记录方式"""
        return DefaultLogHandler(self.name, log_type='stdio', filepath=self.logfileName)

    def shutdown(self):
        """
        关闭进程前的调用
        :return:
        """
        self.log.info("假装在关闭前保存了策略数据")
