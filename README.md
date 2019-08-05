# Traffic Light Classifier

A convolutional network that classifies 170x170 images of driver-POV traffic lights by three categories: stop(0), warning(1), go(2). The network was trained using 3552 images and validated on 889 images. The model can also be run through OpenCV to predict images frame by frame in a live webcam.

## Built With

* [Tensorflow - Keras](https://www.tensorflow.org/guide/keras) - Used to train CNN
* [Kaggle - LISA Traffic Light Dataset](https://www.kaggle.com/mbornoe/lisa-traffic-light-dataset) - Source of training and validation images
* [Pandas](https://pandas.pydata.org/) - Used to iterate through photos (image paths are in dataframe)
* [OpenCV](https://opencv.org/) - Used to run model through live video

## Author

Laura Dang
