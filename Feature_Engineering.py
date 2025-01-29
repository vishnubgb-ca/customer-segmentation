from Data_Preprocessing import preprocess_data
import numpy as np

def feature_engineering():
    data = preprocess_data()
    # Outlier Treatment
    outliers_present = ["age", "income"]
    for value in outliers_present:
        percentile25 = data[value].quantile(0.25)
        percentile75 = data[value].quantile(0.75)
        iqr = percentile75 - percentile25
        upper_limit = percentile75 + 1.5 * iqr
        lower_limit = percentile25 - 1.5 * iqr
        data[value] = np.where(
            data[value] > upper_limit,
            upper_limit,
            np.where(
                data[value] < lower_limit,
                lower_limit,
                data[value]
            ))
    print(data.head())
    data.to_csv("cleaned_data.csv", index=False)
    return data

feature_engineering()
