import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from sklearn.neural_network import MLPClassifier
import pickle as cPickle
import csv
import os.path

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(800,600))
        self.content = QWidget()
        layout = QGridLayout()

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.button = QPushButton('Add_Point')
        self.random_button = QPushButton('Predict_random_points')
        self.teach_NN_button = QPushButton('Teach_NN')
        self.load_csv_button = QPushButton('Load_csv')
        self.show_boundaries_button = QPushButton('Show_boundaries')
        self.clear_plot_button = QPushButton('Clear_plot')
        self.save_NN_button = QPushButton('Save_NN')
        self.load_NN_button = QPushButton('Load_NN')
        self.scale_plot_button = QPushButton('Scale_plot')

        layout.addWidget(self.button,2,0,1,2)
        layout.addWidget(self.random_button, 3, 0, 1, 2)
        layout.addWidget(self.show_boundaries_button,4, 0, 1, 2)
        layout.addWidget(self.clear_plot_button, 5, 0, 1, 2)
        layout.addWidget(self.load_csv_button, 14, 0, 1, 2)
        layout.addWidget(self.teach_NN_button, 16, 0, 1, 2)
        layout.addWidget(self.load_NN_button, 18, 0, 1, 2)
        layout.addWidget(self.save_NN_button, 20, 0, 1, 2)
        layout.addWidget(self.scale_plot_button,6 ,0 ,1 ,2)

        self.X1_input = QLineEdit('Input from -4 to 2')
        self.X2_input = QLineEdit('Input from 2 to 5')
        self.save_name_input = QLineEdit("save_NN_name")
        self.load_name_input = QLineEdit("load_NN_name")
        self.NN_sample_size = QLineEdit("NN_sample_size")
        self.load_CSV_input = QLineEdit("load_CSV_file")

        layout.addWidget(QLabel('X1:'), 0, 0)
        layout.addWidget(QLabel('X2:'), 1, 0)
        layout.addWidget(QLabel('NN_save_name:'), 21, 0)
        layout.addWidget(QLabel('NN_load_name:'), 19, 0)
        layout.addWidget(QLabel('NN_Sample_size'), 17, 0)
        layout.addWidget(QLabel('CSV_file_name'), 15, 0)
        layout.addWidget(self.X1_input, 0, 1)
        layout.addWidget(self.X2_input, 1, 1)
        layout.addWidget(self.load_name_input, 19, 1)
        layout.addWidget(self.save_name_input, 21, 1)
        layout.addWidget(self.NN_sample_size, 17, 1)
        layout.addWidget(self.load_CSV_input,15,1)

        spacer1 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer1, 9, 0, 1, 2)

        self.button.clicked.connect(self.plot)
        self.random_button.clicked.connect(self.predict_random_data)
        self.load_csv_button.clicked.connect(self.load_csv)
        self.show_boundaries_button.clicked.connect(self.show_boundaries)
        self.clear_plot_button.clicked.connect(self.clear_plot)
        self.save_NN_button.clicked.connect(self.save_NN)
        self.load_NN_button.clicked.connect(self.load_NN)
        self.teach_NN_button.clicked.connect(self.teach_NN)
        self.scale_plot_button.clicked.connect(self.scale_plot)

        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.canvas, 0, 2, 22, 1)

        self.content.setLayout(layout)
        self.setCentralWidget(self.content)

    def plot(self):

        try:
            NN = clf

            try:
                X1 = float(self.X1_input.text())
                X2 = float(self.X2_input.text())

                if X1 < -4 or X1 > 2:
                    QMessageBox.critical(self, 'Error', 'Wrong coefficients:\nX1 out of (-4,2) interval')
                if X2 < 2 or X2 > 5:
                    QMessageBox.critical(self, 'Error', 'Wrong coefficients:\nX2 out of (2,5) interval')

                else:
                    prediction = clf.predict([[X1, X2]])
                    color = "r"
                    if prediction < 1:
                        color = "b"
                    plt.scatter(X1, X2, c=color, edgecolors='black')
                    plt.ylim(2, 5)
                    plt.xlim(-4, 2)

                    self.set_plot()
                    self.canvas.draw()

            except ValueError as e:
                QMessageBox.critical(self, 'Error', 'Wrong coefficients:\nValueError: ' + str(e))

        except:
            QMessageBox.critical(self, 'Error', 'No NN loaded')

    def teach_NN(self):

        try:
            float(self.NN_sample_size.text())
            if float(self.NN_sample_size.text()) < 1 or float(self.NN_sample_size.text()) > 3500:
                QMessageBox.critical(self, 'Error', "Sample size too big or negative")

            else:
                inputs, outputs = self.generate_random(int(self.NN_sample_size.text()))
                global clf
                clf = MLPClassifier(solver='lbfgs', alpha=0.9, max_iter=500000, learning_rate_init=0.01,
                                    hidden_layer_sizes=(30, 25, 20, 20, 20), random_state=1)
                clf.fit(inputs, outputs)
        except ValueError as e:
            QMessageBox.critical(self, 'Error', 'Wrong coefficient:' + str(e))

    def generate_random(self, sample_num):

        X1 = np.array([])
        X2 = np.array([])
        Y_output = np.array([])
        data = np.array([])
        it = 0

        for i in range(sample_num):
            x1 = np.random.uniform(-4, 2)
            x2 = np.random.uniform(2, 5)

            X1 = np.append(X1, x1)
            X2 = np.append(X2, x2)

        Y = 0.4444444 * (X1 + 2) ** 2 + 2.3668639 * (X2 - 3) ** 2

        for i in Y:
            if i < 1:
                output = 1
            else:
                output = 0
            Y_output = np.append(Y_output, output)

        for i in X1:
            data = np.append(data, [X1[it], X2[it]])
            it = it + 1

        data = np.reshape(data, (-1, 2))

        return data, Y_output

    def predict_random_data(self):

        pred_data, Ys = self.generate_random(100)
        self.predict_data(pred_data)

    def predict_data(self, pred_data):

        try:

            prediction = clf.predict(pred_data)

            for i in range(len(pred_data)):
                point = pred_data[i]
                color = "r"
                if prediction[i] < 1:
                    color = "b"
                plt.scatter(point[0], point[1], c=color, edgecolors='black')

            self.set_plot()
            self.canvas.draw()

        except:
            QMessageBox.critical(self, 'Error', 'No NN loaded')

    def load_csv(self):

        try:
            NN = clf

            if os.path.isfile(str(self.load_CSV_input.text() + ".csv")):

                filename = str(self.load_CSV_input.text() + ".csv")
                X1 = []
                X2 = []
                data = np.array([])

                with open(filename, 'r') as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=";")

                    try:

                        for row in csvreader:

                                X1.append(float(row[0].replace(',', ".")))
                                X2.append(float(row[1].replace(',', ".")))

                                for i in range(len(X1)):
                                    data = np.append(data, [X1[i], X2[i]])
                                    data = np.reshape(data, (-1, 2))

                                self.predict_data(data)
                                output = clf.predict(data)
                                self.save_csv(X1, X2, output)

                    except:
                        QMessageBox.critical(self, 'Error', 'CSV file error')

            else:
                QMessageBox.critical(self, 'Error', 'File not found')

        except:
            QMessageBox.critical(self, 'Error', 'No NN loaded')

    def save_csv(self,X1,X2,output):

        fields = ["X1","X2","Prediction"]
        filename = "NN_prediction.csv"

        with open(filename, "w") as csvfile:

            csvwriter = csv.writer(csvfile, delimiter=";")
            csvwriter.writerow(fields)

            for i in range(len(X1)):
                csvwriter.writerow([str(X1[i]), str(X2[i]), str(output[i])])

    def show_boundaries(self):

        try:

            h = .01
            xx, yy = np.meshgrid(np.arange(-4, 2, h),
                                 np.arange(2, 5, h))

            Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            plt.contourf(xx, yy, Z, cmap=plt.cm.jet, alpha=0.5)

            self.set_plot()
            self.canvas.draw()

        except:
            QMessageBox.critical(self, 'Error', 'No NN loaded')

    def clear_plot(self):

        plt.clf()
        self.set_plot()
        self.canvas.draw()

    def set_plot(self):

        plt.ylim(2, 5)
        plt.xlim(-4, 2)
        plt.xlabel("X1")
        plt.ylabel("X2")
        blue = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                                  markersize=10, label='Outside')
        red = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                                   markersize=10, label='Inside')
        plt.legend(handles=[red,blue], loc = "upper right")

    def save_NN(self):

        try:

            NN = clf
            with open(str(self.save_name_input.text()) + ".pkl", 'wb') as fid:
                cPickle.dump(clf, fid)

        except:
            QMessageBox.critical(self, 'Error', 'No NN loaded')

    def load_NN(self):

        try:

            global clf
            with open(str(self.load_name_input.text()) + ".pkl", 'rb') as fid:
                clf = cPickle.load(fid)

        except:
            QMessageBox.critical(self, 'Error', 'File not found')

    def scale_plot(self):
        plt.axis("scaled")
        self.set_plot()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
