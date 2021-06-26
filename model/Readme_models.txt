bert_dataprocessV1.ipynb
Read in a execel file with the data format label:sentence
label: [normal , attention]

It will provide a train and test dataset
nlpdata/data_train.csv
nlpdata/data_test.csv
******************************************
To creat new model
bert_TrainNewModelV1.ipynb
Use the dataset in the follow to do training
nlpdata/data_train.csv
nlpdata/data_test.csv

trained result store in the newmodel
newmodel/tf_model.h5
newmodel/tf_model.preproc

*************************************************
To improve current model
bert_TrainCurrentModelV1.ipynb
Use the dataset in the follow to do training
nlpdata/data_train.csv
nlpdata/data_test.csv

copy the previous trained model into currentmodel
currentmodel/tf_model.h5
currentmodel/tf_model.preproc


trained result store in the newmodel
newmodel/tf_model.h5
newmodel/tf_model.preproc
