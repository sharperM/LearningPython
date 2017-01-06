# -*- coding:utf-8 -*- 
import easyquotation

import easyquant
from easyquant import DefaultQuotationEngine, DefaultLogHandler, PushBaseEngine
import time

broker = 'xq'


def get_broker_need_data(choose_broker):
    need_data = input('请输入你的帐号配置文件路径(直接回车使用 %s.json)\n:' % choose_broker)
    if need_data == '':
        return '%s.json' % choose_broker
    return need_data


need_data = 'xqmsp.json'


class LFEngine(PushBaseEngine):
    EventType = 'lf'

    def init(self):
        self.source = easyquotation.use('lf')

    def fetch_quotation(self):
        return self.source.stocks(['00002','000039','002732','002739','603899','600977','601788','601555','600109','000810','002594','002230','601238','000651','000423','600085','000776','600369','002093','600030','002032','600016','600999','002007','000793','600597','601377','600289','600104','600588','002449','600048','600004','600256','600897','002351','000402','601890','000541','000777','600332','000538','000951','600019','600028','600831','601857','000800','600125'])


quotation_choose = 2

quotation_engine = DefaultQuotationEngine if quotation_choose == '1' else LFEngine

push_interval = 3#int(input('请输入行情推送间隔(s)\n:'))
quotation_engine.PushInterval = push_interval

log_type_choose = 2
log_type = 'stdout' if log_type_choose == '1' else 'file'

log_filepath = './logfile/xqtrde_'+time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))+'.log'

log_handler = DefaultLogHandler(name='-=ceshi=-', log_type=log_type, filepath=log_filepath)

m = easyquant.MainEngine(broker, need_data, quotation_engines=[quotation_engine], log_handler=log_handler)
m.is_watch_strategy = True  # 策略文件出现改动时,自动重载,不建议在生产环境下使用
m.load_strategy()
m.start()
