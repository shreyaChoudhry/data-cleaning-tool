import matplotlib.pyplot as plt

def plot_missing(df):
    df.isnull().sum().plot(kind='bar')
    plt.title("Missing Values per Column")
    plt.show()