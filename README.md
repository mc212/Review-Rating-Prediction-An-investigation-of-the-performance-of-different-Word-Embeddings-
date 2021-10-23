# Review-Rating-Prediction-An-investigation-of-the-performance-of-different-Word-Embeddings-
As a part of our study for the course CA683 at Dublin City University, me and my partner conducted an investigation and experiments with respect to the existing embedding approaches in Natural Language Processing as well as Machine Learning and Deep Learning algorithms in the review rating prediction problem. The research has been implemented based on a subset of the Yelp review dataset. 

A range of predicting techniques, i.e. Random Forest, Logistic Regression, Decision Tree and a Recurrent Neural Network (RNN) are utilized along with several embedding techniques for feature transformation to predict the review rating. The results have shown promising performance in the accuracy of the RNN-based and Mean Word2Vec model, which outperforms other embedding and predicting approaches.

The data source, visualisation, data selection and pre-processing are presented at the file Data Exploration
The application of different techniques consisting of bag of word, Word2Vec, Doc2Vec, TF-IDF, word embeddings, and Paragraph Vector-Distributed Memory (PV-DM) model can be found in the file Transformation
Finally, the different kinds of transformed data are utilized to train models consisting of Decision Tree, Logistic Regression, Random Forest and Recurrent Neural Network based model (Bi-LSTM, Bi-GRU) to predict ratings for reviews. The source code and the experiment results are shown in the file Processing however as RNN based model is not my responsibility in the project, the source code of this part won't be uploaded on my personal github.



