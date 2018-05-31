import sys
import supermarket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_grid = QGridLayout()
        self.setLayout(main_grid)
        goods_grid = QGridLayout()
        sale_grid = QGridLayout()
        sell_grid = QGridLayout()
        stock_grid = QGridLayout()
        new_grid = QGridLayout()
        bad_grid = QGridLayout()

        tab = QTabWidget()
        goods_widget = QWidget()
        sale_widget = QWidget()
        sell_widget = QWidget()
        stock_widget = QWidget()
        new_widget = QWidget()
        bad_widget = QWidget()

        goods_widget.setLayout(goods_grid)
        sale_widget.setLayout(sale_grid)
        sell_widget.setLayout(sell_grid)
        stock_widget.setLayout(stock_grid)
        new_widget.setLayout(new_grid)
        bad_widget.setLayout(bad_grid)

        tab.addTab(goods_widget, '商品管理')
        tab.addTab(sale_widget, '售货查询')
        tab.addTab(sell_widget, '模拟销售')
        tab.addTab(stock_widget, '商品进货')
        tab.addTab(new_widget, '新品上市')
        tab.addTab(bad_widget, '下架商品')
        main_grid.addWidget(tab)

        # <editor-fold desc="Init goods_widget">

        sub_grid_1 = QGridLayout()
        sub_grid_1.setSpacing(10)

        self.edit = list()
        for i in range(10):
            self.edit.append(QLineEdit())

        label = list()
        label.append(QLabel('编号'))
        label.append(QLabel('名称'))
        label.append(QLabel('品牌'))
        label.append(QLabel('价格'))
        label.append(QLabel('数量'))
        label.append(QLabel('颜色'))
        label.append(QLabel('大小'))
        label.append(QLabel('适合人群'))
        label.append(QLabel('保质期'))
        label.append(QLabel('产地'))

        btn = QPushButton('查询')
        self.table = QTableWidget(128, 10)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        horizontal_head = ['编号', '名称', '品牌', '价格', '数量', '颜色', '大小', '适合人群', '保质期', '产地']
        self.table.setHorizontalHeaderLabels(horizontal_head)

        sub_grid_1.addWidget(label[0], 0, 0)
        sub_grid_1.addWidget(self.edit[0], 0, 1)
        sub_grid_1.addWidget(label[1], 0, 2)
        sub_grid_1.addWidget(self.edit[1], 0, 3)
        sub_grid_1.addWidget(label[2], 0, 4)
        sub_grid_1.addWidget(self.edit[2], 0, 5)
        sub_grid_1.addWidget(label[3], 1, 0)
        sub_grid_1.addWidget(self.edit[3], 1, 1)
        sub_grid_1.addWidget(label[4], 1, 2)
        sub_grid_1.addWidget(self.edit[4], 1, 3)
        sub_grid_1.addWidget(label[5], 1, 4)
        sub_grid_1.addWidget(self.edit[5], 1, 5)
        sub_grid_1.addWidget(label[6], 2, 0)
        sub_grid_1.addWidget(self.edit[6], 2, 1)
        sub_grid_1.addWidget(label[7], 2, 2)
        sub_grid_1.addWidget(self.edit[7], 2, 3)
        sub_grid_1.addWidget(label[8], 2, 4)
        sub_grid_1.addWidget(self.edit[8], 2, 5)
        sub_grid_1.addWidget(label[9], 3, 0)
        sub_grid_1.addWidget(self.edit[9], 3, 1)
        sub_grid_1.addWidget(btn, 3, 5)

        goods_grid.addLayout(sub_grid_1, 0, 1, 1, 1)
        goods_grid.addWidget(self.table, 1, 0, 1, 2)
        # </editor-fold>

        # <editor-fold desc="Init sale_widget">
        sub_grid_sale = QGridLayout()
        sub_grid_sale.setSpacing(10)

        self.edit_sale = list()
        for i in range(3):
            self.edit_sale.append(QLineEdit())

        label_sale = list()
        label_sale.append(QLabel('产品编号'))
        label_sale.append(QLabel('开始日期'))
        label_sale.append(QLabel('结束日期'))

        btn_sale = QPushButton('查询')
        self.table_sale = QTableWidget(128, 5)
        self.table_sale.setEditTriggers(QTableWidget.NoEditTriggers)

        horizontal_head_sale = ['产品编号', '销售日期', '销售数量', '单价', '总价']
        self.table_sale.setHorizontalHeaderLabels(horizontal_head_sale)

        sub_grid_sale.addWidget(label_sale[0], 0, 0)
        sub_grid_sale.addWidget(self.edit_sale[0], 0, 1)
        sub_grid_sale.addWidget(label_sale[1], 0, 2)
        sub_grid_sale.addWidget(self.edit_sale[1], 0, 3)
        sub_grid_sale.addWidget(label_sale[2], 1, 0)
        sub_grid_sale.addWidget(self.edit_sale[2], 1, 1)
        sub_grid_sale.addWidget(btn_sale, 1, 3)

        sale_grid.addLayout(sub_grid_sale, 0, 0)
        sale_grid.addWidget(self.table_sale, 1, 0)

        # </editor-fold>

        # <editor-fold desc="Init sell_widget">
        sub_grid_sell = QGridLayout()
        sub_grid_sell.setSpacing(10)

        self.edit_sell = list()
        for i in range(4):
            self.edit_sell.append(QLineEdit())

        label_sell = list()
        label_sell.append(QLabel('产品编号'))
        label_sell.append(QLabel('销售时间'))
        label_sell.append(QLabel('数量'))
        label_sell.append(QLabel('单价'))

        btn_sell = QPushButton('销售')
        self.table_sell = QTableWidget(128, 6)
        self.table_sell.setEditTriggers(QTableWidget.NoEditTriggers)

        horizontal_head_sell = ['记录编号', '产品编号', '销售时间', '数量', '单价', '总价']
        self.table_sell.setHorizontalHeaderLabels(horizontal_head_sell)

        sub_grid_sell.addWidget(label_sell[0], 0, 0)
        sub_grid_sell.addWidget(self.edit_sell[0], 0, 1)
        sub_grid_sell.addWidget(label_sell[1], 0, 2)
        sub_grid_sell.addWidget(self.edit_sell[1], 0, 3)
        sub_grid_sell.addWidget(label_sell[2], 1, 0)
        sub_grid_sell.addWidget(self.edit_sell[2], 1, 1)
        sub_grid_sell.addWidget(label_sell[3], 1, 2)
        sub_grid_sell.addWidget(self.edit_sell[3], 1, 3)
        sub_grid_sell.addWidget(btn_sell, 2, 3)

        sell_grid.addLayout(sub_grid_sell, 0, 0)
        sell_grid.addWidget(self.table_sell, 1, 0)
        # </editor-fold>

        # <editor-fold desc="Init stock_widget">
        sub_grid_stock = QGridLayout()
        sub_grid_stock.setSpacing(10)

        self.edit_stock = list()
        for i in range(4):
            self.edit_stock.append(QLineEdit())

        label_stock = list()
        label_stock.append(QLabel('产品编号'))
        label_stock.append(QLabel('进货时间'))
        label_stock.append(QLabel('数量'))
        label_stock.append(QLabel('单价'))

        btn_refresh = QPushButton('刷新')
        btn_stock = QPushButton('采购')
        self.table_stock = QTableWidget(128, 5)
        self.table_stock.setEditTriggers(QTableWidget.NoEditTriggers)

        horizontal_head_stock = ['产品编号', '产品名称', '生产公司', '单价', '剩余数量']
        self.table_stock.setHorizontalHeaderLabels(horizontal_head_stock)

        sub_grid_stock.addWidget(label_stock[0], 0, 0)
        sub_grid_stock.addWidget(self.edit_stock[0], 0, 1)
        sub_grid_stock.addWidget(label_stock[1], 0, 2)
        sub_grid_stock.addWidget(self.edit_stock[1], 0, 3)
        sub_grid_stock.addWidget(label_stock[2], 1, 0)
        sub_grid_stock.addWidget(self.edit_stock[2], 1, 1)
        sub_grid_stock.addWidget(label_stock[3], 1, 2)
        sub_grid_stock.addWidget(self.edit_stock[3], 1, 3)
        sub_grid_stock.addWidget(btn_refresh, 2, 2)
        sub_grid_stock.addWidget(btn_stock, 2, 3)

        stock_grid.addLayout(sub_grid_stock, 0, 0)
        stock_grid.addWidget(self.table_stock, 1, 0)
        # </editor-fold>

        # <editor-fold desc="Init new_widget">
        sub_grid_new = QGridLayout()
        sub_grid_new.setSpacing(10)

        self.edit_new = list()
        for i in range(10):
            self.edit_new.append(QLineEdit())

        label_new = list()
        label_new.append(QLabel('编号'))
        label_new.append(QLabel('名称'))
        label_new.append(QLabel('品牌'))
        label_new.append(QLabel('价格'))
        label_new.append(QLabel('数量'))
        label_new.append(QLabel('服装颜色'))
        label_new.append(QLabel('服装大小'))
        label_new.append(QLabel('服装人群'))
        label_new.append(QLabel('食品保质期'))
        label_new.append(QLabel('食品产地'))

        btn_clothes = QPushButton('服装进货')
        btn_food = QPushButton('食品进货')
        self.table_new = QTableWidget(128, 5)
        self.table_new.setEditTriggers(QTableWidget.NoEditTriggers)

        horizontal_head_new = ['产品编号', '产品名称', '生产公司', '单价', '剩余数量']
        self.table_new.setHorizontalHeaderLabels(horizontal_head_new)

        sub_grid_new.addWidget(label_new[0], 0, 0)
        sub_grid_new.addWidget(self.edit_new[0], 0, 1)
        sub_grid_new.addWidget(label_new[1], 0, 2)
        sub_grid_new.addWidget(self.edit_new[1], 0, 3)
        sub_grid_new.addWidget(label_new[2], 0, 4)
        sub_grid_new.addWidget(self.edit_new[2], 0, 5)
        sub_grid_new.addWidget(label_new[3], 1, 0)
        sub_grid_new.addWidget(self.edit_new[3], 1, 1)
        sub_grid_new.addWidget(label_new[4], 1, 2)
        sub_grid_new.addWidget(self.edit_new[4], 1, 3)
        sub_grid_new.addWidget(label_new[5], 1, 4)
        sub_grid_new.addWidget(self.edit_new[5], 1, 5)
        sub_grid_new.addWidget(label_new[6], 2, 0)
        sub_grid_new.addWidget(self.edit_new[6], 2, 1)
        sub_grid_new.addWidget(label_new[7], 2, 2)
        sub_grid_new.addWidget(self.edit_new[7], 2, 3)
        sub_grid_new.addWidget(label_new[8], 2, 4)
        sub_grid_new.addWidget(self.edit_new[8], 2, 5)
        sub_grid_new.addWidget(label_new[9], 3, 0)
        sub_grid_new.addWidget(self.edit_new[9], 3, 1)
        sub_grid_new.addWidget(btn_clothes, 3, 3)
        sub_grid_new.addWidget(btn_food, 3, 5)

        new_grid.addLayout(sub_grid_new, 0, 0)
        new_grid.addWidget(self.table_new, 1, 0)
        # </editor-fold>

        btn.clicked.connect(self.on_click_btn1)
        btn_sale.clicked.connect(self.on_click_btn2)
        btn_sell.clicked.connect(self.on_click_btn3)
        btn_stock.clicked.connect(self.on_click_btn4)
        btn_refresh.clicked.connect(self.on_click_btn5)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Test")
        self.show()

    def on_click_btn1(self):
        self.table.clearContents()
        l2 = list()
        for i in self.edit:
            l2.append(i.text())
        result = supermarket.select('goods', l2)
        for i in range(len(result)):
            for j in range(len(result[i])):
                if type(result[i][j] == int):
                    r = str(result[i][j])
                else:
                    r = result[i][j].toString()
                item = QTableWidgetItem(r)
                self.table.setItem(i, j, item)

    def on_click_btn2(self):
        self.table_sale.clearContents()
        l2 = list()
        for i in self.edit_sale:
            l2.append(i.text())
        result = supermarket.select('sale', l2)
        for i in range(len(result)):
            for j in range(5):
                if type(result[i][j] == int):
                    r = str(result[i][j])
                else:
                    r = result[i][j].toString()
                item = QTableWidgetItem(r)
                self.table_sale.setItem(i, j, item)

    def on_click_btn3(self):
        self.table_sell.clearContents()
        l2 = list()
        for i in self.edit_sell:
            l2.append(i.text())
        l2.append(str(int(l2[2])*int(l2[3])))
        supermarket.insert('sale_record', l2)
        result = supermarket.select('sale', '*')
        supermarket.update('goods', [l2[0], l2[2]], False)
        for i in range(len(result)):
            for j in range(len(result[i])):
                if type(result[i][j] == int):
                    r = str(result[i][j])
                else:
                    r = result[i][j].toString()
                item = QTableWidgetItem(r)
                self.table_sell.setItem(i, j, item)

    def on_click_btn4(self):
        l2 = list()
        for i in self.edit_stock:
            l2.append(i.text())
        l2.append(str(int(l2[2])*int(l2[3])))
        print(l2)
        supermarket.insert('stock_record', l2)
        supermarket.update('goods', [l2[0], l2[2]], True)

    def on_click_btn5(self):
        self.table_stock.clearContents()
        result = supermarket.select('refresh', [10])
        for i in range(len(result)):
            for j in range(len(result[i])):
                if type(result[i][j] == int):
                    r = str(result[i][j])
                else:
                    r = result[i][j].toString()
                item = QTableWidgetItem(r)
                self.table_stock.setItem(i, j, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
