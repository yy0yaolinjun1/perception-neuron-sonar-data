##
from sonar.sonar_data import *
import numpy as np
from random import seed
from random import randrange
import pickle as pkl
##
from sklearn.model_selection import train_test_split

def perceptron(z):
    return 0 if z <= 0 else 1

def predict(data, weights):
	activation = weights[0]
	bias=np.random.normal()
	for i in range(len(data)-1):
		activation += weights[i+1] * data[i]
    #activation function
	return perceptron(activation + bias)

def train_weights(data_train,data_label, l_rate, n_epoch):
	weights = np.random.normal(size=len(data_train[0]))
	for epoch in range(int(n_epoch)):
		for data,label in zip(data_train,data_label):
			prediction = predict(data, weights)
			err = label - prediction
			weights[0] = weights[0] + err*l_rate 
			for i in range(len(data)-1):
				weights[i + 1] = weights[i + 1] + err * l_rate *  data[i]
	return weights

def accuracy_metric(test_label, predictions):
	correctness = 0
	for i in range(len(predictions)):
		if predictions[i]==test_label[i]:
			correctness += 1
	return correctness / float(len(predictions)) * 100.0    

def training(train_data, test_data,train_label,test_label,l_rate, n_epoch):
	predictions = list()
    #train the weights with training data
	scores=list()
	print("Strat training")
	weights = train_weights(train_data,train_label,l_rate, n_epoch)

	for data in test_data:
		prediction = predict(data, weights)
		predictions.append(prediction)
    #calculate the accuracy
	accuracy = accuracy_metric(test_label, predictions)
	scores.append(accuracy) 
	return scores,weights

def save_model(self,data):
    f = open('results/sonar_model.pkl','wb')
    pkl.dump(data,f)
    f.close()

def main():

    sonar_data = Sonar_Data(data_file_path='../data/', data_file_name='sonar_data.pkl')

    train_data,test_data,train_label, test_label = train_test_split(sonar_data.data,sonar_data.label,test_size=0.3)
    
    accuracy,weights=training(train_data,test_data,train_label,test_label,0.01,500)
    
    save_model(weights)
    
    print("accuracy is ",accuracy)



##
if __name__ == "__main__":
    main()
