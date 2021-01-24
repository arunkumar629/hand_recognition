from ludwig.api import LudwigModel

def make_inference():
    trained_model = LudwigModel.load("results/exp_run/model")
    prediction = trained_model.predict(
        {"image_path":["D:\programs\python\exampl\hand_recognition\infer/right (24).jpg",
        "D:\programs\python\exampl\hand_recognition\infer\left (26).jpg"

        ],

        "label":[-1,-1]
        }
    )
    print(prediction[0]["label_predictions"].values)
if __name__=="__main__":
    make_inference()