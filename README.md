
## CNN for Digit Recognition

Experiment with different pre-processing methods to learn the performance of the CNN model.


## Code style
https://www.python.org/dev/peps/pep-0008/

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## Packages
Important packages:
* tensorflow==2.1.0
* numpy==1.19.3
* h5py==2.10.0


<b>Built with</b>
- [Python](https://www.python.org/)

## Features
There are 3 methods provided (in this repo) to scale pixel values in images. Pixels size set for this model is 28x28. Please refer process_data.py to see data pre-processing flow.

#### Methods:
1) Normalization
2) Mean
3) Standardize

>Note:
>* For development environment only. Not suitable for production.
>* Modify the input shape and type in data.py (if required).
>* Modify the layers in load.py (if required).


## Installation
Install Python packages.

#### Predict
The result is saved in h5.
```sh
python LeNet <method>
```

#### Training

Run modelling to create new model.

>Note: 
>* There are 3 types of activation functions (ReLu, Tan, Sigmoid) tested (in this repo) and model with ReLu has the highest accuracy.

## Testing
Include testing data in data.py file. Assign to
>test_y

## How to use?
Modelling
>Find the best activation function.

Prediction
>Use different pre-processing methods.

## Credits
Dataset 
>http://yann.lecun.com/exdb/mnist/ 

## License
https://github.com/ami-sm/cnn-models/blob/master/LICENSE

MIT © AMI-SM
