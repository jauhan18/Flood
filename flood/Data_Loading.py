import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
for feature in df_train.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df_train[feature])
    plt.title(f'Box Plot of {feature}')
    plt.show()