from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
from matplotlib import ticker
import matplotlib.dates as dates

# import script
import data as d

plt.style.use("seaborn")


x_plot, y_plot = [], []


def plot_history():
    # Set x and y plots
    y_plot, x_plot = d.date_loop()
    
    # Plots
    fig, ax = plt.subplots()
    ax.plot(x_plot, y_plot, label="Bitcoin", color="#FFD54F", linestyle="-")
    
    # Make add dollars to y axis
    formatter = ticker.FormatStrFormatter('$%0.2f')
    ax.yaxis.set_major_formatter(formatter)

    # Accept dates !!!!! Edit spaces between dates
    plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(dates.DayLocator(interval=50))

    # Plot added data
#    plt.plot(x_plot, y_plot, label="Bitcoin", color="#FFD54F", linestyle="-")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.title("Price of Bitcoin in history")
    plt.show()


def plot_current_price(i): # animated; get update every so often
    api = d.actual_api()
    # Set x and y plots
    x_plot.append(f"{str(d.year())}-{str(d.month())}-{str(d.day())} {str(d.hour())}:{str(d.minute())}:{str(d.second())}")
    y_plot.append(api["bpi"]["USD"]["rate_float"])
    print(x_plot)

    """
    # Plots
    fig, ax = plt.subplots()
    ax.plot(x_plot, y_plot, label="Bitcoin", color="#FFD54F", linestyle="-")
    
    # Make add dollars to y axis
    formatter = ticker.FormatStrFormatter('$%0.2f')
    ax.yaxis.set_major_formatter(formatter)
    """

    # Make sure it won't run off wild
    plt.cla()

    # Accept dates
    plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(dates.DayLocator(interval=1))

    # Plot data
    plt.plot(x_plot, y_plot, label="Bitcoin", color="#FFD54F", linestyle="-", marker=".")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.title("Current price of Bitcoin")
    plt.show()
    


if __name__ == "__main__":
    print("Powered by CoinDesk") # https://www.coindesk.com/price/bitcoin"""
    plot_history()
    ani = FuncAnimation(plt.gcf(), plot_current_price, interval=3000)

#NOTES: Add dollars to current price plot + show date on x axis; edit style
