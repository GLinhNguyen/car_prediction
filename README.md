# Car Price Prediction 

## Project structure
~~~
car_prediction/
├── app.py                        # Flask app to run API
├── random_forest_pipeline.pkl    # Pipeline model for preprocessing, trained Random Forest model       
├── car.csv                       # Please change this data path on your machine to run 
├── car_model.ipynb               # Where trained models and data analysis resides
└── ...

~~~
## API
In your terminal:
 ~~~
   python app.py
 ~~~
Here I use Postman to test API, please paste data as JSON to run:
~~~
{
    "brand": "Toyota",
    "type": "Sedan",
    "fuel": "petrol",
    "color": "white",
    "gearbox": "MT",
    "origin": "Vietnam",
    "mileage_v2": 10000,
    "seats": 5,
    "age": 3,
    "condition" : "used"
}
~~~
Result:
![Image](https://github.com/user-attachments/assets/b315aac4-97e3-4e1a-a76c-da8f0126a13d)
 
